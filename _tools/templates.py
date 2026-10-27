# Modelli di pagina. Eseguito dopo build_site.py (stesso namespace): usa PAGES, TIERS, BASE, ecc.
import datetime
import runpy

EXTRA = runpy.run_path(str(pathlib.Path(__file__).with_name("content_extra.py")))
ABOUT = runpy.run_path(str(pathlib.Path(__file__).with_name("content_about.py")))["ABOUT"]
PRODUCTS = runpy.run_path(str(pathlib.Path(__file__).with_name("content_products.py")))["PRODUCTS"]
AREAS_DATA = runpy.run_path(str(pathlib.Path(__file__).with_name("content_areas.py")))
AREAS, AREA_SERVICES, PRIMARY_AREA = AREAS_DATA["AREAS"], AREAS_DATA["AREA_SERVICES"], AREAS_DATA["PRIMARY_AREA"]
TECH_TIERS, PRODUCTS_PAGE, WHERE_PAGE, CALLOUTS = AREAS_DATA["TECH_TIERS"], AREAS_DATA["PRODUCTS_PAGE"], AREAS_DATA["WHERE_PAGE"], AREAS_DATA["CALLOUTS"]
CARD_OVERRIDES = AREAS_DATA["CARD_OVERRIDES"]


def area_of(lang, key):
    return next(a for a in AREAS[lang] if a["key"] == key)


def area_services(lang, key):
    """Competenze dell'area come dict con href, card_title, card_who, card_points."""
    out = []
    for s in AREA_SERVICES[key]:
        if lang == "it":
            p = next(x for x in PAGES if x["slug"] == s)
            out.append(dict(p, href=s, **CARD_OVERRIDES.get((key, s), {}).get("it", {})))
        else:
            out.append(dict(EN_PAGES[s], href=EN_SLUG[s], **CARD_OVERRIDES.get((key, s), {}).get("en", {})))
    return out


def cur(flag):
    return ' aria-current="page"' if flag else ""
PRICES, CITIES, GUIDES, TEST = EXTRA["PRICES"], EXTRA["CITIES"], EXTRA["GUIDES"], EXTRA["TEST"]
EN_SLUG, EN_PAGES, EN_TIERS = EXTRA["EN_SLUG"], EXTRA["EN_PAGES"], EXTRA["EN_TIERS"]
TODAY = datetime.date.today().isoformat()

import hashlib
ASSET_V = {n: hashlib.sha1((REPO / n).read_bytes()).hexdigest()[:8] for n in ("styles.css", "overrides.css", "pages.css", "script.js")}

WA_EN = "https://wa.me/393454656749?text=" + quote("Hello, I'm writing from the JDEVPRO website about a project.")
MAILTO_EN = ("mailto:info@jdevpro.it?subject=" + quote("Project enquiry - JDEVPRO") + "&amp;body=" + quote(
    "Hello,\n\nExisting systems:\n\nWhat I want to achieve:\n\nRough timeline:\n\nCompany / contact:\n"))

UI = {
  "it": dict(lang="it", locale="it_IT", skip="Vai al contenuto", menu="Apri menu", navlabel="Navigazione principale",
             contact="Contatto", guides="Guide", home="Home", crumbs="Percorso", more="Approfondisci →",
             services="Competenze", all_services="Tutte le competenze",
             talk="Parliamone", see_examples="Vedi esempi reali", problem="Il problema", recognise="Ti riconosci?",
             get="Cosa ottieni", get_h="Cosa facciamo, in concreto.", method="Metodo", method_h="Come funziona.",
             examples="Esempi reali", examples_h="Dai nostri progetti.", faq="Domande frequenti",
             faq_h="Le risposte prima della domanda.", others="Altre competenze", visit="Visita ↗",
             sys_e="Sistemi già collegati", sys_h="Cosa abbiamo già integrato.",
             reach_e="Cosa possiamo integrare", reach_h="Se ha un'interfaccia, si può collegare.",
             reach_p="Tre strade, a seconda di cosa offre il sistema da collegare.",
             reach_note="Esempi di servizi e dispositivi integrabili. Nomi e marchi appartengono ai rispettivi proprietari; prima di ogni progetto verifichiamo accessi, limiti e condizioni d'uso.",
             price_e="Prezzi indicativi", price_h="Da dove si parte.", from_="da", per_month="al mese", once="una tantum",
             price_note="Prezzi di partenza indicativi. Il preventivo è a prezzo fisso, dopo aver verificato cosa serve davvero.",
             c_eyebrow="Contatto", c_h="Raccontaci cosa devi collegare.",
             c_p="Descrivici i sistemi che hai, cosa vuoi ottenere e i tempi. Ti rispondiamo per iscritto entro 24 ore, con domande mirate o con una proposta.",
             c_steps='<li><strong>Scrivici</strong> i sistemi presenti e l\'obiettivo, anche in poche righe.</li><li><strong>Ti rispondiamo entro 24 ore</strong> con domande mirate o una proposta di incontro.</li><li><strong>Definiamo</strong> insieme perimetro, tempi e modalità di lavoro.</li>',
             c_steps_label="Come funziona", c_mail="Scrivici una email", copy="Copia", copied="Copiato ✓",
             wa="Scrivici su WhatsApp ↗",
             li="Oppure su LinkedIn ↗", where="Tolmezzo (UD) · Friuli Venezia Giulia · Veneto · anche da remoto",
             f_who="Jacopo Ellero · Tolmezzo (UD)", privacy="privacy.html", cookie="cookie-policy.html", cv="cv.html",
             mailto=MAILTO, wa_url=WA),
  "en": dict(lang="en", locale="en_GB", skip="Skip to content", menu="Open menu", navlabel="Main navigation",
             contact="Contact", guides="Guides", home="Home", crumbs="Breadcrumb", more="Learn more →",
             services="Services", all_services="All services",
             talk="Let's talk", see_examples="See real examples", problem="The problem", recognise="Sound familiar?",
             get="What you get", get_h="What we do, in practice.", method="Method", method_h="How it works.",
             examples="Real examples", examples_h="From our projects.", faq="FAQ",
             faq_h="Answers before you ask.", others="Other services", visit="Visit ↗",
             sys_e="Already connected", sys_h="What we have already integrated.",
             reach_e="What we can integrate", reach_h="If it has an interface, it can be connected.",
             reach_p="Three routes, depending on what the system offers.",
             reach_note="Examples of services and devices that can be integrated. Names and trademarks belong to their owners; before each project we check access, limits and terms of use.",
             price_e="Indicative prices", price_h="Where it starts.", from_="from", per_month="per month", once="one-off",
             price_note="Indicative starting prices. Quotes are fixed-price, after checking what is really needed.",
             c_eyebrow="Contact", c_h="Tell us what you need to connect.",
             c_p="Describe your systems, what you want to achieve and your timeline. We reply in writing within 24 hours, with focused questions or a proposal.",
             c_steps="<li><strong>Write to us</strong> about your current systems and goal, even in a few lines.</li><li><strong>We reply within 24 hours</strong> with focused questions or a proposal for a meeting.</li><li><strong>We define</strong> scope, timeline and way of working together.</li>",
             c_steps_label="How it works", c_mail="Send us an email", copy="Copy", copied="Copied ✓",
             wa="Message us on WhatsApp ↗",
             li="Or on LinkedIn ↗", where="Tolmezzo (Udine), Italy · north-east Italy · remote projects",
             f_who="Jacopo Ellero · Tolmezzo, Italy", privacy="privacy-en.html", cookie="cookie-policy-en.html", cv="cv-en.html",
             mailto=MAILTO_EN, wa_url=WA_EN),
}

PRICE_EN = {"Collegamento di una macchina": "Connecting one machine", "Dati macchina e assistenza": "Machine data and support",
            "Prima versione del gestionale": "First version of the software", "Hosting, backup e assistenza": "Hosting, backups and support",
            "Progetto e configurazione": "Design and configuration", "Dati, allarmi e manutenzione": "Data, alarms and maintenance",
            "Integrazione tra due sistemi": "Integration between two systems", "Monitoraggio e manutenzione": "Monitoring and maintenance",
            "Sito con pannello di gestione": "Website with management panel", "Hosting e manutenzione": "Hosting and maintenance",
            "per tipo di macchina con interfacce documentate": "per machine type with documented interfaces", "per macchina": "per machine",
            "a prezzo fisso, sulla parte più utile": "fixed price, on the most useful part", "dispositivi esclusi": "devices excluded",
            "per dispositivo": "per device", "con API pubbliche": "with public APIs", "": "",
            "Assistenza e controllo da remoto": "Support and remote monitoring", "Configurazione dell'impianto": "System configuration",
            "Assistenza e aggiornamenti": "Support and updates", "Configurazione del centralino": "Phone system configuration",
            "Assistenza e modifiche": "Support and changes", "Controllo da remoto": "Remote monitoring",
            "telecamere e dispositivi esclusi": "cameras and devices excluded", "telefoni esclusi": "phones excluded", "apparati esclusi": "equipment excluded"}

