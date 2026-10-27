# Modelli di pagina. Eseguito dopo build_site.py (stesso namespace): usa PAGES, TIERS, BASE, ecc.
import datetime
import runpy

EXTRA = runpy.run_path(str(pathlib.Path(__file__).with_name("content_extra.py")))
ABOUT = runpy.run_path(str(pathlib.Path(__file__).with_name("content_about.py")))["ABOUT"]
PRICES, CITIES, GUIDES, TEST = EXTRA["PRICES"], EXTRA["CITIES"], EXTRA["GUIDES"], EXTRA["TEST"]
EN_SLUG, EN_PAGES, EN_TIERS = EXTRA["EN_SLUG"], EXTRA["EN_PAGES"], EXTRA["EN_TIERS"]
TODAY = datetime.date.today().isoformat()

import hashlib
ASSET_V = {n: hashlib.sha1((REPO / n).read_bytes()).hexdigest()[:8] for n in ("styles.css", "overrides.css", "pages.css", "script.js")}

WA_EN = "https://wa.me/393454656749?text=" + quote("Hi Jacopo, I'm writing from the JDEVPRO website about a project.")
MAILTO_EN = ("mailto:info@jdevpro.it?subject=" + quote("Project enquiry - JDEVPRO") + "&amp;body=" + quote(
    "Hi Jacopo,\n\nExisting systems:\n\nWhat I want to achieve:\n\nRough timeline:\n\nCompany / contact:\n"))

UI = {
  "it": dict(lang="it", locale="it_IT", skip="Vai al contenuto", menu="Apri menu", navlabel="Navigazione principale",
             contact="Contatto", guides="Guide", home="Home", crumbs="Percorso", more="Approfondisci →",
             talk="Parliamone", see_examples="Vedi esempi reali", problem="Il problema", recognise="Ti riconosci?",
             get="Cosa ottieni", get_h="Cosa faccio, in concreto.", method="Metodo", method_h="Come funziona.",
             examples="Esempi reali", examples_h="Dai miei progetti.", faq="Domande frequenti",
             faq_h="Le risposte prima della domanda.", others="Altre competenze", visit="Visita ↗",
             sys_e="Sistemi già collegati", sys_h="Cosa ho già integrato nei miei progetti.",
             reach_e="Cosa posso integrare", reach_h="Se ha un'interfaccia, si può collegare.",
             reach_p="Tre strade, a seconda di cosa offre il sistema da collegare.",
             reach_note="Esempi di servizi e dispositivi integrabili. Nomi e marchi appartengono ai rispettivi proprietari; prima di ogni progetto verifico accessi, limiti e condizioni d'uso.",
             price_e="Prezzi indicativi", price_h="Da dove si parte.", from_="da", per_month="al mese", once="una tantum",
             price_note="Prezzi di partenza indicativi. Il preventivo è a prezzo fisso, dopo aver verificato cosa serve davvero.",
             c_eyebrow="Contatto", c_h="Raccontami cosa devi collegare.",
             c_p="Descrivimi i sistemi che hai, cosa vuoi ottenere e i tempi. Ti rispondo per iscritto con domande mirate o con una proposta.",
             c_steps='<li><strong>Scrivimi</strong> i sistemi presenti e l\'obiettivo, anche in poche righe.</li><li><strong>Ti rispondo</strong> con domande mirate o una proposta di call conoscitiva.</li><li><strong>Definiamo</strong> insieme perimetro, tempi e modalità di lavoro.</li>',
             c_steps_label="Come funziona", c_mail="Scrivimi una email", copy="Copia", copied="Copiato ✓",
             wa="WhatsApp · solo messaggi ↗", wa_note="Non rispondo alle chiamate: scrivimi e ti rispondo appena posso.",
             li="Oppure scrivimi su LinkedIn ↗", where="Tolmezzo (UD) · Friuli Venezia Giulia · Veneto · anche da remoto",
             f_who="Jacopo Ellero · Tolmezzo (UD)", privacy="privacy.html", cookie="cookie-policy.html", cv="cv.html",
             mailto=MAILTO, wa_url=WA),
  "en": dict(lang="en", locale="en_GB", skip="Skip to content", menu="Open menu", navlabel="Main navigation",
             contact="Contact", guides="Guides", home="Home", crumbs="Breadcrumb", more="Learn more →",
             talk="Let's talk", see_examples="See real examples", problem="The problem", recognise="Sound familiar?",
             get="What you get", get_h="What I do, in practice.", method="Method", method_h="How it works.",
             examples="Real examples", examples_h="From my projects.", faq="FAQ",
             faq_h="Answers before you ask.", others="Other services", visit="Visit ↗",
             sys_e="Already connected", sys_h="What I have already integrated in my projects.",
             reach_e="What I can integrate", reach_h="If it has an interface, it can be connected.",
             reach_p="Three routes, depending on what the system offers.",
             reach_note="Examples of services and devices that can be integrated. Names and trademarks belong to their owners; before each project I check access, limits and terms of use.",
             price_e="Indicative prices", price_h="Where it starts.", from_="from", per_month="per month", once="one-off",
             price_note="Indicative starting prices. Quotes are fixed-price, after checking what is really needed.",
             c_eyebrow="Contact", c_h="Tell me what you need to connect.",
             c_p="Describe your systems, what you want to achieve and your timeline. I reply in writing with focused questions or a proposal.",
             c_steps="<li><strong>Write to me</strong> about your current systems and goal, even in a few lines.</li><li><strong>I reply</strong> with focused questions or a proposal for an intro call.</li><li><strong>We define</strong> scope, timeline and way of working together.</li>",
             c_steps_label="How it works", c_mail="Send me an email", copy="Copy", copied="Copied ✓",
             wa="WhatsApp · messages only ↗", wa_note="I don't take calls: send a message and I'll reply as soon as I can.",
             li="Or message me on LinkedIn ↗", where="Tolmezzo (Udine), Italy · north-east Italy · remote projects",
             f_who="Jacopo Ellero · Tolmezzo, Italy", privacy="privacy-en.html", cookie="cookie-policy-en.html", cv="cv-en.html",
             mailto=MAILTO_EN, wa_url=WA_EN),
}

