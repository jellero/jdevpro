# Modulo contatti JDEVPRO — PHP, SMTP Aruba Business e Turnstile

## Stato
La modifica non è attiva fino al deploy dell'endpoint su un hosting PHP e alla configurazione SMTP/Turnstile. Non pubblicare il frontend nuovo prima che il backend sia stato installato e verificato.

## Architettura
- index.html ed en.html inviano via fetch a https://www.jdevpro.it/api/contact.php.
- api/contact.php convalida i campi, honeypot, Siteverify Turnstile, Origin CORS e rate limiting (5 invii/IP in 15 minuti), poi manda una email a info@jdevpro.it.
- Il mittente è info@jdevpro.it, il Reply-To è l'indirizzo inserito dal visitatore. Nessuna conferma automatica viene spedita al visitatore.
- Resta il pulsante per copiare la richiesta in caso di indisponibilità.
- GitHub Pages non esegue PHP. L'endpoint va messo su www.jdevpro.it con PHP abilitato.

## Requisiti
- PHP >= 8.1, estensioni curl, json e openssl, filesystem temporaneo scrivibile.
- Accesso uscente HTTPS a challenges.cloudflare.com:443 e SMTP a out.postassl.it:465.
- Composer: dalla directory del deploy lanciare: composer install --no-dev --prefer-dist --optimize-autoloader.
- Directory vendor/ protetta dall'accesso web, preferibilmente fuori dalla document root. La protezione .htaccess vale solo su Apache.

## Credenziali private
Impostare come variabili di ambiente del processo PHP o tramite configurazione privata fuori dalla document root:
- JDEVPRO_SMTP_USER = info@jdevpro.it (facoltativo, è il valore predefinito).
- JDEVPRO_SMTP_PASSWORD = password della casella Aruba Business.
- JDEVPRO_TURNSTILE_SECRET = secret key del widget Cloudflare.

Non inserire mai password o secret in HTML, JS o repository pubblico. SMTP Aruba Business: out.postassl.it, porta 465, TLS implicito / SMTPS (non STARTTLS su 587).

## Turnstile invisibile
1. Nel dashboard Cloudflare Turnstile creare un widget in modalità Invisible.
2. Autorizzare gli hostname www.jdevpro.it, jdevpro.it e jellero.github.io.
3. Sostituire INSERISCI_SITEKEY_TURNSTILE in index.html ed en.html con la sitekey PUBBLICA.
4. Impostare la secret key nell'ambiente PHP come JDEVPRO_TURNSTILE_SECRET.
5. Il server valida success, hostname e action=contact con Siteverify. Non rimuovere questo controllo.
6. Per altri host di staging aggiornare widget Cloudflare, whitelist Origin e hostname lato PHP.

Le informative privacy e cookie contengono il link alla Turnstile Privacy Addendum, richiesto per il modo invisibile.

## Procedura di rilascio
1. Installare l'endpoint PHP e le dipendenze vendor sul dominio www.jdevpro.it.
2. Configurare variabili private e sitekey pubblica.
3. Verificare che un GET a https://www.jdevpro.it/api/contact.php risponda HTTP 405 con JSON: non deve mostrare codice PHP.
4. Provare un invio con Turnstile reale: verificare email ricevuta su info@jdevpro.it e intestazione Reply-To.
5. Solo dopo pubblicare index.html, en.html e script.js aggiornati.

## Test
- Controlli di sintassi: php -l api/contact.php e node --check script.js.
- POST senza Turnstile valido: nessuna email.
- Honeypot website valorizzato: nessuna email.
- Origine CORS estranea: HTTP 403.
- Oltre 5 invii validi/IP in 15 minuti: HTTP 429.
- Password SMTP assente: HTTP 503.
- Una richiesta corretta riceve ok=true SOLO dopo il successo del trasporto SMTP.
- Testare sia la pagina ufficiale sia l'anteprima GitHub Pages.

La rate limit salva solo hash SHA-256 dell'IP in una directory temporanea locale e non memorizza i messaggi.
