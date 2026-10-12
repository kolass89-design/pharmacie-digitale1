#!/usr/bin/env python3
"""
Oak International School - Download Portal Server
Serves a clean, responsive HTML download hub with direct download buttons
for all PDF, Word, and ZIP files, bound to 0.0.0.0:8080 for live preview.
"""

import http.server
import socketserver
import os
import urllib.parse

PORT = 8080
DIRECTORY = "/home/user/pharmacie-digitale1"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oak International School — Portail de Téléchargement Mathématiques</title>
    <style>
        :root {
            --navy: #0B2545;
            --blue: #134074;
            --gold: #C59B27;
            --light: #F4F6F9;
            --card-bg: #FFFFFF;
            --text: #1D2D44;
            --green: #2E7D32;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
        body { background: var(--light); color: var(--text); padding-bottom: 50px; }
        
        header {
            background: var(--navy);
            color: white;
            padding: 30px 20px;
            text-align: center;
            border-bottom: 4px solid var(--gold);
        }
        header h1 { font-size: 26px; margin-bottom: 8px; letter-spacing: 0.5px; }
        header p { font-size: 14px; opacity: 0.9; max-width: 800px; margin: 0 auto; line-height: 1.4; }
        
        .container { max-width: 1100px; margin: 30px auto; padding: 0 20px; }
        
        .zip-card {
            background: linear-gradient(135deg, #0B2545 0%, #134074 100%);
            color: white;
            border-radius: 12px;
            padding: 25px 30px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 15px rgba(11, 37, 69, 0.15);
            margin-bottom: 35px;
            border-left: 6px solid var(--gold);
        }
        .zip-info h2 { font-size: 20px; margin-bottom: 6px; }
        .zip-info p { font-size: 13px; opacity: 0.85; }
        .btn-zip {
            background: var(--gold);
            color: #000;
            padding: 14px 26px;
            text-decoration: none;
            font-weight: bold;
            font-size: 14px;
            border-radius: 8px;
            white-space: nowrap;
            transition: transform 0.2s, background 0.2s;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }
        .btn-zip:hover { background: #dcb336; transform: translateY(-2px); }
        
        .section-title {
            font-size: 20px;
            color: var(--navy);
            margin-bottom: 18px;
            display: flex;
            align-items: center;
            gap: 10px;
            border-bottom: 2px solid #E2E8F0;
            padding-bottom: 8px;
        }
        
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 18px;
            margin-bottom: 40px;
        }
        
        .card {
            background: var(--card-bg);
            border-radius: 10px;
            border: 1px solid #E2E8F0;
            padding: 20px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.04);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 10px;
        }
        .badge {
            background: #E8EEF5;
            color: var(--navy);
            font-size: 10px;
            font-weight: 700;
            padding: 4px 8px;
            border-radius: 4px;
            text-transform: uppercase;
        }
        .card h3 { font-size: 16px; color: var(--navy); margin-bottom: 6px; }
        .card p { font-size: 12px; color: #555; line-height: 1.4; margin-bottom: 16px; flex-grow: 1; }
        
        .actions {
            display: flex;
            gap: 10px;
        }
        .btn {
            flex: 1;
            text-align: center;
            padding: 9px 12px;
            border-radius: 6px;
            text-decoration: none;
            font-size: 12px;
            font-weight: 600;
            transition: all 0.2s;
        }
        .btn-pdf {
            background: #E53935;
            color: white;
        }
        .btn-pdf:hover { background: #C62828; }
        .btn-docx {
            background: #1976D2;
            color: white;
        }
        .btn-docx:hover { background: #1565C0; }
        
        footer {
            text-align: center;
            font-size: 12px;
            color: #888;
            margin-top: 40px;
        }
    </style>
</head>
<body>

<header>
    <h1>OAK INTERNATIONAL SCHOOL</h1>
    <p>Centre de Téléchargement des Documents &bull; Dual Mathematics Continuum (IB & Bénin APC)</p>
</header>

<div class="container">

    <!-- Grand bouton Pack Complet ZIP -->
    <div class="zip-card">
        <div class="zip-info">
            <h2>📦 Pack Complet de Téléchargement (ZIP)</h2>
            <p>Contient les 7 Cahiers d'Activités PDF, tous les fichiers Word (.docx), les 6 rapports officiels et les corrigés détaillés (1.9 Mo).</p>
        </div>
        <a href="oak_curriculum_complete_package.zip" download="oak_curriculum_complete_package.zip" class="btn-zip">
            Télécharger Tout le Pack (.ZIP)
        </a>
    </div>

    <!-- Section 1 : Les 7 Cahiers d'activités -->
    <h2 class="section-title">📘 Les 7 Cahiers d'Activités (Workbooks Premium A4)</h2>
    <div class="grid">
        
        <!-- CM2 -->
        <div class="card">
            <div class="card-header">
                <span class="badge">Primaire / MYP 1</span>
                <span style="font-size:11px;color:#888;">10–11 ans</span>
            </div>
            <h3>1. CM2 / IB MYP 1</h3>
            <p>Nombres jusqu'au milliard, 4 opérations, fractions de quantités, arithmétique commerciale (bénéfice/perte), volumes, équivalence métrique et préparation CEP.</p>
            <div class="actions">
                <a href="workbook_01_cm2_myp1.pdf" download class="btn btn-pdf">Télécharger PDF</a>
                <a href="workbook_01_cm2_myp1.docx" download class="btn btn-docx">Fichier Word</a>
            </div>
        </div>

        <!-- 6ème -->
        <div class="card">
            <div class="card-header">
                <span class="badge">Collège / MYP 2</span>
                <span style="font-size:11px;color:#888;">11–12 ans</span>
            </div>
            <h3>2. Sixième / IB MYP 2</h3>
            <p>Géométrie synthétique, médiatrice, symétrie axiale, nombres premiers et PGCD/PPCM, pavé droit/cube et pont vers les entiers relatifs.</p>
            <div class="actions">
                <a href="workbook_02_sixieme_myp2.pdf" download class="btn btn-pdf">Télécharger PDF</a>
                <a href="workbook_02_sixieme_myp2.docx" download class="btn btn-docx">Fichier Word</a>
            </div>
        </div>

        <!-- 5ème -->
        <div class="card">
            <div class="card-header">
                <span class="badge">Collège / MYP 3</span>
                <span style="font-size:11px;color:#888;">12–13 ans</span>
            </div>
            <h3>3. Cinquième / IB MYP 3</h3>
            <p>Opérations sur les relatifs (Z), puissances de 10, notation scientifique, angles alternes-internes, somme des angles (180°), symétrie centrale et parallélogrammes.</p>
            <div class="actions">
                <a href="workbook_03_cinquieme_myp3.pdf" download class="btn btn-pdf">Télécharger PDF</a>
                <a href="workbook_03_cinquieme_myp3.docx" download class="btn btn-docx">Fichier Word</a>
            </div>
        </div>

        <!-- 4ème -->
        <div class="card">
            <div class="card-header">
                <span class="badge">Collège / MYP 4</span>
                <span style="font-size:11px;color:#888;">13–14 ans</span>
            </div>
            <h3>4. Quatrième / IB MYP 4</h3>
            <p>Théorème de Pythagore et sa réciproque, rationnels (Q), calcul littéral, équations, trigonométrie (cosinus), vecteurs et relation de Chasles, pyramides et cônes.</p>
            <div class="actions">
                <a href="workbook_04_quatrieme_myp4.pdf" download class="btn btn-pdf">Télécharger PDF</a>
                <a href="workbook_04_quatrieme_myp4.docx" download class="btn btn-docx">Fichier Word</a>
            </div>
        </div>

        <!-- 3ème -->
        <div class="card">
            <div class="card-header">
                <span class="badge">Diplôme BEPC / MYP 5</span>
                <span style="font-size:11px;color:#888;">14–15 ans</span>
            </div>
            <h3>5. Troisième / IB MYP 5</h3>
            <p>Théorème de Thalès, réels (R), calcul sur radicaux et conjugué, factorisation complète, systèmes linéaires 2x2, géométrie analytique plane et épreuve BEPC officielle.</p>
            <div class="actions">
                <a href="workbook_05_troisieme_myp5.pdf" download class="btn btn-pdf">Télécharger PDF</a>
                <a href="workbook_05_troisieme_myp5.docx" download class="btn btn-docx">Fichier Word</a>
            </div>
        </div>

        <!-- 2nde -->
        <div class="card">
            <div class="card-header">
                <span class="badge">Lycée / DP 1</span>
                <span style="font-size:11px;color:#888;">15–16 ans</span>
            </div>
            <h3>6. Seconde / IB DP 1</h3>
            <p>Trinôme du second degré (Delta), fonctions numériques et transformations, produit scalaire 2D, Al-Kashi, trigonométrie en radians et initiation calculatrice GDC.</p>
            <div class="actions">
                <a href="workbook_06_seconde_dp1.pdf" download class="btn btn-pdf">Télécharger PDF</a>
                <a href="workbook_06_seconde_dp1.docx" download class="btn btn-docx">Fichier Word</a>
            </div>
        </div>

        <!-- 1ère -->
        <div class="card">
            <div class="card-header">
                <span class="badge">Pré-Bac / DP 2</span>
                <span style="font-size:11px;color:#888;">16–17 ans</span>
            </div>
            <h3>7. Première / IB DP 2</h3>
            <p>Calcul différentiel (dérivées, tangentes, extremums), étude de courbes avec asymptotes, suites numériques, barycentres et lignes de niveau, combinatoire et probabilités.</p>
            <div class="actions">
                <a href="workbook_07_premiere_dp2.pdf" download class="btn btn-pdf">Télécharger PDF</a>
                <a href="workbook_07_premiere_dp2.docx" download class="btn btn-docx">Fichier Word</a>
            </div>
        </div>

    </div>

    <!-- Section 2 : Rapports et Cadres Pédagogiques -->
    <h2 class="section-title">📑 Rapports Officiels & Cadres d'Harmonisation</h2>
    <div class="grid">
        
        <div class="card">
            <h3>Rapport de Recherche Curriculaire</h3>
            <p>Analyse statutaire des programmes du Ministère (MEMP/MESTFP) et de l'IB (MYP/DP), fiabilité des sources et faisabilité.</p>
            <div class="actions">
                <a href="01_research_report.pdf" download class="btn btn-pdf">Télécharger PDF</a>
                <a href="01_research_report.docx" download class="btn btn-docx">Fichier Word</a>
            </div>
        </div>

        <div class="card">
            <h3>Inventaire des 20 Domaines Mathématiques</h3>
            <p>Inventaire exhaustif des contenus introduits, consolidés ou étendus pour les 7 niveaux d'Oak.</p>
            <div class="actions">
                <a href="02_seven_level_curriculum_inventory.pdf" download class="btn btn-pdf">Télécharger PDF</a>
                <a href="02_seven_level_curriculum_inventory.docx" download class="btn btn-docx">Fichier Word</a>
            </div>
        </div>

        <div class="card">
            <h3>Matrice d'Alignement IB-APC</h3>
            <p>Tableau comparatif détaillé notion par notion ([DIR], [PAR], [SEQ], [GAP]) avec prérequis et stratégies.</p>
            <div class="actions">
                <a href="03_curriculum_alignment_matrix.pdf" download class="btn btn-pdf">Télécharger PDF</a>
                <a href="03_curriculum_alignment_matrix.docx" download class="btn btn-docx">Fichier Word</a>
            </div>
        </div>

        <div class="card">
            <h3>Stratégie d'Harmonisation Pédagogique</h3>
            <p>Modèle d'enseignement unifié sur les 13 dimensions clés sans compromis sur aucun des deux programmes.</p>
            <div class="actions">
                <a href="04_harmonisation_strategy.pdf" download class="btn btn-pdf">Télécharger PDF</a>
                <a href="04_harmonisation_strategy.docx" download class="btn btn-docx">Fichier Word</a>
            </div>
        </div>

        <div class="card">
            <h3>Planification Scope & Sequence</h3>
            <p>Progression pédagogique trimestre par trimestre pour les 7 classes d'Oak International School.</p>
            <div class="actions">
                <a href="05_harmonised_scope_and_sequence.pdf" download class="btn btn-pdf">Télécharger PDF</a>
                <a href="05_harmonised_scope_and_sequence.docx" download class="btn btn-docx">Fichier Word</a>
            </div>
        </div>

        <div class="card">
            <h3>Rapport d'Assurance Qualité & Audit</h3>
            <p>Certification finale d'exactitude mathématique, de calculs vérifiés et recommandations stratégiques.</p>
            <div class="actions">
                <a href="07_quality_assurance_report.pdf" download class="btn btn-pdf">Télécharger PDF</a>
                <a href="07_quality_assurance_report.docx" download class="btn btn-docx">Fichier Word</a>
            </div>
        </div>

    </div>

</div>

<footer>
    <p>Oak International School &bull; Département de Mathématiques &bull; Année Académique 2026–2027 &bull; Cotonou, Bénin</p>
</footer>

</body>
</html>
"""

class PortalHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Serve custom portal on root
        if self.path in ['/', '/index.html']:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            encoded = HTML_TEMPLATE.encode('utf-8')
            self.send_header('Content-Length', str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)
            return
        
        # Trigger attachment download for PDF, DOCX, ZIP if queried or directly
        return super().do_GET()

def main():
    with socketserver.TCPServer(("0.0.0.0", PORT), PortalHandler) as httpd:
        print(f"Download portal server running on http://0.0.0.0:{PORT}")
        httpd.serve_forever()

if __name__ == '__main__':
    main()
