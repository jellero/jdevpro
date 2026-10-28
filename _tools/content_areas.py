"""Pagine di area, pagina prodotti e pagina dove lavoriamo."""

# competenze per area (slug italiani); la prima area elencata per una competenza è quella del percorso
AREA_SERVICES = {
  "industria": ["interconnessione-macchine-industria-4-0.html", "gestionale-su-misura.html", "integrazione-software-api.html", "migrazione-dati.html", "monitoraggio-iot.html"],
  "strutture": ["automazione-hotel-bnb.html", "domotica-home-assistant.html", "videosorveglianza-citofonia-accessi.html", "centralini-voip-telefonia.html", "internet-offgrid-siti-remoti.html", "monitoraggio-iot.html"],
  "web": ["gestionale-su-misura.html", "integrazione-software-api.html", "migrazione-dati.html", "siti-web-piattaforme.html"],
}
PRIMARY_AREA = {
  "interconnessione-macchine-industria-4-0.html": "industria", "monitoraggio-iot.html": "industria",
  "automazione-hotel-bnb.html": "strutture", "domotica-home-assistant.html": "strutture", "videosorveglianza-citofonia-accessi.html": "strutture",
  "centralini-voip-telefonia.html": "strutture", "internet-offgrid-siti-remoti.html": "strutture",
  "gestionale-su-misura.html": "web", "integrazione-software-api.html": "web", "migrazione-dati.html": "web", "siti-web-piattaforme.html": "web",
}
# il blocco "API / interfacce web / seriale e Modbus" solo dove parla al pubblico giusto
TECH_TIERS = {"interconnessione-macchine-industria-4-0.html", "integrazione-software-api.html", "monitoraggio-iot.html"}

