/* ============================================================
   PHARMACIE DIGITALE - MAIN JS
   Initialisation globale (Lucide, AOS, ripple, header scroll)
   ============================================================ */

(function () {
  'use strict';

  function initAll() {
    // Lucide icons
    if (window.lucide && typeof window.lucide.createIcons === 'function') {
      try { window.lucide.createIcons(); } catch (e) { console.warn('Lucide init failed', e); }
    }

    // AOS animations avec fallback
    if (window.AOS && typeof window.AOS.init === 'function') {
      try {
        window.AOS.init({
          duration: 700,
          easing: 'ease-out-cubic',
          once: true,
          offset: 40,
          disable: false
        });
      } catch (e) {
        console.warn('AOS init failed', e);
        forceAosVisible();
      }
    } else {
      forceAosVisible();
    }

    // Sécurité : après 1.5s, forcer visibilité si AOS a échoué
    setTimeout(() => {
      document.querySelectorAll('[data-aos]').forEach(el => {
        const style = window.getComputedStyle(el);
        if (parseFloat(style.opacity) < 0.1) {
          el.style.opacity = '1';
          el.style.transform = 'none';
        }
      });
    }, 1500);

    // Ripple effect sur les boutons
    document.addEventListener('click', (e) => {
      const btn = e.target.closest('.btn');
      if (!btn) return;
      const ripple = document.createElement('span');
      ripple.className = 'ripple';
      const rect = btn.getBoundingClientRect();
      const size = Math.max(rect.width, rect.height);
      ripple.style.width = ripple.style.height = size + 'px';
      ripple.style.left = (e.clientX - rect.left - size / 2) + 'px';
      ripple.style.top = (e.clientY - rect.top - size / 2) + 'px';
      btn.appendChild(ripple);
      setTimeout(() => ripple.remove(), 600);
    });

    // Header scroll effect
    const header = document.querySelector('.site-header');
    if (header) {
      const onScroll = () => {
        if (window.scrollY > 20) {
          header.style.background = 'rgba(15, 23, 42, 0.85)';
          header.style.boxShadow = '0 4px 20px rgba(0,0,0,0.15)';
        } else {
          header.style.background = 'rgba(15, 23, 42, 0.6)';
          header.style.boxShadow = 'none';
        }
      };
      window.addEventListener('scroll', onScroll, { passive: true });
      onScroll();
    }
  }

  function forceAosVisible() {
    document.querySelectorAll('[data-aos]').forEach(el => {
      el.style.opacity = '1';
      el.style.transform = 'none';
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
})();
