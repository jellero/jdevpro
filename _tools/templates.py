# Modelli di pagina. Eseguito dopo build_site.py (stesso namespace): usa PAGES, TIERS, BASE, ecc.
import datetime
import runpy

EXTRA = runpy.run_path(str(pathlib.Path(__file__).with_name("content_extra.py")))
ABOUT = runpy.run_path(str(pathlib.Path(__file__).with_name("content_about.py")))["ABOUT"]
PRODUCTS = runpy.run_path(str(pathlib.Path(__file__).with_name("content_products.py")))["PRODUCTS"]
AREAS_DATA = runpy.run_path(str(pathlib.Path(__file__).with_name("content_areas.py")))
STATS = runpy.run_path(str(pathlib.Path(__file__).with_name("content_stats.py")))["STATS"]
LEGAL_DATA = runpy.run_path(str(pathlib.Path(__file__).with_name("content_legal.py")))


def stats_html(key, lang):
    """Numeri già realizzati in cima alla pagina."""
    rows = STATS.get(key, {}).get(lang)
    if not rows:
        return ""
    items = ""
    for big, label, link in rows:
        size = ' class="stat-long"' if len(big) > 12 else ""
        inner = f"<strong{size}>{big}</strong><span>{label}</span>"
        if link:
            ext = ' rel="noreferrer" target="_blank"' if link.startswith("http") else ""
            items += f'<li><a class="stat" href="{link}"{ext}>{inner}</a></li>'
        else:
            items += f'<li><div class="stat">{inner}</div></li>'
    return f'<ul class="hero-stats">{items}</ul>'

AREAS, AREA_SERVICES, PRIMARY_AREA = AREAS_DATA["AREAS"], AREAS_DATA["AREA_SERVICES"], AREAS_DATA["PRIMARY_AREA"]
TECH_TIERS, PRODUCTS_PAGE, WHERE_PAGE, CALLOUTS = AREAS_DATA["TECH_TIERS"], AREAS_DATA["PRODUCTS_PAGE"], AREAS_DATA["WHERE_PAGE"], AREAS_DATA["CALLOUTS"]
CARD_OVERRIDES = AREAS_DATA["CARD_OVERRIDES"]
SUPPORT = AREAS_DATA["SUPPORT_SERVICES"]


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
PRICE_NOTES, CTAS = EXTRA["PRICE_NOTES"], EXTRA["CTAS"]
GUIDE_UPDATED, GUIDE_MODIFIED = "ottobre 2026", "2026-10-28"
GUIDES = GUIDES + runpy.run_path(str(pathlib.Path(__file__).with_name("content_guides_more.py")))["MORE_GUIDES"]
EN_SLUG, EN_PAGES, EN_TIERS = EXTRA["EN_SLUG"], EXTRA["EN_PAGES"], EXTRA["EN_TIERS"]
SENSOR_TIER = {"it": ("Sensori aggiunti", "Per macchine e impianti senza nessuna interfaccia, anche vecchi: sensori e contatori rilevano stato, cicli, tempi e consumi e li portano nei vostri sistemi."),
               "en": ("Added sensors", "For machines and plants with no interface at all, old ones included: sensors and meters detect status, cycles, times and consumption and bring them into your systems.")}
TODAY = datetime.date.today().isoformat()

import hashlib
ASSET_V = {n: hashlib.sha1((REPO / n).read_bytes()).hexdigest()[:8] for n in ("styles.css", "overrides.css", "pages.css", "script.js")}

WA_EN = "https://wa.me/393454656749?text=" + quote("Hello, I'm writing from the JDEVPRO website about a project.")
MAILTO_EN = ("mailto:info@jdevpro.it?subject=" + quote("Project enquiry - JDEVPRO") + "&amp;body=" + quote(
    "Hello,\n\nWhat needs doing:\n\nWhere (town):\n\nMachines, rooms or users involved:\n\nExisting systems:\n\nRough timeline:\n\nIncentives or grants expected (if any):\n\nCompany / contact:\n"))

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
             li="Oppure su LinkedIn ↗", where="Tolmezzo (UD) · Friuli Venezia Giulia e Veneto · trasferte · da remoto ovunque",
             f_who="Jacopo Ellero · Tolmezzo (UD)", privacy="privacy.html", cookie="cookie-policy.html",
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
             li="Or on LinkedIn ↗", where="Tolmezzo (Udine), Italy · north-east Italy · travel · remote work anywhere",
             f_who="Jacopo Ellero · Tolmezzo, Italy", privacy="privacy-en.html", cookie="cookie-policy-en.html",
             mailto=MAILTO_EN, wa_url=WA_EN),
}