PRICE_EN = {"Collegamento di una macchina": "Connecting one machine", "Dati macchina e assistenza": "Machine data and support",
            "Prima versione del gestionale": "First version of the software", "Hosting, backup e assistenza": "Hosting, backups and support",
            "Progetto e installazione": "Design and installation", "Dati, allarmi e manutenzione": "Data, alarms and maintenance",
            "Integrazione tra due sistemi": "Integration between two systems", "Monitoraggio e manutenzione": "Monitoring and maintenance",
            "Sito con pannello di gestione": "Website with management panel", "Hosting e manutenzione": "Hosting and maintenance",
            "per tipo di macchina con API documentate": "per machine type with documented APIs", "per macchina": "per machine",
            "a prezzo fisso, sulla parte più utile": "fixed price, on the most useful part", "dispositivi esclusi": "devices excluded",
            "per dispositivo": "per device", "con API pubbliche": "with public APIs", "": ""}

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
  "description": "Interconnessione macchine 4.0, gestionali su misura, IoT, integrazioni software e siti web per aziende del Friuli Venezia Giulia e del Veneto.",
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
    links = "\n".join(
        f'<a href="{p["href"]}"{" aria-current=\"page\"" if p["href"] == current else ""}>{p["nav"]}</a>' for p in pages_for(lang))
    if lang == "it":
        links += f'\n<a href="guide.html"{" aria-current=\"page\"" if current == "guide.html" else ""}>Guide</a>'
    ab = ABOUT[lang]
    links += f'\n<a href="{ab["slug"]}"{" aria-current=\"page\"" if current == ab["slug"] else ""}>{ab["nav"]}</a>'
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
<small class="contact-note">{u['wa_note']}</small>
<a class="contact-alt" href="{LI}" rel="noreferrer" target="_blank">{u['li']}</a>
<span>{u['where']}</span>
</div>
</div>
</section>
"""


def footer(lang="it"):
    u = UI[lang]
    links = "".join(f'<a href="{p["href"]}">{p["nav"]}</a>' for p in pages_for(lang))
    local = ""
    if lang == "it":
        links += '<a href="guide.html">Guide</a>'
        local = '<div class="footer-local">' + "".join(f'<a href="{c["slug"]}">{c["name"]}</a>' for c in CITIES) + "</div>"
    links += f'<a href="{ABOUT[lang]["slug"]}">{ABOUT[lang]["nav"]}</a>'
    return f"""<footer class="footer">
