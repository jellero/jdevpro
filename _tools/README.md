Generatore delle pagine del sito.

    python _tools/build_site.py .

Modifica i testi in build_site.py (pagine italiane) e content_extra.py (prezzi, città, guide, inglese), poi rigenera.


Le pagine `casi-studio-industriali.html` ed `en-industrial-case-studies.html` sono schede redazionali HTML mantenute direttamente nel repository: il generatore non le riscrive, ma include i relativi URL nella sitemap. Nessun dato di cliente non autorizzato o metrica economica non verificata va aggiunto alle schede.
Il modulo di verifica tecnica non invia dati dal browser a un server: prepara una bozza email e offre la copia del testo. Un invio diretto dal sito richiede la successiva configurazione di un endpoint sicuro.
