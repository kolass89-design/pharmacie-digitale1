/* ============================================================
   PHARMACIE DIGITALE - COMPTABILITE SYSCOHADA
   Plan comptable OHADA + ecritures automatiques
   ============================================================ */

class SyscohadaAccounting {
  constructor(pharmacyId) {
    this.pharmacyId = pharmacyId;
    this.entries = [];
    this.chartOfAccounts = this.loadChartOfAccounts();
  }

  loadChartOfAccounts() {
    return {
      '601': { label: 'Achats de marchandises',      type: 'charge'  },
      '603': { label: 'Variation des stocks',        type: 'charge'  },
      '605': { label: 'Autres achats',               type: 'charge'  },
      '641': { label: 'Charges de personnel',        type: 'charge'  },
      '661': { label: 'Charges financieres',         type: 'charge'  },
      '701': { label: 'Ventes de marchandises',      type: 'produit' },
      '706': { label: 'Services vendus',             type: 'produit' },
      '443': { label: 'TVA collectee',               type: 'passif'  },
      '445': { label: 'TVA deductible',              type: 'actif'   },
      '521': { label: 'Banques',                     type: 'actif'   },
      '531': { label: 'Cheques postaux',             type: 'actif'   },
      '571': { label: 'Caisse',                      type: 'actif'   },
      '311': { label: 'Marchandises',                type: 'actif'   },
      '401': { label: 'Fournisseurs',                type: 'passif'  },
      '411': { label: 'Clients',                     type: 'actif'   }
    };
  }

  /* ---------- Enregistrement d'une vente ---------- */
  async recordSale(saleData) {
    const entries = [];
    const tvaRate = saleData.tva_rate ?? 0.18;
    const totalHT = saleData.total_ht ?? saleData.total / (1 + tvaRate);
    const tva     = saleData.tva     ?? (totalHT * tvaRate);
    const totalTTC= saleData.total_ttc ?? (totalHT + tva);

    entries.push({
      date: saleData.date,
      account: '701',
      label: `Vente ${saleData.invoice_number}`,
      debit: 0,
      credit: totalHT
    });

    if (tva > 0) {
      entries.push({
        date: saleData.date,
        account: '443',
        label: `TVA vente ${saleData.invoice_number}`,
        debit: 0,
        credit: tva
      });
    }

    const cashAccount = ['cash', 'espece'].includes(saleData.payment_method) ? '571' : '521';
    entries.push({
      date: saleData.date,
      account: cashAccount,
      label: `Encaissement ${saleData.invoice_number}`,
      debit: totalTTC,
      credit: 0
    });

    return this.saveEntries(entries);
  }

  /* ---------- Enregistrement d'un achat ---------- */
  async recordPurchase(purchaseData) {
    const entries = [];
    const tvaRate = purchaseData.tva_rate ?? 0.18;
    const totalHT = purchaseData.total_ht ?? purchaseData.total / (1 + tvaRate);
    const tva     = purchaseData.tva     ?? (totalHT * tvaRate);
    const totalTTC= purchaseData.total_ttc ?? (totalHT + tva);

    entries.push({
      date: purchaseData.date,
      account: '601',
      label: `Achat ${purchaseData.invoice_number}`,
      debit: totalHT,
      credit: 0
    });

    if (tva > 0) {
      entries.push({
        date: purchaseData.date,
        account: '445',
        label: `TVA achat ${purchaseData.invoice_number}`,
        debit: tva,
        credit: 0
      });
    }

    entries.push({
      date: purchaseData.date,
      account: '401',
      label: `Fournisseur ${purchaseData.supplier_name}`,
      debit: 0,
      credit: totalTTC
    });

    return this.saveEntries(entries);
  }

  /* ---------- Persistence (local + API) ---------- */
  async saveEntries(entries) {
    this.entries.push(...entries);
    // Persist localement
    const key = `syscohada_${this.pharmacyId}`;
    localStorage.setItem(key, JSON.stringify(this.entries));
    return entries;
  }

  loadEntriesFromStorage() {
    const key = `syscohada_${this.pharmacyId}`;
    const raw = localStorage.getItem(key);
    this.entries = raw ? JSON.parse(raw) : [];
    return this.entries;
  }

  /* ---------- Rapports ---------- */
  calculateBalance(account, entries = this.entries) {
    return entries
      .filter(e => e.account === account)
      .reduce((sum, e) => sum + (e.debit || 0) - (e.credit || 0), 0);
  }

  getEntriesBetween(startDate, endDate) {
    return this.entries.filter(e => {
      const d = new Date(e.date);
      return d >= startDate && d <= endDate;
    });
  }

  generateMonthlyReport(month, year) {
    const start = new Date(year, month - 1, 1);
    const end   = new Date(year, month, 0, 23, 59, 59);
    const entries = this.getEntriesBetween(start, end);

    return {
      period: `${String(month).padStart(2, '0')}/${year}`,
      total_sales:      entries.filter(e => e.account === '701').reduce((s, e) => s + e.credit, 0),
      total_purchases:  entries.filter(e => e.account === '601').reduce((s, e) => s + e.debit,  0),
      tva_collected:    entries.filter(e => e.account === '443').reduce((s, e) => s + e.credit, 0),
      tva_deductible:   entries.filter(e => e.account === '445').reduce((s, e) => s + e.debit,  0),
      tva_due:          entries.filter(e => e.account === '443').reduce((s, e) => s + e.credit, 0)
                       - entries.filter(e => e.account === '445').reduce((s, e) => s + e.debit,  0),
      cash_balance:     this.calculateBalance('571', entries),
      bank_balance:     this.calculateBalance('521', entries)
    };
  }

  /* ---------- Export ---------- */
  exportCsv() {
    const headers = ['Date', 'Compte', 'Libelle', 'Debit', 'Credit'];
    const rows = this.entries.map(e => [
      e.date, e.account, e.label, e.debit || 0, e.credit || 0
    ]);
    return [headers, ...rows].map(r => r.join(';')).join('\n');
  }
}

window.SyscohadaAccounting = SyscohadaAccounting;
