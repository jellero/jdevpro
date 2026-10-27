"""Pagine di area, pagina prodotti e pagina dove lavoriamo."""

# competenze per area (slug italiani); la prima area elencata per una competenza è quella del percorso
AREA_SERVICES = {
  "industria": ["interconnessione-macchine-industria-4-0.html", "gestionale-su-misura.html", "integrazione-software-api.html", "monitoraggio-iot.html"],
  "strutture": ["automazione-hotel-bnb.html", "videosorveglianza-citofonia-accessi.html", "centralini-voip-telefonia.html", "internet-offgrid-siti-remoti.html", "monitoraggio-iot.html"],
  "web": ["gestionale-su-misura.html", "integrazione-software-api.html", "siti-web-piattaforme.html"],
}
PRIMARY_AREA = {
  "interconnessione-macchine-industria-4-0.html": "industria", "monitoraggio-iot.html": "industria",
  "automazione-hotel-bnb.html": "strutture", "videosorveglianza-citofonia-accessi.html": "strutture",
  "centralini-voip-telefonia.html": "strutture", "internet-offgrid-siti-remoti.html": "strutture",
  "gestionale-su-misura.html": "web", "integrazione-software-api.html": "web", "siti-web-piattaforme.html": "web",
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
         lead="Falegnamerie, stamperie, mobilifici e aziende manifatturiere: colleghiamo le macchine al gestionale, portiamo in ufficio tempi, scarti e costi reali e teniamo tutto funzionante. Senza toccare il programma delle macchine.",
         who=["Falegnamerie e mobilifici", "Stamperie e metalmeccanica", "Subfornitura e conto terzi", "Costruttori di macchine", "Agroalimentare e lavorazioni"],
         proof=[("10 macchine in produzione", "Collegate al gestionale a Tolmezzo, tra falegnamerie e stamperie."),
                ("JD Industry", "Gestionale di produzione collegato a macchine SCM ed Essetre."),
                ("Costi reali per commessa", "Tempi macchina, materiali ed extra in un consuntivo stampabile, senza Excel.")],
         guides=["test-interconnessione-4-0.html", "guida-interconnessione-iperammortamento.html", "guida-monitorare-fotovoltaico-consumi.html", "guida-integrare-sistemi-senza-api.html"]),
    dict(key="strutture", slug="strutture-edifici.html", nav="Strutture ed edifici",
         title="Automazione per hotel, B&B, sicurezza e telefonia | JDEVPRO",
         desc="Automazione per hotel e B&B, videosorveglianza, citofonia e accessi, centralini VoIP, internet offgrid e domotica per strutture ed edifici in Friuli.",
         card="Hotel e B&B, videosorveglianza, citofonia e accessi, centralini VoIP, internet offgrid e domotica.",
         eyebrow="Strutture, edifici e sicurezza",
         h1="Per chi gestisce una struttura: <span>accessi, sicurezza e comfort da remoto.</span>",
         lead="Hotel, B&B, uffici, aziende, baite e abitazioni: colleghiamo telecamere, citofoni, cancelli, termostati, telefoni e connessione, e li comandi dal telefono. Con installatori abilitati per la parte elettrica.",
         who=["Hotel, B&B e case vacanza", "Uffici e aziende", "Condomini e abitazioni", "Baite, rifugi e cantieri", "Aziende agricole e siti isolati"],
         proof=[("Welora", "Il nostro gestionale per strutture ricettive, tutto incluso a 29 € al mese."),
                ("Decine di impianti Ubiquiti", "In aziende di vario tipo: antenne, telecamere, citofoni e controllo accessi con riconoscimento facciale e targhe."),
                ("Clima camera per camera", "In alberghi e affittacamere: termostati collegati alle prenotazioni, con avvisi di comfort."),
                ("Centralini VoIP installati", "In aziende, alberghi e ristoranti, con Asterisk e 3CX e telefoni Grandstream e Yealink."),
                ("Energia off-grid", "Impianti oltre i 6 kW già realizzati: anche quello piccolo per un sito isolato è dimensionato bene.")],
         guides=["guida-check-in-senza-chiavi.html", "guida-videosorveglianza-norme.html", "guida-passare-centralino-voip.html", "guida-internet-siti-remoti.html"]),
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
         guides=["guida-integrare-amazon-ebay-gestionale.html", "guida-integrare-sistemi-senza-api.html"]),
  ],
  "en": [
    dict(key="industria", slug="en-industry.html", nav="Industry",
         title="Software and machine interconnection for industry | JDEVPRO",
         desc="Machines connected to business software, custom software, integrations and IoT monitoring for manufacturers. 10 machines in production in Tolmezzo.",
         card="Machines connected to business software, real job costs, integrations and sensors for manufacturers.",
         eyebrow="Industry and production",
         h1="For manufacturers: <span>machines, data and software connected.</span>",
         lead="Woodworking shops, metal pressing, furniture and manufacturing companies: we connect machines to business software, bring times, scrap and real costs to the office and keep everything running. Without touching machine programs.",
         who=["Woodworking and furniture", "Metal pressing and engineering", "Subcontractors", "Machine builders", "Food processing"],
         proof=[("10 machines in production", "Connected to business software in Tolmezzo, across woodworking and metal pressing companies."),
                ("JD Industry", "Production management connected to SCM and Essetre machines."),
                ("Real costs per job", "Machine time, materials and extras in a printable costing, without spreadsheets.")],
         guides=[]),
    dict(key="strutture", slug="en-properties-buildings.html", nav="Properties and buildings",
         title="Hotel automation, security and VoIP for buildings | JDEVPRO",
         desc="Hotel and B&B automation, video surveillance, intercoms and access, VoIP phone systems, off-grid internet and smart building in north-east Italy.",
         card="Hotels and B&Bs, video surveillance, intercoms and access, VoIP phones, off-grid internet and smart building.",
         eyebrow="Properties, buildings and security",
         h1="For property managers: <span>access, security and comfort, remotely.</span>",
         lead="Hotels, B&Bs, offices, companies, huts and homes: we connect cameras, intercoms, gates, thermostats, phones and connectivity, and you control them from your phone. With licensed electricians for the electrical work.",
         who=["Hotels, B&Bs and holiday homes", "Offices and companies", "Apartment buildings and homes", "Huts, refuges and building sites", "Farms and isolated sites"],
         proof=[("Welora", "Our hospitality management software, everything included for €29 a month."),
                ("Dozens of Ubiquiti systems", "In all kinds of companies: antennas, cameras, intercoms and access control with face and plate recognition."),
                ("Room-by-room climate", "In hotels and guest houses: thermostats tied to bookings, with comfort alerts."),
                ("VoIP phone systems installed", "In companies, hotels and restaurants, with Asterisk and 3CX and Grandstream and Yealink phones."),
                ("Off-grid power", "Systems above 6 kW already built: even a small one for an isolated site is properly sized.")],
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
             title="Prodotti JDEVPRO: Welora, AKIOS e ORYVAEL | JDEVPRO",
             desc="I nostri prodotti: Welora, gestionale per strutture ricettive; AKIOS, aggiornamenti sicuri per dispositivi IoT; ORYVAEL, sistema operativo per l'AI.",
             eyebrow="Prodotti e ricerca", h1="Non solo progetti per i clienti: <span>i nostri prodotti.</span>",
             lead="Oltre ai progetti su misura sviluppiamo prodotti nostri: un gestionale per strutture ricettive, un firmware per i produttori di dispositivi IoT e una ricerca sui sistemi operativi per l'intelligenza artificiale.",
             points={"welora": ["PMS, booking engine e canali", "Check-in online e Alloggiati Web", "Pagamenti, fatture, pulizie e cassa", "In pre-lancio, arrivo previsto il 15 febbraio 2027"],
                     "akios": ["Aggiornamenti firmati e verificati", "Prova, conferma o ritorno automatico", "Ripristino locale dal telefono", "Firmware operativo su Beken BK7238"],
                     "oryvael": ["L'AI lavora, le persone approvano", "Kernel in Rust che parte su hardware reale", "Profili desktop, mobile ed embedded", "Ricerca documentata e verificabile"]}),
  "en": dict(slug="en-products.html", nav="Products",
             title="JDEVPRO products: Welora, AKIOS and ORYVAEL | JDEVPRO",
             desc="Our products: Welora, hospitality management software; AKIOS, secure updates for IoT devices; ORYVAEL, an AI-native operating system.",
             eyebrow="Products and research", h1="Not only client projects: <span>our own products.</span>",
             lead="Besides custom projects we build our own products: management software for hospitality, firmware for IoT device makers and research on operating systems for artificial intelligence.",
             points={"welora": ["PMS, booking engine and channels", "Online check-in and Italian guest reporting", "Payments, invoices, housekeeping and till", "Pre-launch, expected on 15 February 2027"],
                     "akios": ["Signed and verified updates", "Trial, commit or automatic rollback", "Local recovery from a phone", "Firmware running on Beken BK7238"],
                     "oryvael": ["AI does the work, people approve", "Rust kernel booting on real hardware", "Desktop, mobile and embedded profiles", "Documented and verifiable research"]}),
}