AREAS = {
  "it": [
    dict(key="industria", slug="industria.html", nav="Industria",
         title="Software e macchine 4.0 per l'industria in Friuli | JDEVPRO",
         desc="Macchine collegate al gestionale, gestionali su misura, integrazioni e monitoraggio IoT per aziende manifatturiere. 10 macchine in produzione a Tolmezzo.",
         card="Macchine collegate al gestionale, commesse e costi reali, integrazioni e sensori per chi produce.",
         eyebrow="Industria e produzione",
         h1="Per chi produce: <span>macchine, dati e gestionale collegati.</span>",
         lead="Falegnamerie, stamperie, mobilifici e aziende manifatturiere: colleghiamo al gestionale qualsiasi macchina, 4.0 o datata, portiamo in ufficio tempi, scarti e costi reali e teniamo tutto funzionante. Senza toccare il programma delle macchine.",
         who=["Falegnamerie e mobilifici", "Stamperie e metalmeccanica", "Subfornitura e conto terzi", "Costruttori di macchine", "Agroalimentare e lavorazioni"],
         proof=[("10 macchine in produzione", "Collegate al gestionale a Tolmezzo, tra falegnamerie e stamperie."),
                ("JD Industry", "Gestionale di produzione collegato a macchine SCM ed Essetre."),
                ("Costi reali per commessa", "Tempi macchina, materiali ed extra in un consuntivo stampabile, senza Excel.")],
         guides=["test-interconnessione-4-0.html", "guida-interconnessione-iperammortamento.html", "guida-iperammortamento-software-erp-mes.html", "guida-voucher-bandi-digitalizzazione-2026.html", "guida-monitorare-fotovoltaico-consumi.html", "guida-integrare-sistemi-senza-api.html"],
         products=["erp"]),
    dict(key="strutture", slug="strutture-edifici.html", nav="Hotel e B&B",
         title="Hotel e B&B: automazione, domotica e sicurezza | JDEVPRO",
         desc="Per hotel, B&B, rifugi e ristoranti: check-in e accessi, domotica professionale, videosorveglianza, VoIP e internet offgrid.",
         card="Check-in e accessi, domotica, videosorveglianza, centralini VoIP e internet per hotel, B&B e ristoranti.",
         eyebrow="Hotel, B&B e ristorazione",
         h1="Per chi accoglie ospiti: <span>accessi, comfort e sicurezza, anche da remoto.</span>",
         lead="Hotel, B&B, case vacanza, rifugi e ristoranti: colleghiamo prenotazioni, serrature, clima, luci, telecamere, telefoni e connessione, e li controlli dal telefono. Con installatori abilitati per la parte elettrica.",
         who=["Hotel e alberghi diffusi", "B&B e affittacamere", "Case vacanza", "Rifugi e baite", "Ristoranti"],
         products=["welora"],
         proof=[("Clima camera per camera", "In alberghi e affittacamere: termostati collegati alle prenotazioni, con avvisi di comfort."),
                ("Centralini VoIP installati", "In aziende, alberghi e ristoranti, con Asterisk e 3CX e telefoni Grandstream e Yealink."),
                ("Energia off-grid per rifugi e baite", "Impianti oltre i 6 kW già realizzati: anche quello piccolo per un sito isolato è dimensionato bene.")],
         guides=["guida-contributi-fvg-hotel.html", "guida-conto-termico-building-automation.html", "guida-check-in-senza-chiavi.html", "guida-videosorveglianza-norme.html", "guida-passare-centralino-voip.html", "guida-internet-siti-remoti.html"]),
    dict(key="web", slug="software-web.html", nav="Software e web",
         title="Gestionali su misura, integrazioni e siti web | JDEVPRO",
         desc="Gestionali su misura, integrazioni con Amazon, eBay, corrieri e fatturazione elettronica, siti e piattaforme web gestibili in autonomia. Friuli e remoto.",
         card="Gestionali su misura, integrazioni con marketplace, corrieri e pagamenti, siti gestibili in autonomia.",
         eyebrow="Software e web",
         h1="Software su misura: <span>gestionali, integrazioni e siti che si parlano.</span>",
         lead="Sviluppiamo gestionali su misura, colleghiamo marketplace, corrieri, pagamenti e fatturazione elettronica, e realizziamo siti che puoi aggiornare da solo. Tutto collegato, tutto mantenuto nel tempo.",
         who=["Piccole e medie imprese", "Commercio e e-commerce", "Rivenditori sui marketplace", "Studi e servizi", "Enti e associazioni"],
         proof=[("Gestionale per i marketplace", "Collegato a fornitore, SellRapido, IBS, Temu e corriere GLS."),
                ("Welora", "Piattaforma gestionale con 25 moduli, dalle prenotazioni alla cassa."),
                ("Lauco Experience", "Portale in quattro lingue con pannello di gestione.")],
         guides=["guida-voucher-bandi-digitalizzazione-2026.html", "guida-erpnext-italia-odoo.html", "guida-integrare-amazon-ebay-gestionale.html", "guida-integrare-sistemi-senza-api.html"]),
  ],
  "en": [
    dict(key="industria", slug="en-industry.html", nav="Industry",
         title="Software and machine interconnection for industry | JDEVPRO",
         desc="Machines connected to business software, custom software, integrations and IoT monitoring for manufacturers. 10 machines in production in Tolmezzo.",
         card="Machines connected to business software, real job costs, integrations and sensors for manufacturers.",
         eyebrow="Industry and production",
         h1="For manufacturers: <span>machines, data and software connected.</span>",
         lead="Woodworking shops, metal pressing, furniture and manufacturing companies: we connect any machine to business software, Industry 4.0 or older, bring times, scrap and real costs to the office and keep everything running. Without touching machine programs.",
         who=["Woodworking and furniture", "Metal pressing and engineering", "Subcontractors", "Machine builders", "Food processing"],
         proof=[("10 machines in production", "Connected to business software in Tolmezzo, across woodworking and metal pressing companies."),
                ("JD Industry", "Production software connected to SCM and Essetre machines."),
                ("Real costs per job", "Machine time, materials and extras in a printable costing, without spreadsheets.")],
         guides=[],
         products=["erp"]),
    dict(key="strutture", slug="en-properties-buildings.html", nav="Hotels and B&Bs",
         title="Hotels and B&Bs: automation, security and phones | JDEVPRO",
         desc="For hotels, B&Bs, mountain huts and restaurants: check-in and access, professional automation, cameras, VoIP and off-grid internet.",
         card="Check-in and access, automation, video surveillance, VoIP phones and internet for hotels, B&Bs and restaurants.",
         eyebrow="Hotels, B&Bs and restaurants",
         h1="For those who host guests: <span>access, comfort and security, remotely.</span>",
         lead="Hotels, B&Bs, holiday homes, mountain huts and restaurants: we connect bookings, locks, climate, lights, cameras, phones and connectivity, and you control them from your phone. With licensed electricians for the electrical work.",
         who=["Hotels and scattered hotels", "B&Bs and guest houses", "Holiday homes", "Mountain huts", "Restaurants"],
         products=["welora"],
         proof=[("Room-by-room climate", "In hotels and guest houses: thermostats tied to bookings, with comfort alerts."),
                ("VoIP phone systems installed", "In companies, hotels and restaurants, with Asterisk and 3CX and Grandstream and Yealink phones."),
                ("Off-grid power for mountain huts", "Systems above 6 kW already built: even a small one for an isolated site is properly sized.")],
         guides=[]),
    dict(key="web", slug="en-software-web.html", nav="Software and web",
         title="Custom business software, integrations and websites | JDEVPRO",
         desc="Custom business software, integrations with Amazon, eBay, couriers and e-invoicing, and websites you can manage yourself. North-east Italy and remote.",
         card="Custom business software, integrations with marketplaces, couriers and payments, websites you can manage.",
         eyebrow="Software and web",
         h1="Custom software: <span>business tools, integrations and websites that talk.</span>",
         lead="We build custom business software, connect marketplaces, couriers, payments and e-invoicing, and create websites you can update yourself. All connected, all maintained over time.",
         who=["Small and medium businesses", "Retail and e-commerce", "Marketplace sellers", "Studios and services", "Organisations"],
         proof=[("Marketplace business software", "Connected to supplier, SellRapido, IBS, Temu and GLS courier."),
                ("Welora", "Management platform with 25 modules, from bookings to the till."),
                ("Lauco Experience", "Four-language portal with management panel.")],
         guides=[]),
  ],
}