ADDRESS = {"@type": "PostalAddress", "addressLocality": "Tolmezzo", "postalCode": "33028", "addressRegion": "UD",
           "addressCountry": "IT"}

ORG = {
  "@context": "https://schema.org", "@type": "ProfessionalService", "@id": ORG_ID, "name": "JDEVPRO",
  "url": BASE, "logo": BASE + "assets/icon-512.png", "image": BASE + "assets/og-jdevpro.jpg", "email": EMAIL,
  "vatID": "IT02783420306",
  "founder": {"@type": "Person", "name": "Jacopo Ellero", "url": BASE + "cv.html"},
  "address": ADDRESS,
  "geo": {"@type": "GeoCoordinates", "latitude": 46.4057, "longitude": 13.0154},
  "areaServed": [{"@type": "AdministrativeArea", "name": "Friuli Venezia Giulia"},
                 {"@type": "City", "name": "Udine"}, {"@type": "City", "name": "Pordenone"},
                 {"@type": "City", "name": "Trieste"}, {"@type": "City", "name": "Gorizia"},
                 {"@type": "AdministrativeArea", "name": "Veneto"}, {"@type": "Country", "name": "Italia"}],
  "description": "Interconnessione macchine 4.0, gestionali su misura, integrazioni, IoT, automazione per hotel e B&B, videosorveglianza, internet offgrid e siti web per aziende del Friuli Venezia Giulia e del Veneto.",
  "knowsLanguage": ["it", "en"],
  "sameAs": ["https://github.com/jellero", LI],
  "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Competenze JDEVPRO", "itemListElement": [
    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": p["service_type"], "url": BASE + p["slug"]}} for p in PAGES]},
}
ORG_REF = {"@context": "https://schema.org", "@type": "ProfessionalService", "@id": ORG_ID, "name": "JDEVPRO", "url": BASE,
           "address": ADDRESS}


def url_of(slug):
    return BASE + ("" if slug == "index.html" else slug)


def pages_for(lang):
    if lang == "it":
        return [dict(p, href=p["slug"]) for p in PAGES]
    out = []
    for p in PAGES:
        e = dict(EN_PAGES[p["slug"]])
        e.setdefault("chips", p["chips"])
        e["slug"] = EN_SLUG[p["slug"]]
        e["it_slug"] = p["slug"]
        e["href"] = e["slug"]
        out.append(e)
    return out


# ---------------------------------------------------------------- blocchi comuni

def head(title, desc, slug, jsonld, lang="it", alternates=None, robots="index,follow"):
    u = UI[lang]
    url = url_of(slug)
    ld = "\n".join(f'<script type="application/ld+json">\n{json.dumps(o, ensure_ascii=False, indent=1)}\n</script>' for o in jsonld)
    alt = ""
    if alternates:
        alt = "".join(f'<link href="{url_of(s)}" hreflang="{l}" rel="alternate"/>\n' for l, s in alternates)
        alt += f'<link href="{url_of(dict(alternates)["it"])}" hreflang="x-default" rel="alternate"/>\n'
    return f"""<!DOCTYPE html>
<html lang="{u['lang']}">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<title>{escape(title)}</title>
<meta content="{escape(desc)}" name="description"/>
<meta content="#07111f" name="theme-color"/>
<meta content="{robots}" name="robots"/>
<link href="{url}" rel="canonical"/>
<link href="favicon.ico" rel="icon" sizes="any"/>
<link href="assets/icon-32.png" rel="icon" type="image/png" sizes="32x32"/>
<link href="assets/icon-180.png" rel="apple-touch-icon"/>
<link href="styles.css?v={ASSET_V['styles.css']}" rel="stylesheet"/>
<link href="overrides.css?v={ASSET_V['overrides.css']}" rel="stylesheet"/>
<link href="pages.css?v={ASSET_V['pages.css']}" rel="stylesheet"/>
<meta property="og:title" content="{escape(title)}"/>
<meta property="og:description" content="{escape(desc)}"/>
<meta property="og:type" content="website"/>
<meta property="og:url" content="{url}"/>
<meta property="og:image" content="{BASE}assets/og-jdevpro.jpg"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta property="og:locale" content="{u['locale']}"/>
<meta name="twitter:card" content="summary_large_image"/>
{alt}{ld}
</head>
<body>
<a class="skip-link" href="#main">{u['skip']}</a>
"""


def header(current, lang="it", home=False, switch=None):
    u = UI[lang]
    home_slug = "index.html" if lang == "it" else "en.html"
    all_label = "Tutta l'area" if lang == "it" else "Whole area"
    links = ""
    for a in AREAS[lang]:
        svcs = area_services(lang, a["key"])
        active = current == a["slug"] or any(s["href"] == current for s in svcs)
        sub = f'<a class="nav-sub-all" href="{a["slug"]}"{cur(current == a["slug"])}>{all_label} →</a>\n' + "\n".join(
            f'<a href="{s["href"]}"{cur(s["href"] == current)}>{s["card_title"]}</a>' for s in svcs)
        links += (f'<div class="nav-group{" is-current" if active else ""}">'
                  f'<a class="nav-group-label" href="{a["slug"]}">{a["nav"]} <span aria-hidden="true">▾</span></a>'
                  f'<div class="nav-sub">\n{sub}\n</div></div>\n')
    pp = PRODUCTS_PAGE[lang]
    prods = PRODUCTS[lang]
    active = current == pp["slug"] or any(x["slug"] == current for x in prods)
    psub = f'<a class="nav-sub-all" href="{pp["slug"]}"{cur(current == pp["slug"])}>{"Tutti i prodotti" if lang == "it" else "All products"} →</a>\n' + "\n".join(
        f'<a href="{x["slug"]}"{ext(x["slug"])}{cur(x["slug"] == current)}>{x["nav"]}{" ↗" if x.get("external") else ""}</a>' for x in prods)
    links += (f'<div class="nav-group{" is-current" if active else ""}">'
              f'<a class="nav-group-label" href="{pp["slug"]}">{pp["nav"]} <span aria-hidden="true">▾</span></a>'
              f'<div class="nav-sub">\n{psub}\n</div></div>\n')
    if lang == "it":
        links += f'<a href="guide.html"{cur(current == "guide.html")}>Guide</a>\n'
    ab = ABOUT[lang]
    links += f'<a href="{ab["slug"]}"{cur(current == ab["slug"])}>{ab["nav"]}</a>'
    sw = ""
    if switch:
        if lang == "it":
            sw = f'<span aria-label="Lingua" class="language-switch"><strong aria-current="page">IT</strong><span>/</span><a href="{switch}" hreflang="en">EN</a></span>\n'
        else:
            sw = f'<span aria-label="Language" class="language-switch"><a href="{switch}" hreflang="it">IT</a><span>/</span><strong aria-current="page">EN</strong></span>\n'
    contact = "#contatto" if home else f"{home_slug}#contatto"
    return f"""<header class="site-header" data-header="">
<div class="shell nav-wrap">
<a aria-label="JDEVPRO home" class="brand" href="{'#top' if home else home_slug}"><img class="brand-logo" src="assets/logo-jdevpro-header.png" alt="JDEVPRO" width="440" height="259"></a>
<button aria-expanded="false" aria-label="{u['menu']}" class="menu-toggle" data-menu-toggle="" type="button"><span></span><span></span><span></span></button>
<nav aria-label="{u['navlabel']}" class="nav" data-nav="">
{links}
{sw}<a class="nav-cta" href="{contact}">{u['contact']}</a>
</nav>
</div>
</header>
"""


def contact(lang="it"):
    u = UI[lang]
    return f"""<section class="contact-section" id="contatto">
<div class="shell contact-card reveal">
<div>
<p class="eyebrow">{u['c_eyebrow']}</p>
<h2>{u['c_h']}</h2>
<p>{u['c_p']}</p>
<ol class="contact-steps" aria-label="{u['c_steps_label']}">{u['c_steps']}</ol>
</div>
<div class="contact-actions">
<a class="button light big" href="{u['mailto']}">{u['c_mail']}</a>
<button class="contact-copy" type="button" data-copy-email="{EMAIL}" data-copied-label="{u['copied']}"><span>{EMAIL}</span><em>{u['copy']}</em></button>
<a class="contact-whatsapp" href="{u['wa_url']}" rel="noreferrer" target="_blank">{u['wa']}</a>
<a class="contact-alt" href="{LI}" rel="noreferrer" target="_blank">{u['li']}</a>
<span>{u['where']}</span>
</div>
</div>
</section>
"""


def footer(lang="it"):
    u = UI[lang]
    links = "".join(f'<a href="{a["slug"]}">{a["nav"]}</a>' for a in AREAS[lang])
    links += f'<a href="{PRODUCTS_PAGE[lang]["slug"]}">{PRODUCTS_PAGE[lang]["nav"]}</a>'
    if lang == "it":
        links += '<a href="guide.html">Guide</a>'
        links += f'<a href="{WHERE_PAGE["slug"]}">{WHERE_PAGE["nav"]}</a>'
    links += f'<a href="{ABOUT[lang]["slug"]}">{ABOUT[lang]["nav"]}</a>'
    services = "".join(f'<a href="{p["href"]}">{p["card_title"]}</a>' for p in pages_for(lang))
    if lang == "it":
        services += "".join(f'<a href="{c["slug"]}">{c["name"]}</a>' for c in CITIES)
    return f"""<footer class="footer">
<div class="shell footer-grid footer-wide">
<div><strong>JDEVPRO</strong><span>{u['f_who']}</span></div>
<div class="footer-links">{links}</div>
<div><span>P.IVA IT02783420306</span><a href="{u['privacy']}">Privacy</a><a href="{u['cookie']}">Cookie</a><a href="{u['cv']}">CV</a><a href="https://github.com/jellero" rel="noreferrer" target="_blank">GitHub</a><a href="{LI}" rel="noreferrer" target="_blank">LinkedIn</a></div>
</div>
<div class="shell"><div class="footer-local">{services}</div></div>
</footer>
<script src="script.js?v={ASSET_V['script.js']}"></script>
</body>
</html>
"""


def groups_html(groups):
    return "\n".join(
        f'<div class="system-group reveal"><h3>{g}</h3><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul></div>'
        for g, items in groups)


def euro(n, lang):
    s = f"{n:,}".replace(",", "." if lang == "it" else ",")
    return f"{s} €" if lang == "it" else f"€{s}"


def price_block(it_slug, lang):
    rows = PRICES.get(it_slug)
    if not rows:
        return ""
    u = UI[lang]
    items = []
    for label, amount, kind, note in rows:
        if lang == "en":
            label, note = PRICE_EN[label], PRICE_EN[note]
        unit = u["per_month"] if kind == "al mese" else u["once"]
        items.append(f'<div class="price reveal"><span>{label}</span><strong>{u["from_"]} {euro(amount, lang)}</strong>'
                     f'<small>{unit}{" · " + note if note else ""}</small></div>')
    return f"""<section class="section section-tight section-white">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">{u['price_e']}</p><h2>{u['price_h']}</h2></div>
<div>
<div class="price-grid">{''.join(items)}</div>
<p class="catalog-note">{u['price_note']}</p>
</div>
</div>
</section>
"""


def offers_ld(it_slug):
    rows = PRICES.get(it_slug, [])
    return [{"@type": "Offer", "name": r[0], "priceCurrency": "EUR",
             "priceSpecification": {"@type": "PriceSpecification", "minPrice": r[1], "priceCurrency": "EUR"}} for r in rows]


# ---------------------------------------------------------------- home

def home(lang="it"):
    u = UI[lang]
    if lang == "it":
        t = dict(eyebrow="Software su misura e integrazioni · Friuli Venezia Giulia",
                 h1="Colleghiamo macchine, gestionali e dispositivi. <span>E li teniamo funzionanti.</span>",
                 lead="JDEVPRO nasce a Tolmezzo con Jacopo Ellero. Sviluppiamo gestionali su misura, colleghiamo macchine, sensori e dispositivi ai sistemi aziendali e seguiamo tutto in produzione, per aziende e strutture del Friuli Venezia Giulia e del Veneto.",
                 b1="Scegli la tua area", b2="Scrivici", ae="Da dove parti?", ah="Tre aree, un solo interlocutore.",
                 enter="Entra nell'area →",
                 proof=[("10 macchine in produzione", "Collegate al gestionale a Tolmezzo, tra falegnamerie e stamperie.", "interconnessione-macchine-industria-4-0.html"),
                        ("JD Industry", "Gestionale di produzione collegato a macchine SCM ed Essetre.", "industria.html"),
                        ("E-commerce e marketplace", "Gestionale collegato a fornitore, marketplace e corriere.", "integrazione-software-api.html"),
                        ("Prodotti", "Welora, AKIOS e ORYVAEL: i nostri progetti.", "prodotti.html")],
                 who='<strong>JDEVPRO</strong> è l\'attività di Jacopo Ellero, sviluppatore e integratore di sistemi. <a href="chi-sono.html">Chi sono →</a> · <a href="dove-lavoriamo.html">Dove lavoriamo →</a>',
                 title="JDEVPRO · Gestionali, macchine 4.0 e IoT in Friuli",
                 desc="Gestionali su misura, macchine 4.0, integrazioni, IoT, automazione hotel e B&B, videosorveglianza e internet offgrid in Friuli Venezia Giulia.")
    else:
        t = dict(eyebrow="Custom software and integrations · North-east Italy",
                 h1="We connect machines, business software and devices. <span>And keep them running.</span>",
                 lead="JDEVPRO was founded in Tolmezzo, Friuli, by Jacopo Ellero. We build custom business software, connect machines, sensors and devices to company systems and look after everything in production, for companies and properties in north-east Italy and remotely.",
                 b1="Choose your area", b2="Write to us", ae="Where do you start?", ah="Three areas, one partner.",
                 enter="Enter the area →",
                 proof=[("10 machines in production", "Connected to business software in Tolmezzo, across woodworking and metal pressing companies.", "en-machine-interconnection.html"),
                        ("JD Industry", "Production management connected to SCM and Essetre machines.", "en-industry.html"),
                        ("E-commerce and marketplaces", "Business software connected to supplier, marketplaces and courier.", "en-software-integration-api.html"),
                        ("Products", "Welora, AKIOS and ORYVAEL: our own projects.", "en-products.html")],
                 who='<strong>JDEVPRO</strong> is the business of Jacopo Ellero, software developer and systems integrator. <a href="en-about.html">About me →</a>',
                 title="JDEVPRO · Business software, machines 4.0 and IoT, Italy",
                 desc="Custom business software, machines 4.0, integrations, IoT, hotel automation, video surveillance and off-grid internet in north-east Italy.")
    cards = ""
    for a in AREAS[lang]:
        svc = "".join(f'<li><a href="{s["href"]}">{s["card_title"]}</a></li>' for s in area_services(lang, a["key"]))
        cards += f"""<article class="area-card area-{a['key']} reveal">
<p class="eyebrow">{a['eyebrow']}</p>
<h3><a href="{a['slug']}">{a['nav']}</a></h3>
<p>{a['card']}</p>
<ul>{svc}</ul>
<a class="competence-more" href="{a['slug']}">{t['enter']}</a>
</article>
"""
    proof = "".join(f'<a href="{h}"><strong>{x}</strong><span>{d}</span></a>' for x, d, h in t["proof"])
    body = f"""{header("index.html" if lang == "it" else "en.html", lang, home=True, switch="en.html" if lang == "it" else "index.html")}<main id="main">
<section class="hero hero-min" id="top">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell hero-min-copy reveal">
<p class="eyebrow">{t['eyebrow']}</p>
<h1>{t['h1']}</h1>
<p class="hero-lead">{t['lead']}</p>
<div class="hero-actions">
<a class="button primary" href="#aree">{t['b1']}</a>
<a class="button ghost" href="#contatto">{t['b2']}</a>
</div>
</div>
</section>
<section class="section" id="aree">
<span id="competenze"></span>
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{t['ae']}</p><h2>{t['ah']}</h2></div>
<div class="area-grid">
{cards}</div>
</div>
</section>
<section class="section section-tight proof-band">
<div class="shell">
<div class="proof-grid proof-links reveal">{proof}</div>
<p class="proof-who reveal">{t['who']}</p>
</div>
</section>
{contact(lang)}</main>
"""
    slug = "index.html" if lang == "it" else "en.html"
    org = ORG if lang == "it" else dict(ORG, description="Industry 4.0 machine interconnection, custom business software, IoT, hotel automation, video surveillance and off-grid internet for companies in north-east Italy.")
    return head(t["title"], t["desc"], slug, [org], lang, alternates=[("it", "index.html"), ("en", "en.html")]) + body + footer(lang)


def area_page(a, lang):
    u = UI[lang]
    home_slug = "index.html" if lang == "it" else "en.html"
    url = url_of(a["slug"])
    other = area_of("en" if lang == "it" else "it", a["key"])["slug"]
    svcs = area_services(lang, a["key"])
    cards = "\n".join(f"""<a class="competence-card reveal" href="{s['href']}">
<span class="competence-num">{i:02d}</span>
<h3>{s['card_title']}</h3>
<p>{s['card_who']}</p>
<ul>{''.join(f'<li>{x}</li>' for x in s['card_points'])}</ul>
<span class="competence-more">{u['more']}</span>
</a>""" for i, s in enumerate(svcs, 1))
    who = "".join(f"<li>{x}</li>" for x in a["who"])
    proof = "".join(f"<div><strong>{x}</strong><span>{d}</span></div>" for x, d in a["proof"])
    guides = ""
    if lang == "it" and a["guides"]:
        allg = {g["slug"]: g for g in [TEST] + GUIDES}
        guides = f"""<section class="section section-tight section-white">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Guide e strumenti</p><h2>Per capire prima di chiedere.</h2></div>
<div class="related-grid">{''.join(f'<a href="{s}"><strong>{allg[s]["short"]}</strong><span>{allg[s]["desc"]}</span></a>' for s in a["guides"])}</div>
</div>
</section>
"""
    others = "".join(f'<a href="{o["slug"]}"><strong>{o["nav"]}</strong><span>{o["card"]}</span></a>' for o in AREAS[lang] if o["key"] != a["key"])
    labels = ("Per chi lavoriamo", "Competenze", "Cosa facciamo in quest'area.", "Esempi", "Già fatto.", "Altre aree") if lang == "it" else \
             ("Who we work with", "Services", "What we do in this area.", "Examples", "Already done.", "Other areas")
    jsonld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": a["nav"], "description": a["desc"], "url": url,
               "hasPart": [{"@type": "Service", "name": s["card_title"], "url": BASE + s["href"]} for s in svcs], "publisher": {"@id": ORG_ID}},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": u["home"], "item": url_of(home_slug)},
                  {"@type": "ListItem", "position": 2, "name": a["nav"], "item": url}]}, ORG_REF]
    body = f"""{header(a['slug'], lang, switch=other)}<main id="main">
<section class="hero page-hero area-hero-{a['key']}">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell page-hero-copy reveal">
<nav aria-label="{u['crumbs']}" class="breadcrumb"><a href="{home_slug}">{u['home']}</a><span>/</span><span aria-current="page">{a['nav']}</span></nav>
<p class="eyebrow">{a['eyebrow']}</p>
<h1>{a['h1']}</h1>
<p class="hero-lead">{a['lead']}</p>
<ul class="who-chips">{who}</ul>
<div class="hero-actions"><a class="button primary" href="#competenze">{labels[1]}</a><a class="button ghost" href="#contatto">{u['talk']}</a></div>
</div>
</section>
<section class="section section-tight" id="competenze">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{labels[1]}</p><h2>{labels[2]}</h2></div>
<div class="competence-grid">
{cards}
</div>
</div>
</section>
<section class="section section-tight proof-band">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{labels[3]}</p><h2>{labels[4]}</h2></div>
<div class="proof-grid proof-three reveal">{proof}</div>
</div>
</section>
{guides}{contact(lang)}<section class="section section-tight related">
<div class="shell">
<p class="eyebrow">{labels[5]}</p>
<div class="related-grid">{others}</div>
</div>
</section>
</main>
"""
    alternates = [("it", area_of("it", a["key"])["slug"]), ("en", area_of("en", a["key"])["slug"])]
    return head(a["title"], a["desc"], a["slug"], jsonld, lang, alternates=alternates) + body + footer(lang)


