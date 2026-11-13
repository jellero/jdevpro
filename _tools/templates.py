# Modelli di pagina. Eseguito dopo build_site.py (stesso namespace): usa PAGES, TIERS, BASE, ecc.
import datetime
import runpy

EXTRA = runpy.run_path(str(pathlib.Path(__file__).with_name("content_extra.py")))
ABOUT = runpy.run_path(str(pathlib.Path(__file__).with_name("content_about.py")))["ABOUT"]
METHOD = runpy.run_path(str(pathlib.Path(__file__).with_name("content_method.py")))["METHOD"]
PRODUCTS = runpy.run_path(str(pathlib.Path(__file__).with_name("content_products.py")))["PRODUCTS"]
SMARTDRIVE = runpy.run_path(str(pathlib.Path(__file__).with_name("content_smartdrive.py")))
AREAS_DATA = runpy.run_path(str(pathlib.Path(__file__).with_name("content_areas.py")))
STATS = runpy.run_path(str(pathlib.Path(__file__).with_name("content_stats.py")))["STATS"]
LEGAL_DATA = runpy.run_path(str(pathlib.Path(__file__).with_name("content_legal.py")))
PARTNERS = runpy.run_path(str(pathlib.Path(__file__).with_name("content_partners.py")))["PARTNERS"]


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
GUIDES = GUIDES + runpy.run_path(str(pathlib.Path(__file__).with_name("content_guides_choose.py")))["CHOOSE_GUIDES"]
GUIDES = GUIDES + runpy.run_path(str(pathlib.Path(__file__).with_name("content_guides_tech.py")))["TECH_GUIDES"]
GUIDES = GUIDES + runpy.run_path(str(pathlib.Path(__file__).with_name("content_guides_apps.py")))["APP_PUBLISHING_GUIDES"]
EN_SLUG, EN_PAGES, EN_TIERS = EXTRA["EN_SLUG"], EXTRA["EN_PAGES"], EXTRA["EN_TIERS"]
SENSOR_TIER = {"it": ("Sensori aggiunti", "Per macchine e impianti senza nessuna interfaccia, anche vecchi: sensori e contatori rilevano stato, cicli, tempi e consumi e li portano nei vostri sistemi."),
               "en": ("Added sensors", "For machines and plants with no interface at all, old ones included: sensors and meters detect status, cycles, times and consumption and bring them into your systems.")}
TODAY = datetime.date.today().isoformat()

import hashlib
ASSET_V = {n: hashlib.sha1((REPO / n).read_bytes()).hexdigest()[:8] for n in ("styles.css", "overrides.css", "pages.css", "script.js")}

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
             li="Oppure su LinkedIn ↗", where="Friuli Venezia Giulia e Veneto · trasferte · da remoto ovunque",
             f_who="Software e sistemi integrati · Friuli Venezia Giulia", f_legal="JDEVPRO di Jacopo Ellero · Friuli Venezia Giulia · P.IVA IT02783420306", privacy="privacy.html", cookie="cookie-policy.html",
             mailto=MAILTO),
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
             li="Or on LinkedIn ↗", where="Friuli Venezia Giulia, Italy · north-east Italy · travel · remote work anywhere",
             f_who="Business software and systems integration · North-east Italy", f_legal="JDEVPRO by Jacopo Ellero · Friuli Venezia Giulia, Italy · VAT IT02783420306", privacy="privacy-en.html", cookie="cookie-policy-en.html",
             mailto=MAILTO_EN),
}

