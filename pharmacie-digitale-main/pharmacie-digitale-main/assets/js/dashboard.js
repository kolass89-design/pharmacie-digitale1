/* ============================================================
   PHARMACIE DIGITALE - DASHBOARD SHARED JS
   Sidebar toggle, avatar, notifications, common utilities
   ============================================================ */

(function () {
  'use strict';

  window.PD_DASH = {
    formatPrice(v, currency = 'XOF') {
      return new Intl.NumberFormat('fr-FR', { style: 'currency', currency }).format(v);
    },
    formatNumber(v) {
      return new Intl.NumberFormat('fr-FR').format(v);
    },
    formatDate(d) {
      return new Date(d).toLocaleDateString('fr-FR');
    },
    todayISO() {
      return new Date().toISOString().slice(0, 10);
    },
    uuid() {
      return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (c) => {
        const r = Math.random() * 16 | 0;
        return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
      });
    },
    // LocalStorage helpers
    storage: {
      get(key, fallback = null) {
        try { return JSON.parse(localStorage.getItem(key)) ?? fallback; } catch { return fallback; }
      },
      set(key, value) { localStorage.setItem(key, JSON.stringify(value)); },
      remove(key) { localStorage.removeItem(key); }
    },
    // Toast notifications
    toast(message, type = 'info') {
      let container = document.getElementById('toast-container');
      if (!container) {
        container = document.createElement('div');
        container.id = 'toast-container';
        container.style.cssText = 'position:fixed;top:20px;right:20px;z-index:3000;display:flex;flex-direction:column;gap:10px;';
        document.body.appendChild(container);
      }
      const colors = { success: '#10B981', warning: '#F59E0B', danger: '#EF4444', info: '#0EA5E9' };
      const icons  = { success: 'check-circle', warning: 'alert-triangle', danger: 'x-circle', info: 'info' };
      const toast = document.createElement('div');
      toast.style.cssText = `background:white;border-left:4px solid ${colors[type]};padding:14px 18px;border-radius:10px;box-shadow:0 10px 30px rgba(0,0,0,0.15);display:flex;align-items:center;gap:10px;min-width:280px;max-width:400px;animation:slide-in 0.3s ease;`;
      toast.innerHTML = `<i data-lucide="${icons[type]}" style="color:${colors[type]};width:20px;height:20px;"></i><span style="flex:1;font-size:14px;">${message}</span><button style="background:none;border:none;cursor:pointer;color:#94A3B8;" onclick="this.parentElement.remove()">✕</button>`;
      container.appendChild(toast);
      if (window.lucide) window.lucide.createIcons();
      setTimeout(() => { toast.style.opacity = '0'; toast.style.transform = 'translateX(20px)'; setTimeout(() => toast.remove(), 300); }, 4000);
    }
  };

  // Inject toast animation CSS
  const style = document.createElement('style');
  style.textContent = `@keyframes slide-in { from { opacity: 0; transform: translateX(20px); } to { opacity: 1; transform: translateX(0); } } #toast-container > div { transition: all 0.3s ease; }`;
  document.head.appendChild(style);

  document.addEventListener('DOMContentLoaded', () => {
    // Sidebar toggle mobile
    const toggle = document.querySelector('.sidebar-toggle');
    const sidebar = document.querySelector('.dash-sidebar');
    if (toggle && sidebar) {
      toggle.addEventListener('click', () => sidebar.classList.toggle('open'));
      document.addEventListener('click', (e) => {
        if (window.innerWidth <= 1024 && !sidebar.contains(e.target) && !toggle.contains(e.target)) {
          sidebar.classList.remove('open');
        }
      });
    }

    // User avatar
    const avatar = document.querySelector('.user-avatar');
    if (avatar && !avatar.textContent.trim()) {
      const user = window.PD_DASH.storage.get('user', { name: 'Moukoddi Sadikou' });
      const initials = user.name.split(' ').map(n => n[0]).slice(0, 2).join('').toUpperCase();
      avatar.textContent = initials;
    }

    // Logout
    document.querySelectorAll('[data-action="logout"]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        window.PD_DASH.storage.remove('user');
        window.location.href = '../login.html';
      });
    });
  });
})();
