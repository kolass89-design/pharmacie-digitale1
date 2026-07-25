/* ============================================================
   PHARMACIE DIGITALE - API CONNECTEUR IA UNIVERSEL
   Permet a n'importe quelle IA (ChatGPT, Claude, Kimi, etc.)
   de piloter la plateforme via REST + WebSocket + Webhooks.
   ============================================================ */

class IAConnector {
  constructor(config) {
    this.iaId       = config.iaId;
    this.iaName     = config.iaName;
    this.apiKey     = config.apiKey;
    this.baseUrl    = config.baseUrl || '/api/v1/ia';
    this.wsUrl      = config.wsUrl   || 'wss://api.pharmacie-digitale.com/ws/ia';
    this.token      = null;
    this.sessionId  = null;
    this.ws         = null;
    this.eventListeners = new Map();
    this.reconnectDelay = 5000;
  }

  /* ---------- Authentification ---------- */
  async authenticate() {
    const response = await fetch(`${this.baseUrl}/auth`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        ia_id: this.iaId,
        ia_name: this.iaName,
        api_key: this.apiKey,
        capabilities: ['read', 'write', 'admin'],
        metadata: {
          version: '1.0.0',
          provider: this.iaName,
          endpoint_url: window.location.origin
        }
      })
    });
    const data = await response.json();
    this.token = data.token;
    this.sessionId = data.session_id;
    return data;
  }

  /* ---------- WebSocket temps reel ---------- */
  connectWebSocket() {
    this.ws = new WebSocket(`${this.wsUrl}?token=${this.token}`);

    this.ws.onopen = () => {
      console.log(`[${this.iaName}] Connecte en temps reel`);
      this.emit('connected', { ia: this.iaName });
    };

    this.ws.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        this.emit(data.event, data);
      } catch (e) {
        console.error('[IAConnector] Message WS invalide', e);
      }
    };

    this.ws.onclose = () => {
      console.log(`[${this.iaName}] Deconnecte - reconnexion dans ${this.reconnectDelay}ms...`);
      setTimeout(() => this.connectWebSocket(), this.reconnectDelay);
    };

    this.ws.onerror = (err) => console.error(`[${this.iaName}] Erreur WS`, err);
  }

  /* ---------- CRUD Pharmacies ---------- */
  getPharmacies()               { return this.request('GET',    '/pharmacies'); }
  createPharmacy(data)          { return this.request('POST',   '/pharmacies', data); }
  updatePharmacy(id, data)      { return this.request('PUT',    `/pharmacies/${id}`, data); }
  deletePharmacy(id)            { return this.request('DELETE', `/pharmacies/${id}`); }

  /* ---------- CRUD Stock ---------- */
  getStock(pharmacyId, params = {}) {
    const qs = new URLSearchParams(params).toString();
    return this.request('GET', `/pharmacies/${pharmacyId}/stock${qs ? '?' + qs : ''}`);
  }
  updateStock(pharmacyId, item) {
    return this.request('POST', `/pharmacies/${pharmacyId}/stock`, item);
  }
  batchUpdateStock(pharmacyId, items) {
    return this.request('POST', `/pharmacies/${pharmacyId}/stock/batch`, { items });
  }
  getStockAlerts(pharmacyId) {
    return this.request('GET', `/pharmacies/${pharmacyId}/stock/alerts`);
  }

  /* ---------- Recherche ---------- */
  searchMedicaments(params) {
    const qs = new URLSearchParams(params).toString();
    return this.request('GET', `/search/medicaments?${qs}`);
  }

  /* ---------- Webhooks ---------- */
  configureWebhook(config) {
    return this.request('POST', '/webhooks/configure', config);
  }

  /* ---------- NLP / Commandes ---------- */
  sendCommand(command, context = {}) {
    return this.request('POST', '/nlp/command', {
      ia_id: this.iaId,
      session_id: this.sessionId,
      command,
      context
    });
  }

  /* ---------- Helper HTTP ---------- */
  async request(method, endpoint, body = null) {
    const options = {
      method,
      headers: {
        'Authorization': `Bearer ${this.token}`,
        'Content-Type': 'application/json',
        'X-IA-ID': this.iaId,
        'X-IA-Name': this.iaName
      }
    };
    if (body) options.body = JSON.stringify(body);
    const response = await fetch(`${this.baseUrl}${endpoint}`, options);
    if (!response.ok) throw new Error(`API ${method} ${endpoint} - ${response.status}`);
    return response.json();
  }

  /* ---------- Event system ---------- */
  on(event, callback) {
    if (!this.eventListeners.has(event)) this.eventListeners.set(event, []);
    this.eventListeners.get(event).push(callback);
    return this;
  }
  off(event, callback) {
    if (!this.eventListeners.has(event)) return this;
    const arr = this.eventListeners.get(event).filter(cb => cb !== callback);
    this.eventListeners.set(event, arr);
    return this;
  }
  emit(event, data) {
    (this.eventListeners.get(event) || []).forEach(cb => {
      try { cb(data); } catch (e) { console.error('[IAConnector] listener error', e); }
    });
  }
}

/* Export global */
window.IAConnector = IAConnector;

/* Auto-init si config presente */
if (window.IA_CONFIG) {
  window.iaInstance = new IAConnector(window.IA_CONFIG);
  window.iaInstance.authenticate()
    .then(() => window.iaInstance.connectWebSocket())
    .catch(err => console.error('[IAConnector] Init failed', err));
}