PRICE_EN = {"Collegamento di una macchina": "Connecting one machine", "Gestionale essenziale per interconnessione (solo se necessario)": "Basic management application for interconnection (only if needed)", "Dati macchina e assistenza": "Machine data and support",
            "Prima versione del gestionale": "First version of the software", "Hosting, backup e assistenza": "Hosting, backups and support",
            "Progetto e configurazione": "Design and configuration", "Dati, allarmi e manutenzione": "Data, alarms and maintenance",
            "Integrazione tra due sistemi": "Integration between two systems", "Monitoraggio e manutenzione": "Monitoring and maintenance",
            "Sito con pannello di gestione": "Website with management panel", "Hosting e manutenzione": "Hosting and maintenance",
            "per tipo di macchina · eventuali sensori esclusi": "per machine type · any sensors excluded",
            "per tipo di macchina · integrazione con software esistente, se tecnicamente possibile · eventuali sensori esclusi": "per machine type · integration with existing software where technically feasible · any sensors excluded", "opzionale · quando manca un gestionale utilizzabile o il collegamento non è possibile": "optional · when suitable existing software is unavailable or cannot be integrated", "per macchina": "per machine",
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

ADDRESS = {"@type": "PostalAddress", "addressRegion": "Friuli Venezia Giulia", "addressCountry": "IT"}

ORG = {
  "@context": "https://schema.org", "@type": "ProfessionalService", "@id": ORG_ID, "name": "JDEVPRO",
  "url": BASE, "logo": BASE + "assets/icon-512.png", "image": BASE + "assets/og-jdevpro.jpg", "email": EMAIL,
  "vatID": "IT02783420306", "priceRange": "€€",
  "founder": {"@type": "Person", "name": "Jacopo Ellero", "url": BASE + "chi-siamo.html"},
  "address": ADDRESS,
  "geo": {"@type": "GeoCoordinates", "latitude": 46.4057, "longitude": 13.0154},
  "areaServed": [{"@type": "AdministrativeArea", "name": "Friuli Venezia Giulia"},
                 {"@type": "City", "name": "Udine"}, {"@type": "City", "name": "Pordenone"},
                 {"@type": "City", "name": "Trieste"}, {"@type": "City", "name": "Gorizia"},
                 {"@type": "AdministrativeArea", "name": "Veneto"}, {"@type": "Country", "name": "Italia"}],
  "description": "JDEVPRO sviluppa software, integrazioni industriali e sistemi connessi per imprese: interconnessione macchine 4.0, gestionali, automazione e infrastrutture, in Friuli Venezia Giulia e Veneto.",
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
        if lang == "it" and a["key"] == "industria":
            sub += f'\n<a href="{PARTNERS["slug"]}"{cur(current == PARTNERS["slug"])}>{PARTNERS["nav"]}</a>'
            active = active or current == PARTNERS["slug"]
        links += (f'<div class="nav-group{" is-current" if active else ""}">'
                  f'<a class="nav-group-label" href="{a["slug"]}">{a["nav"]} <span aria-hidden="true">▾</span></a>'
                  f'<div class="nav-sub">\n{sub}\n</div></div>\n')
    pp = PRODUCTS_PAGE[lang]
    prods = products(lang)
    drive_slug = "smartdrive.html" if lang == "it" else "en-smartdrive.html"
    active = current in (pp["slug"], drive_slug, "digital-receptionist.html", "en-digital-receptionist.html") or any(x["slug"] == current for x in prods)
    psub = f'<a class="nav-sub-all" href="{pp["slug"]}"{cur(current == pp["slug"])}>{"Tutti i prodotti" if lang == "it" else "All products"} →</a>\n' + "\n".join(
        f'<a href="{x["slug"]}"{ext(x["slug"])}{cur(x["slug"] == current)}>{x["nav"]}{" ↗" if x.get("external") else ""}</a>' for x in prods)
    psub += f'\n<a href="{drive_slug}"{cur(current == drive_slug)}>SmartDrive</a>'
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


# Modulo statico: i dati sono inviati soltanto tramite il programma di posta del visitatore.
INQUIRY_FORM = {
    "it": """<form class="interconnection-form" data-interconnection-form action="mailto:info@jdevpro.it" method="post" enctype="text/plain">
<h3>Richiedi una verifica di interconnessione</h3>
<p>Inserisci i dati essenziali: prepariamo la richiesta per il nostro indirizzo email.</p>
<div class="interconnection-fields">
<label>Azienda <input name="company" autocomplete="organization" maxlength="120" required placeholder="Ragione sociale"></label>
<label>Email di contatto <input name="email" type="email" autocomplete="email" maxlength="160" required placeholder="nome@azienda.it"></label>
<label>Marca e modello macchina <input name="machine" maxlength="160" required placeholder="Es. SCM, modello e controllo"></label>
<label>Numero di macchine <input name="machines" type="number" min="1" max="999" value="1" required></label>
<label>Gestionale in uso (se presente) <input name="erp" maxlength="160" placeholder="Nome del programma o nessuno"></label>
<label>Provincia / località <input name="location" maxlength="100" placeholder="Dove si trovano le macchine"></label>
<label class="field-wide">Dati da collegare o altre informazioni <textarea name="notes" rows="3" maxlength="1200" placeholder="Commesse, tempi, allarmi, produzione..."></textarea></label>
</div>
<div class="interconnection-form-actions"><button type="submit" class="button primary">Prepara l'email</button><button type="button" class="button ghost dark" data-lead-copy>Copia la richiesta</button></div>
<p class="interconnection-disclaimer">Questo modulo non invia dati a un server: apre il tuo programma di posta con la richiesta compilata. L'invio avviene solo dopo la tua conferma. <a href="privacy.html">Privacy</a>.</p>
<p class="interconnection-form-status" aria-live="polite" data-form-status></p>
</form>""",
    "en": """<form class="interconnection-form" data-interconnection-form action="mailto:info@jdevpro.it" method="post" enctype="text/plain">
<h3>Request an interconnection review</h3>
<p>Add the essential details and prepare an email to our technical team.</p>
<div class="interconnection-fields">
<label>Company <input name="company" autocomplete="organization" maxlength="120" required placeholder="Company name"></label>
<label>Contact email <input name="email" type="email" autocomplete="email" maxlength="160" required placeholder="name@company.com"></label>
<label>Machine make and model <input name="machine" maxlength="160" required placeholder="Make, model and controller"></label>
<label>Number of machines <input name="machines" type="number" min="1" max="999" value="1" required></label>
<label>Current business software (if any) <input name="erp" maxlength="160" placeholder="Software name or none"></label>
<label>Location <input name="location" maxlength="100" placeholder="Machine location"></label>
<label class="field-wide">Data to exchange or other details <textarea name="notes" rows="3" maxlength="1200" placeholder="Jobs, time, alarms, production..."></textarea></label>
</div>
<div class="interconnection-form-actions"><button type="submit" class="button primary">Prepare email</button><button type="button" class="button ghost dark" data-lead-copy>Copy request</button></div>
<p class="interconnection-disclaimer">This form does not send data to a server. It opens your email application with the request filled in; you confirm sending there. <a href="privacy-en.html">Privacy</a>.</p>
<p class="interconnection-form-status" aria-live="polite" data-form-status></p>
</form>""",
}

def inquiry_form(lang):
    return INQUIRY_FORM[lang]


def contact(lang="it", cta=None, show_form=False):
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
{inquiry_form(lang) if show_form else ''}
</div>
<div class="contact-actions">
<a class="button light big" href="{u['mailto']}">{u['c_mail']}</a>
<button class="contact-copy" type="button" data-copy-email="{EMAIL}" data-copied-label="{u['copied']}"><span>{EMAIL}</span><em>{u['copy']}</em></button>
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
    drive_slug = "smartdrive.html" if lang == "it" else "en-smartdrive.html"
    links += f'<a href="{drive_slug}">SmartDrive</a>'
    if lang == "it":
        links += '<a href="guide.html">Guide</a>'
        links += f'<a href="{WHERE_PAGE["slug"]}">{WHERE_PAGE["nav"]}</a>'
        links += f'<a href="{PARTNERS["slug"]}">{PARTNERS["nav"]}</a>'
    links += f'<a href="{ABOUT[lang]["slug"]}">{ABOUT[lang]["nav"]}</a>'
    links += f'<a href="{METHOD[lang]["slug"]}">{METHOD[lang]["nav"]}</a>'
    services = "".join(f'<a href="{p["href"]}">{p["card_title"]}</a>' for p in pages_for(lang))
    if lang == "it":
        services += "".join(f'<a href="{c["slug"]}">{c["name"]}</a>' for c in CITIES)
    return f"""<footer class="footer">
<div class="shell footer-grid footer-wide">
<div><strong>JDEVPRO</strong><span>{u['f_who']}</span></div>
<div class="footer-links">{links}</div>
<div><span>{u['f_legal']}</span><a href="{u['privacy']}">Privacy</a><a href="{u['cookie']}">Cookie</a><a href="https://github.com/jellero" rel="noreferrer" target="_blank">GitHub</a><a href="{LI}" rel="noreferrer" target="_blank">LinkedIn</a></div>
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
    "it": ("Integrazione industriale", "Dalla macchina al gestionale: sviluppo e documentazione per le pratiche.",
           "Sviluppiamo l'integrazione tra macchine e sistemi aziendali, gestiamo lo scambio dei dati e documentiamo collegamenti e collaudi per le pratiche tecniche.",
           [("Interconnessione macchine 4.0", "Torni, centri di lavoro, laser, presse, macchine tessili e da stampa, riempitrici: qualsiasi macchina con PLC o CNC, nuova o datata.", "interconnessione-macchine-industria-4-0.html", "Vedi i tipi di macchine →"),
            ("Asseverate e ammesse", "Le macchine che abbiamo collegato sono tutte certificate e asseverate da ingegneri, verificate per l'interconnessione e ammesse all'iperammortamento.", "guida-interconnessione-iperammortamento.html", "Requisiti e scadenze →"),
            ("JD Industry", "Il nostro gestionale di produzione: dalle macchine collegate all'ERP su ERPNext, con la migrazione dei dati dal vecchio programma.", "gestionale-produzione-erpnext.html", "Scopri JD Industry →")]),
    "en": ("Industrial integration", "From machines to business software: integration development and technical documentation.",
           "We develop integration between machines and business systems, manage data exchange and document connections and testing for technical procedures.",
           [("Industry 4.0 machine interconnection", "Lathes, machining centres, lasers, presses, textile and printing machines, fillers: any machine with a PLC or CNC, new or old.", "en-machine-interconnection.html", "See machine types →"),
            ("Sworn and approved", "The machines we have connected are all certified and sworn by engineers, verified for interconnection and approved for the Italian hyper-depreciation.", "en-machine-interconnection.html", "Requirements →"),
            ("JD Industry", "Our production software: from connected machines to a full ERP on ERPNext, with data migration from the old program.", "en-erpnext-manufacturing.html", "Discover JD Industry →")]),
}

# incentivi in home: (eyebrow, titolo, testo, [(titolo, testo, link, etichetta)])
INCENTIVES = {
    "it": ("Incentivi", "Agevolazioni in cui il nostro lavoro è un requisito.",
           "Senza macchine interconnesse non c'è iperammortamento. Noi curiamo la parte tecnica e la documentazione per il perito; la pratica resta al tuo consulente o commercialista. <a href=\"periti-ingegneri-consulenti.html\">Sei un perito, un ingegnere o un consulente? Ecco come lavoriamo con voi →</a>",
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

# Homepage commerciale: il contenuto HTML principale e' mantenuto qui per non
# reintrodurre, durante le rigenerazioni, vecchie sezioni o promozioni di prodotto.
# Le altre pagine continuano a usare i componenti dinamici del generatore.
HOME_BODY = {
    "it": r'''<main id="main">
<section class="hero hero-min" id="top">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell hero-min-copy reveal">
<p class="eyebrow">JDEVPRO · Software e integrazione per le imprese</p>
<h1>Interconnessione macchine 4.0: <span>25 macchine collegate in 15 aziende.</span></h1>
<p class="hero-lead">Colleghiamo PLC, CNC e macchine industriali ai gestionali aziendali, con collaudo e documentazione tecnica.</p>
<p class="hero-price">Interconnessione macchine <strong>da 1.500 €</strong> · preventivo dopo verifica tecnica. <a href="interconnessione-macchine-industria-4-0.html">Dettagli e condizioni →</a></p>
<div class="hero-actions">
<a class="button primary" href="#contatto">Richiedi una verifica tecnica</a>
<a class="button ghost" href="interconnessione-macchine-industria-4-0.html">Scopri come lavoriamo</a>
</div>
<ul class="hero-stats"><li><a class="stat" href="interconnessione-macchine-industria-4-0.html"><strong>25 macchine</strong><span>collegate in 15 aziende</span></a></li><li><a class="stat" href="gestionale-produzione-erpnext.html"><strong>JD Industry</strong><span>il nostro gestionale di produzione collegato alle macchine</span></a></li><li><a class="stat" href="interconnessione-macchine-industria-4-0.html"><strong class="stat-long">PLC e CNC</strong><span>verifichiamo interfacce e compatibilità, anche su macchine datate</span></a></li><li><a class="stat" href="come-lavoriamo.html"><strong>Metodo</strong><span>analisi, sviluppo, collaudo e documentazione</span></a></li></ul>
</div>
</section>
<section class="section section-tight section-white" id="integrazione-industriale">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Integrazione industriale</p><h2>Dalla macchina al gestionale: sviluppo e documentazione per le pratiche.</h2><p>Sviluppiamo l'integrazione tra macchine e sistemi aziendali, gestiamo lo scambio dei dati e documentiamo collegamenti e collaudi per le pratiche tecniche.</p></div>
<div class="outcome-grid"><article class="outcome reveal"><h3>Interconnessione macchine 4.0</h3><p>Macchine con PLC o CNC, nuove e datate. Esempi reali: bordatrici SCM Maestro Active e CNC Essetre/Tecnoessetre.</p><a class="card-link" href="interconnessione-macchine-industria-4-0.html">Vedi i tipi di macchine →</a></article><article class="outcome reveal"><h3>Documentazione per le verifiche 4.0</h3><p>Prepariamo tracciati, schemi e prove di collaudo per la verifica tecnica dell’interconnessione.</p><a class="card-link" href="periti-ingegneri-consulenti.html">Come collaboriamo con i periti →</a></article><article class="outcome reveal"><h3>JD Industry</h3><p>Il nostro gestionale di produzione: dalle macchine collegate all'ERP su ERPNext, con la migrazione dei dati dal vecchio programma.</p><a class="card-link" href="gestionale-produzione-erpnext.html">Scopri JD Industry →</a></article></div>
</div>
</section>
<section class="section section-tight proof-band" id="progetti-reali">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Realizzazioni concrete</p><h2>Macchine e software che lavorano già insieme.</h2><p>Esempi documentati di collegamenti e integrazioni realizzati. Ogni macchina viene valutata in base alle interfacce disponibili e ai dati necessari.</p></div>
<div class="proof-grid proof-links reveal">
<a href="casi-studio-industriali.html#scm-maestro-active"><strong>Bordatrice SCM · Maestro Active</strong><span>Stato e allarmi in tempo reale, commesse gestite dalla macchina, produzione acquisita e costi per commessa.</span></a>
<a href="casi-studio-industriali.html#cnc-essetre"><strong>CNC Essetre / Tecnoessetre</strong><span>Più macchine in un'unica schermata, file di lavoro, eventi di commessa, magazzino e report.</span></a>
<a href="casi-studio-industriali.html#gestionale-mes"><strong>Gestionale e MES</strong><span>Nei lavori SCM ed Essetre, dati macchina, commesse e avanzamento della produzione collegati al gestionale.</span></a>
</div>
</div>
</section>
<section class="section section-tight section-white" id="metodo-operativo">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Gestione della commessa</p><h2>Dall'analisi alla consegna: <span>un percorso di lavoro definito.</span></h2><p>Per ogni progetto definiamo obiettivi, verifiche e responsabilità. La soluzione viene sviluppata e collaudata sui sistemi reali, con documentazione utile alla gestione successiva.</p></div>
<div class="cert-grid">
<article class="cert reveal"><strong>01 · Analisi tecnica</strong><span>Raccogliamo dati su macchine, software, rete e obiettivi del progetto.</span></article>
<article class="cert reveal"><strong>02 · Proposta e perimetro</strong><span>Definiamo cosa collegare, quali dati scambiare e le attività da preventivare.</span></article>
<article class="cert reveal"><strong>03 · Sviluppo e collaudo</strong><span>Realizziamo l'integrazione e verifichiamo il funzionamento con dati e processi reali.</span></article>
<article class="cert reveal"><strong>04 · Consegna e continuità</strong><span>Documentiamo il lavoro eseguito e concordiamo modalità di assistenza ed evoluzione.</span></article>
</div>
<p class="reveal"><a class="card-link" href="come-lavoriamo.html">Il nostro metodo di lavoro →</a> · <a class="card-link" href="chi-siamo.html">Conosci JDEVPRO →</a></p>
</div>
</section>
<section class="section section-tight industrial-request" id="verifica-macchine">
<div class="shell split industrial-request-grid">
<div class="section-heading reveal"><p class="eyebrow">Per aziende manifatturiere</p><h2>Hai una macchina da collegare al gestionale?</h2>
<p>Per valutare l'interconnessione servono pochi dati: marca e modello della macchina, tipo di controllo e gestionale in uso, se presente. Verifichiamo il collegamento al software esistente oppure proponiamo un gestionale essenziale dedicato, solo quando necessario.</p>
<div class="hero-actions"><a class="button primary" href="#contatto">Richiedi una verifica tecnica</a><a class="button ghost dark" href="test-interconnessione-4-0.html">Test interconnessione 4.0</a></div></div>
<div class="industrial-request-details reveal"><h3>Da dove partiamo</h3>
<ul><li>Identificazione delle interfacce disponibili</li><li>Verifica dei dati da scambiare con ERP o gestionale</li><li>Definizione del collegamento e del collaudo</li><li>Documentazione tecnica per chi dovrà valutare i requisiti</li></ul>
<p>Se sei un perito, un ingegnere o un consulente, consulta <a href="periti-ingegneri-consulenti.html">come collaboriamo sul lato tecnico</a>.</p></div>
</div></section>
<section class="section section-tight section-paper">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Interconnessione e requisiti</p><h2>Parte tecnica documentata, valutazioni fiscali separate.</h2><p>Per i beni agevolabili, l’interconnessione ai sistemi aziendali è un requisito da verificare. JDEVPRO realizza e documenta l’integrazione tecnica; l’ammissibilità fiscale resta da valutare con il perito e il consulente incaricati. <a href="periti-ingegneri-consulenti.html">Collaborazioni con periti e consulenti →</a></p></div>
<div class="outcome-grid"><article class="outcome reveal"><h3>Iperammortamento 2026–2028</h3><p>Le macchine nuove rientrano solo se interconnesse al sistema aziendale e se un perito lo attesta. Requisiti, scadenze e procedura passo per passo.</p><a class="card-link" href="guida-interconnessione-iperammortamento.html">Leggi la guida →</a></article><article class="outcome reveal"><h3>Anche il software di produzione</h3><p>Gestionali di produzione, MES e piattaforme possono rientrare nell'iperammortamento se compresi nell'Allegato V e interconnessi.</p><a class="card-link" href="guida-iperammortamento-software-erp-mes.html">Leggi la guida →</a></article></div>
</div>
</section>
<section class="section section-tight section-white why-band">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">Perché JDEVPRO</p><h2>Un referente tecnico, <span>dall’analisi al collaudo.</span></h2></div>
<div class="reveal"><p class="why-copy">JDEVPRO segue ogni progetto con un responsabile tecnico dedicato, dall’analisi al collaudo. Quando servono interventi specialistici, coordina installatori abilitati e professionisti incaricati con compiti e responsabilità definiti.</p><p><a class="card-link" href="chi-siamo.html">Chi siamo →</a> · <a class="card-link" href="come-lavoriamo.html">Come lavoriamo →</a></p></div>
</div>
</section>

<section class="section section-tight section-paper" id="rete-partner-tecnici"><div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Organizzazione tecnica</p><h2>La nostra rete di partner tecnici.</h2>
<p>Per ogni commessa individuiamo le competenze necessarie e coordiniamo gli incarichi, senza confondere collaboratori esterni e personale JDEVPRO.</p></div>
<div class="outcome-grid">
<article class="outcome reveal"><h3>Installatori abilitati</h3><p>Impianti, cablaggi, quadri e interventi riservati alle figure in possesso delle abilitazioni richieste.</p></article>
<article class="outcome reveal"><h3>Periti e ingegneri</h3><p>Valutazioni, attestazioni e verifiche indipendenti affidate ai professionisti incaricati dal cliente.</p></article>
<article class="outcome reveal"><h3>Fornitori hardware</h3><p>PLC, HMI, rete e componenti industriali selezionati in base alla compatibilità tecnica del progetto.</p></article>
</div><p class="reveal"><a class="card-link" href="periti-ingegneri-consulenti.html">Ruoli e collaborazione con i professionisti →</a> · <a class="card-link" href="come-lavoriamo.html">Metodo e collaudo →</a></p>
</div></section>
<section class="contact-section" id="contatto">
<div class="shell contact-card reveal">
<div>
<p class="eyebrow">Contatto</p>
<h2>Raccontaci cosa devi collegare.</h2>
<p>Descrivici i sistemi che hai, cosa vuoi ottenere e i tempi. Ti rispondiamo per iscritto entro 24 ore, con domande mirate o con una proposta.</p>
<ol class="contact-steps" aria-label="Come funziona"><li><strong>Scrivici</strong> i sistemi presenti e l'obiettivo, anche in poche righe.</li><li><strong>Ti rispondiamo entro 24 ore</strong> con domande mirate o una proposta di incontro.</li><li><strong>Definiamo</strong> insieme perimetro, tempi e modalità di lavoro.</li></ol>
<form class="interconnection-form" data-interconnection-form action="mailto:info@jdevpro.it" method="post" enctype="text/plain">
<h3>Richiedi una verifica di interconnessione</h3>
<p>Inserisci i dati essenziali: prepariamo la richiesta per il nostro indirizzo email.</p>
<div class="interconnection-fields">
<label>Azienda <input name="company" autocomplete="organization" maxlength="120" required placeholder="Ragione sociale"></label>
<label>Email di contatto <input name="email" type="email" autocomplete="email" maxlength="160" required placeholder="nome@azienda.it"></label>
<label>Marca e modello macchina <input name="machine" maxlength="160" required placeholder="Es. SCM, modello e controllo"></label>
<label>Numero di macchine <input name="machines" type="number" min="1" max="999" value="1" required></label>
<label>Gestionale in uso (se presente) <input name="erp" maxlength="160" placeholder="Nome del programma o nessuno"></label>
<label>Provincia / località <input name="location" maxlength="100" placeholder="Dove si trovano le macchine"></label>
<label class="field-wide">Dati da collegare o altre informazioni <textarea name="notes" rows="3" maxlength="1200" placeholder="Commesse, tempi, allarmi, produzione..."></textarea></label>
</div>
<div class="interconnection-form-actions"><button type="submit" class="button primary">Prepara l'email</button><button type="button" class="button ghost dark" data-lead-copy>Copia la richiesta</button></div>
<p class="interconnection-disclaimer">Questo modulo non invia dati a un server: apre il tuo programma di posta con la richiesta compilata. L'invio avviene solo dopo la tua conferma. <a href="privacy.html">Privacy</a>.</p>
<p class="interconnection-form-status" aria-live="polite" data-form-status></p>
</form>
</div>
<div class="contact-actions">
<a class="button light big" href="mailto:info@jdevpro.it?subject=Richiesta%20progetto%20-%20JDEVPRO&amp;body=Buongiorno%2C%0A%0ACosa%20c%27%C3%A8%20da%20fare%3A%0A%0ADove%20%28comune%29%3A%0A%0AMacchine%2C%20camere%20o%20utenti%20coinvolti%3A%0A%0ASistemi%20gi%C3%A0%20presenti%3A%0A%0ATempistiche%20indicative%3A%0A%0AIncentivi%20o%20contributi%20previsti%20%28se%20ci%20sono%29%3A%0A%0AAzienda%20/%20riferimento%3A%0A">Scrivici una email</a>
<button class="contact-copy" type="button" data-copy-email="info@jdevpro.it" data-copied-label="Copiato ✓"><span>info@jdevpro.it</span><em>Copia</em></button>
<a class="contact-alt" href="https://www.linkedin.com/in/jacopo-ellero-a006499a/" rel="noreferrer" target="_blank">Oppure su LinkedIn ↗</a>
<span>Friuli Venezia Giulia e Veneto · trasferte · da remoto ovunque</span>
</div>
</div>
</section>
</main>''',
    "en": r'''<main id="main">
<section class="hero hero-min" id="top">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell hero-min-copy reveal">
<p class="eyebrow">JDEVPRO · Software and systems integration for businesses</p>
<h1>Industrial machine integration: <span>25 machines connected in 15 companies.</span></h1>
<p class="hero-lead">We connect industrial PLCs, CNCs and machines to existing business software, with testing and technical documentation.</p>
<p class="hero-price">Machine integration <strong>from €1,500</strong> · quoted after a technical assessment. <a href="en-machine-interconnection.html">Pricing details →</a></p>
<div class="hero-actions">
<a class="button primary" href="#contatto">Request a technical review</a>
<a class="button ghost" href="en-machine-interconnection.html">How we work</a>
</div>
<ul class="hero-stats"><li><a class="stat" href="en-machine-interconnection.html"><strong>25 machines</strong><span>connected in 15 companies</span></a></li><li><a class="stat" href="en-erpnext-manufacturing.html"><strong>JD Industry</strong><span>our production software connected to machines</span></a></li><li><a class="stat" href="en-machine-interconnection.html"><strong>PLC and CNC</strong><span>interfaces and compatibility assessed, including older machines</span></a></li><li><a class="stat" href="en-how-we-work.html"><strong>Method</strong><span>analysis, implementation, testing and documentation</span></a></li></ul>
</div>
</section>
<section class="section section-tight section-white" id="integrazione-industriale">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Industrial integration</p><h2>From machines to business software: integration development and technical documentation.</h2><p>We develop integration between machines and business systems, manage data exchange and document connections and testing for technical procedures.</p></div>
<div class="outcome-grid"><article class="outcome reveal"><h3>Industry 4.0 machine interconnection</h3><p>Machines equipped with PLCs or CNCs, new or older. Actual integrations include SCM Maestro Active edgebanders and Essetre/Tecnoessetre CNCs.</p><a class="card-link" href="en-machine-interconnection.html">See machine types →</a></article><article class="outcome reveal"><h3>Evidence for technical assessments</h3><p>We deliver connection diagrams, data records and technical testing evidence.</p><a class="card-link" href="en-machine-interconnection.html">Review interconnection requirements →</a></article><article class="outcome reveal"><h3>JD Industry</h3><p>Our production software: from connected machines to a full ERP on ERPNext, with data migration from the old program.</p><a class="card-link" href="en-erpnext-manufacturing.html">Discover JD Industry →</a></article></div>
</div>
</section>
<section class="section section-tight proof-band" id="real-projects">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Real projects</p><h2>Machines and software already working together.</h2><p>Documented examples of completed connections and integrations. We review interfaces and data requirements before proposing each connection.</p></div>
<div class="proof-grid proof-links reveal">
<a href="en-industrial-case-studies.html#scm-maestro-active"><strong>SCM edgebander · Maestro Active</strong><span>Live status and alarms, work orders managed by the machine, automatic production data and job costing.</span></a>
<a href="en-industrial-case-studies.html#cnc-essetre"><strong>Essetre / Tecnoessetre CNC</strong><span>Multiple machines in one view, job events, work files, inventory and reports.</span></a>
<a href="en-industrial-case-studies.html#gestionale-mes"><strong>ERP and MES</strong><span>Real SCM and Essetre integrations connecting machine data, production jobs and shop-floor progress to business software.</span></a>
</div></div></section>
<section class="section section-tight section-white" id="project-delivery">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Project delivery</p><h2>From analysis to handover: <span>a defined way of working.</span></h2><p>For each project, we define goals, checks and responsibilities. Integrations are developed and tested against real systems, with documentation to support ongoing operations.</p></div>
<div class="cert-grid">
<article class="cert reveal"><strong>01 · Technical review</strong><span>Understand machines, software, networking and business requirements.</span></article>
<article class="cert reveal"><strong>02 · Scope and proposal</strong><span>Agree what to connect, which data to exchange and what work to quote.</span></article>
<article class="cert reveal"><strong>03 · Development and testing</strong><span>Implement the integration and verify it against real operations and data.</span></article>
<article class="cert reveal"><strong>04 · Handover and continuity</strong><span>Document the delivered work and agree support and further improvements.</span></article>
</div>
<p class="reveal"><a class="card-link" href="en-how-we-work.html">How we work →</a> · <a class="card-link" href="en-about.html">About JDEVPRO →</a></p>
</div>
</section>
<section class="section section-tight industrial-request" id="machine-review">
<div class="shell split industrial-request-grid">
<div class="section-heading reveal"><p class="eyebrow">For manufacturers</p><h2>Need to connect a machine to business software?</h2>
<p>To review an interconnection, send the machine make and model, controller type and existing business software, if any. We first assess integration with the software you already use, and offer a simple dedicated application only when necessary.</p>
<div class="hero-actions"><a class="button primary" href="#contatto">Request a technical review</a><a class="button ghost dark" href="en-machine-interconnection.html">Machine interconnection</a></div></div>
<div class="industrial-request-details reveal"><h3>What we review</h3>
<ul><li>Available machine interfaces</li><li>Data exchange with ERP or business software</li><li>Connection approach and testing</li><li>Technical documentation for an independent assessor</li></ul>
<p>Tax incentive eligibility remains the responsibility of the appointed professionals.</p></div>
</div></section>
<section class="section section-tight section-paper">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Interconnection and requirements</p><h2>Documented technical work, independent tax assessment.</h2><p>Interconnection is one of the requirements to assess for eligible investments. JDEVPRO delivers and documents the technical integration; tax eligibility must be evaluated by the appointed specialists.</p></div>
<div class="outcome-grid"><article class="outcome reveal"><h3>Italian hyper-depreciation 2026–2028</h3><p>New machines qualify only when interconnected with company systems and certified by an appraiser.</p><a class="card-link" href="en-machine-interconnection.html">Machine interconnection →</a></article><article class="outcome reveal"><h3>Production software too</h3><p>Production management, MES and platforms can qualify for hyper-depreciation when listed in Annex V and interconnected.</p><a class="card-link" href="en-erpnext-manufacturing.html">Discover JD Industry →</a></article></div>
</div>
</section>
<section class="section section-tight section-white why-band">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">Why JDEVPRO</p><h2>One technical point of contact, <span>from assessment to commissioning.</span></h2></div>
<div class="reveal"><p class="why-copy">JDEVPRO follows each project through a dedicated technical lead, from assessment through commissioning. Qualified installers and specialist professionals are involved where required, with responsibilities defined for each engagement.</p><p><a class="card-link" href="en-about.html">About us →</a> · <a class="card-link" href="en-how-we-work.html">How we work →</a></p></div>
</div>
</section>

<section class="section section-tight section-paper" id="technical-partners"><div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Project organisation</p><h2>Our technical partner network.</h2>
<p>Specialist professionals and suppliers are involved according to each project's requirements, with roles clearly defined and without presenting them as JDEVPRO employees.</p></div>
<div class="outcome-grid">
<article class="outcome reveal"><h3>Qualified installers</h3><p>Electrical installation, wiring and control panels are handled by appropriately licensed tradespeople.</p></article>
<article class="outcome reveal"><h3>Independent assessors</h3><p>Engineers and technical experts assess formal requirements under their own appointments and responsibilities.</p></article>
<article class="outcome reveal"><h3>Hardware suppliers</h3><p>PLCs, HMIs, networking and industrial components selected to meet each integration's technical requirements.</p></article>
</div><p class="reveal"><a class="card-link" href="en-how-we-work.html">Method, responsibilities and acceptance testing →</a></p>
</div></section>
<section class="contact-section" id="contatto">
<div class="shell contact-card reveal">
<div>
<p class="eyebrow">Contact</p>
<h2>Tell us what you need to connect.</h2>
<p>Describe your systems, what you want to achieve and your timeline. We reply in writing within 24 hours, with focused questions or a proposal.</p>
<ol class="contact-steps" aria-label="How it works"><li><strong>Write to us</strong> about your current systems and goal, even in a few lines.</li><li><strong>We reply within 24 hours</strong> with focused questions or a proposal for a meeting.</li><li><strong>We define</strong> scope, timeline and way of working together.</li></ol>
<form class="interconnection-form" data-interconnection-form action="mailto:info@jdevpro.it" method="post" enctype="text/plain">
<h3>Request an interconnection review</h3>
<p>Add the essential details and prepare an email to our technical team.</p>
<div class="interconnection-fields">
<label>Company <input name="company" autocomplete="organization" maxlength="120" required placeholder="Company name"></label>
<label>Contact email <input name="email" type="email" autocomplete="email" maxlength="160" required placeholder="name@company.com"></label>
<label>Machine make and model <input name="machine" maxlength="160" required placeholder="Make, model and controller"></label>
<label>Number of machines <input name="machines" type="number" min="1" max="999" value="1" required></label>
<label>Current business software (if any) <input name="erp" maxlength="160" placeholder="Software name or none"></label>
<label>Location <input name="location" maxlength="100" placeholder="Machine location"></label>
<label class="field-wide">Data to exchange or other details <textarea name="notes" rows="3" maxlength="1200" placeholder="Jobs, time, alarms, production..."></textarea></label>
</div>
<div class="interconnection-form-actions"><button type="submit" class="button primary">Prepare email</button><button type="button" class="button ghost dark" data-lead-copy>Copy request</button></div>
<p class="interconnection-disclaimer">This form does not send data to a server. It opens your email application with the request filled in; you confirm sending there. <a href="privacy-en.html">Privacy</a>.</p>
<p class="interconnection-form-status" aria-live="polite" data-form-status></p>
</form>
</div>
<div class="contact-actions">
<a class="button light big" href="mailto:info@jdevpro.it?subject=Project%20enquiry%20-%20JDEVPRO&amp;body=Hello%2C%0A%0AWhat%20needs%20doing%3A%0A%0AWhere%20%28town%29%3A%0A%0AMachines%2C%20rooms%20or%20users%20involved%3A%0A%0AExisting%20systems%3A%0A%0ARough%20timeline%3A%0A%0AIncentives%20or%20grants%20expected%20%28if%20any%29%3A%0A%0ACompany%20/%20contact%3A%0A">Send us an email</a>
<button class="contact-copy" type="button" data-copy-email="info@jdevpro.it" data-copied-label="Copied ✓"><span>info@jdevpro.it</span><em>Copy</em></button>
<a class="contact-alt" href="https://www.linkedin.com/in/jacopo-ellero-a006499a/" rel="noreferrer" target="_blank">Or on LinkedIn ↗</a>
<span>Friuli Venezia Giulia, Italy · north-east Italy · travel · remote work anywhere</span>
</div>
</div>
</section>
</main>''',
}
HOME_META = {
    "it": {"title": "JDEVPRO | Software, integrazione industriale e interconnessione 4.0", "desc": "JDEVPRO progetta software e integrazioni per le imprese: interconnessione macchine 4.0, PLC, CNC, gestionali, automazione e collaudi. Friuli Venezia Giulia e Veneto."},
    "en": {"title": "JDEVPRO | Software, industrial integration and Industry 4.0", "desc": "JDEVPRO develops software and industrial integrations for businesses: Industry 4.0 machine connections, PLCs, CNCs, production software, automation and testing in north-east Italy."},
}

def home(lang="it"):
    slug = "index.html" if lang == "it" else "en.html"
    metadata = HOME_META[lang]
    org = ORG if lang == "it" else dict(ORG, description="JDEVPRO develops software, industrial integrations and connected systems for businesses, including Industry 4.0, production management, automation and infrastructure in north-east Italy.")
    return (head(metadata["title"], metadata["desc"], slug, [org], lang,
                 alternates=[("it", "index.html"), ("en", "en.html")])
            + header(slug, lang, home=True, switch="en.html" if lang == "it" else "index.html")
            + HOME_BODY[lang] + footer(lang))

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


PRODUCT_SHOTS = {"welora": ("assets/welora-app.webp", 756, 572, "Welora: cruscotto con arrivi, prenotazioni, check-in online e incassi"),
                 "erp": ("assets/jd-industry-progetto.webp", 1600, 1000, "JD Industry: cruscotto con macchine, commesse e produzione (dati di esempio)")}


def products_index(lang):
    u = UI[lang]
    pp = PRODUCTS_PAGE[lang]
    home_slug = "index.html" if lang == "it" else "en.html"
    other = PRODUCTS_PAGE["en" if lang == "it" else "it"]["slug"]
    rows = ""
    for idx, x in enumerate(products(lang)):
        if idx == 1:
            rows += f'<div class="section-heading reveal product-group-heading"><h2>{"Altri prodotti" if lang == "it" else "Other products"}</h2><p>{"Disponibilità e modalità di attivazione da verificare: richiedi informazioni per ciascun prodotto." if lang == "it" else "Availability and activation details are confirmed on request for each product."}</p></div>\n'
        pts = "".join(f"<li>{p}</li>" for p in pp["points"][x["key"]])
        label = x["slug"].split("//")[1].rstrip("/") + " ↗" if x.get("external") else u["more"]
        rows += f"""<article class="product-row product-card-{x['key']}{" product-row-secondary" if idx else ""} reveal">
<div><p class="eyebrow">{x['eyebrow']}</p><h2>{x['nav']}</h2><p class="product-card-text">{x['card']}</p>
<a class="button primary" href="{x['slug']}"{ext(x['slug'])}>{label}</a>{(' <a class="button ghost" href="' + x['site'] + '" target="_blank" rel="noreferrer">' + x['site'].split('//')[1].rstrip('/') + ' ↗</a>') if x.get('site') else ''}</div>
<div class="product-side">{(lambda s: f'<img class="product-thumb" src="{s[0]}" alt="{s[3]}" width="{s[1]}" height="{s[2]}" loading="lazy" decoding="async">' if s else '')(PRODUCT_SHOTS.get(x["key"]))}<ul class="status-list">{pts}</ul></div>
</article>
"""
    drive_target = "smartdrive.html" if lang == "it" else "en-smartdrive.html"
    if lang == "it":
        drive_label, drive_title = "Prodotto · Archivio e backup · Informazioni su richiesta", "SmartDrive"
        drive_desc = "Backup incrementale, versioni e recupero dei documenti aziendali. SmartDrive è autonomo o integrabile in SmartAgent, con più terminali gestiti facilmente."
        drive_more = "Scopri SmartDrive →"
        drive_points = ["Windows, Mac, Android e iPhone", "Backup foto, video, cartelle e dati selezionati", "Autonomo o integrato in SmartAgent", "Versionamento e ripristino dei documenti"]
    else:
        drive_label, drive_title = "Product · Storage and backup · Details on request", "SmartDrive"
        drive_desc = "Incremental backup, file versions and recovery for businesses. SmartDrive is standalone or optionally integrated with SmartAgent, with simple multi-device management."
        drive_more = "Explore SmartDrive →"
        drive_points = ["Windows, Mac, Android and iPhone", "Photo, video, folder and selected data backup", "Standalone or with SmartAgent", "File versioning and recovery"]
    rows += f"""<article class="product-row product-card-smartdrive product-row-secondary reveal">
<div><p class="eyebrow">{drive_label}</p><h2>{drive_title}</h2><p class="product-card-text">{drive_desc}</p>
<a class="button primary" href="{drive_target}">{drive_more}</a></div>
<div class="product-side"><ul class="status-list">{''.join(f'<li>{p}</li>' for p in drive_points)}</ul></div>
</article>
"""
    jsonld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": pp["nav"], "description": pp["desc"], "url": url_of(pp["slug"]),
               "hasPart": [{"@type": "CreativeWork", "name": x["nav"], "url": x["slug"] if x.get("external") else BASE + x["slug"]} for x in products(lang)]
               + [{"@type": "SoftwareApplication", "name": "SmartDrive", "url": BASE + drive_target}]},
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

# Foto e schermate reali nelle pagine dei servizi: (file, larghezza, altezza, testo alternativo, didascalia) per lingua
PHOTOS = {
    "interconnessione-macchine-industria-4-0.html": {
        "it": ("Sul campo", "Le macchine che colleghiamo, viste da dentro.", [
            ("assets/interconnessione-plc.webp", 1600, 828, "Quadro elettrico di una macchina collegata: schede PLC in rete con cavi Ethernet", "Il quadro di una delle macchine che abbiamo collegato al gestionale: schede PLC in rete."),
            ("assets/interconnessione-inverter.webp", 1600, 856, "Inverter e morsettiere nel quadro della stessa macchina", "Inverter e morsettiere nello stesso quadro.")]),
        "en": ("In the field", "The machines we connect, seen from inside.", [
            ("assets/interconnessione-plc.webp", 1600, 828, "Electrical cabinet of a connected machine: networked PLC boards", "The cabinet of one of the machines we connected to business software: networked PLC boards."),
            ("assets/interconnessione-inverter.webp", 1600, 856, "Drives and terminal blocks in the same cabinet", "Drives and terminal blocks in the same cabinet.")]),
    },
    "automazione-hotel-bnb.html": {
        "it": ("Il nostro gestionale", "Welora, per hotel, B&B e strutture ricettive.", [
            ("assets/welora-app.webp", 756, 572, "Welora: cruscotto con arrivi, prenotazioni, servizi, flusso del check-in e incasso", "Welora: arrivi, prenotazioni, check-in online, pagamenti e automazioni in un'unica schermata. In arrivo il 15 febbraio 2027.")]),
        "en": ("Our software", "Welora, for hotels, B&Bs and guesthouses.", [
            ("assets/welora-app.webp", 756, 572, "Welora dashboard with arrivals, bookings, services, check-in flow and payment", "Welora: arrivals, bookings, online check-in, payments and automations on one screen. Expected on 15 February 2027.")]),
    },
    "siti-web-piattaforme.html": {
        "it": ("Un esempio reale", "Lauco Experience: la mappa dei sentieri.", [
            ("assets/lauco-mappa-sentieri.webp", 1036, 940, "Mappa interattiva dei sentieri di Lauco Experience con tracciati GPX colorati e dati del percorso", "Mappa interattiva con i tracciati GPX, la posizione di chi la usa e il sentiero più vicino con lunghezza, dislivello e tempo. Tutto gestito dal pannello del sito.")]),
        "en": ("A real example", "Lauco Experience: the trail map.", [
            ("assets/lauco-mappa-sentieri.webp", 1036, 940, "Lauco Experience interactive trail map with coloured GPX tracks and route data", "Interactive map with GPX tracks, the visitor's position and the nearest trail with length, elevation gain and time, all managed from the site's panel.")]),
    },
}


def photos_html(it_slug, lang):
    d = PHOTOS.get(it_slug, {}).get(lang)
    if not d:
        return ""
    eyebrow, h2, items = d
    figs = "".join(f'<figure class="product-shot reveal"><img src="{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async"><figcaption>{cap}</figcaption></figure>'
                   for src, w, h, alt, cap in items)
    cls = "photo-grid" if len(items) > 1 else "photo-grid photo-one"
    return f"""<section class="section section-tight section-white">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{eyebrow}</p><h2>{h2}</h2></div>
<div class="{cls}">{figs}</div>
</div>
</section>
"""


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
        if link:
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
            guide_links = f'<p class="eyebrow local-eyebrow">Guide collegate</p><div class="related-grid related-flex" style="--cols:{grid_cols(len(gl))}">' + "".join(
                f'<a href="{g["slug"]}"><strong>{g["short"]}</strong><span>{g["desc"]}</span></a>' for g in gl) + "</div>"
    switch = EN_SLUG[it_slug] if lang == "it" else it_slug
    integration_guide = (('''<section class="section section-tight section-white" id="gestionale-esistente">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Integrazione con i software aziendali</p><h2>Il gestionale che utilizzi <span>può restare al suo posto.</span></h2><p>Non chiediamo alle aziende di cambiare ERP per interconnettere una macchina. Analizziamo le interfacce del software già in uso e sviluppiamo, quando possibile, il collegamento necessario. Se il gestionale non c'è oppure non consente lo scambio richiesto, proponiamo un applicativo essenziale dedicato.</p></div>
<div class="outcome-grid">
<article class="outcome reveal"><h3>Hai già un gestionale?</h3><p>Verifichiamo come integrare macchine, flussi e dati con il software esistente. L’interconnessione parte da 1.500 €, senza acquistare un nuovo gestionale se non serve.</p></article>
<article class="outcome reveal"><h3>Manca un software utilizzabile?</h3><p>Possiamo aggiungere un gestionale essenziale per l’interconnessione da 500 €: una soluzione completa per una prima macchina parte quindi da 2.000 €, secondo le esigenze tecniche.</p></article>
</div>
</div>
</section>
<section class="section section-tight section-paper" id="tipi-di-intervento">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Due esigenze, un metodo di lavoro</p><h2>Interconnessione 4.0 e monitoraggio produttivo: <span>obiettivi distinti.</span></h2><p>La possibilità tecnica di acquisire dati non determina automaticamente l’accesso alle agevolazioni. La verifica parte sempre da macchina, interfacce e obiettivi aziendali.</p></div>
<div class="outcome-grid">
<article class="outcome reveal"><h3>Macchine e requisiti 4.0</h3><p>Sviluppiamo il collegamento ai sistemi aziendali, ne collaudiamo lo scambio dati e prepariamo le evidenze tecniche. La valutazione fiscale compete ai professionisti incaricati.</p></article>
<article class="outcome reveal"><h3>Macchine già in produzione</h3><p>Valutiamo integrazioni e sensori per monitorare stato, cicli, tempi e consumi, anche quando non è previsto un incentivo.</p></article>
</div>
</div>
</section>''' if lang == "it" else '''<section class="section section-tight section-white" id="existing-business-software">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Integration with your business software</p><h2>Keep your existing system <span>wherever technically possible.</span></h2><p>We do not require companies to replace their ERP to interconnect a machine. We review the interfaces and extend or integrate existing software where feasible. If there is no usable management system, or it cannot exchange the required data, we offer a simple dedicated application.</p></div>
<div class="outcome-grid">
<article class="outcome reveal"><h3>Already using business software?</h3><p>We assess how to connect machines, data and workflows with the existing system. Interconnection starts at €1,500, with no additional management software required when your current system can be used.</p></article>
<article class="outcome reveal"><h3>No suitable software available?</h3><p>A basic dedicated management application can be added from €500. An example complete solution for the first machine therefore starts at €2,000, subject to technical requirements.</p></article>
</div>
</div>
</section>
<section class="section section-tight section-paper" id="types-of-interconnection">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Two needs, one delivery process</p><h2>Industry 4.0 interconnection and production monitoring: <span>different objectives.</span></h2><p>Being able to collect data from a machine does not automatically make it eligible for tax incentives. Every assessment starts with the machine, its interfaces and your business requirements.</p></div>
<div class="outcome-grid">
<article class="outcome reveal"><h3>Machines subject to Industry 4.0 requirements</h3><p>We build and test the integration with business systems, preparing technical evidence. Tax eligibility is assessed separately by the appointed specialists.</p></article>
<article class="outcome reveal"><h3>Existing production equipment</h3><p>We assess integrations and sensors to monitor status, cycles, time and consumption even where no tax incentive is involved.</p></article>
</div>
</div>
</section>''') if it_slug == "interconnessione-macchine-industria-4-0.html" else "")
    method_e = (("Gestione tecnica della commessa" if lang == "it" else "Technical project delivery") if integration_guide else u["method"])
    method_h = (("Un percorso definito, dalla compatibilità al collaudo." if lang == "it" else "A defined process, from compatibility review to commissioning.") if integration_guide else u["method_h"])
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
{integration_guide}
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
{photos_html(it_slug, lang)}{systems}{reach}<section class="section section-tight section-white">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">{method_e}</p><h2>{method_h}</h2></div>
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
{contact(lang, CTAS.get(it_slug, {}).get(lang), show_form=(it_slug == "interconnessione-macchine-industria-4-0.html"))}<section class="section section-tight related">
<div class="shell">
{guide_links}<p class="eyebrow">{("Nella stessa area: " if lang == "it" else "In the same area: ") + area["nav"]}</p>
<div class="related-grid related-flex" style="--cols:{grid_cols(related.count('<a '))}">{related}</div>
<p class="eyebrow local-eyebrow">{"Altre aree" if lang == "it" else "Other areas"}</p>
<div class="related-grid related-flex" style="--cols:{grid_cols(other_areas.count('<a '))}">{other_areas}</div>
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
    target = (
        next((dict(p, label=p["card_title"], key=p["slug"]) for p in PAGES if p["slug"] == g["cta"]), None)
        or next((dict(x, label=x["nav"]) for x in PRODUCTS["it"] if x["slug"] == g["cta"]), None)
        or next((dict(a, label=a["nav"]) for a in AREAS["it"] if a["slug"] == g["cta"]), None)
    )
    if target is None:
        raise ValueError(f"Guida {g['slug']}: CTA sconosciuta {g['cta']}")
    cta = g.get("contact") or CTAS.get(target["key"], {}).get("it")
    inline_h = cta[0] if cta else "Vuoi capire se fa per te?"
    parts.insert(1, f'<div class="article-cta"><p><strong>{inline_h}</strong> Rispondiamo per iscritto entro 24 ore.</p>'
                    f'<a class="button ghost" href="#contatto">Scrivici →</a></div>')
    sections = "\n".join(parts)
    jsonld = [
      {"@context": "https://schema.org", "@type": "Article", "headline": g["short"], "description": g["desc"],
       "url": url, "inLanguage": "it", "datePublished": g.get("published", "2026-10-27"), "dateModified": g.get("modified", g.get("published", GUIDE_MODIFIED)),
       "author": {"@type": "Person", "name": "Jacopo Ellero", "url": BASE + "chi-siamo.html"},
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
<p class="hero-proof">Aggiornata a {g.get("updated", GUIDE_UPDATED)}</p>
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


# temi comuni a tutte le aree: queste guide stanno nel loro gruppo, non ripetute sotto ogni area
COMMON_GUIDES = [
    ("pubblicazione-app", "Pubblicare un'app: store, costi e privacy",
     ["guida-pubblicare-app-microsoft-store.html", "guida-pubblicare-app-macos.html",
      "guida-pubblicare-app-android.html", "guida-pubblicare-app-ios.html",
      "guida-pubblicare-app-gdpr-privacy.html"]),

    ("rete", "Rete, connessione e sicurezza",
     ["guida-rete-aziendale.html", "guida-ponti-radio-frequenze-normative.html", "guida-internet-siti-remoti.html",
      "guida-scegliere-backup.html", "guida-scegliere-hosting.html", "guida-passare-centralino-voip.html",
      "guida-videosorveglianza-norme.html"]),
    ("energia", "Energia e impianti",
     ["guida-monitorare-fotovoltaico-consumi.html", "guida-autoconsumo-fotovoltaico-carichi.html",
      "guida-pompe-di-calore-rs485-modbus.html", "guida-conto-termico-building-automation.html"]),
    ("incentivi", "Bandi e voucher",
     ["guida-voucher-bandi-digitalizzazione-2026.html"]),
]


def grid_cols(n):
    """Colonne per n schede senza lasciarne una sola sull'ultima riga: 1-2 strette, fino a 5 in riga, poi righe da 3 o 4."""
    if n <= 3:
        return 3
    if n <= 5:
        return n
    return 3 if n % 3 == 0 or n % 4 == 1 else 4


def guide_areas(x):
    """Aree in cui elencare una guida: tema comune, indicate a mano o quella del servizio di destinazione."""
    common = [k for k, _, slugs in COMMON_GUIDES if x["slug"] in slugs]
    return common or x.get("areas") or [PRIMARY_AREA[x.get("cta", "interconnessione-macchine-industria-4-0.html")]]


def guide_index():
    groups = ""
    for a in AREAS["it"]:
        gs = [x for x in [TEST] + GUIDES if a["key"] in guide_areas(x)]
        if gs:
            cards = "".join(f'<a href="{x["slug"]}"><strong>{x["short"]}</strong><span>{x["desc"]}</span></a>' for x in gs)
            groups += f'<p class="eyebrow local-eyebrow"><a class="guide-area" href="{a["slug"]}">{a["nav"]} →</a></p><div class="related-grid guides-grid">{cards}</div>\n'
    for key, label, slugs in COMMON_GUIDES:
        gs = [next(x for x in GUIDES if x["slug"] == slug) for slug in slugs]
        cards = "".join(f'<a href="{x["slug"]}"><strong>{x["short"]}</strong><span>{x["desc"]}</span></a>' for x in gs)
        groups += f'<p class="eyebrow local-eyebrow">{label}</p><div class="related-grid guides-grid">{cards}</div>\n'
    jsonld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Guide JDEVPRO", "url": BASE + "guide.html",
               "hasPart": [{"@type": "Article", "headline": g["short"], "url": BASE + g["slug"]} for g in GUIDES]}, ORG_REF]
    body = f"""{header('guide.html')}<main id="main">
<section class="hero page-hero">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell page-hero-copy reveal">
<nav aria-label="Percorso" class="breadcrumb"><a href="index.html">Home</a><span>/</span><span aria-current="page">Guide</span></nav>
<p class="eyebrow">Guide e strumenti</p>
<h1>Guide pratiche, <span>per area e per tema.</span></h1>
<p class="hero-lead">Spiegazioni concrete per capire cosa serve prima di chiedere un preventivo.</p>
</div>
</section>
<section class="section section-tight section-white">
<div class="shell">{groups}</div>
</section>
{contact()}</main>
"""
    return head("Guide JDEVPRO: software, app store, GDPR, industria e tecnologia",
                "Guide pratiche di pubblicazione app su Microsoft Store, macOS, Google Play e iOS con costi, test, GDPR e dati; anche software, industria, reti ed energia.",
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


# ---------------------------------------------------------------- periti, ingegneri e consulenti

def partners_page():
    d = PARTNERS
    who = "".join(f"<li>{x}</li>" for x in d["who"])
    roles = "".join(f'<div class="competence-card competence-plain reveal"><h3>{h}</h3><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul></div>'
                    for h, items in d["roles"])
    dossier = "".join(f"<li><strong>{a}</strong><span>{b}</span></li>" for a, b in d["dossier"])
    models = "".join(f'<article class="tier reveal"><span class="competence-num">0{i}</span><h3>{h}</h3><p class="tier-who">{w}</p><p>{t}</p></article>'
                     for i, (h, w, t) in enumerate(d["models"], 1))
    rules = "".join(f"<li><strong>{a}</strong><span>{b}</span></li>" for a, b in d["rules"])
    faq = "\n".join(f'<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>' for q, a in d["faq"])
    url = url_of(d["slug"])
    jsonld = [{"@context": "https://schema.org", "@type": "WebPage", "name": d["nav"], "description": d["desc"], "url": url, "about": {"@id": ORG_ID}},
              {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                  {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
                  {"@type": "ListItem", "position": 2, "name": d["nav"], "item": url}]}, ORG_REF]
    body = f"""{header(d['slug'])}<main id="main">
<section class="hero page-hero">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell page-hero-copy reveal">
<nav aria-label="Percorso" class="breadcrumb"><a href="index.html">Home</a><span>/</span><span aria-current="page">{d['nav']}</span></nav>
<p class="eyebrow">{d['eyebrow']}</p>
<h1>{d['h1']}</h1>
<p class="hero-lead">{d['lead']}</p>
<ul class="who-chips">{who}</ul>
<div class="hero-actions"><a class="button primary" href="#modi">Come collaborare</a><a class="button ghost" href="#contatto">Scriveteci</a></div>
</div>
</section>
<section class="section section-tight section-white">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Ruoli</p><h2>Ognuno fa la sua parte.</h2></div>
<div class="partner-roles">{roles}</div>
<p class="catalog-note">{d['roles_note']}</p>
</div>
</section>
<section class="section section-tight section-paper">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">Per la perizia</p><h2>Cosa ricevete da noi.</h2><p>Per ogni macchina collegata consegniamo un fascicolo tecnico, pensato per chi deve verificare e attestare l'interconnessione.</p></div>
<ol class="method-steps reveal">{dossier}</ol>
</div>
</section>
<section class="section section-tight section-white" id="modi">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Modello di collaborazione</p><h2>Tre modi di lavorare insieme.</h2></div>
<div class="tier-grid">{models}</div>
</div>
</section>
<section class="section section-tight section-paper">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">Regole</p><h2>Chiare dall'inizio.</h2></div>
<ul class="method-steps partner-rules reveal">{rules}</ul>
</div>
</section>
<section class="section section-tight section-white">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">Domande frequenti</p><h2>Le risposte prima della domanda.</h2></div>
<div class="faq reveal">{faq}</div>
</div>
</section>
{contact("it", d["contact"])}</main>
"""
    return head(d["title"], d["desc"], d["slug"], jsonld) + body + footer()


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

def about_technical_network(lang="it"):
    """Describes specialist collaboration, not employees or unapproved vendor endorsements."""
    return "<section class=\"section section-tight section-paper\" id=\"rete-tecnica\"><div class=\"shell\">\n<div class=\"section-heading reveal\"><p class=\"eyebrow\">Collaborazioni specialistiche</p><h2>La rete di partner tecnici JDEVPRO.</h2>\n<p>Un responsabile tecnico coordina le attività del progetto e coinvolge, quando necessario, professionisti esterni secondo incarichi e competenze effettive. Nessun collaboratore esterno viene presentato come dipendente.</p></div>\n<div class=\"outcome-grid\">\n<article class=\"outcome reveal\"><h3>Installatori abilitati</h3><p>Cablaggi, quadri e attività impiantistiche riservate a professionisti in possesso dei requisiti richiesti.</p></article>\n<article class=\"outcome reveal\"><h3>Periti e ingegneri</h3><p>Verifiche e attestazioni indipendenti di competenza del professionista incaricato, separate dal lavoro tecnico di integrazione.</p></article>\n<article class=\"outcome reveal\"><h3>Fornitori hardware e componenti</h3><p>Dispositivi e tecnologie scelti in base a compatibilità, assistenza e requisiti reali delle macchine e dei sistemi.</p></article>\n</div><p class=\"reveal\"><a class=\"card-link\" href=\"periti-ingegneri-consulenti.html\">Ruoli e collaborazione con periti e installatori →</a> · <a class=\"card-link\" href=\"assistenza.html\">Assistenza e manutenzione →</a></p>\n</div></section>\n" if lang == "it" else "<section class=\"section section-tight section-paper\" id=\"technical-network\"><div class=\"shell\">\n<div class=\"section-heading reveal\"><p class=\"eyebrow\">Specialist collaboration</p><h2>JDEVPRO's technical partner network.</h2>\n<p>A designated technical contact coordinates each project and involves external professionals for specific assignments where needed. External partners are not presented as employees.</p></div>\n<div class=\"outcome-grid\">\n<article class=\"outcome reveal\"><h3>Qualified installers</h3><p>Electrical wiring, panels and regulated site work performed by professionals with the relevant qualifications.</p></article>\n<article class=\"outcome reveal\"><h3>Independent technical assessors</h3><p>Engineers and assessors carry out independent checks and certifications under their own appointment.</p></article>\n<article class=\"outcome reveal\"><h3>Hardware suppliers</h3><p>Components and platforms selected according to compatibility, serviceability and the project's technical requirements.</p></article>\n</div><p class=\"reveal\"><a class=\"card-link\" href=\"en-how-we-work.html\">Project method and responsibilities →</a> · <a class=\"card-link\" href=\"en-support.html\">Support and maintenance →</a></p>\n</div></section>\n"


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

    def ext_attr(link):
        return ' rel="noreferrer" target="_blank"' if link.startswith("http") else ""

    shots = {"Welora": ("assets/welora-app.webp", 756, 572), "JD Industry": ("assets/jd-industry-progetto.webp", 1600, 1000)}
    projects = "".join(
        f'<a class="build-card reveal" href="{link}"{ext_attr(link)}>'
        + (f'<span class="build-shot"><img src="{shots[n][0]}" alt="{n}" width="{shots[n][1]}" height="{shots[n][2]}" loading="lazy" decoding="async"></span>' if n in shots else '')
        + f'<span class="build-body"><strong>{n}{" ↗" if link.startswith("http") else ""}</strong><span>{d}</span></span></a>'
        for n, d, link in a["projects"])
    links = "".join(
        f'<a class="button {"primary" if i == 0 else "ghost dark"}" href="{l}"{ext_attr(l)}>{n}</a>'
        for i, (n, l) in enumerate(a["links"]))
    jsonld = [{"@context": "https://schema.org", "@type": "AboutPage",
               "url": url, "name": a["title"], "about": {"@id": ORG_ID}},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": UI[lang]["home"], "item": url_of(home_slug)},
                  {"@type": "ListItem", "position": 2, "name": a["nav"], "item": url}]},
              ORG_REF]
    profile_e, profile_h = a["profile_e"], a["profile_h"]
    about_proof = ('''<section class="section section-tight section-paper" id="esperienza-operativa"><div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Esperienza operativa</p><h2>Progetti realizzati, sistemi già in funzione.</h2><p>Le competenze di JDEVPRO si misurano nelle integrazioni effettivamente realizzate: macchinari industriali, software di produzione e scambio dati fra piattaforme.</p></div>
<div class="outcome-grid">
<article class="outcome reveal"><h3>Bordatrice SCM · Maestro Active</h3><p>Stato e allarmi della macchina, commesse, produzione acquisita e costi collegati alle lavorazioni.</p><a class="card-link" href="casi-studio-industriali.html#scm-maestro-active">Leggi il caso studio →</a></article>
<article class="outcome reveal"><h3>CNC Essetre / Tecnoessetre</h3><p>Macchine collegate alla gestione di commesse, file di lavoro, dati di produzione e report.</p><a class="card-link" href="casi-studio-industriali.html#cnc-essetre">Leggi il caso studio →</a></article>
<article class="outcome reveal"><h3>Gestionale e MES</h3><p>Macchine e commesse collegate ai sistemi di produzione: stati, lavorazioni e dati disponibili nel gestionale.</p><a class="card-link" href="gestionale-produzione-erpnext.html">Scopri JD Industry →</a></article>
</div>
<p class="reveal"><a class="card-link" href="come-lavoriamo.html">Come gestiamo i progetti →</a></p>
</div></section>''' if lang == "it" else '''<section class="section section-tight section-paper" id="delivered-projects"><div class="shell">
<div class="section-heading reveal"><p class="eyebrow">Delivered projects</p><h2>Real integrations, systems already in operation.</h2><p>JDEVPRO's capabilities are reflected in delivered integrations: industrial machines, production software and data exchange between business platforms.</p></div>
<div class="outcome-grid">
<article class="outcome reveal"><h3>SCM edge bander · Maestro Active</h3><p>Machine status and alarms, production jobs, production data and job costing.</p><a class="card-link" href="en-industrial-case-studies.html#scm-maestro-active">Read the case study →</a></article>
<article class="outcome reveal"><h3>Essetre / Tecnoessetre CNC</h3><p>Machines connected to job management, work files, production data and reporting.</p><a class="card-link" href="en-industrial-case-studies.html#cnc-essetre">Read the case study →</a></article>
<article class="outcome reveal"><h3>ERP and MES</h3><p>Machines and production orders linked to manufacturing systems: status, operations and shop-floor data available in business software.</p><a class="card-link" href="en-erpnext-manufacturing.html">Explore JD Industry →</a></article>
</div>
<p class="reveal"><a class="card-link" href="en-how-we-work.html">How we manage projects →</a></p>
</div></section>''')
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
{about_proof}
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
<div class="build-grid">{projects}</div>
</div>
</section>
{about_technical_network(lang)}{contact(lang, ("Parliamo del tuo progetto.", "Raccontaci cosa vuoi realizzare, quali sistemi utilizzi e quali risultati vuoi ottenere.") if lang == "it" else ("Tell us about your project.", "Describe what you want to build, which systems you use and the results you want to achieve."))}</main>
"""
    return head(a["title"], a["desc"], a["slug"], jsonld, lang,
                alternates=[("it", ABOUT["it"]["slug"]), ("en", ABOUT["en"]["slug"])]) + body + footer(lang)


def method_standards(lang="it"):
    """Reference checklists, not certifications or service-level guarantees."""
    if lang == "it":
        return "<section class=\"section section-tight section-white\" id=\"standard-documentazione\"><div class=\"shell\">\n<div class=\"section-heading reveal\"><p class=\"eyebrow\">Metodo e standard operativi</p><h2>Collaudo, consegna e sicurezza: <span>cosa viene verificato.</span></h2><p>La documentazione viene definita in funzione del perimetro dell'intervento. Il modello pubblico serve come riferimento, non sostituisce un verbale compilato e sottoscritto.</p></div>\n<div class=\"outcome-grid\">\n<article class=\"outcome reveal\"><h3>Verbale di collaudo tipo</h3><p>Identificazione macchina e software, prerequisiti, prove di lettura e scrittura dati, esito, evidenze con data e ora, anomalie e firme di presa visione.</p></article>\n<article class=\"outcome reveal\"><h3>Dossier di consegna</h3><p>Architettura, schema rete, inventario, versioni e configurazioni, mappa dei dati scambiati, log, istruzioni operative, backup e procedure di ripristino.</p></article>\n<article class=\"outcome reveal\"><h3>Accessi remoti e sicurezza</h3><p>Accessi autorizzati per intervento, account nominativi, privilegi minimi, VPN/MFA quando disponibili, tracciamento delle attività e revoca degli accessi.</p></article>\n</div><p class=\"reveal\"><a class=\"card-link\" href=\"https://github.com/jellero/jdevpro/blob/main/docs/modello-verbale-collaudo.md\" rel=\"noreferrer\" target=\"_blank\">Consulta il modello compilabile di verbale di collaudo →</a> · <a class=\"card-link\" href=\"assistenza.html\">Assistenza e manutenzione →</a></p>\n</div></section>\n"
    return "<section class=\"section section-tight section-white\" id=\"operational-standards\"><div class=\"shell\">\n<div class=\"section-heading reveal\"><p class=\"eyebrow\">Method and operating standards</p><h2>Acceptance tests, handover and security.</h2><p>Documentation is tailored to the actual scope of each engagement. The public template is an example, not a completed or certified acceptance report.</p></div>\n<div class=\"outcome-grid\">\n<article class=\"outcome reveal\"><h3>Acceptance report template</h3><p>Machine and system identification, prerequisites, data exchange tests, results, time-stamped evidence, exceptions and client acknowledgement.</p></article>\n<article class=\"outcome reveal\"><h3>Handover dossier</h3><p>Architecture, network diagrams, device inventory, versions, configurations, data mapping, logs, operating instructions, backups and recovery steps.</p></article>\n<article class=\"outcome reveal\"><h3>Remote access and security</h3><p>Access authorised per intervention, individual accounts, least privilege, VPN/MFA where available, logged activity and revocation.</p></article>\n</div><p class=\"reveal\"><a class=\"card-link\" href=\"https://github.com/jellero/jdevpro/blob/main/docs/modello-verbale-collaudo.md\" rel=\"noreferrer\" target=\"_blank\">View acceptance report template (Italian) →</a> · <a class=\"card-link\" href=\"en-support.html\">Support and maintenance →</a></p>\n</div></section>\n"


# ---------------------------------------------------------------- come lavoriamo

def work_method(lang="it"):
    a = METHOD[lang]
    other = METHOD["en" if lang == "it" else "it"]["slug"]
    home_slug = "index.html" if lang == "it" else "en.html"
    url = url_of(a["slug"])
    def stats():
        return '<ul class="hero-stats">' + "".join(
            f'<li><a class="stat" href="{href}"><strong>{name}</strong><span>{detail}</span></a></li>'
            for name, detail, href in a["stats"]) + '</ul>'
    steps = "".join(f'<li><strong>{name}</strong><span>{detail}</span></li>' for name, detail in a["steps"])
    services = "".join(
        f'<article class="outcome reveal"><h3>{name}</h3><p>{detail}</p>'
        f'<a class="card-link" href="{href}">{label} →</a></article>'
        for name, detail, href, label in a["services"])
    identity = "".join(f'<p>{p}</p>' for p in a["identity"])
    jsonld = [
      {"@context": "https://schema.org", "@type": "WebPage", "url": url,
       "name": a["title"], "about": {"@id": ORG_ID}},
      {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": UI[lang]["home"], "item": url_of(home_slug)},
          {"@type": "ListItem", "position": 2, "name": a["nav"], "item": url}]},
      ORG_REF]
    body = f"""{header(a['slug'], lang, switch=other)}<main id="main">
