# JDEVPRO

Nuovo sito pubblico JDEVPRO, riposizionato su **software engineering, systems integration, industrial IoT e connected infrastructure**.

## Obiettivo

Il sito evita di presentare ogni tecnologia o impianto come un servizio indipendente. Il posizionamento principale è:

> Software, integrazioni e sistemi connessi.

Fotovoltaico, reti, accessi, hospitality, macchine e IoT rimangono come **ambiti applicativi** di una competenza centrale: progettare e mantenere sistemi che collegano software, dati e mondo reale.

## Progetti collegati

La pagina include collegamenti ai progetti pubblici e, quando disponibili, alle rispettive GitHub Pages:

- ORYVAEL / ORYVAEL Web
- JD Industry
- Sentry-Bee
- Vehylo Web
- Welora Web
- Lauco Experience
- Space1999 prototype
- Bioapicoltura Pura

## Struttura

- `index.html` — sito principale
- `styles.css` — design responsive
- `script.js` — menu, header e reveal progressivo
- `privacy.html` — informativa essenziale

Non sono richiesti framework, build step o dipendenze esterne.

## Anteprima locale

```bash
python -m http.server 8000
```

Poi apri `http://localhost:8000`.

## Pubblicazione

Il repository può essere pubblicato su GitHub Pages, Cloudflare Pages, Netlify o su un normale web server statico. Per il dominio `jdevpro.it`, configurare il dominio solo quando DNS e hosting di destinazione sono stati definiti.
