# Pharmacie Digitale

Plateforme SaaS Cloud de gestion de pharmacies avec verification de stock en temps reel pour patients, comptabilite SYSCOHADA et API IA universelle.

## Fonctionnalites

- **Recherche de medicaments** en temps reel dans les pharmacies partenaires
- **Gestion complete** : Stock, POS, Ordonnances, Fournisseurs
- **Comptabilite SYSCOHADA** integree (plan comptable OHADA)
- **Mobile Money** : Wave, Orange Money, Moov Money, MTN MoMo
- **Alertes intelligentes** : peremption, rupture, stock bas
- **API IA universelle** : connecteur pour ChatGPT, Claude, Kimi, etc.
- **Multi-officines** : gestion de reseaux et franchises
- **App mobile** SANA pour scan et ventes rapides

## Pays supportes

RDC, Rwanda, Burundi, Ouganda, Kenya, Tanzanie, Cameroun, Cote d'Ivoire, Benin, Senegal, et le reste du monde.

## Tarification

- **Benin** : 10 USD par pharmacie / mois (environ 6 000 FCFA)
- **Autres pays** : 2 500 FCFA par pharmacie / mois
- **Clients (patients)** : gratuit pour toujours

## Stack technique

- HTML5, CSS3, Bootstrap 5
- JavaScript ES6 (modulaire, classes)
- FontAwesome + Lucide Icons
- Google Fonts (Inter + Space Grotesk)
- AOS Animation
- Chart.js (BI)

## Structure du projet

```
.
├── index.html                       # Page d'accueil (identite graphique de reference)
├── register.html                    # Page d'inscription
├── assets/
│   ├── css/
│   │   ├── style.css                # Design system global
│   │   └── register.css             # Styles specifiques inscription
│   └── js/
│       ├── main.js                  # Initialisation globale
│       ├── countries.js             # Base de donnees pays / prefixes
│       ├── register.js              # Logique du formulaire d'inscription
│       ├── ia-connector.js          # Connecteur IA universel
│       ├── stock-manager.js         # Module gestion stock
│       ├── accounting-syscohada.js  # Comptabilite OHADA
│       └── mobile-money.js          # Passerelles Mobile Money
└── README.md
```

## Demarrage rapide

Ouvrez `index.html` ou `register.html` directement dans votre navigateur (aucune compilation requise).

Pour un environnement local :

```bash
python3 -m http.server 8080
# puis http://localhost:8080
```

## Contact developpeur

**Moukoddi Sadikou**

- Telephone : +229 01 97 48 88 05
- WhatsApp  : +229 97 48 88 05
- Email     : moukoddims@gmail.com

---

Developpe avec passion par Moukoddi.
