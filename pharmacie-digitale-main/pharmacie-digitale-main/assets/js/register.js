/* ============================================================
   PHARMACIE DIGITALE - REGISTER FORM LOGIC
   Validation, force mot de passe, tarification dynamique,
   pays + prefixes, testimonial slider, modal succes
   ============================================================ */

(function () {
  'use strict';

  const state = {
    accountType: 'client',
    country: 'BJ',
    countryData: null,
    usdToXof: 600 // taux approximatif USD -> FCFA (BCEAO)
  };

  /* ---------- Utilitaires ---------- */
  const $ = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));

  function showError(fieldId, message) {
    const input = document.getElementById(fieldId);
    const errorEl = document.querySelector(`.form-error[data-for="${fieldId}"]`);
    if (input) input.classList.add('is-invalid');
    if (input) input.classList.remove('is-valid');
    if (errorEl) {
      errorEl.querySelector('span').textContent = message;
      errorEl.classList.add('show');
    }
  }

  function clearError(fieldId) {
    const input = document.getElementById(fieldId);
    const errorEl = document.querySelector(`.form-error[data-for="${fieldId}"]`);
    if (input) {
      input.classList.remove('is-invalid');
      if (input.value.trim()) input.classList.add('is-valid');
    }
    if (errorEl) errorEl.classList.remove('show');
  }

  /* ---------- Account type selector ---------- */
  function initAccountType() {
    const cards = $$('.account-type-card');
    const hiddenInput = $('#account-type');
    const pharmacyField = $('#pharmacy-name-field');

    const applySelection = (type) => {
      state.accountType = type;
      hiddenInput.value = type;
      cards.forEach(c => c.classList.toggle('selected', c.dataset.type === type));
      if (pharmacyField) {
        pharmacyField.classList.toggle('show', type === 'pharmacist');
      }
      updatePricing();
    };

    cards.forEach(card => {
      card.addEventListener('click', () => applySelection(card.dataset.type));
    });

    // initial
    applySelection(state.accountType);
  }

  /* ---------- Country selector ---------- */
  function initCountrySelect() {
    const selectEl = $('#country-select');
    const triggerEl = $('.country-select-trigger', selectEl);
    const dropdownEl = $('.country-select-dropdown', selectEl);
    const listEl = $('#country-list');
    const searchEl = $('#country-search');
    const flagEl = $('#country-flag');
    const nameEl = $('#country-name');
    const codeInput = $('#country-code');
    const phonePrefixEl = $('#phone-prefix');
    const phoneFlagEl = $('#phone-flag');

    const countries = window.COUNTRIES || [];

    const renderList = (filter = '') => {
      const q = filter.trim().toLowerCase();
      const filtered = countries.filter(c => !q || c.name.toLowerCase().includes(q) || c.prefix.includes(q));

      // priority first
      const sorted = [
        ...filtered.filter(c => c.priority),
        ...filtered.filter(c => !c.priority)
      ];

      listEl.innerHTML = sorted.map(c => `
        <li class="country-item ${c.code === state.country ? 'selected' : ''}" data-code="${c.code}">
          <span class="country-flag">${c.flag}</span>
          <span>${c.name}</span>
          <span class="country-prefix">${c.prefix}</span>
        </li>
      `).join('');

      $$('.country-item', listEl).forEach(item => {
        item.addEventListener('click', () => {
          selectCountry(item.dataset.code);
          selectEl.classList.remove('open');
        });
      });
    };

    const selectCountry = (code) => {
      const country = countries.find(c => c.code === code);
      if (!country) return;
      state.country = code;
      state.countryData = country;
      flagEl.textContent = country.flag;
      nameEl.textContent = country.name;
      codeInput.value = code;
      phonePrefixEl.textContent = country.prefix;
      phoneFlagEl.textContent = country.flag;
      updatePricing();
    };

    triggerEl.addEventListener('click', () => {
      selectEl.classList.toggle('open');
      if (selectEl.classList.contains('open')) {
        searchEl.value = '';
        renderList();
        setTimeout(() => searchEl.focus(), 50);
      }
    });

    searchEl.addEventListener('input', (e) => renderList(e.target.value));

    document.addEventListener('click', (e) => {
      if (!selectEl.contains(e.target)) selectEl.classList.remove('open');
    });

    renderList();
    selectCountry(state.country);
  }

  /* ---------- Pricing card ---------- */
  function updatePricing() {
    const priceEl = $('#pricing-price');
    const card = $('#pricing-card');
    if (!priceEl || !card) return;

    let priceHtml;
    if (state.country === 'BJ' && state.accountType === 'pharmacist') {
      const usd = 10;
      const fcfa = usd * state.usdToXof; // 6000 FCFA
      priceHtml = `${fcfa.toLocaleString('fr-FR')} FCFA <span class="price-secondary">(${usd} USD)</span>`;
    } else if (state.accountType === 'pharmacist') {
      priceHtml = `2 500 FCFA <span class="price-secondary">par pharmacie</span>`;
    } else {
      // Client: gratuit
      priceHtml = `Gratuit <span class="price-secondary">pour toujours</span>`;
    }

    priceEl.innerHTML = priceHtml;
    card.classList.add('updating');
    setTimeout(() => card.classList.remove('updating'), 600);
  }

  /* ---------- Password strength ---------- */
  function computePasswordStrength(pwd) {
    let score = 0;
    if (!pwd) return { score: 0, label: '-', color: 'var(--color-text-light)' };
    if (pwd.length >= 8) score++;
    if (pwd.length >= 12) score++;
    if (/[a-z]/.test(pwd) && /[A-Z]/.test(pwd)) score++;
    if (/\d/.test(pwd)) score++;
    if (/[^A-Za-z0-9]/.test(pwd)) score++;

    const map = [
      { label: 'Faible',    color: '#EF4444' },
      { label: 'Faible',    color: '#EF4444' },
      { label: 'Moyen',     color: '#F59E0B' },
      { label: 'Fort',      color: '#0EA5E9' },
      { label: 'Excellent', color: '#10B981' },
      { label: 'Excellent', color: '#10B981' }
    ];
    const s = Math.min(score, 5);
    return { score: Math.min(Math.ceil(s * 4 / 5), 4), label: map[s].label, color: map[s].color };
  }

  function initPasswordStrength() {
    const pwdInput = $('#password');
    const bars = $$('.strength-bars .strength-bar');
    const labelValue = $('.strength-label .label-value');
    const strengthEl = $('#password-strength');

    pwdInput.addEventListener('input', () => {
      const { score, label, color } = computePasswordStrength(pwdInput.value);
      bars.forEach((bar, i) => {
        bar.classList.toggle('filled', i < score);
      });
      strengthEl.style.setProperty('--current-strength-color', color);
      labelValue.textContent = label;
    });
  }

  /* ---------- Password toggle ---------- */
  function initPasswordToggles() {
    $$('.password-toggle').forEach(btn => {
      btn.addEventListener('click', () => {
        const target = document.getElementById(btn.dataset.target);
        if (!target) return;
        const isPwd = target.type === 'password';
        target.type = isPwd ? 'text' : 'password';
        const icon = btn.querySelector('i');
        if (icon) {
          icon.setAttribute('data-lucide', isPwd ? 'eye-off' : 'eye');
          if (window.lucide) window.lucide.createIcons();
        }
      });
    });
  }

  /* ---------- Validation ---------- */
  const validators = {
    fullname: (v) => {
      if (!v.trim()) return 'Le nom complet est requis';
      if (v.trim().length < 3) return 'Minimum 3 caracteres';
      if (!/^[A-Za-zA-ZaÀ-ſ\s'-]+$/.test(v)) return 'Caracteres invalides';
      return null;
    },
    'pharmacy-name': (v) => {
      if (state.accountType !== 'pharmacist') return null;
      if (!v.trim()) return 'Le nom de la pharmacie est requis';
      if (v.trim().length < 2) return 'Nom trop court';
      return null;
    },
    email: (v) => {
      if (!v.trim()) return "L'email est requis";
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) return 'Email invalide';
      return null;
    },
    phone: (v) => {
      if (!v.trim()) return 'Le telephone est requis';
      const digits = v.replace(/\D/g, '');
      if (digits.length < 6) return 'Numero trop court';
      if (digits.length > 15) return 'Numero trop long';
      return null;
    },
    password: (v) => {
      if (!v) return 'Le mot de passe est requis';
      if (v.length < 8) return 'Minimum 8 caracteres';
      if (!/[A-Z]/.test(v) || !/[a-z]/.test(v)) return 'Doit contenir majuscules et minuscules';
      if (!/\d/.test(v)) return 'Doit contenir un chiffre';
      return null;
    },
    'password-confirm': (v) => {
      if (!v) return 'Confirmez votre mot de passe';
      if (v !== $('#password').value) return 'Les mots de passe ne correspondent pas';
      return null;
    },
    terms: () => {
      if (!$('#terms').checked) return 'Vous devez accepter les conditions';
      return null;
    }
  };

  function validateField(fieldId) {
    const validator = validators[fieldId];
    if (!validator) return true;
    const el = document.getElementById(fieldId);
    const value = el && el.type === 'checkbox' ? el.checked : (el ? el.value : '');
    const error = validator(value);
    if (error) { showError(fieldId, error); return false; }
    clearError(fieldId);
    return true;
  }

  function initLiveValidation() {
    Object.keys(validators).forEach(fieldId => {
      const el = document.getElementById(fieldId);
      if (!el) return;
      const eventName = el.type === 'checkbox' ? 'change' : 'blur';
      el.addEventListener(eventName, () => validateField(fieldId));
      el.addEventListener('input', () => {
        if (el.classList.contains('is-invalid')) validateField(fieldId);
        // realtime password-confirm check
        if (fieldId === 'password') {
          const confirm = $('#password-confirm');
          if (confirm && confirm.value) validateField('password-confirm');
        }
      });
    });
  }

  /* ---------- Testimonials slider ---------- */
  function initTestimonials() {
    const slides = $$('.testimonial-slide');
    const dots = $$('.testimonial-dot');
    if (!slides.length) return;
    let current = 0;

    const show = (idx) => {
      slides.forEach((s, i) => s.classList.toggle('active', i === idx));
      dots.forEach((d, i) => d.classList.toggle('active', i === idx));
      current = idx;
    };

    dots.forEach((dot, i) => {
      dot.addEventListener('click', () => show(i));
    });

    setInterval(() => show((current + 1) % slides.length), 5000);
  }

  /* ---------- Submit ---------- */
  function initSubmit() {
    const form = $('#register-form');
    const submitBtn = $('#submit-btn');
    const btnText = $('.btn-text', submitBtn);
    const btnLoading = $('.btn-loading', submitBtn);

    form.addEventListener('submit', (e) => {
      e.preventDefault();

      // Validate all fields
      const fieldsToValidate = Object.keys(validators);
      const results = fieldsToValidate.map(f => validateField(f));
      const allValid = results.every(Boolean);

      if (!allValid) {
        // scroll to first error
        const firstError = document.querySelector('.form-input.is-invalid, .form-error.show');
        if (firstError) firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
        return;
      }

      // Show loading
      submitBtn.disabled = true;
      btnText.style.display = 'none';
      btnLoading.style.display = 'inline-flex';

      // Simulate registration
      setTimeout(() => {
        submitBtn.disabled = false;
        btnText.style.display = 'inline-flex';
        btnLoading.style.display = 'none';
        showSuccessModal();
      }, 1600);
    });
  }

  /* ---------- Success modal ---------- */
  function showSuccessModal() {
    const modal = $('#success-modal');
    const msg = $('#success-message');
    const cta = $('#success-cta');
    const ctaText = $('#success-cta-text');

    if (state.accountType === 'pharmacist') {
      msg.textContent = "Vous pouvez maintenant creer votre premiere pharmacie, configurer votre stock et votre caisse.";
      ctaText.textContent = 'Creer ma premiere pharmacie';
      cta.href = 'dashboard/add-pharmacy.html';
    } else {
      msg.textContent = 'Vous pouvez maintenant rechercher vos medicaments et verifier leur disponibilite.';
      ctaText.textContent = 'Rechercher un medicament';
      cta.href = 'search/medicaments.html';
    }

    modal.classList.add('show');
    if (window.lucide) window.lucide.createIcons();
  }

  /* ---------- OAuth buttons (simulated) ---------- */
  function initOAuth() {
    $$('.btn-oauth').forEach(btn => {
      btn.addEventListener('click', () => {
        const provider = btn.dataset.provider;
        alert(`OAuth ${provider} sera bientot disponible.`);
      });
    });
  }

  /* ---------- Init ---------- */
  document.addEventListener('DOMContentLoaded', () => {
    initAccountType();
    initCountrySelect();
    initPasswordStrength();
    initPasswordToggles();
    initLiveValidation();
    initTestimonials();
    initSubmit();
    initOAuth();
    updatePricing();

    if (window.lucide) window.lucide.createIcons();
  });
})();