def products_index(lang):
    u = UI[lang]
    pp = PRODUCTS_PAGE[lang]
    home_slug = "index.html" if lang == "it" else "en.html"
    other = PRODUCTS_PAGE["en" if lang == "it" else "it"]["slug"]
    rows = ""
    for x in PRODUCTS[lang]:
        pts = "".join(f"<li>{p}</li>" for p in pp["points"][x["key"]])
        label = x["slug"].split("//")[1].rstrip("/") + " ↗" if x.get("external") else u["more"]
        rows += f"""<article class="product-row product-card-{x['key']} reveal">
<div><p class="eyebrow">{x['eyebrow']}</p><h2>{x['nav']}</h2><p class="product-card-text">{x['card']}</p>
<a class="button primary" href="{x['slug']}"{ext(x['slug'])}>{label}</a></div>
<ul class="status-list">{pts}</ul>
</article>
"""
    jsonld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": pp["nav"], "description": pp["desc"], "url": url_of(pp["slug"]),
               "hasPart": [{"@type": "CreativeWork", "name": x["nav"], "url": x["slug"] if x.get("external") else BASE + x["slug"]} for x in PRODUCTS[lang]]},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": u["home"], "item": url_of(home_slug)},
                  {"@type": "ListItem", "position": 2, "name": pp["nav"], "item": url_of(pp["slug"])}]}, ORG_REF]
    body = f"""{header(pp['slug'], lang, switch=other)}<main id="main">
<section class="hero page-hero">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell page-hero-copy reveal">
<nav aria-label="{u['crumbs']}" class="breadcrumb"><a href="{home_slug}">{u['home']}</a><span>/</span><span aria-current="page">{pp['nav']}</span></nav>
<p class="eyebrow">{pp['eyebrow']}</p>
<h1>{pp['h1']}</h1>
<p class="hero-lead">{pp['lead']}</p>
</div>
</section>
<section class="section section-tight section-dark">
<div class="shell product-rows">
{rows}</div>
</section>
{contact(lang)}</main>
"""
    return head(pp["title"], pp["desc"], pp["slug"], jsonld, lang,
                alternates=[("it", PRODUCTS_PAGE["it"]["slug"]), ("en", PRODUCTS_PAGE["en"]["slug"])]) + body + footer(lang)