PRODUCTS_PAGE = {
  "it": dict(slug="prodotti.html", nav="Prodotti",
             title="Prodotti JDEVPRO: Welora e JD Industry | JDEVPRO",
             desc="I nostri prodotti: Welora, il gestionale per strutture ricettive, e JD Industry, l'ecosistema per la produzione dalle macchine collegate all'ERP su ERPNext.",
             eyebrow="I nostri prodotti", h1="Welora e JD Industry: <span>i nostri prodotti.</span>",
             lead="Oltre ai progetti su misura abbiamo due prodotti nostri: Welora per chi accoglie ospiti e JD Industry per chi produce.",
             points={"welora": ["PMS, booking engine e canali", "Check-in online e Alloggiati Web", "Pagamenti, fatture, pulizie e cassa", "In pre-lancio, arrivo previsto il 15 febbraio 2027"],
                     "erp": ["Macchine collegate, ERP su ERPNext o su misura", "Magazzino, lotti e conto lavoro", "Fattura elettronica SdI e tablet in reparto", "In cloud, su server o NAS, avvio da 990 €"],
                     "akios": ["Aggiornamenti firmati e verificati", "Prova, conferma o ritorno automatico", "Ripristino locale dal telefono", "Firmware operativo su Beken BK7238"],
                     "oryvael": ["L'AI lavora, le persone approvano", "Kernel in Rust che parte su hardware reale", "Profili desktop, mobile ed embedded", "Ricerca documentata e verificabile"]}),
  "en": dict(slug="en-products.html", nav="Products",
             title="JDEVPRO products: Welora and JD Industry | JDEVPRO",
             desc="Our products: Welora, hospitality management software, and JD Industry, the production ecosystem from connected machines to ERP on ERPNext.",
             eyebrow="Our products", h1="Not only client projects: <span>our own products.</span>",
             lead="Besides custom projects we have two products of our own: Welora for hospitality and JD Industry for manufacturers.",
             points={"welora": ["PMS, booking engine and channels", "Online check-in and Italian guest reporting", "Payments, invoices, housekeeping and till", "Pre-launch, expected on 15 February 2027"],
                     "erp": ["Bills of materials and work orders", "Stock, batches and subcontracting", "Italian e-invoicing and shop-floor tablets", "Cloud, server or NAS, setup from €990"],
                     "akios": ["Signed and verified updates", "Trial, commit or automatic rollback", "Local recovery from a phone", "Firmware running on Beken BK7238"],
                     "oryvael": ["AI does the work, people approve", "Rust kernel booting on real hardware", "Desktop, mobile and embedded profiles", "Documented and verifiable research"]}),
}

WHERE_PAGE = dict(slug="dove-lavoriamo.html", nav="Dove lavoriamo",
                  title="Dove lavoriamo: Friuli Venezia Giulia e Veneto | JDEVPRO",
                  desc="JDEVPRO lavora da Tolmezzo con aziende e strutture della provincia di Udine e della Carnia, di Pordenone, Trieste e Gorizia, del Veneto e da remoto.",
                  eyebrow="Dove lavoriamo", h1="Da Tolmezzo, <span>in tutto il Friuli Venezia Giulia.</span>",
                  lead="Lavoriamo con aziende e strutture di tutta la regione e del Veneto. Veniamo sul posto per analisi, sopralluoghi e collaudi; sviluppo e assistenza li seguiamo anche da remoto.")

