# JDEVPRO

Sito pubblico JDEVPRO, focalizzato su **software engineering, backend, systems integration, industrial software/IoT e production operations**.

## Posizionamento

Il sito non presenta ogni tecnologia, impianto o dispositivo come un servizio indipendente. Il messaggio principale è:

> **Software che collega sistemi reali.**

Fotovoltaico, reti, hospitality, dispositivi, macchine e siti remoti restano presenti come **ambiti applicativi**. Il nucleo della proposta è progettare, integrare e mantenere sistemi che collegano software, dati, macchine e infrastruttura.

## Struttura dei contenuti

Tre aree principali:

1. **Backend & Systems Integration** — API, database, provider, processi asincroni, automazioni e integrazioni B2B/B2C.
2. **Industrial Software & IoT** — PLC, CODESYS, embedded C, RS-485/RS-232, MQTT, gateway, machine-to-cloud e dati di produzione.
3. **Production & Connected Infrastructure** — Linux, Docker, CI/CD, logging, hardening, monitoring, backup/recovery e networking.

I progetti in homepage sono ordinati per coerenza con questo posizionamento:

- **JD Industry** — industrial software e machine integration;
- **AKIOS** — embedded/IoT lifecycle e affidabilità;
- **Welora** — backend, automation e sistemi asincroni;
- **Sentry-Bee** — field IoT e telemetria;
- **Vehylo** — connected vehicle e data acquisition.

ORYVAEL, Oryzeno e Lauco Experience rimangono visibili come R&D/altri lavori, ma non dominano più il messaggio commerciale.

## File principali

- `index.html` — homepage italiana
- `en.html` — homepage inglese
- `styles.css` — design responsive
- `overrides.css` — logo e system flow card
- `script.js` — menu, reveal, analytics e consenso cookie
- `cv.html` / `cv-en.html` — CV web

Il sito è statico e non richiede framework o build step.

## Anteprima locale

```bash
python -m http.server 8000
```

Poi apri `http://localhost:8000`.