def where_page():
    w = WHERE_PAGE
    cards = ""
    for c in CITIES:
        sectors = "".join(f"<li>{s[0]}</li>" for s in c["sectors"])
        cards += f"""<a class="competence-card reveal" href="{c['slug']}">
<p class="eyebrow">{c['area_title']}</p>
<h3>{c['name']}</h3>
<ul>{sectors}</ul>
<span class="competence-more">Approfondisci →</span>
</a>
"""
    cards += """<div class="competence-card competence-plain reveal">
<p class="eyebrow">Veneto e resto d'Italia</p>
<h3>Anche da remoto</h3>
<p>Gestionali, integrazioni, siti e assistenza si seguono quasi sempre a distanza; veniamo sul posto quando serve.</p>
</div>
"""
    jsonld = [{"@context": "https://schema.org", "@type": "WebPage", "name": w["nav"], "description": w["desc"], "url": url_of(w["slug"]),
               "about": {"@id": ORG_ID}},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
                  {"@type": "ListItem", "position": 2, "name": w["nav"], "item": url_of(w["slug"])}]}, ORG]
    body = f"""{header(w['slug'])}<main id="main">
<section class="hero page-hero">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell page-hero-copy reveal">
<nav aria-label="Percorso" class="breadcrumb"><a href="index.html">Home</a><span>/</span><span aria-current="page">{w['nav']}</span></nav>
<p class="eyebrow">{w['eyebrow']}</p>
<h1>{w['h1']}</h1>
<p class="hero-lead">{w['lead']}</p>
</div>
</section>
<section class="section section-tight">
<div class="shell"><div class="competence-grid">
{cards}</div></div>
</section>
{contact()}</main>
"""
    return head(w["title"], w["desc"], w["slug"], jsonld) + body + footer()


# ---------------------------------------------------------------- pagine competenza

