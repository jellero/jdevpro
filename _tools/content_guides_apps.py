"""Guide pratiche di pubblicazione app e adempimenti correlati (aggiornate 12 novembre 2026)."""

APP_PUBLISHING_GUIDES = [
  {
    "slug": "guida-pubblicare-app-microsoft-store.html",
    "title": "Pubblicare un'app su Microsoft Store: costi e requisiti | JDEVPRO",
    "short": "Pubblicare un'app su Microsoft Store",
    "desc": "Passaggi, account gratuito, MSIX o MSI/EXE, firma, certificazione, ricavi e GDPR per pubblicare app Windows nel Microsoft Store.",
    "h1": "Microsoft Store: <span>pubblicare un'app Windows, con costi e controlli.</span>",
    "intro": "Un'app Windows pronta per funzionare non è automaticamente pronta per lo Store: servono l'account corretto, un pacchetto distribuibile, metadati verificabili, una gestione dei dati chiara e un piano di aggiornamento. Questi sono i passaggi da completare prima dell'invio.",
    "sections": [
      [
        "1. Scegli lo sviluppatore che pubblica",
        [
          "Registra l'account nel <strong>Microsoft Partner Center</strong> attraverso la nuova procedura ufficiale. L'account Individual è pensato per attività non professionali; se la distribuzione riguarda il tuo lavoro o la tua impresa, considera l'account Company. La tipologia Individual non si converte direttamente in Company.",
          "<strong>Quota iniziale:</strong> Microsoft indica registrazione gratuita per i nuovi account individuali e aziendali tramite il nuovo percorso. Verifica requisiti di identificazione personale o aziendale, indirizzi e dati fiscali: <a href=\"https://learn.microsoft.com/windows/apps/publish/partner-center/open-a-developer-account\" rel=\"noreferrer\" target=\"_blank\">Microsoft: apertura account</a>."
        ]
      ],
      [
        "2. Identità dell'app e formato del pacchetto",
        [
          [
            "Scegli nome, publisher, identificativo univoco, versione, architetture supportate, sistemi operativi minimi e logo.",
            "Per una distribuzione classica considera MSIX, con vantaggi di installazione, aggiornamento e firma gestita dallo Store. Valuta MSI/EXE quando la tua applicazione richiede un installer tradizionale; per applicazioni web valutane l'eventuale pubblicazione come PWA.",
            "Allinea l'identità nel manifest, nel pacchetto e nella scheda dello Store. Controlla dipendenze, permessi richiesti, disinstallazione e comportamento offline."
          ]
        ]
      ],
      [
        "3. Firma digitale e installazione",
        [
          "Per <strong>MSIX/AppX distribuito nello Store</strong>, Microsoft firma nuovamente il pacchetto dopo la certificazione: non è necessario acquistare un certificato CA per quel percorso. Gli installer <strong>MSI/EXE</strong> non sono firmati nuovamente dallo Store: verifica la firma Authenticode. Per download diretti, firma e aggiornamenti sono responsabilità del publisher.",
          "Riferimento: <a href=\"https://learn.microsoft.com/en-us/windows/apps/publish/get-started\" rel=\"noreferrer\" target=\"_blank\">Microsoft Learn: pubblicazione e firma</a>."
        ]
      ],
      [
        "4. Crea la scheda e sottoponi l'app",
        [
          [
            "Prenota il nome in Partner Center; crea l'invio e definisci mercati, prezzi, categoria, requisiti e classificazione per età IARC.",
            "Prepara descrizione non ingannevole, screenshot reali, icone, pagina di assistenza, contatto e informativa privacy se tratta dati personali.",
            "Carica il pacchetto corretto, configura le note per i revisori, verifica i controlli automatici e invia alla certificazione. Dopo l'approvazione verifica la scheda dallo Store su PC reale."
          ],
          "I requisiti di invio dipendono dal formato: <a href=\"https://learn.microsoft.com/windows/apps/publish/get-started\" rel=\"noreferrer\" target=\"_blank\">guida ufficiale Microsoft Store</a>."
        ]
      ],
      [
        "5. Quanto costa davvero",
        [
          [
            "Account sviluppatore nel nuovo flusso: 0 USD di registrazione.",
            "Per app non di gioco Microsoft consente in determinati casi l'uso di un sistema di pagamento proprio, mantenendo il 100% del corrispettivo prima dei costi del proprio provider e delle imposte; usando il sistema commerciale Microsoft, la quota indicata per le app è 15%. Per i giochi e altri scenari le regole differiscono.",
            "Budget separato: sviluppo, eventuale firma di MSI/EXE, supporto, server, assistenza, marketing, traduzioni, consulenza legale e fiscale."
          ],
          "Fonte: <a href=\"https://learn.microsoft.com/en-us/windows/apps/publish/get-started\" rel=\"noreferrer\" target=\"_blank\">opzioni commerciali Microsoft Store</a>."
        ]
      ],
      [
        "6. Dati personali e informazioni legali",
        [
          "Prima del rilascio individua titolare del trattamento, dati raccolti, finalità, basi giuridiche, retention e fornitori. Pubblica un'informativa coerente con ciò che l'app, il backend e gli SDK fanno realmente; predisponi un canale per richieste di accesso e cancellazione.",
          "Se usi account, telemetria, crash reporting o pagamenti, verifica log, identificativi, paesi di hosting e contratti con i responsabili del trattamento. Vedi la <a href=\"guida-pubblicare-app-gdpr-privacy.html\">checklist GDPR e adempimenti per le app</a>."
        ]
      ],
      [
        "7. Test prima e dopo la pubblicazione",
        [
          [
            "Verifica installazione pulita, aggiornamento dalla versione precedente, disinstallazione e mantenimento o cancellazione dei dati secondo l'informativa.",
            "Esegui test su dispositivi e versioni di Windows supportate; prova rete assente, login scaduto, errore API, permessi negati e ripristino.",
            "Monitora errori, recensioni, vulnerabilità e versioni obsolete. Mantieni archivio degli artefatti e un processo di rilascio ripetibile."
          ]
        ]
      ],
      [
        "8. Se non vuoi passare dallo Store",
        [
          "La distribuzione diretta da un sito aziendale richiede hosting, download sicuro, firma adeguata, aggiornamenti, verifica integrità e assistenza. Non va presentata come equivalente alla certificazione Microsoft Store. Confronta costi di gestione, reputazione SmartScreen e requisiti dei clienti.",
          "Guida: <a href=\"https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/publish-first-app\" rel=\"noreferrer\" target=\"_blank\">pubblicare la prima app Windows</a>."
        ]
      ],
      [
        "9. Le guide correlate",
        [
          "Confronta <a href=\"guida-pubblicare-app-macos.html\">macOS</a>, <a href=\"guida-pubblicare-app-android.html\">Android</a> e <a href=\"guida-pubblicare-app-ios.html\">iOS</a>. Prima di vendere o raccogliere dati, completa la <a href=\"guida-pubblicare-app-gdpr-privacy.html\">checklist GDPR e adempimenti per le app</a>."
        ]
      ]
    ],
    "cta": "software-web.html",
    "contact": [
      "Vuoi distribuire una tua applicazione Windows?",
      "Descrivi tecnologia, installer attuale, modello commerciale e dati raccolti: valutiamo il percorso tecnico di pubblicazione."
    ],
    "published": "2026-11-12",
    "updated": "novembre 2026"
  },
  {
    "slug": "guida-pubblicare-app-macos.html",
    "title": "Pubblicare un'app su macOS: Mac App Store, firma e costi | JDEVPRO",
    "short": "Pubblicare un'app su macOS",
    "desc": "Mac App Store o download diretto: Apple Developer, sandbox, Developer ID, notarizzazione, DMG/PKG, pagamenti e GDPR.",
    "h1": "Pubblicare su macOS: <span>Mac App Store oppure distribuzione diretta.</span>",
    "intro": "Su macOS ci sono due canali distinti: il Mac App Store, con revisione e distribuzione Apple, oppure il download da un sito, con Developer ID, firma e notarizzazione. La scelta va fatta prima di progettare installer, sandbox, aggiornamenti e pagamenti.",
    "sections": [
      [
        "1. Scegli il canale di distribuzione",
        [
          [
            "Mac App Store: visibilità nello Store, gestione delle installazioni e degli aggiornamenti, App Review e App Sandbox obbligatoria.",
            "Distribuzione diretta: maggiore controllo su installer, vendita e updater; il produttore gestisce hosting, supporto e aggiornamenti. Per il normale flusso di app firmate con Developer ID serve notarizzazione.",
            "Verifica sin dall'inizio entitlement, accesso a file, processi ausiliari, driver, helper e tecnologie non compatibili con la sandbox."
          ],
          "Fonte: <a href=\"https://developer.apple.com/macos/distribution\" rel=\"noreferrer\" target=\"_blank\">Apple: Mac App Store e distribuzione esterna</a>."
        ]
      ],
      [
        "2. Account e costo annuale",
        [
          "Per pubblicare sul Mac App Store, firmare con Developer ID e usare i servizi di distribuzione, iscriviti all'<strong>Apple Developer Program</strong>. La quota di riferimento è <strong>99 USD/anno</strong>, con importo locale mostrato all'iscrizione; lo stesso programma può coprire anche le app iOS.",
          "Scegli individuo o organizzazione secondo la realtà che pubblica; le aziende devono superare le verifiche richieste. Fonte: <a href=\"https://developer.apple.com/help/account/membership/program-enrollment\" rel=\"noreferrer\" target=\"_blank\">Apple Developer: iscrizione e costi</a>."
        ]
      ],
      [
        "3. Preparazione tecnica del progetto",
        [
          [
            "Assegna un Bundle ID stabile, definisci version e build number, imposta icona, metadati, entitlements e minimum macOS.",
            "Controlla permessi per file, cartelle, microfono, fotocamera, contatti e accessibilità. Chiedi soltanto quelli indispensabili e spiega il motivo nell'interfaccia.",
            "Verifica Apple Silicon e architetture supportate, firme delle librerie e degli helper, aggiornamenti e recupero da errori."
          ]
        ]
      ],
      [
        "4. Procedura Mac App Store",
        [
          [
            "Abilita App Sandbox e firma per la distribuzione App Store; crea l'archivio in Xcode e prepara un record in App Store Connect.",
            "Imposta prezzi e mercati, categoria ed età, screenshot e descrizioni, privacy policy, dati raccolti, note di revisione ed eventuale account dimostrativo.",
            "Invia la build a App Review; dopo l'approvazione decidi la pubblicazione e monitora crash e recensioni."
          ],
          "Fonti: <a href=\"https://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution\" rel=\"noreferrer\" target=\"_blank\">preparazione app</a> e <a href=\"https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/overview-of-publishing-your-app-on-the-app-store\" rel=\"noreferrer\" target=\"_blank\">App Store Connect</a>."
        ]
      ],
      [
        "5. Procedura fuori dal Mac App Store",
        [
          [
            "Firma l'app e i relativi eseguibili con certificato Developer ID appropriato, abilita Hardened Runtime e usa un timestamp valido.",
            "Invia il software alla notarizzazione con Xcode oppure notarytool; dopo l'esito positivo applica il ticket quando previsto e controlla l'apertura su un Mac pulito con Gatekeeper.",
            "Distribuisci un archivio o un installer idoneo (.dmg/.pkg, se compatibile) via HTTPS. Gestisci aggiornamenti firmati, rollback, revoca, licenze, pagamenti e assistenza."
          ],
          "La notarizzazione non è App Review: <a href=\"https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution\" rel=\"noreferrer\" target=\"_blank\">Apple: notarizzazione</a>."
        ]
      ],
      [
        "6. Vendite, commissioni e costi accessori",
        [
          [
            "Mac App Store: oltre ai 99 USD/anno, sulle vendite di app e acquisti digitali possono applicarsi commissioni secondo il programma e gli accordi scelti. Il Small Business Program prevede il 15% per gli sviluppatori idonei; non è una commissione universale.",
            "Distribuzione esterna: Apple non gestisce i tuoi incassi; valuta commissioni del provider, imposte, rimborsi, protezione licenze e costi di hosting e aggiornamento.",
            "Per vendere sullo Store, completa i contratti Paid Apps, dati fiscali e bancari in App Store Connect."
          ],
          "Fonti: <a href=\"https://developer.apple.com/app-store/small-business-program/\" rel=\"noreferrer\" target=\"_blank\">Small Business Program</a> e <a href=\"https://developer.apple.com/help/app-store-connect/get-started/app-store-connect-workflow\" rel=\"noreferrer\" target=\"_blank\">accordi fiscali e bancari</a>."
        ]
      ],
      [
        "7. Privacy, GDPR e conformità",
        [
          "Per app distribuite nel Mac App Store fornisci URL della privacy policy e risposte corrette nella sezione App Privacy, includendo SDK esterni; verifica inoltre requisiti su firma e privacy manifest degli SDK che li richiedono. Per i dati personali europei serve una base giuridica, una finalità, misure di sicurezza e una procedura di gestione dei diritti.",
          "Se vendi nell'UE, verifica lo status di operatore economico e gli obblighi DSA applicabili. Consulta la <a href=\"guida-pubblicare-app-gdpr-privacy.html\">checklist GDPR e adempimenti per le app</a> e <a href=\"https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy/\" rel=\"noreferrer\" target=\"_blank\">App Privacy di Apple</a>."
        ]
      ],
      [
        "8. Problemi comuni al rilascio",
        [
          [
            "App respinta per sandbox, entitlement non giustificati, funzioni incomplete, metadati errati o login non accessibile ai revisori.",
            "App esterna bloccata da Gatekeeper per firma, hardened runtime o notarizzazione non validi.",
            "Aggiornamenti che perdono dati utente o cambiano Bundle ID; updater non firmato o incompatibilità tra versioni macOS."
          ]
        ]
      ],
      [
        "9. Guide correlate",
        [
          "Per iPhone e iPad segui <a href=\"guida-pubblicare-app-ios.html\">la guida iOS</a>; per Windows segui <a href=\"guida-pubblicare-app-microsoft-store.html\">Microsoft Store</a>. Per pubblicazione commerciale, informative e trattamento dati: <a href=\"guida-pubblicare-app-gdpr-privacy.html\">checklist GDPR e adempimenti per le app</a>."
        ]
      ]
    ],
    "cta": "software-web.html",
    "contact": [
      "Devi pubblicare un'app per Mac?",
      "Indicaci linguaggio, framework, formato attuale, canale di vendita e permessi richiesti: definiamo firma, distribuzione e aggiornamenti."
    ],
    "published": "2026-11-12",
    "updated": "novembre 2026"
  },
  {
    "slug": "guida-pubblicare-app-android.html",
    "title": "Pubblicare un'app Android su Google Play: costi e GDPR | JDEVPRO",
    "short": "Pubblicare un'app Android su Google Play",
    "desc": "Play Console, costo 25 USD, AAB, test chiuso, Android 16 API 36, Data safety, account deletion, acquisti e GDPR.",
    "h1": "Google Play: <span>pubblicare un'app Android senza dimenticare test e privacy.</span>",
    "intro": "La pubblicazione su Google Play richiede una build Android conforme, un account verificato, una scheda completa, dichiarazioni privacy accurate e, per alcuni account personali, un periodo minimo di test chiuso. Preparare questi requisiti dall'inizio evita revisioni e rifiuti.",
    "sections": [
      [
        "1. Account Google Play Console",
        [
          "Accedi con un account Google, accetta il contratto di distribuzione, scegli il corretto profilo personale o organizzazione, completa le verifiche e paga la quota di registrazione <strong>25 USD una tantum</strong>. Non è un canone annuale: <a href=\"https://support.google.com/googleplay/android-developer/answer/6112435?hl=it\" rel=\"noreferrer\" target=\"_blank\">Google: registrazione Play Console</a>.",
          "Per l'account organizzazione verifica l'identità aziendale e la documentazione richiesta; configura metodi di contatto accessibili e un responsabile per le notifiche di policy."
        ]
      ],
      [
        "2. Crea il pacchetto Android",
        [
          [
            "Configura package name definitivo, versionCode, versionName, icona, adaptive icon, lingue e dispositivi supportati.",
            "Prepara una build release firmata in formato Android App Bundle (AAB) per i nuovi rilasci su Play, con chiave di upload e Play App Signing dove previsto; conserva in sicurezza le credenziali.",
            "Rimuovi debug, segreti dal client, librerie inutili e permessi superflui. Verifica che i servizi backend non espongano token nel pacchetto."
          ]
        ]
      ],
      [
        "3. Target API richiesto nel 2026",
        [
          "Dal <strong>31 agosto 2026</strong>, per le app standard smartphone/tablet nuove e aggiornate Google Play richiede <strong>Android 16, API 36 o superiore</strong>. Le regole per Wear OS, Automotive, TV e XR sono diverse; l'eventuale estensione a novembre va richiesta dove ammesso.",
          "Fonte: <a href=\"https://support.google.com/googleplay/android-developer/answer/11926878?hl=it\" rel=\"noreferrer\" target=\"_blank\">requisiti target API 2026</a>."
        ]
      ],
      [
        "4. Test interno e test chiuso obbligatorio per alcuni account",
        [
          "Per gli <strong>account personali creati dopo il 13 novembre 2023</strong>, prima dell'accesso alla produzione è richiesto un <strong>test chiuso con almeno 12 tester iscritti e attivi ininterrottamente per 14 giorni</strong>; poi si presenta richiesta di accesso alla produzione. Il test interno è utile ma non sostituisce questo requisito.",
          "Fonte: <a href=\"https://support.google.com/googleplay/android-developer/answer/14151465?hl=it\" rel=\"noreferrer\" target=\"_blank\">requisiti di test Google Play</a>."
        ]
      ],
      [
        "5. Scheda Google Play e invio",
        [
          [
            "Inserisci titolo, descrizioni, categoria, contatti, schermate autentiche, icona e informativa sulla privacy.",
            "Compila le sezioni su annunci, accesso all'app, pubblico di destinazione, classificazione dei contenuti, permessi e trattamento dati; fornisci credenziali di test per le funzioni con login.",
            "Carica AAB, crea una release su un canale di test, analizza i pre-launch report e invia la produzione quando l'account è abilitato."
          ]
        ]
      ],
      [
        "6. Data safety, privacy policy e cancellazione account",
        [
          "Ogni app su Google Play deve compilare accuratamente il modulo <strong>Data safety</strong> e rendere accessibile una privacy policy sia nella scheda sia nell'app. Le dichiarazioni includono i dati raccolti o condivisi dagli SDK di analytics, crash reporting, pubblicità e pagamento.",
          "Se l'app permette di creare un account, prevedi una procedura chiara di eliminazione dell'account e dei dati associati secondo le policy; considera le eccezioni di conservazione giustificate e descrivile. Fonte: <a href=\"https://support.google.com/googleplay/android-developer/answer/18265346\" rel=\"noreferrer\" target=\"_blank\">policy Google Play</a> e <a href=\"guida-pubblicare-app-gdpr-privacy.html\">checklist GDPR e adempimenti per le app</a>."
        ]
      ],
      [
        "7. Vendite, abbonamenti e commissioni",
        [
          "La quota di registrazione non include le commissioni sulle transazioni. Per acquisti digitali e funzionalità in-app si applicano le regole Google Play Billing con eccezioni e opzioni specifiche per mercato. Non dare per scontata una percentuale unica: le commissioni dipendono da categoria, paese e programma.",
          "Fonti: <a href=\"https://support.google.com/googleplay/android-developer/answer/9858738?hl=it\" rel=\"noreferrer\" target=\"_blank\">politica dei pagamenti</a> e <a href=\"https://support.google.com/googleplay/android-developer/answer/112622?hl=it\" rel=\"noreferrer\" target=\"_blank\">commissioni attuali</a>."
        ]
      ],
      [
        "8. Dati, GDPR e utenti europei",
        [
          [
            "Mappa accessi a posizione, fotocamera, contatti, notifiche e identificativi; richiedi permessi nel momento appropriato e spiegane il motivo.",
            "Distingui i dati necessari per eseguire il servizio da analytics e marketing; valuta base giuridica, tempi di conservazione, hosting, responsabili esterni e trasferimenti.",
            "Gestisci richieste di accesso/cancellazione, sicurezza delle API, cifratura, credenziali e incidenti. L'informativa deve rispecchiare comportamento reale e Data safety."
          ],
          "Consulta la <a href=\"guida-pubblicare-app-gdpr-privacy.html\">checklist GDPR e adempimenti per le app</a>."
        ]
      ],
      [
        "9. Distribuzione al di fuori di Google Play",
        [
          "La distribuzione tramite APK o store alternativi cambia responsabilità di firma, aggiornamenti, installazione, pagamenti e sicurezza. Non elimina gli obblighi GDPR né quelli contrattuali verso gli utenti. Verifica politiche e condizioni del canale scelto, oltre all'affidabilità della distribuzione."
        ]
      ],
      [
        "10. Checklist dopo il lancio",
        [
          [
            "Conserva chiave di upload, configurazione build e pipeline di rilascio; monitora ANR, crash, recensioni e segnalazioni Play Console.",
            "Aggiorna dipendenze, target SDK e dichiarazioni Data safety quando cambiano funzionalità o SDK.",
            "Verifica l'eliminazione account, il supporto, le sottoscrizioni, i rimborsi e la gestione delle richieste privacy."
          ]
        ]
      ],
      [
        "11. Guide correlate",
        [
          "Consulta <a href=\"guida-pubblicare-app-ios.html\">iOS</a>, <a href=\"guida-pubblicare-app-microsoft-store.html\">Microsoft Store</a>, <a href=\"guida-pubblicare-app-macos.html\">macOS</a> e la <a href=\"guida-pubblicare-app-gdpr-privacy.html\">checklist GDPR e adempimenti per le app</a>."
        ]
      ]
    ],
    "cta": "software-web.html",
    "contact": [
      "Stai preparando un'app Android?",
      "Indicaci framework, stato della build, account Play Console, funzioni e dati raccolti: definiamo test, distribuzione e pubblicazione."
    ],
    "published": "2026-11-12",
    "updated": "novembre 2026"
  },
  {
    "slug": "guida-pubblicare-app-ios.html",
    "title": "Pubblicare un'app iOS su App Store: costi e GDPR | JDEVPRO",
    "short": "Pubblicare un'app iOS su App Store",
    "desc": "Apple Developer Program, Xcode, TestFlight, App Store Connect, App Privacy, ATT, DSA, pagamenti e GDPR per distribuire iPhone e iPad.",
    "h1": "App Store iOS: <span>dall'account Apple alla pubblicazione.</span>",
    "intro": "Per distribuire su iPhone e iPad bisogna preparare il progetto e la firma, gestire App Store Connect, effettuare i test, documentare privacy e dati raccolti, definire il modello commerciale e superare App Review.",
    "sections": [
      [
        "1. Apri l'account Apple Developer",
        [
          "L'<strong>Apple Developer Program costa 99 USD all'anno</strong> (o importo in valuta locale visualizzato all'iscrizione). Consente la distribuzione tramite App Store e l'accesso a TestFlight e alle risorse necessarie. Un singolo abbonamento copre anche lo sviluppo/distribuzione macOS.",
          "Individui e organizzazioni hanno verifiche differenti e denominazioni pubbliche diverse. Fonte: <a href=\"https://developer.apple.com/help/account/membership/program-enrollment\" rel=\"noreferrer\" target=\"_blank\">Apple Developer: iscrizione e costi</a>."
        ]
      ],
      [
        "2. Identifica e firma l'app",
        [
          [
            "Definisci Bundle ID definitivo, versione, build number, team, provisioning e certificati di firma gestiti da Xcode.",
            "Configura capability effettivamente necessarie: notifiche push, Keychain, Sign in with Apple quando applicabile, fotocamera, posizione, Bluetooth e servizi esterni.",
            "Prepara l'archivio release con una versione di Xcode/SDK ammessa al momento dell'invio, testa su dispositivi reali e carica la build su App Store Connect."
          ]
        ]
      ],
      [
        "3. TestFlight e prerequisiti per la revisione",
        [
          "Usa TestFlight per beta interne o esterne, raccogli feedback e correggi blocchi. Prepara credenziali demo funzionanti se l'app richiede login, istruzioni per il revisore e accesso ai servizi esterni indispensabili.",
          "Fonte: <a href=\"https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review\" rel=\"noreferrer\" target=\"_blank\">informazioni richieste per App Review</a>."
        ]
      ],
      [
        "4. Crea la scheda App Store Connect",
        [
          [
            "Inserisci nome, sottotitolo, categoria, parole chiave, descrizione, screenshot reali, support URL, privacy policy URL e classificazione per età.",
            "Completa informazioni sul copyright, disponibilità geografica, prezzo, eventuali acquisti in-app e dichiarazioni richieste per la crittografia.",
            "Seleziona la build, rispondi alle domande della revisione, invia e programma la pubblicazione automatica, manuale o graduale."
          ],
          "Fonte: <a href=\"https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/overview-of-publishing-your-app-on-the-app-store\" rel=\"noreferrer\" target=\"_blank\">Apple: pubblicazione</a>."
        ]
      ],
      [
        "5. App Privacy, SDK e tracking",
        [
          "La privacy policy deve essere accessibile nello Store e nell'app. Nella sezione <strong>App Privacy</strong> dichiara i dati raccolti da te e dagli SDK integrati, la finalità d'uso e l'eventuale collegamento all'identità dell'utente. Alcuni SDK richiedono un privacy manifest e firma.",
          "Se effettui tracciamento tra app/siti di altre aziende, valuta l'obbligo di richiesta tramite <strong>App Tracking Transparency</strong>, oltre agli obblighi di protezione dati applicabili. Fonti: <a href=\"https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy/\" rel=\"noreferrer\" target=\"_blank\">App Privacy</a>, <a href=\"https://developer.apple.com/support/third-party-SDK-requirements/\" rel=\"noreferrer\" target=\"_blank\">SDK di terzi</a> e <a href=\"https://developer.apple.com/documentation/apptrackingtransparency\" rel=\"noreferrer\" target=\"_blank\">ATT</a>."
        ]
      ],
      [
        "6. Accessi, account e cancellazione",
        [
          [
            "Se offri creazione account, esamina i requisiti Apple sulla cancellazione dall'app e realizza la procedura in modo funzionante.",
            "Progetta password e token sicuri, sessioni, account demo per review, autorizzazioni, backup e cancellazione dei dati compatibile con obblighi di conservazione.",
            "Per utenti UE, predisponi canali per l'esercizio dei diritti GDPR, tempi di conservazione e identificazione del titolare del trattamento."
          ],
          "Approfondisci nella <a href=\"guida-pubblicare-app-gdpr-privacy.html\">checklist GDPR e adempimenti per le app</a>."
        ]
      ],
      [
        "7. Pagamenti, abbonamenti e costi",
        [
          "Per vendere app o contenuti digitali tramite i canali Apple, controlla le regole su In-App Purchase, abbonamenti, link esterni e modalità alternative applicabili alla regione. Per i prodotti a pagamento servono Paid Apps Agreement e informazioni fiscali/bancarie.",
          "Il <strong>Small Business Program</strong> prevede una commissione ridotta del 15% per gli sviluppatori idonei; non assumere che valga in ogni situazione né che sia l'unico costo. Fonti: <a href=\"https://developer.apple.com/app-store/small-business-program/\" rel=\"noreferrer\" target=\"_blank\">programma piccole imprese</a> e <a href=\"https://developer.apple.com/help/app-store-connect/get-started/app-store-connect-workflow\" rel=\"noreferrer\" target=\"_blank\">accordi commerciali</a>."
        ]
      ],
      [
        "8. DSA, UE e distribuzione alternativa",
        [
          "Se distribuisci nell'UE, App Store Connect richiede la dichiarazione dello status di <strong>trader</strong> secondo il Digital Services Act; per operatori economici Apple verifica e pubblica i contatti previsti.",
          "Nell'UE esistono anche canali alternativi (marketplace e, a determinate condizioni, distribuzione web), soggetti a requisiti e condizioni commerciali specifici. Non equivalgono a caricare liberamente un file IPA sul proprio sito.",
          "Fonti: <a href=\"https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements\" rel=\"noreferrer\" target=\"_blank\">DSA Apple</a> e <a href=\"https://developer.apple.com/documentation/marketplacekit/participating-in-alternative-distribution-for-specific-regions\" rel=\"noreferrer\" target=\"_blank\">distribuzione alternativa UE</a>."
        ]
      ],
      [
        "9. Esportazione della crittografia e altre dichiarazioni",
        [
          "App Store Connect richiede di determinare la conformità all'esportazione per l'uso della crittografia, anche quando si utilizzano funzionalità standard del sistema. Rispondi al questionario ufficiale e fornisci la documentazione quando dovuta.",
          "Fonte: <a href=\"https://developer.apple.com/help/app-store-connect/manage-app-information/overview-of-export-compliance/\" rel=\"noreferrer\" target=\"_blank\">Apple: export compliance</a>."
        ]
      ],
      [
        "10. Collaudi e manutenzione dopo il rilascio",
        [
          [
            "Prova aggiornamenti, modalità offline, errori server, accessi negati, pagamenti, rinnovi, ripristino, migrazioni e compatibilità tra versioni iOS.",
            "Monitora crash, recensioni e segnalazioni App Review, mantieni SDK e dipendenze aggiornati e rivedi le dichiarazioni privacy a ogni nuova funzionalità.",
            "Organizza supporto e risposta agli incidenti, archivia le build e definisci chi gestisce i certificati e il rinnovo annuale dell'account."
          ]
        ]
      ],
      [
        "11. Guide correlate",
        [
          "Per desktop Apple segui <a href=\"guida-pubblicare-app-macos.html\">macOS</a>; per Android <a href=\"guida-pubblicare-app-android.html\">Google Play</a>. Per GDPR, dati e obblighi commerciali, leggi la <a href=\"guida-pubblicare-app-gdpr-privacy.html\">checklist GDPR e adempimenti per le app</a>."
        ]
      ]
    ],
    "cta": "software-web.html",
    "contact": [
      "Vuoi portare la tua applicazione su iOS?",
      "Indica tecnologia, funzionalità, accesso utenti, pagamenti e dati raccolti: pianifichiamo la pubblicazione e le verifiche."
    ],
    "published": "2026-11-12",
    "updated": "novembre 2026"
  },
  {
    "slug": "guida-pubblicare-app-gdpr-privacy.html",
    "title": "Pubblicare un'app: checklist GDPR, privacy e obblighi UE | JDEVPRO",
    "short": "Checklist GDPR e privacy per pubblicare un'app",
    "desc": "Dati personali, privacy policy, basi giuridiche, SDK, consenso, sicurezza, DPA, cancellazione account, DSA, pagamenti e obblighi per app Windows, Mac, Android e iOS.",
    "h1": "Pubblicare un'app: <span>GDPR, dati, sicurezza e obblighi da verificare.</span>",
    "intro": "Una scheda sullo store non rende automaticamente conforme un'app. Prima del lancio devi sapere quali dati tratta il software, chi ne è responsabile, quali servizi terzi li ricevono, come esercitare i diritti e come prevenire incidenti. Questa checklist si applica a desktop e mobile, con integrazioni specifiche per ciascuno store.",
    "sections": [
      [
        "1. Mappa davvero i dati trattati",
        [
          [
            "Elenca dati di registrazione, email, pagamenti, geolocalizzazione, contatti, file caricati, messaggi, log server, indirizzi IP, identificativi pubblicitari, notifiche e crash report.",
            "Per ogni elemento annota raccolta, finalità, base giuridica, destinazione, accessi, terzi, tempi di conservazione e cancellazione. Considera anche dati raccolti dagli SDK integrati.",
            "Individua quali dati sono indispensabili, quali opzionali e quali possono essere eliminati o resi anonimi. Evita dati di test reali in ambienti di sviluppo."
          ],
          "Riferimento: <a href=\"https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations_en\" rel=\"noreferrer\" target=\"_blank\">Commissione europea: GDPR per imprese</a>."
        ]
      ],
      [
        "2. Titolare, responsabili e accordi",
        [
          "Stabilisci chi decide finalità e mezzi del trattamento (titolare) e chi tratta dati per suo conto (responsabile), per esempio alcuni provider di hosting, servizi di email, monitoraggio o assistenza. Quando richiesto dal GDPR, stipula contratti di nomina/accordi art. 28.",
          "Se operi per clienti aziendali, chiarisci ruoli e responsabilità contrattuali: non sono automaticamente gli stessi per tutte le funzioni del software."
        ]
      ],
      [
        "3. Basi giuridiche, finalità e consenso",
        [
          "Per ciascuna finalità individua una base giuridica appropriata (per esempio esecuzione del contratto, obbligo legale, legittimo interesse dopo valutazione, oppure consenso dove richiesto). <strong>Il consenso non è la base obbligatoria per qualunque dato</strong>, né la semplice accettazione dei termini sostituisce un consenso valido.",
          "Per tracker, tecnologie di marketing e accesso a informazioni sul dispositivo valgono anche le regole ePrivacy applicabili; su iOS il tracking cross-app soggetto alle regole Apple richiede inoltre ATT. Gestisci revoca e preferenze quando necessarie."
        ]
      ],
      [
        "4. Informativa privacy: cosa deve dire",
        [
          [
            "Identità e contatti del titolare, eventuale DPO, finalità e basi giuridiche.",
            "Categorie di dati, destinatari e fornitori, trasferimenti fuori SEE e garanzie applicate.",
            "Tempi di conservazione o criteri per determinarli, diritti, modalità di esercizio, reclamo all'autorità e informazioni ulteriori previste dagli artt. 13-14 GDPR.",
            "Informazioni coerenti con ciò che l'app e gli SDK raccolgono davvero; link raggiungibile sia dall'app sia dalle pagine di distribuzione quando richiesto."
          ],
          "La privacy policy non è il documento dei termini d'uso: sono documenti con scopi distinti."
        ]
      ],
      [
        "5. Hosting, fornitori e trasferimenti internazionali",
        [
          "Inventaria provider cloud, CDN, notifiche push, piattaforme analytics e pagamenti. Controlla paesi di trattamento, sub-responsabili, accessi amministrativi e condizioni contrattuali. Se i dati escono dallo SEE, valuta la base di trasferimento e le garanzie richieste (ad esempio decisione di adeguatezza o clausole contrattuali standard quando appropriate).",
          "La localizzazione di un server in Europa, da sola, non chiude tutte le verifiche."
        ]
      ],
      [
        "6. Sicurezza e privacy by design",
        [
          [
            "Cifra i dati in transito (TLS) e quelli archiviati quando appropriato; proteggi chiavi e token nei sistemi server, non nel codice dell'app.",
            "Applica ruoli e autorizzazioni lato server, MFA agli amministratori, minimo privilegio, log di sicurezza, gestione delle dipendenze e test di vulnerabilità.",
            "Prepara backup verificati e procedure di ripristino; separa sviluppo, test e produzione; stabilisci retention dei log e protocolli di incidente.",
            "Valuta una DPIA quando il trattamento comporta probabilmente un rischio elevato per diritti e libertà; nomina un DPO nei casi in cui la legge lo richiede."
          ]
        ]
      ],
      [
        "7. Diritti, eliminazione account e retention",
        [
          "Implementa procedure per accesso, rettifica, portabilità dove applicabile, opposizione, limitazione e cancellazione. Distingui eliminazione dell'account, cancellazione dei dati associati e dati da conservare per obblighi legali documentati; spiega criteri e tempi all'utente.",
          "Google Play e App Store prevedono anche requisiti propri per le app che consentono la creazione di account. Una disattivazione senza cancellazione non soddisfa automaticamente tali requisiti."
        ]
      ],
      [
        "8. Violazioni dei dati e gestione degli incidenti",
        [
          "Definisci processo di detection, contenimento, analisi, ripristino e registrazione dell'incidente. Quando una violazione di dati presenta un rischio per i diritti delle persone, il titolare deve notificare l'autorità competente senza ingiustificato ritardo e, ove possibile, entro <strong>72 ore</strong> dalla conoscenza; in presenza di rischio elevato possono esservi obblighi di comunicazione agli interessati.",
          "Fonte: <a href=\"https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/obligations/what-data-breach-and-what-do-we-have-do-case-data-breach_it\" rel=\"noreferrer\" target=\"_blank\">Commissione europea: data breach</a>."
        ]
      ],
      [
        "9. Store, età, pubblicità e dati dichiarati",
        [
          [
            "Google Play: Data safety, privacy policy, dichiarazione dei permessi, target utenti, pubblicità e eliminazione account.",
            "App Store: App Privacy, privacy manifest degli SDK dove richiesto, eventuale ATT, classificazione per età e dati per la revisione.",
            "Microsoft Store: classificazione, descrizione, contatti, metadati e dichiarazioni veritiere.",
            "Se l'app è rivolta a minori o tratta dati sensibili, applica verifiche specifiche e non usare impostazioni pensate per utenti adulti senza valutarle."
          ]
        ]
      ],
      [
        "10. Vendita, DSA, consumatori e fiscalità",
        [
          "Prima di vendere definisci chi è il venditore, prezzi e imposte, termini di servizio o licenza d'uso, fatturazione, abbonamenti, disdette, rimborsi e assistenza. Per vendite a consumatori verifica le regole UE sui servizi/contenuti digitali e diritto di recesso, comprese eventuali eccezioni.",
          "Per app commerciali distribuite nell'UE verifica gli obblighi di identificazione dell'operatore economico (DSA e regole dello store) e la pubblicazione dei contatti. Requisiti fiscali, IVA e modalità di incasso dipendono dal contratto e dal ruolo di merchant of record; valuta con il commercialista."
        ]
      ],
      [
        "11. Accessibilità, licenze e proprietà intellettuale",
        [
          "Verifica se al servizio si applicano requisiti di accessibilità, inclusa la normativa UE rilevante; prova tastiera, screen reader, contrasto, controlli e lingua. Verifica licenze dei componenti open source, diritti su font, immagini, musiche e contenuti, marchi e licenze di eventuali API o SDK.",
          "Controlla eventuali requisiti settoriali per salute, finanza, geolocalizzazione, lavoro, identificazione e utenti minorenni: non esiste un'unica checklist legale sufficiente per ogni app."
        ]
      ],
      [
        "12. Checklist finale prima di premere Pubblica",
        [
          [
            "La build è firmata, testata, riproducibile e distribuita tramite il canale corretto.",
            "L'informativa, i termini, i contatti e la scheda dello Store corrispondono alle funzionalità reali.",
            "Basi giuridiche, eventuali consensi, contratti con fornitori, tempi di conservazione e canali per i diritti sono definiti.",
            "Gestione account, cancellazione, backup, sicurezza, incidenti e aggiornamenti sono collaudati.",
            "Commissioni, imposte, pagamenti, rimborsi, supporto e obblighi UE sono stati esaminati."
          ],
          "Questa checklist è informativa: nei casi concreti privacy, contratti e fiscalità richiedono verifiche specialistiche."
        ]
      ],
      [
        "13. Guide per piattaforma",
        [
          "Segui i requisiti specifici per <a href=\"guida-pubblicare-app-microsoft-store.html\">Microsoft Store</a>, <a href=\"guida-pubblicare-app-macos.html\">macOS</a>, <a href=\"guida-pubblicare-app-android.html\">Android / Google Play</a> e <a href=\"guida-pubblicare-app-ios.html\">iOS / App Store</a>."
        ]
      ]
    ],
    "cta": "software-web.html",
    "contact": [
      "Hai un'app pronta da distribuire?",
      "Indica piattaforma, account, strumenti esterni e tipi di dati trattati. Ti aiutiamo a definire il percorso tecnico di pubblicazione, da coordinare con i consulenti privacy e fiscali."
    ],
    "published": "2026-11-12",
    "updated": "novembre 2026"
  }
]
