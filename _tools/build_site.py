"""Genera la home minimal e le pagine competenza di jdevpro.it (italiano)."""
import json
import pathlib
import sys
from html import escape
from urllib.parse import quote

REPO = pathlib.Path(sys.argv[1])
BASE = "https://www.jdevpro.it/"
EMAIL = "info@jdevpro.it"
WA = "https://wa.me/393454656749?text=" + quote("Ciao Jacopo, ti scrivo dal sito JDEVPRO per un progetto.")
LI = "https://www.linkedin.com/in/jacopo-ellero-a006499a/"
MAILTO = ("mailto:info@jdevpro.it?subject=" + quote("Richiesta progetto - JDEVPRO") + "&amp;body=" + quote(
    "Ciao Jacopo,\n\nSistemi già presenti:\n\nCosa vorrei ottenere:\n\nTempistiche indicative:\n\nAzienda / riferimento:\n"))
ORG_ID = BASE + "#jdevpro"

TIERS = [
  ("API pubbliche", "Integrazione completa: lettura, scrittura, eventi e webhook, con le credenziali ufficiali del servizio."),
  ("Interfacce web senza API pubbliche", "Se un servizio si usa dal browser, ne automatizzo le stesse chiamate del pannello web, nel rispetto delle condizioni d'uso."),
  ("Seriale e Modbus", "Per dispositivi senza rete o con protocolli industriali, un middleware legge RS-485/RS-232 e Modbus RTU/TCP e porta i dati via API o MQTT."),
]

# ---------------------------------------------------------------- contenuti