PRICE_EN = {"Collegamento di una macchina": "Connecting one machine", "Dati macchina e assistenza": "Machine data and support",
            "Prima versione del gestionale": "First version of the software", "Hosting, backup e assistenza": "Hosting, backups and support",
            "Progetto e configurazione": "Design and configuration", "Dati, allarmi e manutenzione": "Data, alarms and maintenance",
            "Integrazione tra due sistemi": "Integration between two systems", "Monitoraggio e manutenzione": "Monitoring and maintenance",
            "Sito con pannello di gestione": "Website with management panel", "Hosting e manutenzione": "Hosting and maintenance",
            "per tipo di macchina · eventuali sensori esclusi": "per machine type · any sensors excluded",
            "per tipo di macchina · sviluppo del collegamento via API compreso · eventuali sensori esclusi": "per machine type · API connection development included · any sensors excluded", "per macchina": "per machine",
            "a prezzo fisso, sulla parte più utile": "fixed price, on the most useful part", "dispositivi esclusi": "devices excluded",
            "per dispositivo": "per device", "con API pubbliche": "with public APIs", "": "",
            "Assistenza e controllo da remoto": "Support and remote monitoring", "Configurazione dell'impianto": "System configuration",
            "Assistenza e aggiornamenti": "Support and updates", "Configurazione del centralino": "Phone system configuration",
            "Assistenza e modifiche": "Support and changes", "Controllo da remoto": "Remote monitoring",
            "telecamere e dispositivi esclusi": "cameras and devices excluded", "telefoni esclusi": "phones excluded", "apparati esclusi": "equipment excluded",
            "fino a 6 camere · dispositivi esclusi": "up to 6 rooms · devices excluded", "per struttura": "per property",
            "fino a 4 telecamere · dispositivi esclusi": "up to 4 cameras · devices excluded", "per impianto": "per system",
            "Centralino Asterisk configurato": "Asterisk phone system set up",
            "fino a 10 interni · nessuna licenza · telefoni esclusi": "up to 10 extensions · no licence · phones excluded",
            "fino a 10 interni": "up to 10 extensions", "per sito · apparati esclusi": "per site · equipment excluded", "per sito": "per site",
            "Impianto base configurato": "Basic system set up",
            "Cloud Key, una telecamera e switch inclusi · cablaggio escluso": "Cloud Key, one camera and switch included · cabling excluded",
            "nessuna licenza · telefoni esclusi": "no licence · phones excluded",
            "Server, aggiornamenti e assistenza": "Server, updates and support",
            "Installazione Starlink professionale": "Professional Starlink installation",
            "kit e abbonamento Starlink esclusi": "Starlink kit and plan excluded",
            "Fotovoltaico off-grid per la connettività": "Off-grid solar for connectivity",
            "per router, antenne e telecamere · cablaggi esclusi": "for routers, antennas and cameras · cabling excluded",
            "Fotovoltaico off-grid a 230 V": "Off-grid solar at 230 V",
            "corrente di casa · cablaggi esclusi": "household power · cabling excluded",
            "Cruscotto e allarmi sul nostro server": "Dashboard and alarms on our server", "per impianto": "per system",
            "Server, monitoraggio e manutenzione": "Server, monitoring and maintenance", "se gira sul nostro server": "if it runs on our server",
            "Telecamera aggiuntiva configurata": "Additional camera set up", "per telecamera · cablaggio escluso": "per camera · cabling excluded",
            "Migrazione di un blocco di dati": "Migrating one data block",
            "Macchina aggiuntiva dello stesso tipo": "Additional machine of the same type",
            "stessa marca e modello · collegamento già sviluppato": "same make and model · connection already developed",
            "anagrafiche, articoli, giacenze o saldi · da file o esportazione": "master data, items, stock or balances · from file or export",
            "Estrazione da database senza esportazione": "Extraction from a database with no export",
            "Access, SQL Server, DBF, Firebird e simili": "Access, SQL Server, DBF, Firebird and similar",
            "Progetto e installazione dell'impianto domotico": "Building automation design and installation",
            "hardware dedicato, rete separata, backup · dispositivi esclusi": "dedicated hardware, separate network, backups · devices excluded",
            "Camera o zona configurata": "Room or zone set up",
            "per camera o zona · dispositivi esclusi": "per room or zone · devices excluded"}

ADDRESS = {"@type": "PostalAddress", "addressLocality": "Tolmezzo", "postalCode": "33028", "addressRegion": "UD",
           "addressCountry": "IT"}