<div class="shell footer-grid footer-wide">
<div><strong>JDEVPRO</strong><span>{u['f_who']}</span></div>
<div class="footer-links">{links}</div>
<div><span>P.IVA IT02783420306</span><a href="{u['privacy']}">Privacy</a><a href="{u['cookie']}">Cookie</a><a href="{u['cv']}">CV</a><a href="https://github.com/jellero" rel="noreferrer" target="_blank">GitHub</a><a href="{LI}" rel="noreferrer" target="_blank">LinkedIn</a></div>
</div>
{f'<div class="shell">{local}</div>' if local else ''}
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
    pages = pages_for(lang)
    cards = "\n".join(f"""<a class="competence-card reveal" href="{p['href']}">
<span class="competence-num">0{i}</span>
<h3>{p['card_title']}</h3>
<p>{p['card_who']}</p>
<ul>{''.join(f'<li>{x}</li>' for x in p['card_points'])}</ul>
<span class="competence-more">{u['more']}</span>
</a>""" for i, p in enumerate(pages, 1))
    if lang == "it":
        t = dict(eyebrow="Software su misura e integrazioni · Friuli Venezia Giulia",
                 h1="Collego macchine, gestionali e dispositivi. <span>E li tengo funzionanti.</span>",
                 lead="Sono Jacopo Ellero, da Tolmezzo. Sviluppo gestionali su misura, collego macchine e sensori ai sistemi aziendali e seguo tutto in produzione, per aziende del Friuli Venezia Giulia e del Veneto.",
                 b1="Scegli cosa ti serve", b2="Scrivimi", ce="Competenze", ch="Cinque modi per far lavorare meglio i tuoi sistemi.",
                 cp="Ogni competenza ha una pagina dedicata con esempi reali, metodo, prezzi indicativi e domande frequenti.",
                 cta_h="Non sai quale ti serve?", cta_p="Descrivimi il problema in poche righe: ti dico io da dove partire.", cta_m="Scrivimi →",
                 me="Come lavoro", mh="Prezzo chiaro, consegna rapida, assistenza continua.",
                 steps=[("Analisi", "Capisco i sistemi che hai e cosa deve cambiare."), ("Prezzo fisso a fasi", "Sai cosa paghi prima di iniziare."),
                        ("Consegna rapida", "Si parte dalla parte più utile, provata sul lavoro reale."), ("Canone di assistenza", "Backup, aggiornamenti e interventi senza sorprese.")],
                 proof=[("JD Industry", "Gestionale di produzione collegato a macchine SCM ed Essetre."), ("Welora", "Piattaforma gestionale con 25 moduli e oltre 370 file di test automatici."),
                        ("Marketplace", "Gestionale collegato a fornitore, marketplace e corriere."), ("Lauco Experience", "Portale in quattro lingue con backoffice, notifiche e newsletter.")],
                 who='<strong>JDEVPRO</strong> è l\'attività di Jacopo Ellero, sviluppatore e integratore di sistemi. <a href="chi-sono.html">Chi sono →</a>',
                 title="JDEVPRO · Gestionali, macchine 4.0 e IoT in Friuli",
                 desc="Gestionali su misura, interconnessione macchine 4.0, IoT, integrazioni e siti web per aziende del Friuli Venezia Giulia e del Veneto. Jacopo Ellero.")
    else:
        t = dict(eyebrow="Custom software and integrations · North-east Italy",
                 h1="I connect machines, business software and devices. <span>And keep them running.</span>",
                 lead="I'm Jacopo Ellero, based in Tolmezzo, Friuli. I build custom business software, connect machines and sensors to company systems and look after everything in production, for companies in north-east Italy and remotely.",
                 b1="Choose what you need", b2="Write to me", ce="Services", ch="Five ways to make your systems work better.",
                 cp="Each service has its own page with real examples, method, indicative prices and FAQ.",
                 cta_h="Not sure which one?", cta_p="Describe the problem in a few lines: I'll tell you where to start.", cta_m="Write to me →",
                 me="How I work", mh="Clear prices, fast delivery, ongoing support.",
                 steps=[("Analysis", "I understand your systems and what must change."), ("Fixed price in phases", "You know the cost before we start."),
                        ("Fast delivery", "We start from the most useful part, tested on real work."), ("Support plan", "Backups, updates and fixes without surprises.")],
                 proof=[("JD Industry", "Production management connected to SCM and Essetre machines."), ("Welora", "Business platform with 25 modules and over 370 automated test files."),
                        ("Marketplaces", "Business software connected to supplier, marketplaces and courier."), ("Lauco Experience", "Four-language portal with back office, notifications and newsletter.")],
                 who='<strong>JDEVPRO</strong> is the business of Jacopo Ellero, software developer and systems integrator. <a href="en-about.html">About me →</a>',
                 title="JDEVPRO · Business software, machines 4.0 and IoT, Italy",
                 desc="Custom business software, Industry 4.0 machine interconnection, IoT, integrations and websites for companies in north-east Italy. Jacopo Ellero.")
    steps = "".join(f"<li><strong>{a}</strong><span>{b}</span></li>" for a, b in t["steps"])
    proof = "".join(f"<div><strong>{a}</strong><span>{b}</span></div>" for a, b in t["proof"])
    extra = ""
    if lang == "it":
        g = "".join(f'<a href="{x["slug"]}"><strong>{x["short"]}</strong><span>{x["desc"]}</span></a>' for x in [TEST] + GUIDES)
        c = "".join(f'<a href="{x["slug"]}"><strong>{x["name"]}</strong><span>{x["area"].capitalize()}</span></a>' for x in CITIES)
        extra = f"""<section class="section section-tight section-white">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Guide e strumenti</p><h2>Per capire prima di chiedere.</h2></div>
<div class="related-grid">{g}</div>
<p class="eyebrow local-eyebrow">Dove lavoro</p>
<div class="related-grid cities-grid">{c}</div>
</div>
</section>
"""
    body = f"""{header("index.html" if lang == "it" else "en.html", lang, home=True, switch="en.html" if lang == "it" else "index.html")}<main id="main">
<section class="hero hero-min" id="top">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell hero-min-copy reveal">
<p class="eyebrow">{t['eyebrow']}</p>
<h1>{t['h1']}</h1>
<p class="hero-lead">{t['lead']}</p>
<div class="hero-actions">
<a class="button primary" href="#competenze">{t['b1']}</a>
<a class="button ghost" href="#contatto">{t['b2']}</a>
</div>
</div>
</section>
<section class="section" id="competenze">
<div class="shell">
<div class="section-heading reveal">
<p class="eyebrow">{t['ce']}</p>
<h2>{t['ch']}</h2>
<p>{t['cp']}</p>
</div>
<div class="competence-grid">
{cards}
<a class="competence-card competence-cta reveal" href="#contatto">
<h3>{t['cta_h']}</h3>
<p>{t['cta_p']}</p>
<span class="competence-more">{t['cta_m']}</span>
</a>
</div>
</div>
</section>
<section class="section section-tight method-band">
<div class="shell method-grid reveal">
<div>
<p class="eyebrow">{t['me']}</p>
<h2>{t['mh']}</h2>
</div>
<ol class="method-steps">{steps}</ol>
</div>
</section>
<section class="section section-tight proof-band">
<div class="shell">
<div class="proof-grid reveal">{proof}</div>
<p class="proof-who reveal">{t['who']}</p>
</div>
</section>
{extra}{contact(lang)}</main>
"""
    slug = "index.html" if lang == "it" else "en.html"
    org = ORG if lang == "it" else dict(ORG, description="Industry 4.0 machine interconnection, custom business software, IoT, software integrations and websites for companies in north-east Italy.")
    return head(t["title"], t["desc"], slug, [org], lang, alternates=[("it", "index.html"), ("en", "en.html")]) + body + footer(lang)


