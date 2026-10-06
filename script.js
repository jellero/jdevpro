(() => {
  const ready = (fn) => document.readyState === 'loading'
    ? document.addEventListener('DOMContentLoaded', fn, { once: true })
    : fn();

  ready(() => {
    const header = document.querySelector('[data-header]');
    const menuToggle = document.querySelector('[data-menu-toggle]');
    const nav = document.querySelector('[data-nav]');
    const year = document.querySelector('[data-year]');

    if (year) year.textContent = new Date().getFullYear();

    const syncHeader = () => {
      if (header) header.classList.toggle('scrolled', window.scrollY > 24);
    };
    syncHeader();
    window.addEventListener('scroll', syncHeader, { passive: true });

    if (menuToggle && nav) {
      menuToggle.addEventListener('click', () => {
        const open = nav.classList.toggle('open');
        menuToggle.setAttribute('aria-expanded', String(open));
      });

      nav.querySelectorAll('a').forEach((link) => {
        link.addEventListener('click', () => {
          nav.classList.remove('open');
          menuToggle.setAttribute('aria-expanded', 'false');
        });
      });
    }

    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const items = document.querySelectorAll('.reveal');

    if (prefersReducedMotion || !('IntersectionObserver' in window)) {
      items.forEach((item) => item.classList.add('visible'));
    } else {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

      items.forEach((item) => observer.observe(item));
    }
  });
})();

