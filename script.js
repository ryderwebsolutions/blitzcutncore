/* Blitz Cut n Core — site scripts */

/* ── Scroll reveal ───────────────────────────────── */
const revealNodes = document.querySelectorAll('.reveal');

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.15 }
);

revealNodes.forEach((node) => revealObserver.observe(node));

/* ── Mobile menu ─────────────────────────────────── */
const mobileMenuToggles = document.querySelectorAll('.js-mobile-menu-toggle');

mobileMenuToggles.forEach((toggle) => {
  const navWrap = toggle.closest('.nav-wrap');
  if (!navWrap) return;

  toggle.addEventListener('click', () => {
    const isOpen = navWrap.classList.toggle('menu-open');
    toggle.setAttribute('aria-expanded', String(isOpen));
  });
});

document.addEventListener('click', (event) => {
  document.querySelectorAll('.nav-wrap.menu-open').forEach((navWrap) => {
    if (navWrap.contains(event.target)) return;
    navWrap.classList.remove('menu-open');
    const toggle = navWrap.querySelector('.js-mobile-menu-toggle');
    if (toggle) toggle.setAttribute('aria-expanded', 'false');
  });
});

/* ── Photo gallery lightbox ──────────────────────── */
function initLightbox() {
  const overlay = document.getElementById('lightbox-overlay');
  if (!overlay) return;

  const img      = overlay.querySelector('.lightbox-img');
  const closeBtn = overlay.querySelector('.lightbox-close');

  document.querySelectorAll('.gallery-thumb').forEach((thumb) => {
    thumb.addEventListener('click', () => {
      img.src = thumb.src;
      img.alt = thumb.alt;
      overlay.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  });

  function closeLightbox() {
    overlay.classList.remove('open');
    document.body.style.overflow = '';
    img.src = '';
  }

  closeBtn.addEventListener('click', closeLightbox);
  overlay.addEventListener('click', (e) => { if (e.target === overlay) closeLightbox(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeLightbox(); });
}

initLightbox();