<section class="hero page-hero">
<div aria-hidden="true" class="hero-grid"></div>
<div class="shell page-hero-copy reveal">
<nav aria-label="{UI[lang]['crumbs']}" class="breadcrumb"><a href="{home_slug}">{UI[lang]['home']}</a><span>/</span><span aria-current="page">{a['nav']}</span></nav>
<p class="eyebrow">{a['eyebrow']}</p>
<h1>{a['h1']}</h1>
<p class="hero-lead">{a['lead']}</p>
<div class="hero-actions"><a class="button primary" href="{a['actionHref']}">{a['action']}</a><a class="button ghost" href="{a['moreHref']}">{a['more']}</a></div>
{stats()}
</div></section>
<section class="section section-tight section-white" id="metodo">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">{a['methodEyebrow']}</p><h2>{a['methodTitle']}</h2><p>{a['methodLead']}</p></div>
<ol class="method-steps reveal">{steps}</ol>
</div></section>
<section class="section section-tight section-paper">
<div class="shell">
<div class="section-heading reveal"><p class="eyebrow">{a['servicesEyebrow']}</p><h2>{a['servicesTitle']}</h2></div>
<div class="outcome-grid">{services}</div>
</div></section>
<section class="section section-tight section-white">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">{a['proofEyebrow']}</p><h2>{a['proofTitle']}</h2><p>{a['proofText']}</p><a class="card-link" href="{a['proofHref']}">{a['proofLink']} →</a></div>
<div class="profile-copy reveal"><p><strong>{("Architettura." if lang == "it" else "Architecture.")}</strong> {("Componenti e flussi definiti con chiarezza." if lang == "it" else "Clearly defined components and data flows.")}</p><p><strong>{("Controllo." if lang == "it" else "Control.")}</strong> {("Permessi, log e test anche in caso di errore." if lang == "it" else "Permissions, logs and failure testing.")}</p><p><strong>{("Continuità." if lang == "it" else "Continuity.")}</strong> {("Manutenzione e procedure di ripristino previste." if lang == "it" else "Maintenance and recovery procedures planned.")}</p></div>
</div></section>
<section class="section section-tight section-paper">
<div class="shell split">
<div class="section-heading reveal"><p class="eyebrow">{a['identityEyebrow']}</p><h2>{a['identityTitle']}</h2></div>
<div class="profile-copy reveal">{identity}<a class="card-link" href="{a['identityHref']}">{a['identityLink']} →</a></div>
</div></section>
{method_standards(lang)}{contact(lang, ("Raccontaci il progetto.", "Descrivici cosa vuoi realizzare, i sistemi presenti e gli obiettivi.") if lang == "it" else ("Tell us about your project.", "Describe what you want to build, your existing systems and your goals."))}</main>"""
    return head(a["title"], a["desc"], a["slug"], jsonld, lang,
                alternates=[("it", METHOD["it"]["slug"]), ("en", METHOD["en"]["slug"])]) + body + footer(lang)



def ext(href):
    return ' rel="noreferrer" target="_blank"' if href.startswith("http") else ""


def products(lang):
    """Solo i prodotti in vendita: AKIOS e ORYVAEL sono sviluppo."""
    order = {"erp": 0, "smartagent": 1, "receptionist": 2, "welora": 3}
    return sorted((x for x in PRODUCTS[lang] if not x.get("dev")), key=lambda x: order.get(x["key"], 99))


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
<div class="outcome-grid{' outcome-grid-4' if len(items) == 4 else ''}">{cards}</div>
</div>
</section>
"""
    if kind == "flow":
        _, eyebrow, h2, steps = b
        li = "".join(f"<li><strong>{t}</strong><span>{d}</span></li>" for t, d in steps)
        anchor = ' id="smartdrive"' if eyebrow.startswith("SmartDrive") else ""
        return f"""<section{anchor} class="section section-tight {bg}">
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
    if pr["key"] == "erp":
        buttons += f'<a class="button ghost" href="{"casi-studio-industriali.html" if lang == "it" else "en-industrial-case-studies.html"}">{"Casi studio industriali" if lang == "it" else "Industrial case studies"}</a>'
    def other_card(x):
        shot = PRODUCT_SHOTS.get(x["key"])
        img = f'<span class="other-shot"><img src="{shot[0]}" alt="{shot[3]}" width="{shot[1]}" height="{shot[2]}" loading="lazy" decoding="async"></span>' if shot else ''
        cta = (x["slug"].split("//")[1].rstrip("/") + " ↗") if x.get("external") else u["more"]
        return (f'<a class="other-product reveal{" has-shot" if shot else ""}" href="{x["slug"]}"{ext(x["slug"])}>{img}'
                f'<span class="other-body"><span class="eyebrow">{x["eyebrow"]}</span><strong>{x["nav"]}</strong><span>{x["card"]}</span>'
                f'<span class="other-cta">{cta}</span></span></a>')
    others = "".join(other_card(x) for x in PRODUCTS[lang] if x["key"] != pr["key"] and bool(x.get("dev")) == bool(pr.get("dev")))
    if pr["key"] == "welora":
        main_ld = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Welora", "description": pr["desc"], "url": url,
                   "applicationCategory": "BusinessApplication", "operatingSystem": "Web",
                   "offers": {"@type": "Offer", "price": "29", "priceCurrency": "EUR", "availability": "https://schema.org/PreOrder"},
                   "publisher": {"@id": ORG_ID}, "sameAs": ["https://welora.it/"]}
    elif pr["key"] == "smartagent":
        main_ld = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "SmartAgent",
                   "description": pr["desc"], "url": url, "applicationCategory": "BusinessApplication",
                   "operatingSystem": "Web", "publisher": {"@id": ORG_ID}, "sameAs": ["https://smartagent.jdevpro.it/"],
                   "offers": {"@type": "Offer", "price": "29.90", "priceCurrency": "EUR"}}
    elif pr["key"] == "erp":
        main_ld = {"@context": "https://schema.org", "@type": "Service", "name": pr["nav"], "description": pr["desc"], "url": url,
                   "serviceType": "ERP", "provider": {"@id": ORG_ID}, "areaServed": "IT",
                   "offers": {"@type": "Offer", "priceCurrency": "EUR",
                              "priceSpecification": {"@type": "PriceSpecification", "minPrice": 990, "priceCurrency": "EUR"}}}
    elif pr["key"] == "receptionist":
        main_ld = {"@context": "https://schema.org", "@type": "SoftwareApplication",
                   "name": "Digital Receptionist", "description": pr["desc"], "url": url,
                   "applicationCategory": "BusinessApplication", "publisher": {"@id": ORG_ID}}
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
<div class="other-products">{others}</div>
</div>
</section>
</main>
"""
    alternates = [("it", next(x for x in PRODUCTS["it"] if x["key"] == pr["key"])["slug"]),
                  ("en", next(x for x in PRODUCTS["en"] if x["key"] == pr["key"])["slug"])]
    return head(pr["title"], pr["desc"], pr["slug"], jsonld, lang, alternates=alternates) + body + footer(lang)