ORG = {
  "@context": "https://schema.org", "@type": "ProfessionalService", "@id": ORG_ID, "name": "JDEVPRO",
  "url": BASE, "logo": BASE + "assets/icon-512.png", "image": BASE + "assets/og-jdevpro.jpg", "email": EMAIL,
  "vatID": "IT02783420306", "priceRange": "€€",
  "founder": {"@type": "Person", "name": "Jacopo Ellero", "url": BASE + "chi-sono.html"},
  "address": ADDRESS,
  "geo": {"@type": "GeoCoordinates", "latitude": 46.4057, "longitude": 13.0154},
  "areaServed": [{"@type": "AdministrativeArea", "name": "Friuli Venezia Giulia"},
                 {"@type": "City", "name": "Udine"}, {"@type": "City", "name": "Pordenone"},
                 {"@type": "City", "name": "Trieste"}, {"@type": "City", "name": "Gorizia"},
                 {"@type": "AdministrativeArea", "name": "Veneto"}, {"@type": "Country", "name": "Italia"}],
  "description": "Interconnessione macchine 4.0 per l'iperammortamento e gestionale di produzione JD Industry. Anche software su misura e automazione per hotel e B&B, in Friuli Venezia Giulia e Veneto.",
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
<script>document.documentElement.classList.add("js")</script>
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
    prods = products(lang)
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


def contact(lang="it", cta=None):
    """cta: (titolo, testo) specifici della pagina, altrimenti quelli generici."""
    u = UI[lang]
    c_h, c_p = cta or (u['c_h'], u['c_p'])
    return f"""<section class="contact-section" id="contatto">
<div class="shell contact-card reveal">
<div>
<p class="eyebrow">{u['c_eyebrow']}</p>
<h2>{c_h}</h2>
<p>{c_p}</p>
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
<div><span>P.IVA IT02783420306</span><a href="{u['privacy']}">Privacy</a><a href="{u['cookie']}">Cookie</a><a href="https://github.com/jellero" rel="noreferrer" target="_blank">GitHub</a><a href="{LI}" rel="noreferrer" target="_blank">LinkedIn</a></div>
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
{(lambda n: f'<p class="price-extra">{n}</p>' if n else '')(PRICE_NOTES.get(it_slug, {}).get(lang))}
<p class="catalog-note">{u['price_note']}</p>
</div>
</div>
</section>
"""


def offers_ld(it_slug):
    rows = PRICES.get(it_slug, [])
    return [{"@type": "Offer", "name": r[0], "priceCurrency": "EUR",
             "priceSpecification": {"@type": "PriceSpecification", "minPrice": r[1], "priceCurrency": "EUR"}} for r in rows]


WHY = {
    "it": dict(e="Perché JDEVPRO", h="Un elettricista installa. Un informatico programma. <span>Noi teniamo insieme il sistema.</span>",
               p="Quando macchine, impianti, rete e software devono funzionare insieme, serve qualcuno che governi l'insieme invece di tanti fornitori separati. Progettiamo, colleghiamo e documentiamo il sistema; cablaggi e quadri li realizzano installatori abilitati con cui collaboriamo.",
               partners="Partner: <strong>Efficasa</strong> per il fotovoltaico, <strong>DWIN</strong> per i display HMI, <strong>Aruba Business</strong> per l'hosting, <strong>Siportal</strong> per il VoIP.<br>Tecnologie e servizi che usiamo nei progetti: <strong>Open Fiber</strong> per la fibra FTTH, <strong>Aruba</strong> per connettività e cloud, <strong>MikroTik</strong> e <strong>Ubiquiti</strong> per reti, connettività e videosorveglianza, <strong>WuBook</strong> per le OTA."),
    "en": dict(e="Why JDEVPRO", h="An electrician installs. A programmer codes. <span>We hold the whole system together.</span>",
               p="When machines, installations, network and software have to work together, someone has to govern the whole instead of many separate suppliers. We design, connect and document the system; wiring and panels are done by licensed installers we work with.",
               partners="Partners: <strong>Efficasa</strong> for solar, <strong>DWIN</strong> for HMI displays, <strong>Aruba Business</strong> for hosting, <strong>Siportal</strong> for VoIP.<br>Technologies and services we use in projects: <strong>Open Fiber</strong> for FTTH fibre, <strong>Aruba</strong> for connectivity and cloud, <strong>MikroTik</strong> and <strong>Ubiquiti</strong> for networks, connectivity and video surveillance, <strong>WuBook</strong> for OTA channels."),
}

# specializzazione in home: (eyebrow, titolo, testo, [(titolo, testo, link, etichetta)])
INDUSTRIAL = {
    "it": ("Integrazione industriale", "Dalla macchina al gestionale, documentato per il perito.",
           "È la nostra specializzazione: collegare al gestionale macchine di ogni tipo di produzione e tenerle sempre connesse.",
           [("Interconnessione macchine 4.0", "Torni, centri di lavoro, laser, presse, macchine tessili e da stampa, riempitrici: qualsiasi macchina con PLC o CNC, nuova o datata.", "interconnessione-macchine-industria-4-0.html", "Vedi i tipi di macchine →"),
            ("Asseverate e ammesse", "Le macchine che abbiamo collegato sono tutte certificate e asseverate da ingegneri, verificate per l'interconnessione e ammesse all'iperammortamento.", "guida-interconnessione-iperammortamento.html", "Requisiti e scadenze →"),
            ("JD Industry", "Il nostro gestionale di produzione: dalle macchine collegate all'ERP su ERPNext, con la migrazione dei dati dal vecchio programma.", "gestionale-produzione-erpnext.html", "Scopri JD Industry →")]),
    "en": ("Industrial integration", "From the machine to business software, documented for the appraiser.",
           "It is our specialisation: connecting machines from any kind of production to business software and keeping them always connected.",
           [("Industry 4.0 machine interconnection", "Lathes, machining centres, lasers, presses, textile and printing machines, fillers: any machine with a PLC or CNC, new or old.", "en-machine-interconnection.html", "See machine types →"),
            ("Sworn and approved", "The machines we have connected are all certified and sworn by engineers, verified for interconnection and approved for the Italian hyper-depreciation.", "en-machine-interconnection.html", "Requirements →"),
            ("JD Industry", "Our production software: from connected machines to a full ERP on ERPNext, with data migration from the old program.", "en-erpnext-manufacturing.html", "Discover JD Industry →")]),
}

# incentivi in home: (eyebrow, titolo, testo, [(titolo, testo, link, etichetta)])
INCENTIVES = {
    "it": ("Incentivi", "Agevolazioni in cui il nostro lavoro è un requisito.",
           "Senza macchine interconnesse non c'è iperammortamento. Noi curiamo la parte tecnica e la documentazione per il perito; la pratica resta al tuo consulente o commercialista.",
           [("Iperammortamento 2026–2028", "Le macchine nuove rientrano solo se interconnesse al sistema aziendale e se un perito lo attesta. Requisiti, scadenze e procedura passo per passo.", "guida-interconnessione-iperammortamento.html", "Leggi la guida →"),
            ("Contributi FVG per hotel e alberghi diffusi", "La Regione sostiene l'ammodernamento e l'efficienza delle strutture ricettive: clima, accessi e domotica possono far parte del progetto.", "guida-contributi-fvg-hotel.html", "Leggi la guida →"),
            ("Anche il software di produzione", "Gestionali di produzione, MES e piattaforme possono rientrare nell'iperammortamento se compresi nell'Allegato V e interconnessi.", "guida-iperammortamento-software-erp-mes.html", "Leggi la guida →")]),
    "en": ("Incentives", "Incentives where our work is a requirement.",
           "No interconnected machines, no hyper-depreciation. We handle the technical side and the documentation for the appraiser; the application stays with your advisor or accountant.",
           [("Italian hyper-depreciation 2026–2028", "New machines qualify only when interconnected with company systems and certified by an appraiser.", "en-machine-interconnection.html", "Machine interconnection →"),
            ("Regional grants for hotels", "Friuli Venezia Giulia supports modernisation and efficiency of accommodation: climate, access and automation can be part of the project.", "en-hotel-bnb-automation.html", "Hotel automation →"),
            ("Production software too", "Production management, MES and platforms can qualify for hyper-depreciation when listed in Annex V and interconnected.", "en-erpnext-manufacturing.html", "Discover JD Industry →")]),
}

# fase documentazione, prima dell'assistenza, in tutti i servizi
DOC_STEP = {"it": ("Documentazione", "Schemi, configurazioni, credenziali e procedure consegnati a te: il sistema resta comprensibile anche dopo la consegna."),
            "en": ("Documentation", "Diagrams, configurations, credentials and procedures handed over to you: the system stays understandable after delivery.")}


# ---------------------------------------------------------------- home

def home(lang="it"):
    u = UI[lang]
    if lang == "it":
        t = dict(eyebrow="Integrazione macchine e gestionali · Friuli Venezia Giulia",
                 h1="Macchine, impianti e software: <span>integrati e sempre connessi.</span>",
                 lead="JDEVPRO nasce in Friuli con Jacopo Ellero. Colleghiamo al gestionale qualsiasi macchina con PLC o CNC per l'interconnessione 4.0 e l'iperammortamento: decine di macchine già collegate, tutte asseverate e ammesse. Sviluppiamo anche JD Industry, il gestionale di produzione, e seguiamo tutto nel tempo, in trasferta dove serve e da remoto ovunque.",
                 b1="Interconnessione macchine", b1h="interconnessione-macchine-industria-4-0.html", b2="Scrivici", ae="Anche", ah="Strutture ricettive e software su misura.",
                 enter="Entra nell'area →",
                 proof=[("JD Industry", "Gestionale di produzione collegato a macchine SCM ed Essetre.", "gestionale-produzione-erpnext.html"),
                        ("E-commerce e marketplace", "Gestionale collegato a fornitore, marketplace e corriere.", "integrazione-software-api.html"),
                        ("Prodotti", "Welora per le strutture ricettive e JD Industry per la produzione.", "prodotti.html")],
                 title="JDEVPRO · Interconnessione macchine e gestionali in Friuli",
                 desc="Interconnessione macchine 4.0 per l'iperammortamento: decine di macchine collegate al gestionale, tutte asseverate e ammesse. Friuli Venezia Giulia e Veneto.")
    else:
        t = dict(eyebrow="Machine and business software integration · North-east Italy",
                 h1="Machines, installations and software: <span>integrated and always connected.</span>",
                 lead="JDEVPRO was founded in Friuli by Jacopo Ellero. We connect any PLC or CNC machine to business software for Industry 4.0 interconnection and the Italian tax incentive: dozens of machines already connected, all certified and approved. We also build JD Industry, our production software, and look after everything over time, on site where needed and remotely anywhere.",
                 b1="Machine interconnection", b1h="en-machine-interconnection.html", b2="Write to us", ae="Also", ah="Hospitality and custom software.",
                 enter="Enter the area →",
                 proof=[("JD Industry", "Production software connected to SCM and Essetre machines.", "en-erpnext-manufacturing.html"),
                        ("E-commerce and marketplaces", "Business software connected to supplier, marketplaces and courier.", "en-software-integration-api.html"),
                        ("Products", "Welora for hospitality and JD Industry for manufacturing.", "en-products.html")],
                 title="JDEVPRO · Machine interconnection and business software, Italy",
                 desc="Industry 4.0 machine interconnection: dozens of machines connected to business software, all certified and approved. North-east Italy.")
    cards = ""
    for a in AREAS[lang]:
        if a["key"] == "industria":
            continue  # l'industria ha già la sua sezione subito sotto l'apertura
        svcs = area_services(lang, a["key"])
        svc = "<ul>" + "".join(f'<li><a href="{s["href"]}">{s["card_title"]}</a></li>' for s in svcs if s.get("it_slug", s["href"]) not in SUPPORT) + "</ul>"
        also = [s for s in svcs if s.get("it_slug", s["href"]) in SUPPORT]
        if also:
            svc += "<p class=\"area-also\">" + ("Anche: " if lang == "it" else "Also: ") + ", ".join(
                f'<a href="{s["href"]}">{s["card_title"]}</a>' for s in also) + "</p>"
        cards += f"""<article class="area-card area-{a['key']} reveal">
<p class="eyebrow">{a['eyebrow']}</p>
<h3><a href="{a['slug']}">{a['nav']}</a></h3>
<p>{a['card']}</p>
{svc}
<a class="competence-more" href="{a['slug']}">{t['enter']}</a>
</article>
"""
    proof = "".join(f'<a href="{h}"><strong>{x}</strong><span>{d}</span></a>' for x, d, h in t["proof"])
    ne, nh, np_, nitems = INDUSTRIAL[lang]
    industrial = "".join(f'<article class="outcome reveal"><h3>{a}</h3><p>{b}</p><a class="card-link" href="{h}">{lbl}</a></article>' for a, b, h, lbl in nitems)
    ie, ih, ip, items = INCENTIVES[lang]
    incentives = "".join(f'<article class="outcome reveal"><h3>{a}</h3><p>{b}</p><a class="card-link" href="{h}">{lbl}</a></article>' for a, b, h, lbl in items)
    w = WHY[lang]
    body = f"""{header("index.html" if lang == "it" else "en.html", lang, home=True, switch="en.html" if lang == "it" else "index.html")}<main id="main">
<section class="hero hero-min" id="top">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell hero-min-copy reveal">
<p class="eyebrow">{t['eyebrow']}</p>
<h1>{t['h1']}</h1>
<p class="hero-lead">{t['lead']}</p>
<div class="hero-actions">
<a class="button primary" href="{t['b1h']}">{t['b1']}</a>
<a class="button ghost" href="#contatto">{t['b2']}</a>
</div>
{stats_html("home", lang)}
</div>
</section>
<section class="section section-tight section-white" id="integrazione-industriale">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{ne}</p><h2>{nh}</h2><p>{np_}</p></div>
<div class="outcome-grid">{industrial}</div>
</div>
</section>
<section class="section" id="aree">
<span id="competenze"></span>
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{t['ae']}</p><h2>{t['ah']}</h2></div>
<div class="area-grid area-grid-2">
{cards}</div>
</div>
</section>
<section class="section section-tight section-paper">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{ie}</p><h2>{ih}</h2><p>{ip}</p></div>
<div class="outcome-grid">{incentives}</div>
</div>
</section>
<section class="section section-tight section-white why-band">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">{w['e']}</p><h2>{w['h']}</h2></div>
<div class="reveal"><p class="why-copy">{w['p']}</p><p class="why-partners">{w['partners']}</p></div>
</div>
</section>
<section class="section section-tight proof-band">
<div class="shell">
<div class="proof-grid proof-links reveal">{proof}</div>
</div>
</section>
{contact(lang)}</main>
"""
    slug = "index.html" if lang == "it" else "en.html"
    org = ORG if lang == "it" else dict(ORG, description="Industry 4.0 machine interconnection and JD Industry production software. Also custom software and hotel automation, in north-east Italy.")
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
    prods = [x for k in a.get("products", []) for x in PRODUCTS[lang] if x["key"] == k]
    products = ""
    if prods:
        pe, ph = ("Prodotto", "Pronto da usare, adattato a voi.") if lang == "it" else ("Product", "Ready to use, adapted to you.")
        pcards = "".join(f'<a class="product-card product-card-{x["key"]} reveal" href="{x["slug"]}"{ext(x["slug"])}><span class="eyebrow">{x["eyebrow"]}</span>'
                         f'<strong>{x["nav"]}</strong><span class="product-card-text">{x["card"]}</span><span class="competence-more">{(x["slug"].split("//")[1].rstrip("/") + " ↗") if x.get("external") else u["more"]}</span></a>'
                         for x in prods)
        products = f"""<section class="section section-tight section-dark">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{pe}</p><h2>{ph}</h2></div>
<div class="product-grid">{pcards}</div>
</div>
</section>
"""
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
{stats_html("area:" + a["key"], lang)}
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
{products}<section class="section section-tight proof-band">
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
    for x in products(lang):
        pts = "".join(f"<li>{p}</li>" for p in pp["points"][x["key"]])
        label = x["slug"].split("//")[1].rstrip("/") + " ↗" if x.get("external") else u["more"]
        rows += f"""<article class="product-row product-card-{x['key']} reveal">
<div><p class="eyebrow">{x['eyebrow']}</p><h2>{x['nav']}</h2><p class="product-card-text">{x['card']}</p>
<a class="button primary" href="{x['slug']}"{ext(x['slug'])}>{label}</a></div>
<ul class="status-list">{pts}</ul>
</article>
"""
    jsonld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": pp["nav"], "description": pp["desc"], "url": url_of(pp["slug"]),
               "hasPart": [{"@type": "CreativeWork", "name": x["nav"], "url": x["slug"] if x.get("external") else BASE + x["slug"]} for x in products(lang)]},
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
    steps = "\n".join(f'<li><strong>{a}</strong><span>{b}</span></li>' for a, b in p["steps"][:-1] + [DOC_STEP[lang]] + p["steps"][-1:])

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
        reach_p, grid = u["reach_p"], "tier-grid"
        # macchine e impianti senza interfaccia: si aggiungono sensori
        if it_slug in ("interconnessione-macchine-industria-4-0.html", "monitoraggio-iot.html"):
            tiers_src = tiers_src + [SENSOR_TIER[lang]]
            reach_p = reach_p.replace("Tre strade", "Quattro strade").replace("Three routes", "Four routes")
            grid = "tier-grid tier-grid-4"
        tiers = "\n".join(
            f'<article class="tier reveal"><span class="competence-num">0{i}</span><h3>{a}</h3><p>{b}</p></article>'
            for i, (a, b) in enumerate(tiers_src, 1))
        if it_slug in TECH_TIERS:
            intro = f"""<div class="section-heading reveal"><p class="eyebrow">{u['reach_e']}</p><h2>{u['reach_h']}</h2><p>{reach_p}</p></div>
<div class="{grid}">
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
{stats_html(it_slug, lang) or (f'<p class="hero-proof">{p["proof"]}</p>' if p.get("proof") else '')}
{(lambda c: f'<p class="hero-callout">{c[0]} <a href="{c[2]}"{ext(c[2])}>{c[1]}</a></p>' if c else '')(CALLOUTS.get(it_slug, {}).get(lang))}
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
{contact(lang, CTAS.get(it_slug, {}).get(lang))}<section class="section section-tight related">
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
<li><strong>Assistenza nel tempo</strong><span>Per gestionali, integrazioni e siti un canone con backup e aggiornamenti; per macchine e impianti interventi quando servono.</span></li>
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
    parts = [f'<h2>{h}</h2>\n' + "\n".join(render_block(b) for b in blocks) for h, blocks in g["sections"]]
    # la guida può portare a un servizio o a un prodotto
    target = next((dict(p, label=p["card_title"], key=p["slug"]) for p in PAGES if p["slug"] == g["cta"]), None) or \
        next(dict(x, label=x["nav"]) for x in PRODUCTS["it"] if x["slug"] == g["cta"])
    cta = g.get("contact") or CTAS.get(target["key"], {}).get("it")
    inline_h = cta[0] if cta else "Vuoi capire se fa per te?"
    parts.insert(1, f'<div class="article-cta"><p><strong>{inline_h}</strong> Rispondiamo per iscritto entro 24 ore.</p>'
                    f'<a class="button ghost" href="#contatto">Scrivici →</a></div>')
    sections = "\n".join(parts)
    jsonld = [
      {"@context": "https://schema.org", "@type": "Article", "headline": g["short"], "description": g["desc"],
       "url": url, "inLanguage": "it", "datePublished": "2026-10-27", "dateModified": GUIDE_MODIFIED,
       "author": {"@type": "Person", "name": "Jacopo Ellero", "url": BASE + "chi-sono.html"},
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
<p class="hero-proof">Aggiornata a {GUIDE_UPDATED}</p>
</div>
</section>
<section class="section section-tight section-white">
<div class="shell article">
{sections}
<div class="article-cta">
<p><strong>Ti serve una mano?</strong> {target['label']}: metodo, esempi e prezzi indicativi.</p>
<a class="button primary" href="{target['slug']}">Vai alla pagina →</a>
</div>
</div>
</section>
{contact("it", cta)}</main>
"""
    return head(g["title"], g["desc"], g["slug"], jsonld) + body + footer()


