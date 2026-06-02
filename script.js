/* Blitz Cut n Core — site scripts */

/* ── Service-page testimonials (injected dynamically) ── */
function createServiceTestimonialsSection() {
  if (!document.querySelector('.service-contact') || document.querySelector('.service-testimonials')) {
    return;
  }

  /* TODO: Replace these placeholder testimonials with real client feedback */
  const testimonials = [
    {
      name: 'John D.',
      context: 'Residential — Cork City',
      text: '[PLACEHOLDER] Mike and the team did a fantastic job cutting the opening for our new door. Clean, fast, and no mess left behind. Would highly recommend Blitz for any concrete cutting work.'
    },
    {
      name: 'Sarah M.',
      context: 'Commercial — Limerick',
      text: '[PLACEHOLDER] We needed core drilling done quickly on a live site and Blitz delivered. Professional from start to finish — dust-free, on time, and great communication throughout.'
    },
    {
      name: 'Tom R.',
      context: 'New Build — Waterford',
      text: '[PLACEHOLDER] Blitz came in and cut all our electrical and plumbing chases in one day. Precision work, very tidy. The whole site team was impressed with how clean the cuts were.'
    }
  ];

  const section = document.createElement('section');
  section.className = 'section service-testimonials';
  section.setAttribute('aria-label', 'Client testimonials');
  section.innerHTML = `
    <div class="container">
      <p class="eyebrow reveal">Trusted Across Munster</p>
      <h2 class="reveal">What Our Clients Say</h2>
      <p class="service-testimonials-intro reveal">From residential coring to large commercial wall sawing, our clients choose Blitz for precision, cleanliness and reliability on every job.</p>
      <div class="service-testimonials-grid">
        ${testimonials.map(t => `
          <article class="service-testimonial-card reveal">
            <div class="service-rating" aria-label="5 star rating">★★★★★</div>
            <p class="service-testimonial-text">"${t.text}"</p>
            <div class="service-testimonial-meta"><strong>${t.name}</strong><span>${t.context}</span></div>
          </article>
        `).join('')}
      </div>
    </div>
  `;

  const serviceContact = document.querySelector('.service-contact');
  serviceContact.parentNode.insertBefore(section, serviceContact);

  /* Observe the newly injected reveal nodes */
  section.querySelectorAll('.reveal').forEach(node => revealObserver.observe(node));
}

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

createServiceTestimonialsSection();

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

  const img     = overlay.querySelector('.lightbox-img');
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
