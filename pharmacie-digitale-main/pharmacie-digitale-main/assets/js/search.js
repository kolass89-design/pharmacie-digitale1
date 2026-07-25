/* ============================================================
   PHARMACIE DIGITALE - SEARCH MEDICAMENTS
   Recherche + filtres + mock data (a remplacer par API)
   ============================================================ */

(function () {
  'use strict';

  // Mock database
  const MOCK_STOCK = [
    { id: 1, name: 'Paracetamol 500mg', dci: 'Paracetamol', category: 'Antalgique', quantity: 150, price: 1500, prescription: false, pharmacy: { name: 'Pharmacie du Centre', city: 'Cotonou', address: 'Ganhi, Avenue Steinmetz', phone: '+229 21 30 12 34', distance: 1.2 } },
    { id: 2, name: 'Paracetamol 1g', dci: 'Paracetamol', category: 'Antalgique', quantity: 80, price: 2500, prescription: false, pharmacy: { name: 'Pharmacie Sainte-Rita', city: 'Cotonou', address: 'Sainte-Rita, Rue 234', phone: '+229 21 35 67 89', distance: 2.5 } },
    { id: 3, name: 'Ibuprofene 400mg', dci: 'Ibuprofene', category: 'Anti-inflammatoire', quantity: 45, price: 3500, prescription: false, pharmacy: { name: 'Pharmacie du Centre', city: 'Cotonou', address: 'Ganhi, Avenue Steinmetz', phone: '+229 21 30 12 34', distance: 1.2 } },
    { id: 4, name: 'Amoxicilline 500mg', dci: 'Amoxicilline', category: 'Antibiotique', quantity: 30, price: 4500, prescription: true, pharmacy: { name: 'Pharmacie Camp Guezo', city: 'Cotonou', address: 'Camp Guezo, Bd St-Michel', phone: '+229 21 32 45 78', distance: 3.1 } },
    { id: 5, name: 'Vitamine C 1000mg', dci: 'Acide ascorbique', category: 'Vitamine', quantity: 200, price: 2000, prescription: false, pharmacy: { name: 'Pharmacie Sainte-Rita', city: 'Cotonou', address: 'Sainte-Rita, Rue 234', phone: '+229 21 35 67 89', distance: 2.5 } },
    { id: 6, name: 'Artemether-Lumefantrine', dci: 'Artemether/Lumefantrine', category: 'Antipaludique', quantity: 60, price: 6500, prescription: true, pharmacy: { name: 'Pharmacie du Port', city: 'Cotonou', address: 'Zone portuaire', phone: '+229 21 31 89 12', distance: 4.5 } },
    { id: 7, name: 'Doliprane 500mg', dci: 'Paracetamol', category: 'Antalgique', quantity: 120, price: 1800, prescription: false, pharmacy: { name: 'Pharmacie du Port', city: 'Cotonou', address: 'Zone portuaire', phone: '+229 21 31 89 12', distance: 4.5 } },
    { id: 8, name: 'Aspirine 500mg', dci: 'Acide acetylsalicylique', category: 'Antalgique', quantity: 0, price: 1200, prescription: false, pharmacy: { name: 'Pharmacie Sainte-Rita', city: 'Cotonou', address: 'Sainte-Rita, Rue 234', phone: '+229 21 35 67 89', distance: 2.5 } },
    { id: 9, name: 'Ciprofloxacine 500mg', dci: 'Ciprofloxacine', category: 'Antibiotique', quantity: 25, price: 5500, prescription: true, pharmacy: { name: 'Pharmacie Centrale de Dakar', city: 'Dakar', address: 'Plateau, Av. Georges Pompidou', phone: '+221 33 821 45 67', distance: 12.4 } },
    { id: 10, name: 'Diclofenac 50mg', dci: 'Diclofenac', category: 'Anti-inflammatoire', quantity: 55, price: 3200, prescription: false, pharmacy: { name: 'Pharmacie du Plateau', city: 'Abidjan', address: 'Plateau, Rue du Commerce', phone: '+225 27 20 21 34 56', distance: 18.2 } }
  ];

  const $ = (s) => document.querySelector(s);
  const $$ = (s) => Array.from(document.querySelectorAll(s));

  const formatPrice = (p) => new Intl.NumberFormat('fr-FR').format(p) + ' FCFA';

  function performSearch() {
    const query = $('#search-input').value.trim().toLowerCase();
    const inStockOnly = $('#filter-in-stock').checked;
    const noPrescription = $('#filter-prescription').checked;
    const city = $('#filter-city').value;
    const maxPrice = parseInt($('#filter-price').value, 10);
    const cats = $$('.filter-cat:checked').map(c => c.value);
    const sort = $('#sort-select').value;

    let results = MOCK_STOCK.filter(item => {
      if (query && !item.name.toLowerCase().includes(query) && !item.dci.toLowerCase().includes(query)) return false;
      if (inStockOnly && item.quantity === 0) return false;
      if (noPrescription && item.prescription) return false;
      if (city && item.pharmacy.city !== city) return false;
      if (item.price > maxPrice) return false;
      if (cats.length && !cats.includes(item.category)) return false;
      return true;
    });

    // Sort
    switch (sort) {
      case 'price_asc':  results.sort((a, b) => a.price - b.price); break;
      case 'price_desc': results.sort((a, b) => b.price - a.price); break;
      case 'stock':      results.sort((a, b) => b.quantity - a.quantity); break;
      default:           results.sort((a, b) => a.pharmacy.distance - b.pharmacy.distance);
    }

    renderResults(results, query);
  }

  function renderResults(results, query) {
    const container = $('#results-container');
    $('#results-count').textContent = results.length;

    if (!query) {
      container.innerHTML = `
        <div style="text-align:center;padding:60px 20px;color:white;">
          <i data-lucide="search" style="width:48px;height:48px;opacity:0.5;"></i>
          <h3 style="color:white;margin-top:16px;">Commencez a rechercher</h3>
          <p style="color:rgba(255,255,255,0.7);">Tapez le nom du medicament recherche dans la barre ci-dessus.</p>
        </div>`;
      if (window.lucide) window.lucide.createIcons();
      return;
    }

    if (!results.length) {
      container.innerHTML = `
        <div style="text-align:center;padding:60px 20px;color:white;">
          <i data-lucide="search-x" style="width:48px;height:48px;opacity:0.5;"></i>
          <h3 style="color:white;margin-top:16px;">Aucun resultat</h3>
          <p style="color:rgba(255,255,255,0.7);">Essayez d'ajuster vos filtres ou de reformuler votre recherche.</p>
        </div>`;
      if (window.lucide) window.lucide.createIcons();
      return;
    }

    container.innerHTML = results.map(item => `
      <div class="result-card" data-aos="fade-up">
        <div class="result-icon"><i data-lucide="pill"></i></div>
        <div class="result-info">
          <h4>${item.name}</h4>
          <div class="result-pharmacy">
            <i data-lucide="map-pin" style="width:14px;height:14px;"></i>
            <strong>${item.pharmacy.name}</strong> - ${item.pharmacy.address}
          </div>
          <div class="result-meta">
            <span class="meta-item"><i data-lucide="navigation" style="width:12px;height:12px;"></i> ${item.pharmacy.distance} km</span>
            <span class="meta-item"><i data-lucide="phone" style="width:12px;height:12px;"></i> ${item.pharmacy.phone}</span>
            <span class="badge ${item.quantity === 0 ? 'badge-danger' : (item.quantity < 20 ? 'badge-warning' : 'badge-success')}">
              ${item.quantity === 0 ? 'Rupture' : (item.quantity < 20 ? 'Stock faible' : 'En stock')}
            </span>
            ${item.prescription ? '<span class="badge badge-primary">Sur ordonnance</span>' : ''}
            <span class="badge badge-primary">${item.category}</span>
          </div>
        </div>
        <div class="result-actions">
          <div class="result-price">${formatPrice(item.price)}</div>
          <a href="tel:${item.pharmacy.phone}" class="btn btn-primary" style="padding:8px 16px;font-size:13px;">
            <i data-lucide="phone"></i> Appeler
          </a>
        </div>
      </div>
    `).join('');

    if (window.lucide) window.lucide.createIcons();
  }

  document.addEventListener('DOMContentLoaded', () => {
    // Debounced search on input
    let timeout;
    const debouncedSearch = () => {
      clearTimeout(timeout);
      timeout = setTimeout(performSearch, 250);
    };

    $('#search-input').addEventListener('input', debouncedSearch);
    $('#search-btn').addEventListener('click', performSearch);
    $('#search-input').addEventListener('keydown', (e) => { if (e.key === 'Enter') performSearch(); });

    // Filters
    $('#filter-in-stock').addEventListener('change', performSearch);
    $('#filter-prescription').addEventListener('change', performSearch);
    $('#filter-city').addEventListener('change', performSearch);
    $('#sort-select').addEventListener('change', performSearch);
    $$('.filter-cat').forEach(c => c.addEventListener('change', performSearch));

    // Price slider
    const priceInput = $('#filter-price');
    const priceValue = $('#price-value');
    priceInput.addEventListener('input', () => {
      priceValue.textContent = new Intl.NumberFormat('fr-FR').format(priceInput.value) + ' FCFA';
    });
    priceInput.addEventListener('change', performSearch);
  });
})();