def guide_areas(x):
    """Aree in cui elencare una guida: indicate a mano o quella del servizio di destinazione."""
    return x.get("areas") or [PRIMARY_AREA[x.get("cta", "interconnessione-macchine-industria-4-0.html")]]


def guide_index():
    groups = ""
    for a in AREAS["it"]:
        gs = [x for x in [TEST] + GUIDES if a["key"] in guide_areas(x)]
        if gs:
            cards = "".join(f'<a href="{x["slug"]}"><strong>{x["short"]}</strong><span>{x["desc"]}</span></a>' for x in gs)
            groups += f'<p class="eyebrow local-eyebrow"><a class="guide-area" href="{a["slug"]}">{a["nav"]} →</a></p><div class="related-grid guides-grid">{cards}</div>\n'
    jsonld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Guide JDEVPRO", "url": BASE + "guide.html",
               "hasPart": [{"@type": "Article", "headline": g["short"], "url": BASE + g["slug"]} for g in GUIDES]}, ORG_REF]
    body = f"""{header('guide.html')}<main id="main">
<section class="hero page-hero">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell page-hero-copy reveal">
<nav aria-label="Percorso" class="breadcrumb"><a href="index.html">Home</a><span>/</span><span aria-current="page">Guide</span></nav>
<p class="eyebrow">Guide e strumenti</p>
<h1>Guide pratiche, <span>area per area.</span></h1>
<p class="hero-lead">Spiegazioni concrete per capire cosa serve prima di chiedere un preventivo.</p>
</div>
</section>
<section class="section section-tight section-white">
<div class="shell">{groups}</div>
</section>
{contact()}</main>
"""
    return head("Guide: incentivi 2026, macchine 4.0, gestionale e hotel | JDEVPRO",
                "Guide pratiche: iperammortamento 2026, voucher, Conto Termico, Fondo turismo FVG, interconnessione 4.0, ERPNext, VoIP e videosorveglianza.",
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
              'href="assets/', 'src="assets/', 'href="index.html', 'href="privacy.html"', 'href="cookie-policy.html"', 'href="guide.html"'):
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