def service(p, lang="it"):
    u = UI[lang]
    it_slug = p.get("it_slug", p["slug"])
    url = url_of(p["slug"])
    home_slug = "index.html" if lang == "it" else "en.html"
    area = area_of(lang, PRIMARY_AREA[it_slug])
    svc = {"@context": "https://schema.org", "@type": "Service", "name": p["service_type"], "serviceType": p["service_type"],
           "description": p["desc"], "url": url, "provider": {"@id": ORG_ID},
           "areaServed": ["Friuli Venezia Giulia", "Veneto", "Italia"]}
    if offers_ld(it_slug):
        svc["offers"] = offers_ld(it_slug)
    jsonld = [svc,
      {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
      {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": u["home"], "item": url_of(home_slug)},
        {"@type": "ListItem", "position": 2, "name": area["nav"], "item": url_of(area["slug"])},
        {"@type": "ListItem", "position": 3, "name": p["card_title"], "item": url}]},
      ORG_REF]
    problems = "\n".join(f'<li><strong>{a}</strong> {b}</li>' for a, b in p["problems"])
    outcomes = "\n".join(f'<article class="outcome reveal"><h3>{a}</h3><p>{b}</p></article>' for a, b in p["outcomes"])
    steps = "\n".join(f'<li><strong>{a}</strong><span>{b}</span></li>' for a, b in p["steps"])

    def ex(t, d, link):
        more = ""
        if link and (lang == "it" or link.startswith("http")):
            ext = link.startswith("http")
            more = f'<a class="card-link" href="{link}"{" rel=\"noreferrer\" target=\"_blank\"" if ext else ""}>{u["visit"] if ext else u["more"]}</a>'
        return f'<article class="example reveal"><h3>{t}</h3><p>{d}</p>{more}</article>'
    examples = "\n".join(ex(*e) for e in p["examples"])
    systems = ""
    if p.get("systems"):
        systems = f"""<section class="section section-tight section-white">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{u['sys_e']}</p><h2>{u['sys_h']}</h2></div>
<div class="system-groups">
{groups_html(p['systems'])}
</div>
</div>
</section>
"""
    reach = ""
    if p.get("catalog"):
        tiers_src = TIERS if lang == "it" else EN_TIERS
        tiers = "\n".join(
            f'<article class="tier reveal"><span class="competence-num">0{i}</span><h3>{a}</h3><p>{b}</p></article>'
            for i, (a, b) in enumerate(tiers_src, 1))
        if it_slug in TECH_TIERS:
            intro = f"""<div class="section-heading reveal"><p class="eyebrow">{u['reach_e']}</p><h2>{u['reach_h']}</h2><p>{u['reach_p']}</p></div>
<div class="tier-grid">
{tiers}
</div>"""
        else:
            intro = f"""<div class="section-heading reveal"><p class="eyebrow">{u['reach_e']}</p><h2>{"Marche e sistemi compatibili." if lang == "it" else "Compatible brands and systems."}</h2></div>"""
        reach = f"""<section class="section section-tight section-paper">
<div class="shell">
{intro}
<div class="system-groups catalog">
{groups_html(p['catalog'])}
</div>
<p class="catalog-note">{u['reach_note']}</p>
</div>
</section>
"""
    chips = "".join(f"<span>{c}</span>" for c in p["chips"])
    faq = "\n".join(f'<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>' for q, a in p["faq"])
    same = [s for s in area_services(lang, area["key"]) if s["href"] != p["slug"]]
    related = "".join(f'<a href="{o["href"]}"><strong>{o["card_title"]}</strong><span>{o["card_who"]}</span></a>' for o in same)
    other_areas = "".join(f'<a href="{o["slug"]}"><strong>{o["nav"]}</strong><span>{o["card"]}</span></a>' for o in AREAS[lang] if o["key"] != area["key"])
    guide_links = ""
    if lang == "it":
        gl = [g for g in GUIDES if g["cta"] == it_slug]
        if it_slug == "interconnessione-macchine-industria-4-0.html":
            gl = [TEST] + gl
        if gl:
            guide_links = '<p class="eyebrow local-eyebrow">Guide collegate</p><div class="related-grid">' + "".join(
                f'<a href="{g["slug"]}"><strong>{g["short"]}</strong><span>{g["desc"]}</span></a>' for g in gl) + "</div>"
    switch = EN_SLUG[it_slug] if lang == "it" else it_slug
    body = f"""{header(p['slug'], lang, switch=switch)}<main id="main">
<section class="hero page-hero">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell page-hero-copy reveal">
<nav aria-label="{u['crumbs']}" class="breadcrumb"><a href="{home_slug}">{u['home']}</a><span>/</span><a href="{area['slug']}">{area['nav']}</a><span>/</span><span aria-current="page">{p['card_title']}</span></nav>
<p class="eyebrow">{p['eyebrow']}</p>
<h1>{p['h1']}</h1>
<p class="hero-lead">{p['lead']}</p>
{f'<p class="hero-proof">{p["proof"]}</p>' if p.get("proof") else ''}
{(lambda c: f'<p class="hero-callout">{c[0]} <a href="{c[2]}" rel="noreferrer" target="_blank">{c[1]}</a></p>' if c else '')(CALLOUTS.get(it_slug, {}).get(lang))}
<div class="hero-actions">
<a class="button primary" href="#contatto">{u['talk']}</a>
{f'<a class="button ghost" href="#esempi">{u["see_examples"]}</a>' if p["examples"] else ''}
</div>
</div>
</section>
<section class="section section-tight section-white">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">{u['problem']}</p><h2>{u['recognise']}</h2></div>
<ul class="problem-list reveal">
{problems}
</ul>
</div>
</section>
<section class="section section-tight section-paper">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{u['get']}</p><h2>{u['get_h']}</h2></div>
<div class="outcome-grid">
{outcomes}
</div>
</div>
</section>
{systems}{reach}<section class="section section-tight section-white">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">{u['method']}</p><h2>{u['method_h']}</h2></div>
<ol class="method-steps reveal">
{steps}
</ol>
</div>
</section>
{price_block(it_slug, lang)}{f'''<section class="section section-tight section-dark" id="esempi">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{u['examples']}</p><h2>{u['examples_h']}</h2></div>
<div class="example-grid">
{examples}
</div>
<div class="chips reveal" aria-label="Tech">{chips}</div>
</div>
</section>
''' if p["examples"] else ''}<section class="section section-tight">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">{u['faq']}</p><h2>{u['faq_h']}</h2></div>
<div class="faq reveal">
{faq}
</div>
</div>
</section>
{contact(lang)}<section class="section section-tight related">
<div class="shell">
{guide_links}<p class="eyebrow">{("Nella stessa area: " if lang == "it" else "In the same area: ") + area["nav"]}</p>
<div class="related-grid">{related}</div>
<p class="eyebrow local-eyebrow">{"Altre aree" if lang == "it" else "Other areas"}</p>
<div class="related-grid">{other_areas}</div>
</div>
</section>
</main>
"""
    return head(p["title"], p["desc"], p["slug"], jsonld, lang,
                alternates=[("it", it_slug), ("en", EN_SLUG[it_slug])]) + body + footer(lang)


# ---------------------------------------------------------------- città

def city(c):
    url = url_of(c["slug"])
    sectors = "\n".join(f'<article class="outcome reveal"><h3>{a}</h3><p>{b}</p></article>' for a, b in c["sectors"])
    faq = "\n".join(f'<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>' for q, a in c["faq"])
    services = "".join(f'<a href="{p["slug"]}"><strong>{p["card_title"]}</strong><span>{p["card_who"]}</span></a>' for p in PAGES)
    jsonld = [
      {"@context": "https://schema.org", "@type": "Service", "name": f"Software, gestionali e integrazioni a {c['name']}",
       "description": c["desc"], "url": url, "provider": {"@id": ORG_ID},
       "areaServed": [{"@type": "City", "name": n.strip()} for n in c["name"].split(" e ")]},
      {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]]},
      {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
        {"@type": "ListItem", "position": 2, "name": c["name"], "item": url}]},
      ORG_REF]
    body = f"""{header(c['slug'])}<main id="main">
<section class="hero page-hero">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell page-hero-copy reveal">
<nav aria-label="Percorso" class="breadcrumb"><a href="index.html">Home</a><span>/</span><span aria-current="page">{c['name']}</span></nav>
<p class="eyebrow">{c['area_title']}</p>
<h1>Software, gestionali e integrazioni a <span>{c['name']}.</span></h1>
<p class="hero-lead">{c['lead']}</p>
<div class="hero-actions">
<a class="button primary" href="#contatto">Parliamone</a>
<a class="button ghost" href="#competenze">Cosa facciamo</a>
</div>
</div>
</section>
<section class="section section-tight section-paper">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Settori</p><h2>Cosa facciamo per le aziende della {c['area']}.</h2></div>
<div class="outcome-grid">
{sectors}
</div>
</div>
</section>
<section class="section section-tight section-white">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">Come lavoriamo</p><h2>Vicini quando serve, da remoto il resto.</h2></div>
<ol class="method-steps reveal">
<li><strong>Analisi in azienda</strong><span>Vediamo macchine, programmi e processi dove lavorano davvero.</span></li>
<li><strong>Proposta a prezzo fisso</strong><span>Fasi chiare, si parte dalla parte più utile.</span></li>
<li><strong>Sviluppo e collaudo</strong><span>Sviluppo da remoto, collaudo sul posto con i dati reali.</span></li>
<li><strong>Assistenza continua</strong><span>Canone mensile con backup, aggiornamenti e interventi.</span></li>
</ol>
</div>
</section>
<section class="section section-tight" id="competenze">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Competenze</p><h2>Cosa facciamo.</h2></div>
<div class="related-grid">{services}</div>
</div>
</section>
<section class="section section-tight section-white">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">Domande frequenti</p><h2>{c['name']}: le domande più comuni.</h2></div>
<div class="faq reveal">
{faq}
</div>
</div>
</section>
{contact()}</main>
"""
    return head(c["title"], c["desc"], c["slug"], jsonld) + body + footer()


