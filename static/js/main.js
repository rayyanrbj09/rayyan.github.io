// ── Custom cursor ───────────────────────────────────────────
const cursor = document.getElementById('cursor');
const trail  = document.getElementById('cursorTrail');
let mx = 0, my = 0, tx = 0, ty = 0;

document.addEventListener('mousemove', e => {
  mx = e.clientX; my = e.clientY;
  cursor.style.left = mx + 'px';
  cursor.style.top  = my + 'px';
});

(function animTrail() {
  tx += (mx - tx) * 0.12;
  ty += (my - ty) * 0.12;
  trail.style.left = tx + 'px';
  trail.style.top  = ty + 'px';
  requestAnimationFrame(animTrail);
})();

document.querySelectorAll('a, button').forEach(el => {
  el.addEventListener('mouseenter', () => {
    cursor.style.transform = 'translate(-50%,-50%) scale(2)';
    trail.style.opacity = '0.15';
  });
  el.addEventListener('mouseleave', () => {
    cursor.style.transform = 'translate(-50%,-50%) scale(1)';
    trail.style.opacity = '0.5';
  });
});

// ── Typing effect ───────────────────────────────────────────
const phrases = [
  'AI & ML Engineer',
  'Python Developer',
  'NLP Enthusiast',
  'Cloud Builder',
  'Deep Learning Explorer',
];
let pi = 0, ci = 0, deleting = false;
const typingEl = document.getElementById('typingText');

function type() {
  const word = phrases[pi];
  if (!deleting) {
    typingEl.textContent = word.slice(0, ci + 1);
    ci++;
    if (ci === word.length) { deleting = true; setTimeout(type, 1600); return; }
  } else {
    typingEl.textContent = word.slice(0, ci - 1);
    ci--;
    if (ci === 0) { deleting = false; pi = (pi + 1) % phrases.length; }
  }
  setTimeout(type, deleting ? 60 : 100);
}
type();

// ── Navbar scroll ───────────────────────────────────────────
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 60);
});

// ── Hamburger menu ──────────────────────────────────────────
const hamburger = document.getElementById('hamburger');
const navLinks  = document.querySelector('.nav-links');
hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('open');
});
navLinks.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => navLinks.classList.remove('open'));
});

// ── Scroll reveal ────────────────────────────────────────────
const reveals = document.querySelectorAll(
  '.project-card, .timeline-item, .about-text, .skills-panel, .edu-card, .contact-card, .contact-terminal'
);
reveals.forEach(el => el.classList.add('reveal'));

const observer = new IntersectionObserver(entries => {
  entries.forEach((e, i) => {
    if (e.isIntersecting) {
      setTimeout(() => e.target.classList.add('visible'), i * 60);
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.1 });

reveals.forEach(el => observer.observe(el));

// ── Project filter ──────────────────────────────────────────
const filterBtns = document.querySelectorAll('.filter-btn');
const cards      = document.querySelectorAll('.project-card');

filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const filter = btn.dataset.filter;

    cards.forEach(card => {
      const tags = card.dataset.tags || '';
      if (filter === 'all' || tags.includes(filter)) {
        card.classList.remove('hidden');
        card.classList.add('reveal');
        setTimeout(() => card.classList.add('visible'), 80);
      } else {
        card.classList.add('hidden');
      }
    });
  });
});

// ── Smooth active nav link highlight ────────────────────────
const sections = document.querySelectorAll('section[id]');
const navAs    = document.querySelectorAll('.nav-links a');

window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(sec => {
    if (window.scrollY >= sec.offsetTop - 200) current = sec.id;
  });
  navAs.forEach(a => {
    a.style.color = a.getAttribute('href') === '#' + current
      ? 'var(--accent3)' : '';
  });
});