# ---------------------------------------------------------------- privacy e cookie

def legal_page(kind, lang):
    d = LEGAL_DATA["LEGAL"][kind][lang]
    u = UI[lang]
    home_slug = "index.html" if lang == "it" else "en.html"
    sections = "\n".join(f'<h2>{h}</h2>\n' + "\n".join(render_block(b) for b in blocks) for h, blocks in d["sections"])
    label = "Preferenze cookie" if lang == "it" else "Cookie preferences"
    back = "Torna al sito" if lang == "it" else "Back to the site"
    jsonld = [{"@context": "https://schema.org", "@type": "WebPage", "name": d["nav"], "description": d["desc"], "url": url_of(d["slug"]),
               "inLanguage": lang, "about": {"@id": ORG_ID}},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": u["home"], "item": url_of(home_slug)},
                  {"@type": "ListItem", "position": 2, "name": d["nav"], "item": url_of(d["slug"])}]}, ORG_REF]
    body = f"""{header(d['slug'], lang, switch=d['other'])}<main id="main">
<section class="hero page-hero">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell page-hero-copy reveal">
<nav aria-label="{u['crumbs']}" class="breadcrumb"><a href="{home_slug}">{u['home']}</a><span>/</span><span aria-current="page">{d['nav']}</span></nav>
<p class="eyebrow">{d['eyebrow']}</p>
<h1>{d['h1']}</h1>
<p class="hero-lead">{d['lead']}</p>
</div>
</section>
<section class="section section-tight section-white">
<div class="shell article">
{sections}
<p class="legal-updated">{LEGAL_DATA["UPDATED"][lang]}</p>
<div class="hero-actions"><a class="button primary" href="{home_slug}">{back}</a><a class="button ghost dark" data-cookie-settings="" href="#">{label}</a></div>
</div>
</section>
</main>
"""
    alternates = [("it", LEGAL_DATA["LEGAL"][kind]["it"]["slug"]), ("en", LEGAL_DATA["LEGAL"][kind]["en"]["slug"])]
    return head(d["title"], d["desc"], d["slug"], jsonld, lang, alternates=alternates) + body + footer(lang)


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
{stats_html("about", lang)}
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


