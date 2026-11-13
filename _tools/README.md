Generatore delle pagine del sito.

    python _tools/build_site.py .

Modifica i testi in build_site.py (pagine italiane) e content_extra.py (prezzi, città, guide, inglese), poi rigenera.


Le pagine `casi-studio-industriali.html` ed `en-industrial-case-studies.html` sono schede redazionali HTML mantenute direttamente nel repository: il generatore non le riscrive, ma include i relativi URL nella sitemap. Nessun dato di cliente non autorizzato o metrica economica non verificata va aggiunto alle schede.
Il modulo di verifica tecnica non invia dati dal browser a un server: prepara una bozza email e offre la copia del testo. Un invio diretto dal sito richiede la successiva configurazione di un endpoint sicuro.

Le pagine Digital Receptionist sono generate da `content_products.py`,
`content_areas.py` e `templates.py`, nel catalogo dei prodotti.
Stato commerciale: **prodotto sviluppato, a breve disponibile**. Funzioni: risposte in italiano,
smistamento/filtro chiamate, connettori VoIP e gestionali, prenotazioni, disdette,
notifiche e schede strutturate. Nessun prezzo o data esatta di disponibilità annunciata.

Il workflow di audit rigenera il sito in una directory temporanea di GitHub Actions
per verificare che i sorgenti siano coerenti. Non pubblica e non distribuisce nulla.