def products_home(lang):
    if lang == "it":
        e, h, p = "Prodotti e ricerca", "Non solo progetti per i clienti.", "Prodotti nostri, in uso e in sviluppo."
    else:
        e, h, p = "Products and research", "Not only client projects.", "Our own products, in use and in development."
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
write("chi-siamo.html", about("it"))
write("come-lavoriamo.html", work_method("it"))
for _lang in ("it", "en"):
    for _a in AREAS[_lang]:
        write(_a["slug"], area_page(_a, _lang))
    write(PRODUCTS_PAGE[_lang]["slug"], products_index(_lang))
write(WHERE_PAGE["slug"], where_page())
write(PARTNERS["slug"], partners_page())
for _lang in ("it", "en"):
    for _pr in PRODUCTS[_lang]:
        if not _pr.get("external"):
            write(_pr["slug"], product_page(_pr, _lang))
write("smartdrive.html", SMARTDRIVE["build_page"]("it", head, header, footer, contact, BASE, ORG_REF, ORG_ID))
write("en-smartdrive.html", SMARTDRIVE["build_page"]("en", head, header, footer, contact, BASE, ORG_REF, ORG_ID))
write("en-about.html", about("en"))
write("en-how-we-work.html", work_method("en"))
write("404.html", not_found())
for _kind in ("privacy", "cookie"):
    for _lang in ("it", "en"):
        write(LEGAL_DATA["LEGAL"][_kind][_lang]["slug"], legal_page(_kind, _lang))
for old, target in OLD_URLS.items():
    write(f"{old}/index.html", redirect_stub(target))

urls = (["", "en.html"] + [p["slug"] for p in PAGES] + [EN_SLUG[p["slug"]] for p in PAGES]
        + [c["slug"] for c in CITIES] + ["guide.html", TEST["slug"]] + [g["slug"] for g in GUIDES]
        + [x["slug"] for l in ("it", "en") for x in PRODUCTS[l] if not x.get("external")] + ["smartdrive.html", "en-smartdrive.html", "smartdrive-privacy.html"] + [a["slug"] for l in ("it", "en") for a in AREAS[l]] + [PRODUCTS_PAGE["it"]["slug"], PRODUCTS_PAGE["en"]["slug"], WHERE_PAGE["slug"], PARTNERS["slug"]] + ["casi-studio-industriali.html", "en-industrial-case-studies.html"] + ["chi-siamo.html", "en-about.html", "come-lavoriamo.html", "en-how-we-work.html", "privacy.html", "privacy-en.html", "cookie-policy.html", "cookie-policy-en.html"])
sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sitemap += [f"  <url><loc>{BASE}{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls]
sitemap.append("</urlset>")
(REPO / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8", newline="\n")
print("ok", len(urls), "URL in sitemap")