# ---------------------------------------------------------------- pagine competenza

def service(p, lang="it"):
    u = UI[lang]
    it_slug = p.get("it_slug", p["slug"])
    url = url_of(p["slug"])
    home_slug = "index.html" if lang == "it" else "en.html"
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
        {"@type": "ListItem", "position": 2, "name": p["card_title"], "item": url}]},
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
        reach = f"""<section class="section section-tight section-paper">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{u['reach_e']}</p><h2>{u['reach_h']}</h2><p>{u['reach_p']}</p></div>
<div class="tier-grid">
{tiers}
</div>
<div class="system-groups catalog">
{groups_html(p['catalog'])}
</div>
<p class="catalog-note">{u['reach_note']}</p>
</div>
</section>
"""
    chips = "".join(f"<span>{c}</span>" for c in p["chips"])
    faq = "\n".join(f'<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>' for q, a in p["faq"])
    related = "".join(f'<a href="{o["href"]}"><strong>{o["card_title"]}</strong><span>{o["card_who"]}</span></a>' for o in pages_for(lang) if o["href"] != p["slug"])
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
<nav aria-label="{u['crumbs']}" class="breadcrumb"><a href="{home_slug}">{u['home']}</a><span>/</span><span aria-current="page">{p['card_title']}</span></nav>
<p class="eyebrow">{p['eyebrow']}</p>
<h1>{p['h1']}</h1>
<p class="hero-lead">{p['lead']}</p>
<div class="hero-actions">
<a class="button primary" href="#contatto">{u['talk']}</a>
<a class="button ghost" href="#esempi">{u['see_examples']}</a>
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
{price_block(it_slug, lang)}<section class="section section-tight section-dark" id="esempi">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{u['examples']}</p><h2>{u['examples_h']}</h2></div>
<div class="example-grid">
{examples}
</div>
<div class="chips reveal" aria-label="Tech">{chips}</div>
</div>
</section>
<section class="section section-tight">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">{u['faq']}</p><h2>{u['faq_h']}</h2></div>
<div class="faq reveal">
{faq}
</div>
</div>
</section>
{contact(lang)}<section class="section section-tight related">
<div class="shell">
{guide_links}<p class="eyebrow">{u['others']}</p>
<div class="related-grid">{related}</div>
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
<p class="eyebrow">{c['area'].capitalize()}</p>
<h1>Software, gestionali e integrazioni a <span>{c['name']}.</span></h1>
<p class="hero-lead">{c['lead']}</p>
<div class="hero-actions">
<a class="button primary" href="#contatto">Parliamone</a>
<a class="button ghost" href="#competenze">Cosa faccio</a>
</div>
</div>
</section>
<section class="section section-tight section-paper">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Settori</p><h2>Cosa faccio per le aziende della {c['area']}.</h2></div>
<div class="outcome-grid">
{sectors}
</div>
</div>
</section>
<section class="section section-tight section-white">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">Come lavoro</p><h2>Vicino quando serve, da remoto il resto.</h2></div>
<ol class="method-steps reveal">
<li><strong>Analisi in azienda</strong><span>Vedo macchine, software e processi dove lavorano davvero.</span></li>
<li><strong>Proposta a prezzo fisso</strong><span>Fasi chiare, si parte dalla parte più utile.</span></li>
<li><strong>Sviluppo e collaudo</strong><span>Sviluppo da remoto, collaudo sul posto con i dati reali.</span></li>
<li><strong>Assistenza continua</strong><span>Canone mensile con backup, aggiornamenti e interventi.</span></li>
</ol>
</div>
</section>
<section class="section section-tight" id="competenze">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Competenze</p><h2>Le cinque cose che faccio.</h2></div>
<div class="related-grid related-five">{services}</div>
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
<p class="eyebrow">Guida · Jacopo Ellero</p>
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
    out.innerHTML = text + ' <a href="interconnessione-macchine-industria-4-0.html#contatto">Scrivimi per una verifica \\u2192</a>';
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
<div class="shell"><div class="related-grid related-five">{''.join(f'<a href="/{p["slug"]}"><strong>{p["card_title"]}</strong><span>{p["card_who"]}</span></a>' for p in PAGES)}</div></div>
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
write("en-about.html", about("en"))
write("404.html", not_found())
for old, target in OLD_URLS.items():
    write(f"{old}/index.html", redirect_stub(target))

urls = (["", "en.html"] + [p["slug"] for p in PAGES] + [EN_SLUG[p["slug"]] for p in PAGES]
        + [c["slug"] for c in CITIES] + ["guide.html", TEST["slug"]] + [g["slug"] for g in GUIDES]
        + ["chi-sono.html", "en-about.html", "cv.html", "cv-en.html", "privacy.html", "privacy-en.html", "cookie-policy.html", "cookie-policy-en.html"])
sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sitemap += [f"  <url><loc>{BASE}{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls]
sitemap.append("</urlset>")
(REPO / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8", newline="\n")
print("ok", len(urls), "URL in sitemap")