# ---------------------------------------------------------------- guide

def render_block(b):
    if isinstance(b, list):
        return "<ul>" + "".join(f"<li>{i}</li>" for i in b) + "</ul>"
    return f"<p>{b}</p>"


def guide(g):
    url = url_of(g["slug"])
    sections = "\n".join(f'<h2>{h}</h2>\n' + "\n".join(render_block(b) for b in blocks) for h, blocks in g["sections"])
    target = next(p for p in PAGES if p["slug"] == g["cta"])
    jsonld = [
      {"@context": "https://schema.org", "@type": "Article", "headline": g["short"], "description": g["desc"],
       "url": url, "inLanguage": "it", "datePublished": "2026-10-27", "dateModified": TODAY,
       "author": {"@type": "Person", "name": "Jacopo Ellero", "url": BASE + "cv.html"},
       "publisher": {"@id": ORG_ID}, "image": BASE + "assets/og-jdevpro.jpg"},
      {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
        {"@type": "ListItem", "position": 2, "name": "Guide", "item": BASE + "guide.html"},
        {"@type": "ListItem", "position": 3, "name": g["short"], "item": url}]},
      ORG_REF]
    body = f"""{header(g['slug'])}<main id="main">
<section class="hero page-hero">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell page-hero-copy reveal">
<nav aria-label="Percorso" class="breadcrumb"><a href="index.html">Home</a><span>/</span><a href="guide.html">Guide</a><span>/</span><span aria-current="page">{g['short']}</span></nav>
<p class="eyebrow">Guida JDEVPRO</p>
<h1>{g['h1']}</h1>
<p class="hero-lead">{g['intro']}</p>
</div>
</section>
<section class="section section-tight section-white">
<div class="shell article">
{sections}
<div class="article-cta">
<p><strong>Ti serve una mano?</strong> {target['card_title']}: metodo, esempi e prezzi indicativi.</p>
<a class="button primary" href="{target['slug']}">Vai alla pagina →</a>
</div>
</div>
</section>
{contact()}</main>
"""
    return head(g["title"], g["desc"], g["slug"], jsonld) + body + footer()


def guide_index():
    items = "".join(f'<a href="{x["slug"]}"><strong>{x["short"]}</strong><span>{x["desc"]}</span></a>' for x in [TEST] + GUIDES)
    jsonld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Guide JDEVPRO", "url": BASE + "guide.html",
               "hasPart": [{"@type": "Article", "headline": g["short"], "url": BASE + g["slug"]} for g in GUIDES]}, ORG_REF]
    body = f"""{header('guide.html')}<main id="main">
<section class="hero page-hero">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell page-hero-copy reveal">
<nav aria-label="Percorso" class="breadcrumb"><a href="index.html">Home</a><span>/</span><span aria-current="page">Guide</span></nav>
<p class="eyebrow">Guide e strumenti</p>
<h1>Guide pratiche su <span>macchine, integrazioni e dati.</span></h1>
<p class="hero-lead">Spiegazioni concrete per capire cosa serve prima di chiedere un preventivo.</p>
</div>
</section>
<section class="section section-tight section-white">
<div class="shell"><div class="related-grid guides-grid">{items}</div></div>
</section>
{contact()}</main>
"""
    return head("Guide su interconnessione 4.0, integrazioni e IoT | JDEVPRO",
                "Guide pratiche su interconnessione 4.0 e iperammortamento, collegamento di Amazon ed eBay al gestionale e integrazione di sistemi senza API.",
                "guide.html", jsonld) + body + footer()


TEST_JS = """<script>
(() => {
  const form = document.querySelector('[data-quiz]');
  if (!form) return;
  const out = form.querySelector('[data-quiz-result]');
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const total = form.querySelectorAll('fieldset').length;
    const answered = form.querySelectorAll('input:checked').length;
    if (answered < total) {
      out.className = 'quiz-result warn';
      out.innerHTML = '<strong>Rispondi a tutte le domande.</strong>';
      return;
    }
    const yes = form.querySelectorAll('input[value="si"]:checked').length;
    let cls = 'bad';
    let text = '<strong>Probabilmente non interconnesse.</strong> Lo scambio di dati con il sistema aziendale manca o è troppo debole: senza interconnessione rischi di perdere l\\u2019agevolazione.';
    if (yes === total) {
      cls = 'good';
      text = '<strong>Probabilmente interconnesse.</strong> Conserva documentazione e storico degli scambi da mostrare al perito.';
    } else if (yes >= 3) {
      cls = 'warn';
      text = '<strong>Interconnessione parziale.</strong> Alcuni requisiti tecnici sembrano mancare: conviene completarli prima della perizia.';
    }
    out.className = 'quiz-result ' + cls;
    out.innerHTML = text + ' <a href="interconnessione-macchine-industria-4-0.html#contatto">Scrivici per una verifica \\u2192</a>';
  });
})();
</script>
"""


def test_page():
    q = "\n".join(f"""<fieldset class="quiz-q">
<legend><span>0{i}</span>{text}</legend>
<label><input type="radio" name="q{i}" value="si" required> Sì</label>
<label><input type="radio" name="q{i}" value="no"> No</label>
</fieldset>""" for i, text in enumerate(TEST["questions"], 1))
    url = url_of(TEST["slug"])
    jsonld = [{"@context": "https://schema.org", "@type": "WebPage", "name": TEST["short"], "description": TEST["desc"], "url": url,
               "isPartOf": {"@type": "WebSite", "url": BASE}, "publisher": {"@id": ORG_ID}},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
                {"@type": "ListItem", "position": 2, "name": "Guide", "item": BASE + "guide.html"},
                {"@type": "ListItem", "position": 3, "name": TEST["short"], "item": url}]}, ORG_REF]
    body = f"""{header(TEST['slug'])}<main id="main">
<section class="hero page-hero">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell page-hero-copy reveal">
<nav aria-label="Percorso" class="breadcrumb"><a href="index.html">Home</a><span>/</span><a href="guide.html">Guide</a><span>/</span><span aria-current="page">Test interconnessione</span></nav>
<p class="eyebrow">Test · 1 minuto</p>
<h1>Le tue macchine sono <span>interconnesse davvero?</span></h1>
<p class="hero-lead">Sei domande per capire se lo scambio di dati con il sistema aziendale è reale o se rischi di perdere l'iperammortamento. Le risposte restano nel tuo browser.</p>
</div>
</section>
<section class="section section-tight section-white">
<div class="shell article">
<form class="quiz" data-quiz>
{q}
<button class="button primary" type="submit">Vedi il risultato</button>
<div class="quiz-result" data-quiz-result aria-live="polite"></div>
</form>
<p class="catalog-note">Il test dà un'indicazione tecnica e non sostituisce la perizia. Per i requisiti completi leggi la <a href="guida-interconnessione-iperammortamento.html">guida all'interconnessione 4.0</a>.</p>
</div>
</section>
{contact()}</main>
{TEST_JS}"""
    return head(TEST["title"], TEST["desc"], TEST["slug"], jsonld) + body + footer()


# ---------------------------------------------------------------- 404 e vecchi indirizzi