PAGES = [
  dict(
    slug="interconnessione-macchine-industria-4-0.html",
    nav="Macchine 4.0",
    card_title="Interconnessione macchine 4.0",
    card_who="Falegnamerie, mobilifici, aziende manifatturiere con macchine CNC.",
    card_points=["Dati macchina nel gestionale", "Costi reali per commessa", "Requisito di interconnessione per l'iperammortamento"],
    title="Interconnessione macchine 4.0 e raccolta dati | JDEVPRO",
    desc="Collego le macchine al gestionale (SCM Maestro Active, Essetre, Modbus, API): commesse, tempi e costi reali. Interconnessione per l'iperammortamento.",
    service_type="Interconnessione macchine Industria 4.0",
    eyebrow="Interconnessione macchine · Industria 4.0",
    h1="Interconnessione macchine 4.0: <span>dalla macchina al gestionale.</span>",
    lead="Leggo i dati dalle macchine e li porto dove servono: stato, commesse, produzione, allarmi e costi reali per commessa. Senza toccare il programma della macchina.",
    problems=[
      ("La macchina è nuova ma non è collegata.", "Senza interconnessione al sistema aziendale rischi di perdere l'iperammortamento."),
      ("Tempi e costi li stimi a mano.", "Ore macchina, scarti e consumi finiscono in Excel, quando ci finiscono."),
      ("Il fornitore non collega il tuo gestionale.", "La macchina ha le API, ma nessuno le usa per portare i dati in ufficio."),
    ],
    outcomes=[
      ("Stato macchina in tempo reale", "Stato, allarmi, avanzamento e commessa in lavorazione, visibili dall'ufficio."),
      ("Commesse verso la macchina", "Apertura e chiusura commesse e invio dei file di lavoro (per esempio BTL/TS7) dove la macchina lo supporta."),
      ("Produzione e storico", "Eventi, tagli, pezzi e scarti archiviati e associati automaticamente alla commessa."),
      ("Costi reali per commessa", "Tariffario per ora macchina e lavorazione, materiali ed extra, consuntivo e report A4/PDF."),
      ("Interconnessione documentata", "Scambio dati automatico con il sistema aziendale, documentato per il perito."),
      ("Tutto nella rete aziendale", "Gira su un server o NAS in azienda, con sincronizzazione automatica pianificata."),
    ],
    steps=[
      ("Verifica di compatibilità", "Marca, modello, API o protocolli disponibili e rete. Prima di qualsiasi preventivo."),
      ("Installazione", "Collegamento e configurazione nella rete aziendale, in pochi giorni per macchine con API documentate."),
      ("Collaudo sui dati reali", "Verifico stato, produzione e commesse con la macchina al lavoro."),
      ("Assistenza con canone", "Aggiornamenti, backup e interventi quando la macchina o il gestionale cambiano."),
    ],
    examples=[
      ("JD Industry · bordatrice SCM con Maestro Active",
       "Stato e allarmi in tempo reale, commesse aperte e chiuse verso la macchina, produzione importata in automatico e costo reale per commessa calcolato su tempi effettivi e metri di bordo.", None),
      ("JD Industry · CNC Essetre/Tecnoessetre",
       "Dashboard multi-macchina, eventi associati alla commessa, invio file BTL/TS7, magazzino e residui, tariffario e report economici stampabili.", None),
    ],
    catalog=[
      ("Macchine con API web", ["SCM Maestro Active", "Essetre / Tecnoessetre", "Supervisori e software di linea con API REST"]),
      ("Protocolli industriali", ["Modbus TCP", "Modbus RTU su RS-485", "OPC UA", "MQTT"]),
      ("Collegamenti seriali", ["RS-485 / RS-232", "Gateway seriale-Ethernet", "Middleware su PC industriale o NAS"]),
      ("Sensori e misure", ["Contatori di energia", "Analizzatori di rete", "Sensori di temperatura, pressione e umidità"]),
    ],
    chips=["API REST macchina", "SCM Maestro Active", "Essetre / Tecnoessetre", "Modbus RTU / TCP", "MQTT", "RS-485 / RS-232", "Gateway seriali", "PHP", "MariaDB", "Linux / NAS"],
    faq=[
      ("L'interconnessione serve per l'iperammortamento?", "L'iperammortamento 2026–2028 richiede che il bene sia interconnesso al sistema informativo aziendale o alla rete di fornitura. Realizzo il collegamento e lo documento; la valutazione finale spetta al tuo perito o consulente."),
      ("Devo cambiare gestionale?", "No. I dati della macchina arrivano in un'applicazione dedicata e, dove serve, vengono passati al gestionale che usi già."),
      ("Modificate il programma della macchina?", "No. Leggo e scrivo solo attraverso le interfacce previste dal costruttore. Il programma della macchina resta di chi l'ha fatto."),
      ("Con quali macchine funziona?", "Ho integrazioni già sviluppate per SCM Maestro Active ed Essetre/Tecnoessetre. Per altre marche verifico API e protocolli disponibili prima di qualsiasi preventivo."),
      ("E se la macchina non ha API?", "Si può collegare lo stesso: tramite l'interfaccia web del supervisore, se c'è, oppure con un middleware che legge la porta seriale o Modbus RS-485 e porta i dati nel sistema."),
      ("Cosa succede se cade Internet?", "Niente: il sistema lavora nella rete locale dell'azienda e continua a raccogliere i dati."),
    ],
  ),
  dict(
    slug="gestionale-su-misura.html",
    nav="Gestionali",
    card_title="Gestionali su misura",
    card_who="Piccole e medie imprese che lavorano con Excel o con un gestionale che non si adatta.",
    card_points=["Commesse, clienti, magazzino, prenotazioni", "Report e stampe pronti", "Assistenza continuativa"],
    title="Gestionale su misura per PMI in Friuli | JDEVPRO",
    desc="Gestionali web su misura per PMI in Friuli: commesse, clienti, magazzino, prenotazioni e report. Al posto di Excel, con hosting e assistenza.",
    service_type="Sviluppo gestionale su misura",
    eyebrow="Gestionali su misura · PMI",
    h1="Gestionale su misura: <span>il software segue il tuo lavoro.</span>",
    lead="Sviluppo gestionali web per piccole e medie imprese: costruiti sui tuoi processi, non il contrario. Partiamo da quello che fai oggi, anche da Excel, e arriviamo a uno strumento unico, sicuro e mantenuto nel tempo.",
    problems=[
      ("Excel e fogli sparsi.", "Ogni persona ha la sua versione dei dati e nessuno sa qual è quella giusta."),
      ("Un gestionale generico che non si adatta.", "Paghi funzioni che non usi e ti mancano quelle che servono davvero."),
      ("Dati ricopiati tra programmi.", "Ogni passaggio a mano è tempo perso e un errore possibile."),
    ],
    outcomes=[
      ("Moduli su misura", "Commesse, clienti, fornitori, magazzino, prenotazioni, scadenze: solo quello che serve."),
      ("Accessi e ruoli", "Login sicuro, permessi per ruolo, secondo fattore di autenticazione."),
      ("Report e stampe", "Report per cliente e periodo, stampe A4/PDF, esportazioni CSV e XLSX."),
      ("Importazione dei dati esistenti", "Da Excel o CSV, con anteprima, controllo dei duplicati e conferma."),
      ("Collegato agli altri sistemi", "Contabilità, macchine, sito, email: i dati passano da soli dove servono."),
      ("Hosting, backup e aggiornamenti", "Il gestionale resta veloce, aggiornato e salvato ogni giorno."),
    ],
    steps=[
      ("Analisi dei processi", "Capisco come lavori oggi e cosa deve cambiare."),
      ("Prima versione usabile", "Si parte dalla parte più utile, a prezzo fisso, in tempi brevi."),
      ("Rilasci a fasi", "Ogni fase aggiunge funzioni provate sul lavoro reale."),
      ("Assistenza con canone", "Hosting, backup, correzioni e piccoli sviluppi inclusi."),
    ],
    examples=[
      ("Welora · gestionale per strutture ricettive e attività su prenotazione",
       "Piattaforma multi-struttura con planning, prenotazioni, tariffe, pulizie, portale ospiti, importazioni e sicurezza degli account. 25 moduli e oltre 370 file di test automatici.", "https://welora.it/"),
      ("Gestionale per la rivendita sui marketplace",
       "Prodotti, offerte e ricarichi, clienti, ordini, acquisti dal fornitore e spedizioni in un unico gestionale, collegato a marketplace e corriere.", "integrazione-software-api.html"),
      ("JD Industry · gestionale di produzione",
       "Commesse, clienti, tariffari e consuntivi collegati direttamente alle macchine in officina.", "interconnessione-macchine-industria-4-0.html"),
    ],
    chips=["PHP 8", "Go", "PostgreSQL", "MariaDB / MySQL", "Redis", "RabbitMQ", "Docker", "Linux"],
    faq=[
      ("Posso partire da Excel?", "Sì. Importo i dati che hai già, con anteprima e controllo dei duplicati, così non riparti da zero."),
      ("Sostituisce il programma di contabilità?", "No. La contabilità e la fatturazione elettronica restano nel tuo programma; il gestionale si affianca e ci passa i dati."),
      ("Quanto costa?", "Lavoro a fasi con prezzo fisso concordato prima di iniziare, più un canone mensile per hosting e assistenza."),
      ("Dove gira il gestionale?", "Su un server in cloud oppure su un server dell'azienda, a seconda di dove devono stare i dati."),
      ("Chi lo mantiene dopo la consegna?", "Io, con un canone mensile che copre backup, aggiornamenti di sicurezza, correzioni e piccoli sviluppi."),
    ],
  ),
  dict(
    slug="monitoraggio-iot.html",
    nav="IoT",
    card_title="Monitoraggio IoT",
    card_who="Aziende, impianti e strutture con sensori, consumi o siti remoti da tenere d'occhio.",
    card_points=["Tuya, Aqara, Honeywell, Shelly e altri", "Energia: inverter, contatori, accumuli", "Modbus RS-485 e dispositivi senza rete"],
    title="Integrazione IoT e domotica: energia e Modbus | JDEVPRO",
    desc="Integro domotica e IoT (Tuya, Aqara, Honeywell, Shelly, Netatmo), inverter e contatori Modbus RS-485 con cruscotti, allarmi e gestionale.",
    service_type="Sistemi di monitoraggio IoT",
    eyebrow="IoT · Sensori · Monitoraggio",
    h1="Monitoraggio IoT: <span>sensori collegati ai tuoi sistemi.</span>",
    lead="Progetto sistemi che raccolgono dati da sensori e dispositivi, li portano in un cruscotto o nel gestionale e avvisano quando qualcosa non va. Anche dove la rete è debole o manca la corrente.",
    problems=[
      ("Scopri i problemi solo andando sul posto.", "Un impianto lontano si ferma e lo sai il giorno dopo."),
      ("Consumi senza dati.", "Bollette alte, ma nessuno sa dove e quando si consuma."),
      ("Dispositivi che non si parlano.", "Ogni apparecchio ha la sua app e nessuna vista d'insieme."),
    ],
    systems=[
      ("Microcontrollori", ["STM32", "Raspberry Pi Pico / RP2040", "Beken BK7238", "Firmware in C"]),
      ("Connettività", ["LTE Cat-1", "NB-IoT", "Wi-Fi", "Bluetooth / BLE", "RS-485 / Modbus"]),
      ("Dati e cloud", ["MQTT con TLS", "Mosquitto", "Python / FastAPI", "PostgreSQL", "Cruscotti e allarmi"]),
      ("Dispositivi e domotica", ["Tuya / Smart Life", "Home Assistant", "Termostati", "OBD-II per veicoli"]),
    ],
    catalog=[
      ("Domotica e clima", ["Tuya / Smart Life", "Aqara", "Honeywell / Resideo", "Google Nest", "Netatmo", "Philips Hue", "Shelly", "Daikin", "Somfy", "Nuki", "Home Assistant", "Zigbee2MQTT"]),
      ("Energia e fotovoltaico", ["Fronius", "SMA", "SolarEdge", "Huawei FusionSolar", "Victron Energy", "Contatori e analizzatori Modbus"]),
      ("Sensori e campo", ["Sensori industriali RS-485", "Stazioni meteo Ecowitt", "LoRaWAN / The Things Network", "Gateway LTE e NB-IoT"]),
      ("Protocolli", ["MQTT", "Modbus RTU / TCP", "RS-485 / RS-232", "HTTP / REST", "Bluetooth / BLE", "Zigbee tramite bridge"]),
    ],
    outcomes=[
      ("Raccolta dati da sensori", "RS-485/Modbus, MQTT, Wi-Fi, Bluetooth/BLE, LTE e NB-IoT."),
      ("Cruscotti e allarmi", "Soglie, notifiche e storico consultabili da computer e telefono."),
      ("Energia", "Consumi, fotovoltaico, accumuli, inverter e pompe di calore."),
      ("Siti remoti", "Alimentazione solare, buffering dei dati quando manca la rete, connessione LTE."),
      ("Termostati e domotica", "Dispositivi Tuya/Smart Life e Home Assistant integrati nel gestionale."),
      ("Aggiornamenti sicuri", "Firmware firmato con rollback e recovery locale per i dispositivi."),
    ],
    steps=[
      ("Sopralluogo e obiettivi", "Cosa misurare, dove, con quale alimentazione e connessione."),
      ("Scelta dei dispositivi", "Sensori e gateway adatti, anche riusando quelli che hai già."),
      ("Installazione e cruscotto", "Dati, allarmi e collegamento ai tuoi sistemi."),
      ("Manutenzione con canone", "Controllo da remoto, aggiornamenti e assistenza."),
    ],
    examples=[
      ("Sentry-Bee · monitoraggio sul campo",
       "Firmware per STM32 con sensori RS-485, modem LTE, MQTT con TLS, buffering dei dati, backend FastAPI e alimentazione solare con batterie LiFePO4.", "https://github.com/jellero/sentry-bee"),
      ("Webcam autonoma a basso consumo",
       "Firmware per Raspberry Pi Pico con fotocamera e connessione NB-IoT, pensata per siti senza rete fissa.", None),
      ("Vehylo · diagnostica veicolo",
       "App Android che legge i dati del veicolo via OBD-II e Bluetooth, con mapping dinamico dei segnali.", None),
      ("Welora · clima delle camere",
       "Termostati collegati al gestionale della struttura, con avvisi di comfort e comandi manuali per singola camera.", "https://welora.it/"),
      ("AKIOS · ciclo di vita dei dispositivi IoT",
       "Firmware con verifica crittografica, doppio slot A/B, rollback e recovery locale.", "https://akios.cloud/"),
    ],
    chips=["MQTT / TLS", "RS-485 / Modbus", "LTE / NB-IoT", "Wi-Fi", "Bluetooth / BLE", "STM32", "RP2040", "Embedded C", "Python / FastAPI", "OTA firmato"],
    faq=[
      ("Funziona anche senza Internet?", "Sì. I dati vengono salvati localmente e inviati quando la connessione torna disponibile."),
      ("Posso usare i sensori che ho già?", "Spesso sì. Verifico protocolli e interfacce prima di proporre dispositivi nuovi."),
      ("Quali marche si possono integrare?", "Tutte quelle con API pubbliche, come Tuya, Aqara, Honeywell, Shelly, Netatmo, Philips Hue, Fronius, SMA o SolarEdge. Se un dispositivo ha solo un'app o un pannello web, ne automatizzo le chiamate; se ha solo una porta seriale o Modbus, uso un middleware."),
      ("I dati sono al sicuro?", "Le comunicazioni sono cifrate e i dispositivi stanno su reti separate da quelle dell'ufficio."),
      ("Chi segue l'impianto dopo l'installazione?", "Io, con un canone che copre controllo da remoto, aggiornamenti e assistenza."),
    ],
  ),
  dict(
    slug="integrazione-software-api.html",
    nav="Integrazioni",
    card_title="Integrazioni e automazioni",
    card_who="Aziende con gestionale, e-commerce, marketplace, corrieri e portali che devono scambiarsi dati.",
    card_points=["Amazon, eBay, Shopify e altri marketplace", "Corrieri, pagamenti, fatture elettroniche", "Anche senza API: web, seriale, Modbus"],
    title="Integrazione gestionale, Amazon ed eBay | JDEVPRO",
    desc="Collego gestionale, Amazon, eBay, Shopify, corrieri, pagamenti e fatturazione elettronica via API, interfacce web o seriale. Con code e log.",
    service_type="Integrazione software, API e automazione dei processi",
    eyebrow="Integrazioni · API · Marketplace · Automazioni",
    h1="Integrazioni e automazioni: <span>i tuoi software si parlano.</span>",
    lead="Collego gestionale, marketplace, corrieri, fornitori, pagamenti, fatturazione elettronica e portali in modo che ordini, prezzi, disponibilità e documenti passino da soli. Senza doppioni, senza perdite, con lo storico di ogni passaggio.",
    problems=[
      ("Ordini e disponibilità ricopiati a mano.", "Marketplace, magazzino, fornitore e corriere non si parlano e ogni passaggio è copia-incolla."),
      ("Integrazioni che si rompono in silenzio.", "Un token scade, un'API cambia, e te ne accorgi quando un cliente si lamenta."),
      ("Un software diverso per ogni cosa.", "Pagamenti, fatture, portali e comunicazioni vivono in sistemi separati."),
    ],
    outcomes=[
      ("Marketplace ed e-commerce", "Pubblicazione offerte, prezzi e disponibilità, importazione degli ordini, stati e riconciliazione."),
      ("Fornitori e corrieri", "Cataloghi e ordini verso i fornitori, spedizioni, etichette e tracking dai corrieri."),
      ("Pagamenti e fatturazione elettronica", "Incassi, preautorizzazioni, rimborsi, generazione FatturaPA e invio tramite intermediario."),
      ("Portali e adempimenti", "Portali di prenotazione, comunicazioni obbligatorie (per esempio Alloggiati Web e ISTAT), messaggistica."),
      ("Sincronizzazione affidabile", "Code ed eventi, tentativi ripetuti, controlli anti-doppione, limiti di chiamata rispettati: niente dati persi o duplicati."),
      ("Credenziali protette e storico", "Token e password cifrati e mai mostrati, rotazione, log di ogni operazione e avvisi quando qualcosa si ferma."),
    ],
    systems=[
      ("E-commerce e marketplace", ["SellRapido", "IBS", "Temu", "Booking.com", "Channel manager WuBook"]),
      ("Fornitori e logistica", ["API fornitori e cataloghi", "Corrieri GLS", "Discogs e MusicBrainz (metadati prodotto)"]),
      ("Pagamenti e fisco", ["Stripe Connect, Checkout e Identity", "Fatturazione elettronica FatturaPA / SdI", "Alloggiati Web", "ISTAT / WebTur"]),
      ("Comunicazioni", ["WhatsApp Business", "Email SMTP / IMAP", "Notifiche push", "Telegram"]),
      ("Macchine e dispositivi", ["SCM Maestro Active", "Essetre / Tecnoessetre", "Tuya / Smart Life", "MQTT"]),
      ("Architettura", ["REST API e webhook", "RabbitMQ", "Inbox / outbox", "Dead letter e retry", "PostgreSQL"]),
    ],
    catalog=[
      ("Marketplace ed e-commerce", ["Amazon (Selling Partner API)", "eBay", "Shopify", "WooCommerce", "PrestaShop", "Magento / Adobe Commerce", "Etsy", "ManoMano", "Zalando", "Temu", "IBS", "SellRapido"]),
      ("Corrieri e spedizioni", ["BRT", "GLS", "Poste Italiane / SDA", "DHL", "UPS", "FedEx"]),
      ("Pagamenti", ["Stripe", "PayPal", "Satispay", "Nexi", "SumUp"]),
      ("Fatturazione e contabilità", ["FatturaPA / SdI", "Fatture in Cloud", "Aruba Fatturazione Elettronica", "Gestionali contabili via API, file o database"]),
      ("Prenotazioni e turismo", ["Booking.com", "Channel manager", "Alloggiati Web", "ISTAT / WebTur"]),
      ("Comunicazioni e ufficio", ["WhatsApp Business", "Email SMTP / IMAP", "Telegram", "Google Workspace", "Microsoft 365"]),
    ],
    steps=[
      ("Mappa dei sistemi", "Quali software ci sono, quali dati devono passare e quando."),
      ("Progetto del flusso", "Formati, errori possibili, controlli e responsabilità."),
      ("Sviluppo e collaudo", "Prove con dati reali prima di andare in produzione."),
      ("Monitoraggio con canone", "Controllo continuo e interventi quando un sistema cambia."),
    ],
    examples=[
      ("Gestionale collegato a fornitore, marketplace e corriere",
       "Gestionale per un'azienda che compra da un fornitore e rivende sui marketplace. Un servizio separato collega catalogo del fornitore, SellRapido, IBS, Temu e il corriere GLS: offerte, ordini, acquisti e spedizioni senza passaggi manuali.", None),
      ("Welora Automation · motore di automazione a eventi",
       "Servizio in Go con RabbitMQ e PostgreSQL: lavori che sopravvivono ai riavvii, tentativi ripetuti, controlli di salute. Importa le prenotazioni da Booking.com e aggiorna le disponibilità.", None),
      ("Welora · pagamenti, fatture e adempimenti",
       "Stripe Connect per incassi, preautorizzazioni e rimborsi, verifica dei documenti con Stripe Identity, generazione FatturaPA, Alloggiati Web, ISTAT e WhatsApp Business.", "https://welora.it/"),
    ],
    chips=["REST API", "Webhook", "OAuth / token", "RabbitMQ", "Inbox / outbox", "Idempotenza", "PostgreSQL", "Go", "PHP", "Python", "Docker", "Linux / Nginx"],
    faq=[
      ("Collegate anche Amazon, eBay e gli altri marketplace?", "Sì. Ho già sviluppato integrazioni con SellRapido, IBS, Temu e il corriere GLS; Amazon, eBay, Shopify e gli altri marketplace con API pubbliche si collegano allo stesso modo: offerte, prezzi, disponibilità, ordini e spedizioni."),
      ("Si può integrare un servizio senza API pubbliche?", "Sì. Se il servizio si usa da browser, ne automatizzo le stesse chiamate del pannello web, verificando prima le condizioni d'uso. Per dispositivi e macchine senza rete uso un middleware seriale o Modbus."),
      ("E la fatturazione elettronica?", "Genero l'XML FatturaPA e lo invio tramite il tuo intermediario o il tuo programma di fatturazione, senza sostituirlo."),
      ("E se il mio software non ha API?", "Si può lavorare con esportazioni di file, accesso al database o cartelle condivise. Valuto la soluzione più sicura caso per caso."),
      ("Cosa succede se un sistema è fermo?", "I dati restano in coda e vengono inviati quando il sistema torna disponibile, senza doppioni."),
      ("Posso vedere cosa è successo?", "Sì: ogni passaggio viene registrato e gli errori generano un avviso."),
      ("Lavori anche da remoto?", "Sì. Per le integrazioni software lavoro quasi sempre da remoto, con accessi concordati e tracciati."),
    ],
  ),
  dict(
    slug="siti-web-piattaforme.html",
    nav="Siti web",
    card_title="Siti e piattaforme web",
    card_who="Aziende ed enti che vogliono un sito da gestire in autonomia, collegato ai propri sistemi.",
    card_points=["Pannello di gestione", "Multilingua e notifiche", "Hosting e manutenzione"],
    title="Siti web con pannello di gestione e multilingua | JDEVPRO",
    desc="Siti e piattaforme web gestibili in autonomia: testi modificabili, multilingua, contatti con notifiche, newsletter. Hosting e manutenzione inclusi.",
    service_type="Sviluppo siti web e piattaforme",
    eyebrow="Siti web · Piattaforme · Backoffice",
    h1="Siti web e piattaforme <span>gestibili in autonomia.</span>",
    lead="Siti veloci e curati con un pannello per aggiornare testi, pagine e contenuti senza toccare il codice. E collegati ai tuoi sistemi: prenotazioni, gestionale, notifiche.",
    problems=[
      ("Non puoi aggiornare il sito da solo.", "Ogni modifica è una richiesta, un'attesa e un costo."),
      ("Le richieste dal sito si perdono.", "Il modulo contatti finisce in una casella che nessuno guarda."),
      ("Il sito è slegato dal resto.", "Prenotazioni e dati dei clienti vanno ricopiati a mano."),
    ],
    outcomes=[
      ("Pannello di gestione", "Testi, pagine, gallerie, eventi e contenuti modificabili con anteprima."),
      ("Multilingua", "Contenuti in più lingue, con traduzioni assistite da rivedere prima di pubblicare."),
      ("Contatti e notifiche", "Messaggi raccolti nel pannello e notifiche sul telefono a ogni richiesta."),
      ("Newsletter e comunicazioni", "Iscrizioni, invii e casella email gestiti dallo stesso pannello."),
      ("Collegato ai tuoi sistemi", "Widget di prenotazione, aree clienti, dati dal gestionale."),
      ("Hosting e manutenzione", "Sicurezza, backup, aggiornamenti e rilasci con possibilità di tornare indietro."),
    ],
    steps=[
      ("Obiettivi e contenuti", "A chi parla il sito e cosa deve far fare a chi lo visita."),
      ("Struttura e design", "Pagine pensate per chi cerca, anche su Google."),
      ("Sviluppo e pannello", "Contenuti caricati e pannello pronto all'uso."),
      ("Hosting e assistenza", "Canone mensile per tenerlo veloce, sicuro e aggiornato."),
    ],
    examples=[
      ("Lauco Experience · portale turistico in quattro lingue",
       "Sito in italiano, inglese, tedesco e sloveno con percorsi GPX, eventi e luoghi. Backoffice con ruoli, posta integrata, notifiche push, newsletter e statistiche dei QR code.", "https://www.laucoexperience.it/"),
      ("Welora · widget di prenotazione per siti",
       "Widget JavaScript che porta disponibilità e prenotazioni del gestionale direttamente nel sito della struttura.", "https://welora.it/"),
    ],
    chips=["PHP 8", "Slim 4", "MariaDB", "JavaScript", "Multilingua", "Web Push", "SEO tecnico", "Linux / Nginx"],
    faq=[
      ("Posso modificare il sito da solo?", "Sì. Testi, immagini e contenuti si cambiano dal pannello, con anteprima prima di pubblicare."),
      ("Il sito sarà visibile su Google?", "Struttura delle pagine, velocità, testi e dati strutturati sono pensati fin dall'inizio per essere trovati da chi cerca."),
      ("Gestite anche l'hosting?", "Sì, con un canone mensile che copre hosting, sicurezza, backup e aggiornamenti."),
      ("Il sito può collegarsi al gestionale?", "Sì: prenotazioni, aree clienti e dati possono arrivare direttamente dal gestionale."),
    ],
  ),
]


# Modelli e scrittura delle pagine
exec(compile(pathlib.Path(__file__).with_name("templates.py").read_text(encoding="utf-8"), "templates.py", "exec"))
