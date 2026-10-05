(() => {
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
})();

(() => {
  const GA_ID = 'G-K33R7FQ50C';
  const STORAGE_KEY = 'jdevpro_cookie_consent_v1';
  const CONSENT_VERSION = 1;
  const isEnglish = (document.documentElement.lang || 'it').toLowerCase().startsWith('en');

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function gtag() { window.dataLayer.push(arguments); };

  // Basic Google Consent Mode: no Google tag is loaded before explicit consent.
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
    document.querySelectorAll('[data-cookie-settings]').forEach((el) => el.addEventListener('click', (event) => { event.preventDefault(); showBanner(); }));
  }

  document.addEventListener('DOMContentLoaded', () => {
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
