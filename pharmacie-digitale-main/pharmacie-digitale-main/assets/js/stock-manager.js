/* ============================================================
   PHARMACIE DIGITALE - STOCK MANAGER
   Gestion stock : peremption FEFO, alertes, seuils, lots
   ============================================================ */

class StockManager {
  constructor(pharmacyId, options = {}) {
    this.pharmacyId = pharmacyId;
    this.apiBase    = options.apiBase || '/api/v1/pharmacies';
    this.stock      = [];
    this.categories = [];
    this.refreshInterval = options.refreshInterval || 60000;
    this._timer = null;
  }

  async init() {
    await this.loadStock();
    this.setupAlerts();
    this.startAutoRefresh();
  }

  async loadStock() {
    try {
      const res = await fetch(`${this.apiBase}/${this.pharmacyId}/stock`);
      const data = await res.json();
      this.stock = data.items || [];
      this.categories = [...new Set(this.stock.map(i => i.category))];
    } catch (e) {
      console.warn('[StockManager] loadStock failed, using empty', e);
      this.stock = [];
    }
  }

  /* ---------- Helpers ---------- */
  daysUntilExpiry(date) {
    const expiry = new Date(date);
    const today = new Date();
    return Math.ceil((expiry - today) / 86400000);
  }

  formatPrice(price, currency = 'XOF') {
    return new Intl.NumberFormat('fr-FR', { style: 'currency', currency }).format(price);
  }

  formatDate(date) {
    return new Date(date).toLocaleDateString('fr-FR');
  }

  /* ---------- Statuts ---------- */
  getStatus(item) {
    if (item.quantity === 0) return 'out_of_stock';
    if (item.quantity <= item.threshold) return 'low_stock';
    const days = this.daysUntilExpiry(item.expiry_date);
    if (days <= 30 && days > 0) return 'expiring';
    if (days <= 0) return 'expired';
    return 'available';
  }

  /* ---------- Stats ---------- */
  getStats() {
    return {
      total:         this.stock.length,
      low_stock:     this.stock.filter(i => i.quantity <= i.threshold && i.quantity > 0).length,
      out_of_stock:  this.stock.filter(i => i.quantity === 0).length,
      expiring_soon: this.stock.filter(i => {
        const d = this.daysUntilExpiry(i.expiry_date);
        return d > 0 && d <= 30;
      }).length,
      expired:       this.stock.filter(i => this.daysUntilExpiry(i.expiry_date) <= 0).length
    };
  }

  /* ---------- Alertes ---------- */
  checkAlerts() {
    const alerts = [];
    this.stock.forEach(item => {
      if (item.quantity === 0) {
        alerts.push({
          type: 'out_of_stock',
          severity: 'danger',
          message: `Rupture de stock : ${item.name}`,
          product_id: item.id
        });
      } else if (item.quantity <= item.threshold) {
        alerts.push({
          type: 'low_stock',
          severity: 'warning',
          message: `Stock faible : ${item.name} (${item.quantity} restants)`,
          product_id: item.id
        });
      }
      const days = this.daysUntilExpiry(item.expiry_date);
      if (days > 0 && days <= 30) {
        alerts.push({
          type: 'expiring',
          severity: days <= 7 ? 'danger' : 'warning',
          message: `Peremption dans ${days} jours : ${item.name}`,
          product_id: item.id
        });
      }
    });
    return alerts;
  }

  setupAlerts() {
    setInterval(() => {
      const alerts = this.checkAlerts();
      if (typeof this.onAlerts === 'function') this.onAlerts(alerts);
    }, 300000);
  }

  /* ---------- Auto refresh ---------- */
  startAutoRefresh() {
    this._timer = setInterval(() => this.loadStock(), this.refreshInterval);
  }

  stopAutoRefresh() {
    if (this._timer) clearInterval(this._timer);
  }

  /* ---------- CRUD ---------- */
  async addProduct(product) {
    const res = await fetch(`${this.apiBase}/${this.pharmacyId}/stock`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(product)
    });
    return res.json();
  }

  async updateProduct(id, updates) {
    const res = await fetch(`${this.apiBase}/${this.pharmacyId}/stock/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(updates)
    });
    return res.json();
  }

  async deleteProduct(id) {
    const res = await fetch(`${this.apiBase}/${this.pharmacyId}/stock/${id}`, { method: 'DELETE' });
    return res.json();
  }
}

window.StockManager = StockManager;