(() => {
  const ready = (fn) => document.readyState === 'loading'
    ? document.addEventListener('DOMContentLoaded', fn, { once: true })
    : fn();

  ready(() => {
    const projectsSection = document.querySelector('#progetti');
    if (!projectsSection) return;

    const isEnglish = (document.documentElement.lang || 'it').toLowerCase().startsWith('en');

    if (!document.getElementById('jdevpro-portfolio-overrides')) {
      const style = document.createElement('style');
      style.id = 'jdevpro-portfolio-overrides';
      style.textContent = `
        .hero-brand-logo{display:inline-block;margin:0 0 24px;text-decoration:none}
        .hero-brand-logo img{width:min(430px,80vw);height:auto;display:block;border-radius:14px;box-shadow:0 18px 50px rgba(0,0,0,.22)}
        .akios-featured{border-color:rgba(86,200,255,.28)!important;background:radial-gradient(circle at 72% 28%,rgba(86,200,255,.12),transparent 30%),radial-gradient(circle at 18% 82%,rgba(45,212,191,.08),transparent 30%),var(--navy-2)!important}
        .akios-featured .project-meta span:first-child{color:var(--cyan)}
        .featured-project + .featured-project{margin-top:18px}
        @media(max-width:760px){.hero-brand-logo{margin-bottom:18px}.hero-brand-logo img{width:min(350px,88vw)}}
      `;
      document.head.appendChild(style);
    }

    const heroCopy = document.querySelector('.hero-copy');
    if (heroCopy && !heroCopy.querySelector('.hero-brand-logo')) {
      const logo = document.createElement('a');
      logo.className = 'hero-brand-logo';
      logo.href = '#top';
      logo.setAttribute('aria-label', 'JDEVPRO');
      logo.innerHTML = '<img src="assets/logo-jdevpro.png" alt="JDEVPRO Developer">';
      heroCopy.prepend(logo);
    }

    const heroLinks = document.querySelector('.hero-links');
    if (heroLinks && !heroLinks.querySelector('a[href="https://akios.cloud/"]')) {
      const akiosLink = document.createElement('a');
      akiosLink.href = 'https://akios.cloud/';
      akiosLink.target = '_blank';
      akiosLink.rel = 'noreferrer';
      akiosLink.textContent = 'AKIOS ↗';
      heroLinks.prepend(akiosLink);
    }

    const sectionShell = projectsSection.querySelector('.shell');
    const firstFeatured = sectionShell?.querySelector('.featured-project');
    if (sectionShell && firstFeatured && !sectionShell.querySelector('.akios-featured')) {
      const article = document.createElement('article');
      article.className = 'featured-project reveal visible akios-featured';
      article.innerHTML = isEnglish ? `
        <div class="featured-copy">
          <div class="project-meta"><span>FLAGSHIP · EMBEDDED / IoT LIFECYCLE</span><span>AKIOS.CLOUD</span></div>
          <h3>AKIOS</h3>
          <p class="project-lead">A native firmware and lifecycle layer for IoT devices that separates the device-survival layer from the replaceable System, with cryptographic verification, A/B slots, controlled trial boot, rollback and local recovery.</p>
          <p>The AKIOS BIOS keeps critical device invariants below the replaceable signed System. On BK7238 it manages A/B selection, health gates, redundant metadata, local Wi-Fi recovery and update flows designed so an update cannot destroy both the recovery path and the last-known-good System.</p>
          <div class="tags"><span>embedded C</span><span>BK7238</span><span>signed updates</span><span>A/B</span><span>health gate</span><span>rollback</span><span>recovery</span></div>
          <div class="project-actions"><a class="button light" href="https://akios.cloud/" rel="noreferrer" target="_blank">Visit AKIOS.cloud ↗</a></div>
        </div>
        <div aria-label="AKIOS lifecycle model" class="terminal">
          <div class="terminal-bar"><span></span><span></span><span></span><b>akios::lifecycle</b></div>
          <pre><code>$ boot\nstage-0 → AKIOS BIOS → verified System\n\n$ update\ncandidate → verify → trial → health\n\n$ failure\nrollback → last-known-good\nno valid system → local recovery\n\n$ invariant\nupdate must preserve recovery</code></pre>
        </div>` : `
        <div class="featured-copy">
          <div class="project-meta"><span>FLAGSHIP · EMBEDDED / IoT LIFECYCLE</span><span>AKIOS.CLOUD</span></div>
          <h3>AKIOS</h3>
          <p class="project-lead">Firmware e lifecycle layer nativo per dispositivi IoT: separa il livello di sopravvivenza del device dal System sostituibile, con verifica crittografica, slot A/B, trial controllato, rollback e recovery locale.</p>
          <p>Il BIOS AKIOS mantiene gli invarianti critici del dispositivo sotto il System firmato e sostituibile. Sul BK7238 gestisce selezione A/B, health gate, metadata ridondanti, recovery Wi-Fi locale e aggiornamenti progettati affinché non possano distruggere insieme il percorso di recupero e l'ultima versione valida.</p>
          <div class="tags"><span>embedded C</span><span>BK7238</span><span>signed updates</span><span>A/B</span><span>health gate</span><span>rollback</span><span>recovery</span></div>
          <div class="project-actions"><a class="button light" href="https://akios.cloud/" rel="noreferrer" target="_blank">Visita AKIOS.cloud ↗</a></div>
        </div>
        <div aria-label="Modello lifecycle AKIOS" class="terminal">
          <div class="terminal-bar"><span></span><span></span><span></span><b>akios::lifecycle</b></div>
          <pre><code>$ boot\nstage-0 → AKIOS BIOS → verified System\n\n$ update\ncandidate → verify → trial → health\n\n$ failure\nrollback → last-known-good\nno valid system → local recovery\n\n$ invariant\nupdate must preserve recovery</code></pre>
        </div>`;
      firstFeatured.before(article);
    }

    const findCard = (title) => [...projectsSection.querySelectorAll('.project-card')]
      .find((card) => card.querySelector('h3')?.textContent.trim() === title);

    const oryzeno = findCard('Oryzeno OpenLink');
    if (oryzeno) {
      const link = oryzeno.querySelector('.card-link');
      if (link) {
        link.href = 'https://jellero.github.io/Oryzeno/';
        link.textContent = isEnglish ? 'Website ↗' : 'Apri il sito ↗';
      }
    }

    const lauco = findCard('Lauco Experience');
    if (lauco && !lauco.querySelector('a[href="https://www.laucoexperience.it/"]')) {
      const repo = lauco.querySelector('.card-link');
      if (repo) {
        const wrap = document.createElement('div');
        wrap.className = 'dual-links';
        const website = document.createElement('a');
        website.className = 'card-link';
        website.href = 'https://www.laucoexperience.it/';
        website.target = '_blank';
        website.rel = 'noreferrer';
        website.textContent = isEnglish ? 'Website ↗' : 'Sito ↗';
        repo.classList.add('secondary');
        repo.textContent = 'Repository ↗';
        repo.before(wrap);
        wrap.append(website, repo);
      }
    }

    const footerLinks = document.querySelector('.footer-grid > div:last-child');
    if (footerLinks && !footerLinks.querySelector('a[href="https://akios.cloud/"]')) {
      const a = document.createElement('a');
      a.href = 'https://akios.cloud/';
      a.target = '_blank';
      a.rel = 'noreferrer';
      a.textContent = 'AKIOS';
      footerLinks.prepend(a);
    }
  });
})();

