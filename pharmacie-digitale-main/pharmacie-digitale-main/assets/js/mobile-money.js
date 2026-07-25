/* ============================================================
   PHARMACIE DIGITALE - MOBILE MONEY GATEWAY
   Wave / Orange Money / Moov / MTN MoMo
   ============================================================ */

class MobileMoneyGateway {
  constructor(provider, credentials = {}) {
    this.provider = provider;
    this.credentials = credentials;
    this.config = this.getProviderConfig(provider);
  }

  getProviderConfig(provider) {
    const configs = {
      wave: {
        name:    'Wave',
        apiUrl:  'https://api.wave.com/v1',
        authType:'api_key',
        currency:'XOF'
      },
      orange: {
        name:    'Orange Money',
        apiUrl:  'https://api.orange.com/orange-money-webpay/dev/v1',
        authType:'oauth2',
        currency:'XOF'
      },
      moov: {
        name:    'Moov Money',
        apiUrl:  'https://api.moov.com/v1',
        authType:'api_key',
        currency:'XOF'
      },
      mtn: {
        name:    'MTN Mobile Money',
        apiUrl:  'https://sandbox.momodeveloper.mtn.com/collection/v1_0',
        authType:'oauth2',
        currency:'XOF'
      }
    };
    const cfg = configs[provider];
    if (!cfg) throw new Error(`Provider inconnu : ${provider}`);
    return cfg;
  }

  getToken() {
    return this.credentials.token || this.credentials.api_key || '';
  }

  /* ---------- Initiate payment ---------- */
  async initiatePayment({ amount, phoneNumber, description, callbackUrl }) {
    const payload = {
      amount,
      currency: this.config.currency,
      phone_number: phoneNumber,
      description,
      callback_url: callbackUrl || `${window.location.origin}/api/payments/callback`
    };

    const response = await fetch(`${this.config.apiUrl}/payments`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.getToken()}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });
    return response.json();
  }

  /* ---------- Verify payment ---------- */
  async verifyPayment(transactionId) {
    const response = await fetch(`${this.config.apiUrl}/payments/${transactionId}`, {
      headers: { 'Authorization': `Bearer ${this.getToken()}` }
    });
    return response.json();
  }

  /* ---------- Refund ---------- */
  async refund(transactionId, amount) {
    const response = await fetch(`${this.config.apiUrl}/payments/${transactionId}/refund`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.getToken()}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ amount })
    });
    return response.json();
  }
}

window.MobileMoneyGateway = MobileMoneyGateway;