CALLOUTS = {
  "interconnessione-macchine-industria-4-0.html": {
    "it": ("È il primo livello di <strong>JD Industry</strong>: si parte dalle macchine collegate e si aggiunge l'ERP su ERPNext quando serve.", "Scopri JD Industry →", "gestionale-produzione-erpnext.html"),
    "en": ("This is the first level of <strong>JD Industry</strong>: start with connected machines and add the ERP on ERPNext when needed.", "Discover JD Industry →", "en-erpnext-manufacturing.html"),
  },
  "gestionale-su-misura.html": {
    "it": ("Produzione con distinte base, magazzino e fattura elettronica? Prima di un gestionale su misura guarda <strong>JD Industry</strong>, il nostro gestionale di produzione, con ERP su ERPNext da 990 €.", "Scopri JD Industry →", "gestionale-produzione-erpnext.html"),
    "en": ("Production with bills of materials, stock and e-invoicing? Before custom software, look at <strong>JD Industry</strong>, our production management, with ERP on ERPNext from €990.", "Discover JD Industry →", "en-erpnext-manufacturing.html"),
  },
  "domotica-home-assistant.html": {
    "it": ("Questa pagina riguarda l'impianto: clima, luci, sensori ed energia. Per check-in online, codici di accesso e adempimenti legati alla prenotazione c'è <strong>Automazione per hotel e B&B</strong>.", "Vai alla pagina →", "automazione-hotel-bnb.html"),
    "en": ("This page is about the installation: climate, lights, sensors and energy. For online check-in, access codes and compliance tied to bookings see <strong>Hotel and B&B automation</strong>.", "Go to the page →", "en-hotel-bnb-automation.html"),
  },
  "automazione-hotel-bnb.html": {
    "it": ("Il gestionale per strutture ricettive lo abbiamo fatto noi: <strong>Welora</strong>. PMS, canali, check-in, pagamenti, fatture e automazioni, tutto incluso a 29 € al mese, in arrivo il 15 febbraio 2027.", "Scopri Welora ↗", "https://welora.it/"),
    "en": ("We built the hospitality management software ourselves: <strong>Welora</strong>. PMS, channels, check-in, payments, invoices and automation, all included for €29 a month, launching on 15 February 2027.", "Discover Welora ↗", "https://welora.it/"),
  },
}

# schede competenza adattate al pubblico dell'area
CARD_OVERRIDES = {
  ("industria", "integrazione-software-api.html"): {
    "it": dict(card_who="Aziende che devono far parlare gestionale, macchine, fornitori e corrieri.",
               card_points=["Gestionale, fornitori e corrieri", "Documenti e fatture elettroniche", "Anche senza API: web, seriale, Modbus"]),
    "en": dict(card_who="Companies that need business software, machines, suppliers and couriers to talk.",
               card_points=["Business software, suppliers and couriers", "Documents and e-invoices", "Even without APIs: web, serial, Modbus"]),
  },
  ("strutture", "videosorveglianza-citofonia-accessi.html"): {
    "it": dict(card_who="Hotel, B&B, rifugi e ristoranti che vogliono controllare ingressi, parcheggi e aree comuni anche da remoto.",
               card_points=["Telecamere su ingressi e parcheggi", "Videocitofono sul telefono della reception", "Cancelli e accessi da remoto"]),
    "en": dict(card_who="Hotels, B&Bs, mountain huts and restaurants that want to watch entrances, car parks and common areas remotely.",
               card_points=["Cameras on entrances and car parks", "Video intercom on the reception phone", "Gates and access, remotely"]),
  },
  ("strutture", "centralini-voip-telefonia.html"): {
    "it": dict(card_who="Hotel e ristoranti che vogliono un centralino moderno, con la reception raggiungibile anche dal cellulare.",
               card_points=["Interni per reception, camere e cucina", "Chiamate deviate sul cellulare", "Citofoni collegati al centralino"]),
    "en": dict(card_who="Hotels and restaurants that want a modern phone system, with reception reachable on the mobile too.",
               card_points=["Extensions for reception, rooms and kitchen", "Calls forwarded to the mobile", "Intercoms connected to the system"]),
  },
  ("strutture", "internet-offgrid-siti-remoti.html"): {
    "it": dict(card_who="Rifugi, baite, agriturismi e strutture in quota senza linea fissa o senza rete elettrica.",
               card_points=["Wi-Fi per gli ospiti anche in quota", "Internet via 4G/5G, ponte radio o satellite", "Energia solare con batterie"]),
    "en": dict(card_who="Mountain huts, chalets, farm stays and high-altitude properties with no fixed line or no power grid.",
               card_points=["Guest Wi-Fi even at altitude", "Internet via 4G/5G, radio link or satellite", "Solar power with batteries"]),
  },
  ("strutture", "monitoraggio-iot.html"): {
    "it": dict(card_who="Hotel e ristoranti che vogliono tenere d'occhio consumi, celle frigo e impianti.",
               card_points=["Consumi per camera o per struttura", "Temperature di celle e frigoriferi", "Avvisi su telefono per guasti e perdite"]),
    "en": dict(card_who="Hotels and restaurants that want to keep an eye on consumption, cold rooms and installations.",
               card_points=["Consumption per room or property", "Cold-room and fridge temperatures", "Phone alerts for faults and leaks"]),
  },
}