def not_found():
    body = f"""{header(None)}<main id="main">
<section class="hero page-hero">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell page-hero-copy">
<p class="eyebrow">Errore 404</p>
<h1>Pagina non trovata. <span>Ecco da dove ripartire.</span></h1>
<p class="hero-lead">La pagina potrebbe essere stata spostata durante il rinnovo del sito.</p>
<div class="hero-actions"><a class="button primary" href="/">Vai alla home</a><a class="button ghost" href="/guide.html">Guide</a></div>
</div>
</section>
<section class="section section-tight section-white">
<div class="shell"><div class="related-grid">{''.join(f'<a href="/{p["slug"]}"><strong>{p["card_title"]}</strong><span>{p["card_who"]}</span></a>' for p in PAGES)}</div></div>
</section>
</main>
"""
    html = head("Pagina non trovata | JDEVPRO", "La pagina cercata non esiste più.", "404.html", [], robots="noindex,follow") + body + footer()
    # percorsi assoluti: la 404 può essere servita da qualsiasi cartella
    for a in ('href="styles.css', 'href="overrides.css', 'href="pages.css', 'href="favicon.ico"', 'src="script.js',
              'href="assets/', 'src="assets/', 'href="index.html', 'href="privacy.html"', 'href="cookie-policy.html"', 'href="cv.html"', 'href="guide.html"'):
        html = html.replace(a, a.replace('="', '="/', 1))
    for p in PAGES:
        html = html.replace(f'href="{p["slug"]}"', f'href="/{p["slug"]}"')
    for c in CITIES:
        html = html.replace(f'href="{c["slug"]}"', f'href="/{c["slug"]}"')
    return html


OLD_URLS = {"privacy-policy": "/privacy.html", "privacy": "/privacy.html", "cookie-policy": "/cookie-policy.html",
            "privacy-policy-en": "/privacy-en.html", "privacy-en": "/privacy-en.html", "cookie-policy-en": "/cookie-policy-en.html"}


def redirect_stub(target):
    return f"""<!DOCTYPE html>
<html lang="it"><head><meta charset="utf-8"/><title>Pagina spostata</title>
<meta content="noindex,follow" name="robots"/>
<link href="{BASE.rstrip('/')}{target}" rel="canonical"/>
<meta http-equiv="refresh" content="0; url={target}"/>
</head><body><p>Pagina spostata: <a href="{target}">{BASE.rstrip('/')}{target}</a></p></body></html>
"""


# ---------------------------------------------------------------- chi sono

def about(lang="it"):
    a = ABOUT[lang]
    other = ABOUT["en" if lang == "it" else "it"]["slug"]
    home_slug = "index.html" if lang == "it" else "en.html"
    url = url_of(a["slug"])
    profile = "".join(f"<p>{x}</p>" for x in a["profile"])
    skills = "\n".join(
        f'<article class="pillar reveal"><span class="competence-num">0{i}</span><h3>{h}</h3><p>{d}</p>'
        f'<ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></article>'
        for i, (h, d, items) in enumerate(a["skills"], 1))
    certs = "".join(f'<article class="cert reveal"><strong>{h}</strong><span>{d}</span></article>' for h, d in a["certs"])
    path = "".join(f'<li><span class="when">{w}</span><strong>{role}</strong><span>{d}</span></li>' for w, role, d in a["path"])

    def ext_attr(link):
        return ' rel="noreferrer" target="_blank"' if link.startswith("http") else ""

    projects = "".join(
        f'<a href="{link}"{ext_attr(link)}><strong>{n}{" ↗" if link.startswith("http") else ""}</strong><span>{d}</span></a>'
        for n, d, link in a["projects"])
    edu = "".join(f"<div><strong>{h}</strong><span>{d}</span></div>" for h, d in a["edu"])
    links = "".join(
        f'<a class="button {"primary" if i == 0 else "ghost dark"}" href="{l}"{ext_attr(l)}>{n}</a>'
        for i, (n, l) in enumerate(a["links"]))
    person = {"@context": "https://schema.org", "@type": "Person", "name": "Jacopo Ellero", "url": url,
              "jobTitle": "Sviluppatore e integratore di sistemi" if lang == "it" else "Software developer and systems integrator",
              "worksFor": {"@id": ORG_ID}, "address": ADDRESS,
              "knowsAbout": [s[0] for s in a["skills"]],
              "hasCredential": [{"@type": "EducationalOccupationalCredential", "name": c[0], "description": c[1]} for c in a["certs"]],
              "sameAs": ["https://github.com/jellero", LI]}
    jsonld = [{"@context": "https://schema.org", "@type": "ProfilePage", "url": url, "mainEntity": person},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": UI[lang]["home"], "item": url_of(home_slug)},
                  {"@type": "ListItem", "position": 2, "name": a["nav"], "item": url}]},
              ORG_REF]
    profile_e, profile_h = ("Profilo", "Come lavoro.") if lang == "it" else ("Profile", "How I work.")
    body = f"""{header(a['slug'], lang, switch=other)}<main id="main">
<section class="hero page-hero">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell page-hero-copy reveal">
<nav aria-label="{UI[lang]['crumbs']}" class="breadcrumb"><a href="{home_slug}">{UI[lang]['home']}</a><span>/</span><span aria-current="page">{a['nav']}</span></nav>
<p class="eyebrow">{a['eyebrow']}</p>
<h1>{a['h1']}</h1>
<p class="hero-lead">{a['lead']}</p>
</div>
</section>
<section class="section section-tight section-white">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">{profile_e}</p><h2>{profile_h}</h2></div>
<div class="profile-copy reveal">{profile}<div class="hero-actions">{links}</div></div>
</div>
</section>
<section class="section section-tight section-paper">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{a['skills_e']}</p><h2>{a['skills_h']}</h2></div>
<div class="pillar-grid">
{skills}
</div>
</div>
</section>
<section class="section section-tight section-dark">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{a['field_e']}</p><h2>{a['field_h']}</h2><p class="field-lead">{a['field_p']}</p></div>
<div class="cert-grid">{certs}</div>
</div>
</section>
<section class="section section-tight section-white">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">{a['path_e']}</p><h2>{a['path_h']}</h2></div>
<ol class="timeline reveal">{path}</ol>
</div>
</section>
<section class="section section-tight section-dark akios-section">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">{a['akios_e']}</p><h2>{a['akios_h']}</h2>
<ul class="akios-points">{"".join(f"<li>{x}</li>" for x in a["akios_points"])}</ul></div>
<div class="research-copy reveal">{"".join(f"<p>{x}</p>" for x in a["akios_p"])}<div class="hero-actions">{"".join(f'<a class="button {"primary" if i == 0 else "ghost"}" href="{l}" rel="noreferrer" target="_blank">{n}</a>' for i, (n, l) in enumerate(a["akios_links"]))}</div></div>
</div>
</section>
<section class="section section-tight section-dark">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">{a['research_e']}</p><h2>{a['research_h']}</h2></div>
<div class="research-copy reveal">{"".join(f"<p>{x}</p>" for x in a["research_p"])}<div class="hero-actions"><a class="button primary" href="{product_slug(lang, 'oryvael')}">{UI[lang]['more'].replace(' →', '')}</a><a class="button ghost" href="{a['research_link'][1]}" rel="noreferrer" target="_blank">{a['research_link'][0]}</a></div></div>
</div>
</section>
<section class="section section-tight section-paper">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{a['projects_e']}</p><h2>{a['projects_h']}</h2></div>
<div class="related-grid">{projects}</div>
<p class="eyebrow local-eyebrow">{a['edu_e']}</p>
<div class="edu-grid reveal">{edu}</div>
</div>
</section>
{contact(lang)}</main>
"""
    return head(a["title"], a["desc"], a["slug"], jsonld, lang,
                alternates=[("it", ABOUT["it"]["slug"]), ("en", ABOUT["en"]["slug"])]) + body + footer(lang)


# ---------------------------------------------------------------- prodotti (AKIOS, ORYVAEL)

def ext(href):
    return ' rel="noreferrer" target="_blank"' if href.startswith("http") else ""


def product_slug(lang, key):
    return next(x for x in PRODUCTS[lang] if x["key"] == key)["slug"]


def product_counterpart(pr, lang):
    other = "en" if lang == "it" else "it"
    return next(x for x in PRODUCTS[other] if x["key"] == pr["key"])["slug"]


