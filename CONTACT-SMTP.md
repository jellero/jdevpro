# Invio moduli JDEVPRO – Aruba Business

Il sito usa `POST /contact.php` e SMTP autenticato (come SmartAgent, ma senza dipendenza dal suo database).
Parametri ufficiali Aruba Business: `out.postassl.it`, porta `465`, SSL/TLS, autenticazione con password. Destinatario fisso: `info@jdevpro.it`. Il mittente è la casella autenticata, il visitatore è in Reply-To.

## Configurazione Plesk (prima della pubblicazione)

1. PHP 8.1+ con OpenSSL abilitato e accesso in uscita TCP 465.
2. Configurare le variabili d'ambiente PHP `JDEVPRO_SMTP_USER` (default `info@jdevpro.it`) e `JDEVPRO_SMTP_PASSWORD`.
   In alternativa creare **fuori dalla document root** (ad esempio accanto a `httpdocs`) `jdevpro-smtp.php`:
   ```php
   <?php
   return [
       'username' => 'info@jdevpro.it',
       'password' => 'INSERIRE_LA_PASSWORD_REALE_SOLO_SUL_SERVER',
   ];
   ```
   Limitare i permessi al processo PHP (0600, o 0640 con gruppo corretto), verificare open_basedir. Non aggiungere questo file a Git.
3. Verificare HTTPS, esecuzione PHP, directory temporanea scrivibile e assenza di blocchi SMTP del provider.
4. Inviare una richiesta di prova dalla home e da Assistenza, verificare ricezione e Reply-To. Il successo sul sito significa accettazione SMTP, non garantisce consegna nella posta in arrivo.
5. Controllare DevTools: POST HTTPS, HTTP 200 e JSON ok=true. Provare dati invalidi (422), GET (405) e credenziali non disponibili (503, senza dettagli riservati). Il modulo senza JS mostra una risposta HTML.
   
Protezione base: validazione lato server, honeypot, limite cinque tentativi per IP in 10 minuti, destinatario fisso e nessun allegato. Il limite usa REMOTE_ADDR: in presenza di proxy configurare il ripristino dell'IP reale su Apache/Plesk, senza fidarsi di header arbitrari. Gli identificativi scaduti sono rimossi alla successiva richiesta; rimuovere il file temporaneo in caso di dismissione. Non è un sistema ticket.

Riferimento: https://guide.arubabusiness.it/email/configurazioni-email-arubabusiness/utilizzare-casella-arubabusiness-client-posta