def products(lang):
    """Solo i prodotti in vendita: AKIOS e ORYVAEL sono sviluppo."""
    return [x for x in PRODUCTS[lang] if not x.get("dev")]


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
    if kind == "prices":
        _, eyebrow, h2, intro, rows, note = b
        items = "".join(f'<div class="price reveal"><span>{t}</span><strong>{p}</strong><small>{d}</small></div>' for t, p, d in rows)
        intro_html = f"<p>{intro}</p>" if intro else ""
        note_html = f'<p class="price-extra">{note}</p>' if note else ""
        return f"""<section class="section section-tight {bg}" data-prices>
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{eyebrow}</p><h2>{h2}</h2>{intro_html}</div>
<div class="price-grid">{items}</div>
{note_html}
</div>
</section>
"""
    if kind == "figure":
        _, eyebrow, h2, src, alt, caption, w, h = b
        return f"""<section class="section section-tight {bg}">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{eyebrow}</p><h2>{h2}</h2></div>
<figure class="product-shot reveal"><img src="{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async"><figcaption>{caption}</figcaption></figure>
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
    # il primo blocco prezzi diventa l'ancora del pulsante "Vedi i prezzi"
    has_prices = "data-prices" in blocks
    blocks = blocks.replace(" data-prices", ' id="prezzi"', 1).replace(" data-prices", "")
    buttons = "".join(f'<a class="button {"primary" if i == 0 else "ghost"}" href="{l}" rel="noreferrer" target="_blank">{n}</a>'
                      for i, (n, l) in enumerate(pr["links"]))
    if not pr.get("dev"):
        buttons += f'<a class="button {"ghost" if pr["links"] else "primary"}" href="#contatto">{u["talk"]}</a>'
    if has_prices:
        buttons += f'<a class="button ghost" href="#prezzi">{"Vedi i prezzi" if lang == "it" else "See prices"}</a>'
    others = "".join(f'<a href="{x["slug"]}"{ext(x["slug"])}><strong>{x["nav"]}</strong><span>{x["card"]}</span></a>'
                     for x in PRODUCTS[lang] if x["key"] != pr["key"] and bool(x.get("dev")) == bool(pr.get("dev")))
    if pr["key"] == "welora":
        main_ld = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Welora", "description": pr["desc"], "url": url,
                   "applicationCategory": "BusinessApplication", "operatingSystem": "Web",
                   "offers": {"@type": "Offer", "price": "29", "priceCurrency": "EUR", "availability": "https://schema.org/PreOrder"},
                   "publisher": {"@id": ORG_ID}, "sameAs": ["https://welora.it/"]}
    elif pr["key"] == "erp":
        main_ld = {"@context": "https://schema.org", "@type": "Service", "name": pr["nav"], "description": pr["desc"], "url": url,
                   "serviceType": "ERP", "provider": {"@id": ORG_ID}, "areaServed": "IT",
                   "offers": {"@type": "Offer", "priceCurrency": "EUR",
                              "priceSpecification": {"@type": "PriceSpecification", "minPrice": 990, "priceCurrency": "EUR"}}}
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
    other_label = ("Altri progetti di sviluppo" if lang == "it" else "Other development projects") if pr.get("dev") else \
        ("Altri prodotti" if lang == "it" else "Other products")
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
{blocks}{contact(lang, CTAS.get(pr["key"], {}).get(lang))}<section class="section section-tight related">
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
for _kind in ("privacy", "cookie"):
    for _lang in ("it", "en"):
        write(LEGAL_DATA["LEGAL"][_kind][_lang]["slug"], legal_page(_kind, _lang))
for old, target in OLD_URLS.items():
    write(f"{old}/index.html", redirect_stub(target))

urls = (["", "en.html"] + [p["slug"] for p in PAGES] + [EN_SLUG[p["slug"]] for p in PAGES]
        + [c["slug"] for c in CITIES] + ["guide.html", TEST["slug"]] + [g["slug"] for g in GUIDES]
        + [x["slug"] for l in ("it", "en") for x in PRODUCTS[l] if not x.get("external")] + [a["slug"] for l in ("it", "en") for a in AREAS[l]] + [PRODUCTS_PAGE["it"]["slug"], PRODUCTS_PAGE["en"]["slug"], WHERE_PAGE["slug"]] + ["chi-sono.html", "en-about.html", "privacy.html", "privacy-en.html", "cookie-policy.html", "cookie-policy-en.html"])
sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sitemap += [f"  <url><loc>{BASE}{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls]
sitemap.append("</urlset>")
(REPO / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8", newline="\n")
print("ok", len(urls), "URL in sitemap")
