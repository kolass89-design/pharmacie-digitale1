/* ============================================================
   PHARMACIE DIGITALE - POS (Point Of Sale)
   Panier, paiement multi-modes, ticket, ecritures comptables
   ============================================================ */

(function () {
  'use strict';

  const STOCK_KEY = 'pd_stock';
  const SALES_KEY = 'pd_sales';

  const TVA_RATE = 0.18;
  let cart = [];
  let paymentMethod = 'cash';
  let stock = [];

  const $ = (s) => document.querySelector(s);
  const $$ = (s) => Array.from(document.querySelectorAll(s));

  function loadStock() {
    stock = PD_DASH.storage.get(STOCK_KEY, []);
  }

  function renderProducts(filter = '') {
    const container = $('#pos-products');
    const q = filter.toLowerCase();
    const filtered = stock.filter(p => p.quantity > 0 && (!q || p.name.toLowerCase().includes(q) || (p.dci||'').toLowerCase().includes(q)));

    container.innerHTML = filtered.map(p => `
      <div class="product-tile" data-id="${p.id}">
        <div style="width:44px;height:44px;border-radius:8px;background:var(--gradient-primary);display:flex;align-items:center;justify-content:center;color:white;margin-bottom:8px;">
          <i data-lucide="pill"></i>
        </div>
        <div style="font-weight:600;font-size:13px;line-height:1.3;margin-bottom:2px;">${p.name}</div>
        <div style="font-size:11px;color:var(--color-text-light);margin-bottom:6px;">${p.category}</div>
        <div style="display:flex;justify-content:space-between;align-items:center;">
          <span style="font-weight:700;color:var(--color-primary-dark);font-size:14px;">${PD_DASH.formatNumber(p.price)} F</span>
          <span style="font-size:11px;color:var(--color-text-light);">Stock : ${p.quantity}</span>
        </div>
      </div>
    `).join('') || '<div style="padding:40px;text-align:center;color:var(--color-text-light);grid-column:1/-1;">Aucun produit trouve</div>';

    if (window.lucide) window.lucide.createIcons();

    $$('.product-tile').forEach(tile => {
      tile.addEventListener('click', () => addToCart(tile.dataset.id));
    });
  }

  function addToCart(productId) {
    const product = stock.find(p => p.id === productId);
    if (!product) return;
    if (product.quantity === 0) { PD_DASH.toast('Produit en rupture', 'warning'); return; }

    const existing = cart.find(c => c.id === productId);
    if (existing) {
      if (existing.qty + 1 > product.quantity) { PD_DASH.toast('Stock insuffisant', 'warning'); return; }
      existing.qty++;
    } else {
      cart.push({ id: productId, name: product.name, price: product.price, qty: 1, stock: product.quantity });
    }
    renderCart();
  }

  function updateQty(id, delta) {
    const item = cart.find(c => c.id === id);
    if (!item) return;
    item.qty += delta;
    if (item.qty <= 0) cart = cart.filter(c => c.id !== id);
    else if (item.qty > item.stock) { item.qty = item.stock; PD_DASH.toast('Stock maximum atteint', 'warning'); }
    renderCart();
  }

  function removeFromCart(id) {
    cart = cart.filter(c => c.id !== id);
    renderCart();
  }

  function renderCart() {
    const container = $('#cart-items');
    if (!cart.length) {
      container.innerHTML = '<div style="padding:32px;text-align:center;color:var(--color-text-light);"><i data-lucide="shopping-cart" style="width:32px;height:32px;opacity:0.4;"></i><p style="margin-top:12px;font-size:13px;">Panier vide</p></div>';
    } else {
      container.innerHTML = cart.map(item => `
        <div style="display:flex;gap:8px;padding:10px 0;border-bottom:1px solid var(--color-border);align-items:center;">
          <div style="flex:1;">
            <div style="font-weight:500;font-size:13px;">${item.name}</div>
            <div style="font-size:12px;color:var(--color-text-light);">${PD_DASH.formatNumber(item.price)} F x ${item.qty}</div>
          </div>
          <div style="display:flex;align-items:center;gap:4px;">
            <button class="btn-icon" onclick="PD_POS.updateQty('${item.id}',-1)"><i data-lucide="minus" style="width:14px;height:14px;"></i></button>
            <span style="width:24px;text-align:center;font-weight:600;">${item.qty}</span>
            <button class="btn-icon" onclick="PD_POS.updateQty('${item.id}',1)"><i data-lucide="plus" style="width:14px;height:14px;"></i></button>
            <button class="btn-icon danger" onclick="PD_POS.removeFromCart('${item.id}')"><i data-lucide="x" style="width:14px;height:14px;"></i></button>
          </div>
        </div>
      `).join('');
    }

    const subtotal = cart.reduce((s,i) => s + i.price * i.qty, 0);
    const tva = subtotal * TVA_RATE / (1 + TVA_RATE);
    const total = subtotal;

    $('#cart-subtotal').textContent = PD_DASH.formatNumber(Math.round(subtotal - tva)) + ' FCFA';
    $('#cart-tax').textContent = PD_DASH.formatNumber(Math.round(tva)) + ' FCFA';
    $('#cart-total').textContent = PD_DASH.formatNumber(Math.round(total)) + ' FCFA';

    $('#btn-checkout').disabled = cart.length === 0;

    if (window.lucide) window.lucide.createIcons();
  }

  function checkout() {
    if (!cart.length) return;
    const subtotal = cart.reduce((s,i) => s + i.price * i.qty, 0);
    const tva = subtotal * TVA_RATE / (1 + TVA_RATE);

    const sale = {
      id: PD_DASH.uuid(),
      invoice_number: 'INV-' + Date.now(),
      date: new Date().toISOString(),
      items: cart.slice(),
      total: subtotal,
      total_ht: subtotal - tva,
      tva: tva,
      total_ttc: subtotal,
      payment_method: paymentMethod
    };

    // Update stock
    cart.forEach(item => {
      const p = stock.find(s => s.id === item.id);
      if (p) p.quantity -= item.qty;
    });
    PD_DASH.storage.set(STOCK_KEY, stock);

    // Save sale
    const sales = PD_DASH.storage.get(SALES_KEY, []);
    sales.push(sale);
    PD_DASH.storage.set(SALES_KEY, sales);

    // Record accounting entry (if module available)
    if (window.SyscohadaAccounting) {
      const acc = new SyscohadaAccounting('current');
      acc.loadEntriesFromStorage();
      acc.recordSale(sale);
    }

    // Show ticket
    showTicket(sale);

    // Reset
    cart = [];
    renderCart();
    renderProducts($('#pos-search').value);
  }

  function showTicket(sale) {
    const modal = $('#ticket-modal');
    const content = $('#ticket-content');
    content.innerHTML = `
      <div style="text-align:center;margin-bottom:16px;">
        <div style="width:60px;height:60px;margin:0 auto 12px;border-radius:50%;background:var(--gradient-accent);display:flex;align-items:center;justify-content:center;color:white;"><i data-lucide="check" style="width:32px;height:32px;"></i></div>
        <h2 style="margin:0;font-size:22px;">Vente enregistree !</h2>
        <p style="color:var(--color-text-medium);font-size:13px;margin:4px 0 0;">${sale.invoice_number}</p>
      </div>
      <div style="background:var(--color-bg-light);padding:16px;border-radius:8px;text-align:left;font-size:13px;font-family:monospace;">
        ${sale.items.map(i => `<div style="display:flex;justify-content:space-between;padding:4px 0;"><span>${i.qty}x ${i.name}</span><span>${PD_DASH.formatNumber(i.price * i.qty)} F</span></div>`).join('')}
        <div style="border-top:1px dashed var(--color-border);margin-top:8px;padding-top:8px;">
          <div style="display:flex;justify-content:space-between;"><span>HT</span><span>${PD_DASH.formatNumber(Math.round(sale.total_ht))} F</span></div>
          <div style="display:flex;justify-content:space-between;"><span>TVA 18%</span><span>${PD_DASH.formatNumber(Math.round(sale.tva))} F</span></div>
          <div style="display:flex;justify-content:space-between;font-weight:700;font-size:15px;margin-top:4px;"><span>TOTAL</span><span>${PD_DASH.formatNumber(Math.round(sale.total_ttc))} FCFA</span></div>
        </div>
        <div style="text-align:center;margin-top:12px;color:var(--color-text-light);">Paiement : ${sale.payment_method.toUpperCase()}</div>
      </div>
      <div style="display:flex;gap:8px;margin-top:16px;">
        <button class="btn btn-secondary" style="flex:1;" onclick="window.print()"><i data-lucide="printer"></i> Imprimer</button>
        <button class="btn btn-primary" style="flex:1;" onclick="document.getElementById('ticket-modal').classList.remove('show')"><i data-lucide="check"></i> Terminer</button>
      </div>
    `;
    modal.classList.add('show');
    if (window.lucide) window.lucide.createIcons();
  }

  window.PD_POS = { updateQty, removeFromCart };

  document.addEventListener('DOMContentLoaded', () => {
    loadStock();
    renderProducts();
    renderCart();

    $('#pos-search').addEventListener('input', (e) => renderProducts(e.target.value));

    $$('.payment-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        $$('.payment-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        paymentMethod = btn.dataset.method;
      });
    });

    $('#btn-checkout').addEventListener('click', checkout);
  });
})();