WHERE_PAGE = dict(slug="dove-lavoriamo.html", nav="Dove lavoriamo",
                  title="Dove lavoriamo: Friuli Venezia Giulia e Veneto | JDEVPRO",
                  desc="JDEVPRO lavora da Tolmezzo con aziende e strutture della provincia di Udine e della Carnia, di Pordenone, Trieste e Gorizia, del Veneto e da remoto.",
                  eyebrow="Dove lavoriamo", h1="Da Tolmezzo, <span>in tutto il Friuli Venezia Giulia.</span>",
                  lead="Lavoriamo con aziende e strutture di tutta la regione e del Veneto. Veniamo sul posto per analisi, sopralluoghi e collaudi; sviluppo e assistenza li seguiamo anche da remoto.")

CALLOUTS = {
  "automazione-hotel-bnb.html": {
    "it": ("Il gestionale per strutture ricettive lo abbiamo fatto noi: <strong>Welora</strong>. PMS, canali, check-in, pagamenti, fatture e automazioni, tutto incluso a 29 € al mese.", "Scopri Welora ↗", "https://welora.it/"),
    "en": ("We built the hospitality management software ourselves: <strong>Welora</strong>. PMS, channels, check-in, payments, invoices and automation, all included for €29 a month.", "Discover Welora ↗", "https://welora.it/"),
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
}
