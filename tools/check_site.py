#!/usr/bin/env python3
"""Controlli statici SEO e integrità dei link del sito JDEVPRO.

Eseguire: python3 tools/check_site.py
Non richiede dipendenze o accesso a Internet.
"""
from __future__ import annotations

from collections import defaultdict
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://www.jdevpro.it/"
HOSTS = {"www.jdevpro.it", "jdevpro.it"}
NOT_INDEXABLE = {"404.html", "chi-sono.html"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.title_active = False
        self.lang = ""
        self.h1 = 0
        self.canonical = []
        self.robots = ""
        self.description = ""
        self.links: list[tuple[str, str]] = []
        self.resources: list[tuple[str, str]] = []
        self.images_without_alt = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang", "")
        if tag == "title":
            self.title_active = True
        if tag == "h1":
            self.h1 += 1
        if tag == "meta" and a.get("name", "").lower() == "description":
            self.description = a.get("content", "")
        if tag == "meta" and a.get("name", "").lower() == "robots":
            self.robots = a.get("content", "")
        if tag == "link":
            rel = a.get("rel", "").lower().split()
            if "canonical" in rel:
                self.canonical.append(a.get("href", ""))
            if "stylesheet" in rel and a.get("href"):
                self.resources.append(("stylesheet", a["href"]))
        if tag == "script" and a.get("src"):
            self.resources.append(("script", a["src"]))
        if tag == "img":
            if "alt" not in a:
                self.images_without_alt += 1
            if a.get("src"):
                self.resources.append(("image", a["src"]))
        if tag == "a" and a.get("href"):
            self.links.append(("link", a["href"]))

    def handle_endtag(self, tag):
        if tag == "title":
            self.title_active = False

    def handle_data(self, data):
        if self.title_active:
            self.title += data


def target_file(source: str, href: str) -> str | None:
    """Restituisce il file locale cui punta href, ignorando servizi esterni."""
    full = urljoin(urljoin(ORIGIN, source), href)
    parsed = urlsplit(full)
    if parsed.scheme not in ("http", "https") or parsed.hostname not in HOSTS:
        return None
    path = unquote(parsed.path).lstrip("/")
    if not path or path.endswith("/"):
        path += "index.html"
    # impedisce riferimenti a percorsi che escono dalla radice
    parts = Path(path).parts
    if ".." in parts:
        return path
    return path


def check() -> list[str]:
    errors: list[str] = []
    site_pages = {p.name: p for p in ROOT.glob("*.html")}
    indexable = set(site_pages) - NOT_INDEXABLE
    xml_path = ROOT / "sitemap.xml"
    try:
        sitemap = ET.parse(xml_path)
        urls = sitemap.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url")
    except (ET.ParseError, OSError) as exc:
        return [f"sitemap.xml non leggibile: {exc}"]

    paths = []
    for entry in urls:
        loc = entry.findtext("{http://www.sitemaps.org/schemas/sitemap/0.9}loc", "")
        full = urlsplit(loc)
        if full.scheme != "https" or full.netloc != "www.jdevpro.it":
            errors.append(f"URL sitemap non canonica: {loc}")
        path = full.path.lstrip("/") or "index.html"
        paths.append(path)
        lastmod = entry.findtext("{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod", "")
        try:
            if lastmod and date.fromisoformat(lastmod) > date.today():
                errors.append(f"lastmod nel futuro: {path}")
        except ValueError:
            errors.append(f"lastmod non valido: {path}: {lastmod}")

    listed = set(paths)
    if len(paths) != len(listed):
        duplicates = sorted(p for p in listed if paths.count(p) > 1)
        errors.append(f"URL duplicate nella sitemap: {duplicates}")
    for missing in sorted(indexable - listed):
        errors.append(f"Pagina esclusa dalla sitemap: {missing}")
    for extra in sorted(listed - indexable):
        errors.append(f"URL non indicizzabile o file inesistente in sitemap: {extra}")

    titles: dict[str, list[str]] = defaultdict(list)
    for name, file in sorted(site_pages.items()):
        page = Page()
        page.feed(file.read_text(encoding="utf-8"))
        if name not in NOT_INDEXABLE:
            if not page.title.strip():
                errors.append(f"{name}: titolo mancante")
            else:
                titles[page.title.strip()].append(name)
            if not page.description.strip():
                errors.append(f"{name}: meta description mancante")
            if page.h1 != 1:
                errors.append(f"{name}: atteso 1 H1, trovati {page.h1}")
            if "noindex" in page.robots.lower():
                errors.append(f"{name}: noindex su pagina in sitemap")
        if not page.lang:
            errors.append(f"{name}: attributo lang mancante")
        expected = ORIGIN if name == "index.html" else ORIGIN + name
        if len(page.canonical) != 1 or page.canonical[0] != expected:
            errors.append(f"{name}: canonical incoerente ({page.canonical})")
        if name in NOT_INDEXABLE and name == "404.html" and "noindex" not in page.robots.lower():
            errors.append("404.html: manca noindex")
        if page.images_without_alt:
            errors.append(f"{name}: {page.images_without_alt} immagini senza attributo alt")
        for typ, raw in page.links + page.resources:
            target = target_file(name, raw)
            if target and not (ROOT / target).is_file():
                errors.append(f"{name}: {typ} non trovato: {raw} => {target}")

    for title, sources in titles.items():
        if len(sources) > 1:
            errors.append(f"Titolo duplicato: {title} nelle pagine {', '.join(sources)}")

    robots_file = ROOT / "robots.txt"
    if not robots_file.exists() or "Sitemap: " + ORIGIN + "sitemap.xml" not in robots_file.read_text(encoding="utf-8"):
        errors.append("robots.txt non indica la sitemap canonica")
    return errors


if __name__ == "__main__":
    problems = check()
    if problems:
        print("Verifica del sito FALLITA:")
        for problem in problems:
            print(" -", problem)
        sys.exit(1)
    print("Verifica del sito OK: sitemap, canonical, metadati, asset e link interni.")