def product_block(b, bg):
    kind = b[0]
    if kind == "cards":
        _, eyebrow, h2, intro, items = b
        cards = "".join(f'<article class="outcome reveal"><h3>{t}</h3><p>{d}</p></article>' for t, d in items)
        intro_html = f"<p>{intro}</p>" if intro else ""
        return f"""<section class="section section-tight {bg}">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{eyebrow}</p><h2>{h2}</h2>{intro_html}</div>
<div class="outcome-grid">{cards}</div>
</div>
</section>
"""
    if kind == "flow":
        _, eyebrow, h2, steps = b
        li = "".join(f"<li><strong>{t}</strong><span>{d}</span></li>" for t, d in steps)
        return f"""<section class="section section-tight {bg}">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">{eyebrow}</p><h2>{h2}</h2></div>
<ol class="method-steps reveal">{li}</ol>
</div>
</section>
"""
    if kind == "split":
        _, eyebrow, h2, paragraphs, points = b
        pts = "".join(f"<li>{x}</li>" for x in points)
        paras = "".join(f"<p>{x}</p>" for x in paragraphs)
        return f"""<section class="section section-tight {bg}">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">{eyebrow}</p><h2>{h2}</h2><ul class="product-points">{pts}</ul></div>
<div class="profile-copy reveal">{paras}</div>
</div>
</section>
"""
    if kind == "compare":
        _, eyebrow, h2, (lt, li_), (rt, ri) = b
        left = "".join(f"<li>{x}</li>" for x in li_)
        right = "".join(f"<li>{x}</li>" for x in ri)
        return f"""<section class="section section-tight {bg}">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{eyebrow}</p><h2>{h2}</h2></div>
<div class="compare-grid reveal"><div class="compare-col yes"><h3>{lt}</h3><ul>{left}</ul></div><div class="compare-col no"><h3>{rt}</h3><ul>{right}</ul></div></div>
</div>
</section>
"""
    if kind == "status":
        _, eyebrow, h2, items, note = b
        li = "".join(f"<li>{x}</li>" for x in items)
        return f"""<section class="section section-tight section-dark">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">{eyebrow}</p><h2>{h2}</h2></div>
<div class="reveal"><ul class="status-list">{li}</ul><p class="status-note">{note}</p></div>
</div>
</section>
"""
    raise ValueError(kind)


def product_page(pr, lang):
    u = UI[lang]
    home_slug = "index.html" if lang == "it" else "en.html"
    url = url_of(pr["slug"])
    other = product_counterpart(pr, lang)
    bgs = ["section-white", "section-paper"]
    blocks = "".join(product_block(b, bgs[i % 2]) for i, b in enumerate(pr["blocks"]))
    buttons = "".join(f'<a class="button {"primary" if i == 0 else "ghost"}" href="{l}" rel="noreferrer" target="_blank">{n}</a>'
                      for i, (n, l) in enumerate(pr["links"]))
    buttons += f'<a class="button ghost" href="#contatto">{u["talk"]}</a>'
    others = "".join(f'<a href="{x["slug"]}"{ext(x["slug"])}><strong>{x["nav"]}</strong><span>{x["card"]}</span></a>'
                     for x in PRODUCTS[lang] if x["key"] != pr["key"])
    if pr["key"] == "welora":
        main_ld = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Welora", "description": pr["desc"], "url": url,
                   "applicationCategory": "BusinessApplication", "operatingSystem": "Web",
                   "offers": {"@type": "Offer", "price": "29", "priceCurrency": "EUR", "availability": "https://schema.org/PreOrder"},
                   "publisher": {"@id": ORG_ID}, "sameAs": ["https://welora.it/"]}
    elif pr["key"] == "akios":
        main_ld = {"@context": "https://schema.org", "@type": "Product", "name": "AKIOS", "description": pr["desc"], "url": url,
                   "brand": {"@type": "Brand", "name": "AKIOS"}, "manufacturer": {"@id": ORG_ID}, "sameAs": ["https://akios.cloud/", "https://akios-pilot.com/"]}
    else:
        main_ld = {"@context": "https://schema.org", "@type": "ResearchProject", "name": "ORYVAEL", "description": pr["desc"], "url": url,
                   "founder": {"@type": "Person", "name": "Jacopo Ellero"}, "sameAs": ["https://jellero.github.io/ORYVAEL-web/", "https://github.com/jellero/ORYVAEL"]}
    jsonld = [main_ld,
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": u["home"], "item": url_of(home_slug)},
                  {"@type": "ListItem", "position": 2, "name": pr["nav"], "item": url}]},
              ORG_REF]
    other_label = "Altri prodotti" if lang == "it" else "Other products"
    body = f"""{header(pr['slug'], lang, switch=other)}<main id="main">
<section class="hero page-hero product-hero product-{pr['key']}">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell page-hero-copy reveal">
<nav aria-label="{u['crumbs']}" class="breadcrumb"><a href="{home_slug}">{u['home']}</a><span>/</span><span aria-current="page">{pr['nav']}</span></nav>
<p class="eyebrow">{pr['eyebrow']}</p>
<h1>{pr['h1']}</h1>
<p class="hero-lead">{pr['lead']}</p>
<div class="hero-actions">{buttons}</div>
</div>
</section>
{blocks}{contact(lang)}<section class="section section-tight related">
<div class="shell">
<p class="eyebrow">{other_label}</p>
<div class="related-grid">{others}</div>
</div>
</section>
</main>
"""
    alternates = [("it", next(x for x in PRODUCTS["it"] if x["key"] == pr["key"])["slug"]),
                  ("en", next(x for x in PRODUCTS["en"] if x["key"] == pr["key"])["slug"])]
    return head(pr["title"], pr["desc"], pr["slug"], jsonld, lang, alternates=alternates) + body + footer(lang)


def products_home(lang):
    if lang == "it":
        e, h, p = "Prodotti e ricerca", "Non solo progetti per i clienti.", "Tre progetti nostri."
    else:
        e, h, p = "Products and research", "Not only client projects.", "Three projects of our own."
    cards = "".join(f'<a class="product-card product-card-{x["key"]} reveal" href="{x["slug"]}"{ext(x["slug"])}><span class="eyebrow">{x["eyebrow"]}</span>'
                    f'<strong>{x["nav"]}</strong><span class="product-card-text">{x["card"]}</span><span class="competence-more">{(x["slug"].split("//")[1].rstrip("/") + " ↗") if x.get("external") else UI[lang]["more"]}</span></a>'
                    for x in PRODUCTS[lang])
    return f"""<section class="section section-tight section-dark" id="prodotti">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{e}</p><h2>{h}</h2><p>{p}</p></div>
<div class="product-grid">{cards}</div>
</div>
</section>
"""


# ---------------------------------------------------------------- scrittura

def write(name, html):
    path = REPO / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8", newline="\n")


write("index.html", home("it"))
write("en.html", home("en"))
for p in PAGES:
    write(p["slug"], service(dict(p, href=p["slug"]), "it"))
for p in pages_for("en"):
    write(p["slug"], service(p, "en"))
for c in CITIES:
    write(c["slug"], city(c))
for g in GUIDES:
    write(g["slug"], guide(g))
write("guide.html", guide_index())
write(TEST["slug"], test_page())
write("chi-sono.html", about("it"))
for _lang in ("it", "en"):
    for _a in AREAS[_lang]:
        write(_a["slug"], area_page(_a, _lang))
    write(PRODUCTS_PAGE[_lang]["slug"], products_index(_lang))
write(WHERE_PAGE["slug"], where_page())
for _lang in ("it", "en"):
    for _pr in PRODUCTS[_lang]:
        if not _pr.get("external"):
            write(_pr["slug"], product_page(_pr, _lang))
write("en-about.html", about("en"))
write("404.html", not_found())
for old, target in OLD_URLS.items():
    write(f"{old}/index.html", redirect_stub(target))

urls = (["", "en.html"] + [p["slug"] for p in PAGES] + [EN_SLUG[p["slug"]] for p in PAGES]
        + [c["slug"] for c in CITIES] + ["guide.html", TEST["slug"]] + [g["slug"] for g in GUIDES]
        + [x["slug"] for l in ("it", "en") for x in PRODUCTS[l] if not x.get("external")] + [a["slug"] for l in ("it", "en") for a in AREAS[l]] + [PRODUCTS_PAGE["it"]["slug"], PRODUCTS_PAGE["en"]["slug"], WHERE_PAGE["slug"]] + ["chi-sono.html", "en-about.html", "cv.html", "cv-en.html", "privacy.html", "privacy-en.html", "cookie-policy.html", "cookie-policy-en.html"])
sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sitemap += [f"  <url><loc>{BASE}{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls]
sitemap.append("</urlset>")
(REPO / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8", newline="\n")
print("ok", len(urls), "URL in sitemap")