(() => {
  const GA_ID = 'G-K33R7FQ50C';
  const STORAGE_KEY = 'jdevpro_cookie_consent_v1';
  const CONSENT_VERSION = 1;
  const isEnglish = (document.documentElement.lang || 'it').toLowerCase().startsWith('en');
  const ready = (fn) => document.readyState === 'loading'
    ? document.addEventListener('DOMContentLoaded', fn, { once: true })
    : fn();

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function gtag() { window.dataLayer.push(arguments); };

  window.gtag('consent', 'default', {
    analytics_storage: 'denied',
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    functionality_storage: 'granted',
    security_storage: 'granted'
  });

  let analyticsLoaded = false;
  let banner;
  let preferencesTrigger;

  const text = isEnglish ? {
    title: 'Cookie preferences',
    body: 'This website uses necessary storage and, only with your consent, Google Analytics to measure visits and understand how the site is used.',
    reject: 'Reject analytics',
    accept: 'Accept analytics',
    privacy: 'Privacy',
    policy: 'Cookie policy',
    settings: 'Cookie preferences',
    privacyHref: 'privacy-en.html',
    policyHref: 'cookie-policy-en.html'
  } : {
    title: 'Preferenze cookie',
    body: 'Questo sito usa solo memorizzazione tecnica necessaria e, soltanto con il tuo consenso, Google Analytics per misurare le visite e capire come viene usato il sito.',
    reject: 'Rifiuta analytics',
    accept: 'Accetta analytics',
    privacy: 'Privacy',
    policy: 'Cookie policy',
    settings: 'Preferenze cookie',
    privacyHref: 'privacy.html',
    policyHref: 'cookie-policy.html'
  };

  function injectStyles() {
    if (document.getElementById('jdevpro-cookie-styles')) return;
    const style = document.createElement('style');
    style.id = 'jdevpro-cookie-styles';
    style.textContent = `
      .cookie-consent[hidden],.cookie-preferences-trigger[hidden]{display:none!important}
      .cookie-consent{position:fixed;inset:auto 0 0;z-index:10000;padding:18px;background:rgba(7,17,31,.76);backdrop-filter:blur(12px)}
      .cookie-consent__box{width:min(1120px,100%);margin:0 auto;display:grid;grid-template-columns:1fr auto;gap:28px;align-items:center;padding:22px;border:1px solid rgba(255,255,255,.14);border-radius:20px;background:#fff;color:#0a1321;box-shadow:0 24px 70px rgba(0,0,0,.32)}
      .cookie-consent__copy strong{display:block;margin-bottom:7px;font-size:1.05rem}.cookie-consent__copy p{margin:0;color:#526070;line-height:1.55;max-width:760px}
      .cookie-consent__links{display:flex;flex-wrap:wrap;gap:16px;margin-top:10px}.cookie-consent__links a{color:#087d73;font-size:.82rem;font-weight:750;text-decoration:none}.cookie-consent__links a:hover{text-decoration:underline}
      .cookie-consent__actions{display:flex;gap:10px;align-items:center}.cookie-consent__button,.cookie-preferences-trigger{border:0;font:inherit;cursor:pointer}
      .cookie-consent__button{min-height:45px;padding:0 16px;border-radius:10px;font-size:.84rem;font-weight:800;white-space:nowrap}.cookie-consent__button--secondary{color:#172433;background:#edf2f4;border:1px solid #d6e0e4}.cookie-consent__button--primary{color:#05211e;background:#2dd4bf;border:1px solid #2dd4bf}
      .cookie-consent__button:focus-visible,.cookie-preferences-trigger:focus-visible{outline:3px solid #56c8ff;outline-offset:2px}.cookie-preferences-trigger{position:fixed;z-index:9998;right:14px;bottom:14px;min-height:36px;padding:0 12px;border-radius:999px;color:#d9e6ed;background:rgba(7,17,31,.92);border:1px solid rgba(255,255,255,.18);box-shadow:0 8px 28px rgba(0,0,0,.18);font-size:.72rem;font-weight:700}
      @media(max-width:760px){.cookie-consent{padding:10px}.cookie-consent__box{grid-template-columns:1fr;gap:16px;padding:18px;border-radius:16px}.cookie-consent__actions{display:grid;grid-template-columns:1fr 1fr}.cookie-consent__button{white-space:normal}}
    `;
    document.head.appendChild(style);
  }

  function loadGoogleAnalytics() {
    if (analyticsLoaded) return;
    analyticsLoaded = true;
    const script = document.createElement('script');
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(GA_ID)}`;
    document.head.appendChild(script);
    window.gtag('js', new Date());
    window.gtag('config', GA_ID);
  }

  function deleteCookie(name) {
    const host = location.hostname;
    ['', host, `.${host}`, '.jdevpro.it'].forEach((domain) => {
      const domainPart = domain ? `; domain=${domain}` : '';
      document.cookie = `${name}=; Max-Age=0; path=/${domainPart}; SameSite=Lax`;
    });
  }

  function deleteAnalyticsCookies() {
    document.cookie.split(';').forEach((part) => {
      const name = part.split('=')[0].trim();
      if (name === '_ga' || name.startsWith('_ga_') || name === '_gid' || name === '_gat' || name.startsWith('_gat_')) deleteCookie(name);
    });
  }

  function applyConsent(choice) {
    const accepted = choice === 'accepted';
    window.gtag('consent', 'update', {
      analytics_storage: accepted ? 'granted' : 'denied',
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied'
    });
    if (accepted) loadGoogleAnalytics();
    else deleteAnalyticsCookies();
  }

  function readConsent() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      const saved = JSON.parse(raw);
      if (saved && saved.version === CONSENT_VERSION && (saved.choice === 'accepted' || saved.choice === 'rejected')) return saved.choice;
    } catch (_) {}
    return null;
  }

  function writeConsent(choice) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({ choice, version: CONSENT_VERSION, updatedAt: new Date().toISOString() }));
    } catch (_) {}
    applyConsent(choice);
    if (banner) banner.hidden = true;
    if (preferencesTrigger) preferencesTrigger.hidden = false;
  }

  function showBanner() {
    if (banner) banner.hidden = false;
    if (preferencesTrigger) preferencesTrigger.hidden = true;
  }

  function buildUi() {
    injectStyles();
    banner = document.createElement('section');
    banner.className = 'cookie-consent';
    banner.id = 'cookie-consent';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-modal', 'true');
    banner.setAttribute('aria-labelledby', 'cookie-consent-title');
    banner.hidden = true;
    banner.innerHTML = `
      <div class="cookie-consent__box">
        <div class="cookie-consent__copy">
          <strong id="cookie-consent-title">${text.title}</strong>
          <p>${text.body}</p>
          <div class="cookie-consent__links"><a href="${text.privacyHref}">${text.privacy}</a><a href="${text.policyHref}">${text.policy}</a></div>
        </div>
        <div class="cookie-consent__actions">
          <button type="button" class="cookie-consent__button cookie-consent__button--secondary" data-cookie-reject>${text.reject}</button>
          <button type="button" class="cookie-consent__button cookie-consent__button--primary" data-cookie-accept>${text.accept}</button>
        </div>
      </div>`;

    preferencesTrigger = document.createElement('button');
    preferencesTrigger.type = 'button';
    preferencesTrigger.className = 'cookie-preferences-trigger';
    preferencesTrigger.textContent = text.settings;
    preferencesTrigger.hidden = true;
    preferencesTrigger.addEventListener('click', showBanner);

    document.body.appendChild(banner);
    document.body.appendChild(preferencesTrigger);
    banner.querySelector('[data-cookie-reject]').addEventListener('click', () => writeConsent('rejected'));
    banner.querySelector('[data-cookie-accept]').addEventListener('click', () => writeConsent('accepted'));
    document.querySelectorAll('[data-cookie-settings]').forEach((el) => el.addEventListener('click', (event) => {
      event.preventDefault();
      showBanner();
    }));
  }

  ready(() => {
    buildUi();
    const saved = readConsent();
    if (saved) {
      applyConsent(saved);
      preferencesTrigger.hidden = false;
    } else {
      showBanner();
    }
  });
})();
