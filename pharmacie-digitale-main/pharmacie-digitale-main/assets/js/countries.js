/* ============================================================
   PHARMACIE DIGITALE - COUNTRIES DATABASE
   Codes ISO, drapeaux emoji, prefixes telephoniques
   ============================================================ */

window.COUNTRIES = [
  // Afrique prioritaire (spec)
  { code: 'CD', name: 'RD Congo',       flag: '🇨🇩', prefix: '+243', priority: true },
  { code: 'RW', name: 'Rwanda',         flag: '🇷🇼', prefix: '+250', priority: true },
  { code: 'BI', name: 'Burundi',        flag: '🇧🇮', prefix: '+257', priority: true },
  { code: 'UG', name: 'Ouganda',        flag: '🇺🇬', prefix: '+256', priority: true },
  { code: 'KE', name: 'Kenya',          flag: '🇰🇪', prefix: '+254', priority: true },
  { code: 'TZ', name: 'Tanzanie',       flag: '🇹🇿', prefix: '+255', priority: true },
  { code: 'CM', name: 'Cameroun',       flag: '🇨🇲', prefix: '+237', priority: true },
  { code: 'CI', name: "Cote d'Ivoire",  flag: '🇨🇮', prefix: '+225', priority: true },
  { code: 'BJ', name: 'Benin',          flag: '🇧🇯', prefix: '+229', priority: true },
  { code: 'SN', name: 'Senegal',        flag: '🇸🇳', prefix: '+221', priority: true },

  // Reste de l'Afrique
  { code: 'TG', name: 'Togo',           flag: '🇹🇬', prefix: '+228' },
  { code: 'BF', name: 'Burkina Faso',   flag: '🇧🇫', prefix: '+226' },
  { code: 'ML', name: 'Mali',           flag: '🇲🇱', prefix: '+223' },
  { code: 'NE', name: 'Niger',          flag: '🇳🇪', prefix: '+227' },
  { code: 'GN', name: 'Guinee',         flag: '🇬🇳', prefix: '+224' },
  { code: 'GA', name: 'Gabon',          flag: '🇬🇦', prefix: '+241' },
  { code: 'CG', name: 'Congo',          flag: '🇨🇬', prefix: '+242' },
  { code: 'TD', name: 'Tchad',          flag: '🇹🇩', prefix: '+235' },
  { code: 'CF', name: 'RCA',            flag: '🇨🇫', prefix: '+236' },
  { code: 'MA', name: 'Maroc',          flag: '🇲🇦', prefix: '+212' },
  { code: 'DZ', name: 'Algerie',        flag: '🇩🇿', prefix: '+213' },
  { code: 'TN', name: 'Tunisie',        flag: '🇹🇳', prefix: '+216' },
  { code: 'EG', name: 'Egypte',         flag: '🇪🇬', prefix: '+20'  },
  { code: 'NG', name: 'Nigeria',        flag: '🇳🇬', prefix: '+234' },
  { code: 'GH', name: 'Ghana',          flag: '🇬🇭', prefix: '+233' },
  { code: 'ZA', name: 'Afrique du Sud', flag: '🇿🇦', prefix: '+27'  },

  // Europe
  { code: 'FR', name: 'France',         flag: '🇫🇷', prefix: '+33'  },
  { code: 'BE', name: 'Belgique',       flag: '🇧🇪', prefix: '+32'  },
  { code: 'CH', name: 'Suisse',         flag: '🇨🇭', prefix: '+41'  },
  { code: 'DE', name: 'Allemagne',      flag: '🇩🇪', prefix: '+49'  },
  { code: 'ES', name: 'Espagne',        flag: '🇪🇸', prefix: '+34'  },
  { code: 'IT', name: 'Italie',         flag: '🇮🇹', prefix: '+39'  },
  { code: 'GB', name: 'Royaume-Uni',    flag: '🇬🇧', prefix: '+44'  },
  { code: 'NL', name: 'Pays-Bas',       flag: '🇳🇱', prefix: '+31'  },
  { code: 'PT', name: 'Portugal',       flag: '🇵🇹', prefix: '+351' },

  // Ameriques
  { code: 'US', name: 'Etats-Unis',     flag: '🇺🇸', prefix: '+1'   },
  { code: 'CA', name: 'Canada',         flag: '🇨🇦', prefix: '+1'   },
  { code: 'BR', name: 'Bresil',         flag: '🇧🇷', prefix: '+55'  },
  { code: 'MX', name: 'Mexique',        flag: '🇲🇽', prefix: '+52'  },

  // Asie / Moyen-Orient
  { code: 'CN', name: 'Chine',          flag: '🇨🇳', prefix: '+86'  },
  { code: 'IN', name: 'Inde',           flag: '🇮🇳', prefix: '+91'  },
  { code: 'JP', name: 'Japon',          flag: '🇯🇵', prefix: '+81'  },
  { code: 'KR', name: 'Coree du Sud',   flag: '🇰🇷', prefix: '+82'  },
  { code: 'SA', name: 'Arabie Saoudite',flag: '🇸🇦', prefix: '+966' },
  { code: 'AE', name: 'Emirats AU',     flag: '🇦🇪', prefix: '+971' },
  { code: 'TR', name: 'Turquie',        flag: '🇹🇷', prefix: '+90'  },

  // Oceanie
  { code: 'AU', name: 'Australie',      flag: '🇦🇺', prefix: '+61'  },
  { code: 'NZ', name: 'Nouvelle-Zelande', flag: '🇳🇿', prefix: '+64' }
];
