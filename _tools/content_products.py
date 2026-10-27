"""Pagine dedicate ai prodotti: AKIOS e ORYVAEL (italiano e inglese).

Blocchi: ("cards", eyebrow, h2, intro, [(titolo, testo)]), ("flow", eyebrow, h2, [(titolo, testo)]),
("split", eyebrow, h2, [paragrafi], [punti]), ("compare", eyebrow, h2, (titolo, [voci]), (titolo, [voci])),
("status", eyebrow, h2, [voci], nota)
"""

PRODUCTS = {
  "it": [
    dict(
      key="akios", slug="akios.html", nav="AKIOS",
      title="AKIOS: aggiornamenti sicuri e ripristino per dispositivi IoT | JDEVPRO",
      desc="AKIOS governa il ciclo di vita dei dispositivi IoT: aggiornamenti firmati in prova, ritorno automatico e ripristino locale. Per produttori europei e CRA.",
      card="Aggiornamenti firmati, ritorno automatico e ripristino locale per i dispositivi IoT dei produttori europei.",
      eyebrow="Prodotto · Firmware e ciclo di vita IoT",
      h1="AKIOS: dispositivi IoT che si aggiornano <span>senza rompersi.</span>",
      lead="AKIOS è uno strato che vive dentro il dispositivo e ne governa tutto il ciclo di vita: prima configurazione, aggiornamenti, ritorno all'ultima versione buona e ripristino. Per i produttori europei che devono garantire aggiornamenti sicuri per anni, senza cambiare cloud.",
      links=[("Sito AKIOS ↗", "https://akios.cloud/"), ("Programma pilota ↗", "https://akios-pilot.com/")],
      blocks=[
        ("cards", "Il problema", "Ogni linea di prodotto rifà da capo le stesse cose.", "Quando i dispositivi crescono per modelli e chip, gli errori nel ciclo di vita smettono di essere problemi tecnici isolati e diventano costi di assistenza e rischio sul campo.", [
          ("Firmware diversi per ogni chip", "Varianti, regressioni e comportamenti diversi da mantenere per anni."),
          ("Aggiornamenti rischiosi", "Un aggiornamento fallito può bloccare il dispositivo: assistenza, resi, clienti persi."),
          ("Configurazione fragile", "La prima configurazione fallisce sul campo e nessuno sa perché."),
          ("Obblighi in arrivo", "Il Cyber Resilience Act europeo chiede aggiornamenti di sicurezza per tutto il periodo di supporto e prove documentate."),
        ]),
        ("flow", "Come funziona", "Prova, conferma, ritorno, ripristino.", [
          ("Aggiornamento firmato", "Ogni versione è verificata con firma digitale (ECDSA P-256) e impronta SHA-256 prima di essere accettata."),
          ("Prova controllata", "Il nuovo sistema parte in uno spazio separato: l'ultima versione buona resta intatta."),
          ("Conferma o ritorno", "Viene confermato solo se i controlli di salute passano; altrimenti il dispositivo torna da solo alla versione buona."),
          ("Ripristino locale", "Se non resta un sistema valido, il dispositivo apre una rete Wi-Fi protetta e si recupera dal telefono."),
        ]),
        ("split", "Il principio", "Ogni aggiornamento lascia sempre una via di ripristino.", [
          "Un aggiornamento non può mai sovrascrivere insieme il BIOS AKIOS e l'ultimo sistema confermato. Caricamenti interrotti, firme non valide, versioni corrotte o prove fallite non possono sostituire il sistema buono.",
          "Il BIOS AKIOS si occupa della sopravvivenza del dispositivo; il sistema, con la logica di prodotto e i collegamenti al cloud, è sostituibile e firmato separatamente.",
        ], ["Due spazi separati per il sistema (A/B)", "Dati di stato ridondanti", "Controllo di salute dopo ogni aggiornamento", "Rete di ripristino locale protetta", "Nessun cloud obbligato: il vostro resta"]),
        ("cards", "Per chi", "Pensato per i produttori, non per il singolo progetto.", "", [
          ("Produttori europei con più linee di prodotto", "O che stanno per allargare la gamma."),
          ("Più chip e varianti firmware", "Con il rischio ricorrente di aggiornamenti falliti sul campo."),
          ("Supporto lungo e normative", "Periodi di assistenza più lunghi e pressione di CRA ed ETSI."),
          ("Chi vuole tenere il proprio cloud", "AKIOS governa il dispositivo; app, cloud e clienti restano vostri."),
        ]),
        ("status", "Stato", "Già funzionante su hardware reale.", [
          "Firmware nativo operativo sui chip Beken BK7238, molto diffusi nei dispositivi Wi-Fi",
          "Prima configurazione e ripristino locale dimostrati",
          "Aggiornamento in prova e ritorno automatico dimostrati, anche con guasti forzati",
          "Integrazione con il cloud mostrata in dimostrazione",
          "Dimostrazioni dal vivo su hardware disponibili sotto NDA",
        ], "Matrici di compatibilità e dettagli tecnici completi sono condivisi sotto NDA."),
        ("flow", "Programma pilota", "Un dispositivo, un perimetro chiaro.", [
          ("Scelta del dispositivo", "Si parte dal modello più importante per voi."),
          ("Confine definito", "Cosa governa AKIOS e cosa resta al vostro cloud e alla vostra app."),
          ("Integrazione e prove", "Configurazione, aggiornamenti, ritorno e ripristino provati con guasti forzati."),
          ("Prove documentate", "Report di validazione e registri da usare con clienti e verifiche."),
        ]),
      ],
    ),
    dict(
      key="oryvael", slug="oryvael.html", nav="ORYVAEL",
      title="ORYVAEL: sistema operativo per l'intelligenza artificiale | JDEVPRO",
      desc="ORYVAEL è un sistema operativo in Rust dove l'AI progetta, scrive e mantiene software, ma l'autorità resta alle persone. Ricerca di Jacopo Ellero.",
      card="Un sistema operativo in Rust dove l'intelligenza artificiale lavora, ma l'autorità resta alle persone.",
      eyebrow="Ricerca · Sistema operativo per l'intelligenza artificiale",
      h1="ORYVAEL: l'intelligenza artificiale lavora, <span>le persone comandano.</span>",
      lead="ORYVAEL è un sistema operativo pensato per l'intelligenza artificiale: l'AI può progettare, scrivere, provare, integrare e mantenere software, ma l'autorità resta sempre, in modo esplicito, nelle mani delle persone.",
      links=[("Sito ORYVAEL ↗", "https://jellero.github.io/ORYVAEL-web/"), ("Codice su GitHub ↗", "https://github.com/jellero/ORYVAEL")],
      blocks=[
        ("split", "L'idea", "Separare l'intelligenza dall'autorità.", [
          "ORYVAEL non presume che un'intelligenza artificiale diventi abbastanza affidabile da ricevere accesso illimitato. Presume il contrario: i componenti AI sono potenti ma non fidati.",
          "Ogni loro azione deve essere limitata, osservabile, attribuibile, riproducibile e reversibile. Nessun modello AI fa parte della radice di fiducia del sistema.",
        ], ["Limitata", "Osservabile", "Attribuibile", "Riproducibile", "Reversibile"]),
        ("compare", "Confini", "Cosa può fare l'AI, e cosa no.",
         ("L'AI può", ["analizzare requisiti e proporre architetture", "scrivere codice e test", "eseguire build e analisi di sicurezza", "preparare rilasci", "diagnosticare guasti e proporre correzioni"]),
         ("L'AI non può", ["darsi permessi da sola", "cambiare le regole di base del sistema", "toccare la radice di fiducia", "disattivare il registro delle azioni", "saltare le verifiche obbligatorie", "firmare rilasci privilegiati o allargare il proprio raggio d'azione"])),
        ("flow", "Ogni modifica", "Chi scrive il codice non può approvarlo.", [
          ("Intenzione umana", "Una persona definisce cosa serve e approva il piano."),
          ("Permesso limitato", "L'AI riceve solo i permessi necessari a quel compito."),
          ("Implementazione", "L'AI scrive e prova la modifica nel suo spazio isolato."),
          ("Verifica indipendente", "Controlli separati producono le prove della modifica."),
          ("Rilascio graduale", "Regole deterministiche decidono; il rilascio avanza per gradi."),
          ("Registro firmato", "Ogni passaggio resta tracciato e verificabile."),
        ]),
        ("cards", "Profili", "Stesso modello di fiducia, dispositivi diversi.", "", [
          ("Desktop", "Spazi di lavoro isolati, agenti AI locali, permessi espliciti; x86-64 e ARM64."),
          ("Mobile", "ARM64, consumi ridotti, identità su elemento sicuro, stesse regole del desktop."),
          ("Embedded ed edge", "IoT, robotica e gateway: permessi applicati sul dispositivo, aggiornamenti firmati e ritorno, Rust per microcontrollori."),
        ]),
        ("status", "Stato", "Le fondamenta girano già sull'hardware.", [
          "Kernel in Rust che parte direttamente da UEFI su x86-64, senza Linux sotto",
          "Gestione propria di memoria, processi utente, timer e chiamate di sistema",
          "Rete nativa: DHCP, DNS, ping e TCP",
          "Accesso remoto SSH solo con chiavi Ed25519; password e root disabilitati",
          "Grafica nativa e verifica automatica di build e avvio a ogni modifica",
        ], "Non è ancora un sistema operativo di produzione e non contiene ancora un motore AI nativo: è ricerca in corso, documentata e verificabile."),
        ("split", "Perché conta", "Lo stesso principio, nei sistemi dei clienti.", [
          "ORYVAEL è ricerca, ma il principio guida ogni sistema che realizziamo: automazione sì, con permessi minimi, storico di ogni azione e possibilità di tornare indietro.",
        ], ["Permessi minimi", "Storico di ogni azione", "Verifiche indipendenti", "Ritorno alla versione precedente"]),
      ],
    ),
  ],
  "en": [
    dict(
      key="akios", slug="en-akios.html", nav="AKIOS",
      title="AKIOS: secure updates and recovery for IoT devices | JDEVPRO",
      desc="AKIOS governs the IoT device lifecycle: signed trial updates, automatic rollback and local recovery. For European manufacturers facing the CRA.",
      card="Signed updates, automatic rollback and local recovery for European manufacturers' IoT devices.",
      eyebrow="Product · IoT firmware and lifecycle",
      h1="AKIOS: IoT devices that update <span>without breaking.</span>",
      lead="AKIOS is a layer living inside the device that governs its whole lifecycle: first setup, updates, rollback to the last good version and recovery. For European manufacturers who must guarantee secure updates for years, without changing cloud.",
      links=[("AKIOS website ↗", "https://akios.cloud/"), ("Pilot programme ↗", "https://akios-pilot.com/")],
      blocks=[
        ("cards", "The problem", "Every product line rebuilds the same things.", "As devices grow across models and chips, lifecycle failures stop being isolated engineering issues and become support cost and field risk.", [
          ("Different firmware per chip", "Variants, regressions and inconsistent behaviour to maintain for years."),
          ("Risky updates", "A failed update can brick the device: support, returns, lost customers."),
          ("Fragile setup", "First setup fails in the field and nobody knows why."),
          ("New obligations", "The EU Cyber Resilience Act requires security updates for the whole support period and documented evidence."),
        ]),
        ("flow", "How it works", "Trial, commit, rollback, recovery.", [
          ("Signed update", "Every version is verified with a digital signature (ECDSA P-256) and SHA-256 hash before being accepted."),
          ("Controlled trial", "The new system starts in a separate slot: the last good version stays intact."),
          ("Commit or rollback", "It is committed only if health checks pass; otherwise the device rolls back by itself."),
          ("Local recovery", "If no valid system is left, the device opens a protected Wi-Fi network and is restored from a phone."),
        ]),
        ("split", "The principle", "Every update always leaves a way back.", [
          "An update can never overwrite both the AKIOS BIOS and the last committed system. Interrupted uploads, invalid signatures, corrupted versions or failed trials cannot replace the good system.",
          "The AKIOS BIOS takes care of device survival; the system, with product logic and cloud connections, is replaceable and signed separately.",
        ], ["Two separate system slots (A/B)", "Redundant state data", "Health check after every update", "Protected local recovery network", "No forced cloud: yours stays"]),
        ("cards", "Who it is for", "Built for manufacturers, not single projects.", "", [
          ("European makers with several product lines", "Or about to expand their range."),
          ("Several chips and firmware variants", "With recurring risk of failed field updates."),
          ("Long support and regulation", "Longer support windows and CRA and ETSI pressure."),
          ("Teams keeping their own cloud", "AKIOS governs the device; app, cloud and customers stay yours."),
        ]),
        ("status", "Status", "Already running on real hardware.", [
          "Native firmware running on Beken BK7238 chips, widely used in Wi-Fi devices",
          "First setup and local recovery demonstrated",
          "Trial update and automatic rollback demonstrated, including forced failures",
          "Cloud integration shown in demo",
          "Live hardware demos available under NDA",
        ], "Compatibility matrices and full technical details are shared under NDA."),
        ("flow", "Pilot programme", "One device, one clear scope.", [
          ("Choose the device", "We start from the model that matters most to you."),
          ("Defined boundary", "What AKIOS governs and what stays with your cloud and app."),
          ("Integration and tests", "Setup, updates, rollback and recovery tested with forced failures."),
          ("Documented evidence", "Validation reports and logs for customers and audits."),
        ]),
      ],
    ),
    dict(
      key="oryvael", slug="en-oryvael.html", nav="ORYVAEL",
      title="ORYVAEL: an AI-native operating system | JDEVPRO",
      desc="ORYVAEL is a Rust operating system where AI designs, writes and maintains software while authority stays with people. Research by Jacopo Ellero.",
      card="A Rust operating system where AI does the work while authority stays with people.",
      eyebrow="Research · AI-native operating system",
      h1="ORYVAEL: AI does the work, <span>people stay in charge.</span>",
      lead="ORYVAEL is an AI-native operating system: AI can design, write, test, integrate and maintain software, while authority always remains explicitly with people.",
      links=[("ORYVAEL website ↗", "https://jellero.github.io/ORYVAEL-web/"), ("Code on GitHub ↗", "https://github.com/jellero/ORYVAEL")],
      blocks=[
        ("split", "The idea", "Separate intelligence from authority.", [
          "ORYVAEL does not assume that an AI becomes trustworthy enough to receive unrestricted access. It assumes the opposite: AI components are powerful but untrusted.",
          "Every action must be scoped, observable, attributable, reproducible and reversible. No AI model belongs to the system's root of trust.",
        ], ["Scoped", "Observable", "Attributable", "Reproducible", "Reversible"]),
        ("compare", "Boundaries", "What AI can do, and what it cannot.",
         ("AI can", ["analyse requirements and propose architecture", "write code and tests", "run builds and security analysis", "prepare releases", "diagnose failures and propose fixes"]),
         ("AI cannot", ["grant itself permissions", "change the system's core rules", "touch the root of trust", "disable the audit log", "skip mandatory verification", "sign privileged releases or expand its own scope"])),
        ("flow", "Every change", "Whoever writes the code cannot approve it.", [
          ("Human intent", "A person defines the need and approves the plan."),
          ("Scoped permission", "The AI receives only the permissions that task needs."),
          ("Implementation", "The AI writes and tests the change in its isolated space."),
          ("Independent verification", "Separate checks produce evidence for the change."),
          ("Staged rollout", "Deterministic rules decide; release advances in stages."),
          ("Signed record", "Every step stays traced and verifiable."),
        ]),
        ("cards", "Profiles", "Same trust model, different devices.", "", [
          ("Desktop", "Isolated workspaces, local AI agents, explicit permissions; x86-64 and ARM64."),
          ("Mobile", "ARM64, low power, secure-element identity, same rules as desktop."),
          ("Embedded and edge", "IoT, robotics and gateways: on-device permission enforcement, signed updates and rollback, Rust for microcontrollers."),
        ]),
        ("status", "Status", "The foundations already run on hardware.", [
          "Rust kernel booting directly from UEFI on x86-64, with no Linux underneath",
          "Its own memory management, user processes, timer and system calls",
          "Native networking: DHCP, DNS, ping and TCP",
          "SSH remote access with Ed25519 keys only; passwords and root disabled",
          "Native graphics and automatic build and boot verification on every change",
        ], "It is not yet a production operating system and does not yet include a native AI engine: it is ongoing, documented and verifiable research."),
        ("split", "Why it matters", "The same principle, in clients' systems.", [
          "ORYVAEL is research, but its principle guides every system we build: automation yes, with least privilege, a history of every action and the ability to roll back.",
        ], ["Least privilege", "History of every action", "Independent checks", "Rollback to the previous version"]),
      ],
    ),
  ],
}
