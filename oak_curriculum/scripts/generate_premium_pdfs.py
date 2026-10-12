#!/usr/bin/env python3
"""
Oak International School - Premium PDF Publishing Engine
Produces publisher-grade, print-ready A4 workbooks and curriculum reports.
"""

import os
import re
import pymupdf  # PyMuPDF
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

# Brand Color Palette
COLOR_NAVY = colors.HexColor("#0B2545")       # Primary Oak Navy
COLOR_BLUE = colors.HexColor("#134074")       # Secondary Slate Blue
COLOR_ACCENT = colors.HexColor("#C59B27")     # Elegant Gold Accent
COLOR_TEAL = colors.HexColor("#007A78")       # Section & badge teal
COLOR_PURPLE = colors.HexColor("#4A2574")     # Level 4 badge purple
COLOR_DARK = colors.HexColor("#1D2D44")       # Body text dark slate
COLOR_LIGHT_BG = colors.HexColor("#F4F6F9")   # Soft callout box background
COLOR_BORDER = colors.HexColor("#D0D7DE")     # Clean grid border
COLOR_WHITE = colors.white

class PremiumNumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(PremiumNumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            if self._pageNumber > 1:
                self.draw_header_footer(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_header_footer(self, total_pages):
        self.saveState()
        
        # Running Top Header
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(COLOR_NAVY)
        self.drawString(54, 802, "OAK INTERNATIONAL SCHOOL")
        self.setFont("Helvetica", 7.5)
        self.setFillColor(COLOR_BLUE)
        self.drawRightString(541, 802, "Dual Mathematics Continuum: IB & Benin APC")
        
        # Header rule
        self.setStrokeColor(COLOR_ACCENT)
        self.setLineWidth(1)
        self.line(54, 794, 541, 794)

        # Running Bottom Footer
        self.setStrokeColor(COLOR_BORDER)
        self.setLineWidth(0.5)
        self.line(54, 45, 541, 45)
        
        self.setFont("Helvetica", 7)
        self.setFillColor(colors.HexColor("#666666"))
        self.drawString(54, 34, "Oak International School | Department of Mathematics | 2026–2027 Academic Year")
        
        page_str = f"Page {self._pageNumber} of {total_pages}"
        self.setFont("Helvetica-Bold", 7.5)
        self.setFillColor(COLOR_NAVY)
        self.drawRightString(541, 34, page_str)
        
        self.restoreState()


def create_cover_page(title, grade_label, academic_year, version, code):
    elements = []
    
    # Top banner
    banner_data = [
        [Paragraph(f"<font size=11 color='#C59B27'><b>OAK INTERNATIONAL SCHOOL</b></font><br/>"
                   f"<font size=8 color='#FFFFFF'>EXCELLENCE ENSEMBLE &bull; DUAL CURRICULUM MATHEMATICS</font>",
                   ParagraphStyle('BannerText', alignment=1, textColor=COLOR_WHITE))]
    ]
    banner_table = Table(banner_data, colWidths=[487], rowHeights=[45])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_NAVY),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(banner_table)
    elements.append(Spacer(1, 35))

    # Badge Row
    badges_data = [
        [
            Paragraph("<b>IB MIDDLE YEARS & DIPLOMA</b>", ParagraphStyle('B1', fontName='Helvetica-Bold', fontSize=8, textColor=COLOR_NAVY, alignment=1)),
            Paragraph("<b>BENIN NATIONALE APC</b>", ParagraphStyle('B2', fontName='Helvetica-Bold', fontSize=8, textColor=COLOR_BLUE, alignment=1)),
            Paragraph("<b>BILINGUAL EN / FR</b>", ParagraphStyle('B3', fontName='Helvetica-Bold', fontSize=8, textColor=colors.HexColor("#7A5500"), alignment=1)),
        ]
    ]
    badge_table = Table(badges_data, colWidths=[162, 162, 163])
    badge_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor("#E8EEF5")),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor("#E2ECF8")),
        ('BACKGROUND', (2,0), (2,0), colors.HexColor("#FDF5E2")),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (0,0), 0.5, COLOR_NAVY),
        ('BOX', (1,0), (1,0), 0.5, COLOR_BLUE),
        ('BOX', (2,0), (2,0), 0.5, COLOR_ACCENT),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    elements.append(badge_table)
    elements.append(Spacer(1, 30))

    # Main Title
    elements.append(Paragraph("PREMIUM MATHEMATICS ACTIVITY WORKBOOK", 
                              ParagraphStyle('CoverSubtitle', fontName='Helvetica-Bold', fontSize=12, leading=14, textColor=COLOR_ACCENT, alignment=1)))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(grade_label.upper(), 
                              ParagraphStyle('CoverGrade', fontName='Helvetica-Bold', fontSize=23, leading=27, textColor=COLOR_NAVY, alignment=1)))
    elements.append(Spacer(1, 15))
    
    # Gold separator line
    elements.append(HRFlowable(width="60%", thickness=2, color=COLOR_ACCENT, spaceAfter=18, spaceBefore=4))

    elements.append(Paragraph("A Harmonised Dual-Curriculum Mathematics Learning Companion", 
                              ParagraphStyle('CoverDesc', fontName='Helvetica-Bold', fontSize=10.5, leading=14, textColor=COLOR_BLUE, alignment=1)))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph("Connecting Conceptual Inquiry, Axiomatic Proof, and Examination Mastery", 
                              ParagraphStyle('CoverDesc2', fontName='Helvetica-Oblique', fontSize=9, leading=12, textColor=COLOR_DARK, alignment=1)))
    elements.append(Spacer(1, 35))

    # Metadata Card
    meta_data = [
        [Paragraph("<b>Target Cohort:</b>", ParagraphStyle('M1', fontSize=8, textColor=COLOR_NAVY)),
         Paragraph(grade_label, ParagraphStyle('M2', fontSize=8, textColor=COLOR_DARK))],
        [Paragraph("<b>Academic Year:</b>", ParagraphStyle('M1', fontSize=8, textColor=COLOR_NAVY)),
         Paragraph(academic_year, ParagraphStyle('M2', fontSize=8, textColor=COLOR_DARK))],
        [Paragraph("<b>Curricular Alignment:</b>", ParagraphStyle('M1', fontSize=8, textColor=COLOR_NAVY)),
         Paragraph("International Baccalaureate & République du Bénin (MEMP/MESTFP)", ParagraphStyle('M2', fontSize=8, textColor=COLOR_DARK))],
        [Paragraph("<b>Publication Code:</b>", ParagraphStyle('M1', fontSize=8, textColor=COLOR_NAVY)),
         Paragraph(code, ParagraphStyle('M2', fontSize=8, textColor=COLOR_DARK))],
        [Paragraph("<b>Series Version:</b>", ParagraphStyle('M1', fontSize=8, textColor=COLOR_NAVY)),
         Paragraph(f"{version} (Classroom & Exam Certified)", ParagraphStyle('M2', fontSize=8, textColor=COLOR_DARK))],
    ]
    meta_table = Table(meta_data, colWidths=[120, 347])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, COLOR_NAVY),
        ('INNERGRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    elements.append(meta_table)
    elements.append(Spacer(1, 25))

    # Table of Contents Preview
    toc_data = [
        [Paragraph("<b>WORKBOOK TABLE OF CONTENTS / SOMMAIRE</b>", ParagraphStyle('TOCHead', fontName='Helvetica-Bold', fontSize=8.5, textColor=COLOR_NAVY, alignment=1))],
        [Paragraph("&bull; <b>Section A:</b> Student Introduction & Dual-Curriculum Philosophy<br/>"
                   "&bull; <b>Section B:</b> Bilingual Mathematical Glossary (Technical Lexicon & Pitfalls)<br/>"
                   "&bull; <b>Section C:</b> Shared Conceptual Foundations (Theorems & Comparative Models)<br/>"
                   "&bull; <b>Section D:</b> Contextualised 6-Step Bridging Activities (Real-World Scenarios)<br/>"
                   "&bull; <b>Section E:</b> 5-Level Progressive Practice (From Foundations to Exam Challenge)<br/>"
                   "&bull; <b>Section F:</b> Integrated Application Tasks (Authentic Complex Problems)<br/>"
                   "&bull; <b>Section G:</b> Programme-Specific Reinforcement (IB Inquiry & Beninese Exams)<br/>"
                   "&bull; <b>Section H:</b> Assessment, Diagnostics, Reflection & Complete Worked Solutions",
                   ParagraphStyle('TOCText', fontName='Helvetica', fontSize=8, leading=11.5, textColor=COLOR_DARK))]
    ]
    toc_table = Table(toc_data, colWidths=[487])
    toc_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor("#EAEFF5")),
        ('BACKGROUND', (0,1), (0,1), colors.white),
        ('BOX', (0,0), (-1,-1), 1, COLOR_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    elements.append(toc_table)

    elements.append(PageBreak())
    return elements


def clean_math_to_unicode(text):
    """Converts LaTeX math commands into beautiful, clean Unicode characters."""
    t = text
    
    # Clean control characters (like formfeed \x0c)
    t = t.replace('\x0c', '')

    # Common non-breaking spaces
    t = t.replace(r'\ ', ' ')

    # Specific common macros
    t = re.sub(r'\\(?:text|mathbf|mathrm)\{([^{}]+)\}', r'\1', t)
    
    # Fractions: \frac{a}{b} -> (a / b)
    t = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', r'(\1 / \2)', t)
    t = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', r'(\1 / \2)', t) # nested
    
    # Square root
    t = re.sub(r'\\sqrt\{([^{}]+)\}', r'√(\1)', t)
    t = re.sub(r'\\sqrt\[([^{}]+)\]\{([^{}]+)\}', r'^{\1}√(\2)', t)
    
    # Vectors
    t = re.sub(r'\\vec\{([A-Za-z0-9_]+)\}', r'\1⃗', t)
    
    # Angles
    t = re.sub(r'\\widehat\{([A-Za-z0-9_]+)\}', r'∠\1', t)
    
    # Greek letters
    t = t.replace(r'\Delta', 'Δ').replace(r'\theta', 'θ').replace(r'\pi', 'π')
    t = t.replace(r'\alpha', 'α').replace(r'\beta', 'β').replace(r'\phi', 'φ')
    t = t.replace(r'\sigma', 'σ').replace(r'\mu', 'μ')
    
    # Operators & relations
    t = t.replace(r'\times', '×').replace(r'\div', '÷').replace(r'\pm', '±')
    t = t.replace(r'\le', '≤').replace(r'\ge', '≥').replace(r'\neq', '≠')
    t = t.replace(r'\approx', '≈').replace(r'\dots', '...')
    t = t.replace(r'\in', '∈').replace(r'\notin', '∉')
    t = t.replace(r'\perp', '⊥').replace(r'\parallel', '∥')
    t = t.replace(r'\cap', '∩').replace(r'\cup', '∪')
    t = t.replace(r'\implies', '⇒').replace(r'\iff', '⇔')
    t = t.replace(r'\to', '→').replace(r'\infty', '∞')
    t = t.replace(r'\subset', '⊂')

    # Mathematical Sets (use bold capitals to render reliably in Helvetica)
    t = t.replace(r'\mathbb{N}', '<b>N</b>').replace(r'\mathbb{Z}', '<b>Z</b>')
    t = t.replace(r'\mathbb{D}', '<b>D</b>').replace(r'\mathbb{Q}', '<b>Q</b>')
    t = t.replace(r'\mathbb{R}', '<b>R</b>')
    t = t.replace('ℕ', '<b>N</b>').replace('ℤ', '<b>Z</b>')
    t = t.replace('𝔻', '<b>D</b>').replace('ℚ', '<b>Q</b>')
    t = t.replace('ℝ', '<b>R</b>')

    # Metric units and exponents
    t = t.replace('^2', '²').replace('^3', '³').replace('^4', '⁴')
    t = t.replace('^n', 'ⁿ').replace('^k', 'ᵏ')

    # Clean leftover formatting
    t = t.replace(r'\quad', '  ').replace(r'\,', ' ').replace(r'\;', ' ')
    t = t.replace(r'\left(', '(').replace(r'\right)', ')')
    t = t.replace(r'\{', '{').replace(r'\}', '}')
    t = t.replace('{', '').replace('}', '')
    t = t.replace(chr(92), '') # remove any dangling backslashes
    
    return t


def format_text_for_pdf(text):
    """Cleans markdown text and turns bold/symbols into clean HTML for ReportLab."""
    t = text.strip()
    
    if '$' in t or '\\' in t:
        t = clean_math_to_unicode(t)
    
    t = t.replace('$$', '').replace('$', '')
    
    # Markdown Bold: **word** -> <b>word</b>
    t = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', t)
    
    # Markdown Italic: *word* -> <i>word</i>
    t = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', t)
    
    # Protect XML entities
    t = t.replace('&amp;', '&').replace('&', '&amp;')
    t = t.replace('&amp;bull;', '&bull;')
    t = t.replace('&amp;le;', '&le;').replace('&amp;ge;', '&ge;')
    t = t.replace('&amp;times;', '&times;').replace('&amp;div;', '&div;')
    t = t.replace('&amp;nbsp;', '&nbsp;')
    
    return t


def build_premium_pdf(md_path, pdf_path, meta):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    style_h1 = ParagraphStyle(
        'SectionBanner',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=COLOR_WHITE
    )
    style_h2 = ParagraphStyle(
        'SubSection',
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13.5,
        textColor=COLOR_NAVY,
        spaceBefore=10,
        spaceAfter=3,
        keepWithNext=True
    )
    style_h3 = ParagraphStyle(
        'SubSubSection',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=COLOR_BLUE,
        spaceBefore=7,
        spaceAfter=2,
        keepWithNext=True
    )
    style_body = ParagraphStyle(
        'Body',
        fontName='Helvetica',
        fontSize=8,
        leading=11.5,
        textColor=COLOR_DARK,
        spaceBefore=2,
        spaceAfter=2.5
    )
    style_bullet = ParagraphStyle(
        'Bullet',
        parent=style_body,
        leftIndent=12,
        firstLineIndent=-8,
        spaceBefore=1,
        spaceAfter=1
    )

    story = []

    # 1. Cover Page
    story.extend(create_cover_page(
        title=meta.get('title', 'Activity Workbook'),
        grade_label=meta.get('grade', 'CM2 / MYP 1'),
        academic_year="2026–2027",
        version=meta.get('version', 'V1.0'),
        code=meta.get('code', 'OIS-WB-2026')
    ))

    # Helper table flush
    in_table = False
    table_rows = []

    def flush_table():
        nonlocal in_table, table_rows
        if not table_rows:
            in_table = False
            return
        
        num_cols = max(len(r) for r in table_rows)
        avail_width = 487

        if num_cols == 2:
            col_widths = [150, 337]
        elif num_cols == 3:
            col_widths = [130, 130, 227]
        elif num_cols == 4:
            col_widths = [100, 110, 157, 120]
        elif num_cols == 5:
            col_widths = [97] * 5
        else:
            col_widths = [avail_width / num_cols] * num_cols

        formatted_table = []
        for row_idx, r in enumerate(table_rows):
            is_header = (row_idx == 0)
            formatted_row = []
            for c_idx in range(num_cols):
                val = r[c_idx] if c_idx < len(r) else ""
                clean_text = format_text_for_pdf(val)
                
                if is_header:
                    p = Paragraph(f"<b>{clean_text}</b>", 
                                  ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=7.5, leading=9.5, textColor=COLOR_WHITE))
                else:
                    p = Paragraph(clean_text, 
                                  ParagraphStyle('TD', fontName='Helvetica', fontSize=7, leading=9, textColor=COLOR_DARK))
                formatted_row.append(p)
            formatted_table.append(formatted_row)

        t = Table(formatted_table, colWidths=col_widths, repeatRows=1)
        t_style = [
            ('BACKGROUND', (0,0), (-1,0), COLOR_NAVY),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
            ('RIGHTPADDING', (0,0), (-1,-1), 4),
            ('GRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ]
        for r_i in range(1, len(formatted_table)):
            if r_i % 2 == 1:
                t_style.append(('BACKGROUND', (0, r_i), (-1, r_i), colors.HexColor("#F8FAFC")))
        t.setStyle(TableStyle(t_style))

        story.append(t)
        story.append(Spacer(1, 6))
        table_rows = []
        in_table = False

    in_working_space = False

    for idx, line in enumerate(lines):
        raw = line.rstrip('\r\n')
        trimmed = raw.strip()

        # Skip top markdown titles
        if idx < 6 and (trimmed.startswith('# OAK') or trimmed.startswith('# PREMIUM') or trimmed.startswith('## Grade')):
            continue

        # Tables
        if trimmed.startswith('|') and trimmed.endswith('|'):
            if set(trimmed.replace('|', '').replace('-', '').replace(':', '').strip()) == set():
                continue
            cells = [c.strip() for c in trimmed.split('|')[1:-1]]
            table_rows.append(cells)
            in_table = True
            continue
        else:
            if in_table:
                flush_table()

        if not trimmed:
            continue

        # Ruled Working Space Lines (only once per exercise prompt)
        if 'Working space:' in trimmed or 'Espace de réponse' in trimmed or '_____' in trimmed:
            if not in_working_space:
                story.append(Paragraph("<font color='#666666' size=7><i>Student Working Space / Espace réservé à la rédaction de l'élève :</i></font>", style_body))
                for _ in range(3):
                    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#D3D3D3"), spaceBefore=6, spaceAfter=4))
                story.append(Spacer(1, 4))
                in_working_space = True
            continue

        in_working_space = False

        # Section Header (e.g. ## SECTION A — STUDENT INTRODUCTION)
        if trimmed.startswith('## SECTION'):
            sec_title = format_text_for_pdf(trimmed[3:])
            sec_table = Table([[Paragraph(f"<b>{sec_title}</b>", style_h1)]], colWidths=[487], rowHeights=[24])
            sec_table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), COLOR_NAVY),
                ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                ('LEFTPADDING', (0,0), (-1,-1), 8),
                ('RIGHTPADDING', (0,0), (-1,-1), 8),
                ('TOPPADDING', (0,0), (-1,-1), 3),
                ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ]))
            
            # Start major sections B, E, G, H on fresh page
            if any(trimmed.startswith(s) for s in ['## SECTION B', '## SECTION E', '## SECTION G', '## SECTION H']):
                story.append(PageBreak())
            else:
                story.append(Spacer(1, 10))
                
            story.append(sec_table)
            story.append(Spacer(1, 6))
            continue

        # Level Headings in Section E
        if trimmed.startswith('### Level '):
            level_text = format_text_for_pdf(trimmed[4:])
            if 'Level 1' in trimmed:
                badge_bg = colors.HexColor("#E2F0D9")
                badge_fg = colors.HexColor("#385723")
            elif 'Level 2' in trimmed:
                badge_bg = colors.HexColor("#DDEBF7")
                badge_fg = colors.HexColor("#1F4E79")
            elif 'Level 3' in trimmed:
                badge_bg = colors.HexColor("#FCE4D6")
                badge_fg = colors.HexColor("#C65911")
            elif 'Level 4' in trimmed:
                badge_bg = colors.HexColor("#EAE1F5")
                badge_fg = COLOR_PURPLE
            else:
                badge_bg = colors.HexColor("#FDE8E8")
                badge_fg = colors.HexColor("#C00000")

            lvl_table = Table([[Paragraph(f"<b>{level_text}</b>", 
                                          ParagraphStyle('LvlP', fontName='Helvetica-Bold', fontSize=8.5, textColor=badge_fg))]], 
                              colWidths=[487], rowHeights=[18])
            lvl_table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), badge_bg),
                ('BOX', (0,0), (-1,-1), 0.5, badge_fg),
                ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                ('LEFTPADDING', (0,0), (-1,-1), 6),
                ('TOPPADDING', (0,0), (-1,-1), 1),
                ('BOTTOMPADDING', (0,0), (-1,-1), 1),
            ]))
            story.append(Spacer(1, 6))
            story.append(lvl_table)
            story.append(Spacer(1, 4))
            continue

        # Headings
        if trimmed.startswith('### '):
            clean_sub = format_text_for_pdf(trimmed[4:])
            story.append(Paragraph(clean_sub, style_h2))
        elif trimmed.startswith('#### '):
            clean_sub = format_text_for_pdf(trimmed[5:])
            story.append(Paragraph(clean_sub, style_h3))
        elif trimmed.startswith('# '):
            clean_sub = format_text_for_pdf(trimmed[2:])
            story.append(Paragraph(clean_sub, style_h2))

        # Checkboxes
        elif trimmed.startswith('- [ ]'):
            clean_item = format_text_for_pdf(trimmed[5:])
            box_text = f"<font face='Helvetica-Bold' color='#0B2545'>[&nbsp;&nbsp;]</font> {clean_item}"
            story.append(Paragraph(box_text, style_bullet))

        # Bullets
        elif trimmed.startswith('- ') or trimmed.startswith('* '):
            clean_item = format_text_for_pdf(trimmed[2:])
            story.append(Paragraph(f"&bull; {clean_item}", style_bullet))

        # Numbered list
        elif (len(trimmed) > 2 and trimmed[0].isdigit() and trimmed[1] == '.') or (len(trimmed) > 3 and trimmed[:2].isdigit() and trimmed[2] == '.'):
            dot_pos = trimmed.find('.')
            num_part = trimmed[:dot_pos+1]
            rest_part = format_text_for_pdf(trimmed[dot_pos+1:])
            story.append(Paragraph(f"<b>{num_part}</b> {rest_part}", style_bullet))

        # Separator
        elif trimmed == '---':
            story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_BORDER, spaceBefore=4, spaceAfter=4))

        # Regular body text
        else:
            clean_p = format_text_for_pdf(trimmed)
            story.append(Paragraph(clean_p, style_body))

    if in_table:
        flush_table()

    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    doc.build(story, canvasmaker=PremiumNumberedCanvas)
    print(f"Generated Premium PDF: {pdf_path}")


def main():
    workbooks = [
        {
            "md": "oak_curriculum/workbooks/workbook_01_cm2_myp1.md",
            "pdf": "oak_curriculum/exports/pdf/workbook_01_cm2_myp1.pdf",
            "title": "CM2 / IB MYP 1 Activity Workbook",
            "grade": "CM2 / IB MYP 1 (Ages 10–11)",
            "version": "OIS-WB-CM2-MYP1-V1.0",
            "code": "OIS-MATH-01-CM2-MYP1"
        },
        {
            "md": "oak_curriculum/workbooks/workbook_02_sixieme_myp2.md",
            "pdf": "oak_curriculum/exports/pdf/workbook_02_sixieme_myp2.pdf",
            "title": "Sixième / IB MYP 2 Activity Workbook",
            "grade": "Sixième (6ème) / IB MYP 2 (Ages 11–12)",
            "version": "OIS-WB-6EME-MYP2-V1.0",
            "code": "OIS-MATH-02-6EME-MYP2"
        },
        {
            "md": "oak_curriculum/workbooks/workbook_03_cinquieme_myp3.md",
            "pdf": "oak_curriculum/exports/pdf/workbook_03_cinquieme_myp3.pdf",
            "title": "Cinquième / IB MYP 3 Activity Workbook",
            "grade": "Cinquième (5ème) / IB MYP 3 (Ages 12–13)",
            "version": "OIS-WB-5EME-MYP3-V1.0",
            "code": "OIS-MATH-03-5EME-MYP3"
        },
        {
            "md": "oak_curriculum/workbooks/workbook_04_quatrieme_myp4.md",
            "pdf": "oak_curriculum/exports/pdf/workbook_04_quatrieme_myp4.pdf",
            "title": "Quatrième / IB MYP 4 Activity Workbook",
            "grade": "Quatrième (4ème) / IB MYP 4 (Ages 13–14)",
            "version": "OIS-WB-4EME-MYP4-V1.0",
            "code": "OIS-MATH-04-4EME-MYP4"
        },
        {
            "md": "oak_curriculum/workbooks/workbook_05_troisieme_myp5.md",
            "pdf": "oak_curriculum/exports/pdf/workbook_05_troisieme_myp5.pdf",
            "title": "Troisième / IB MYP 5 Activity Workbook",
            "grade": "Troisième (3ème) / IB MYP 5 (Ages 14–15)",
            "version": "OIS-WB-3EME-MYP5-V1.0",
            "code": "OIS-MATH-05-3EME-MYP5"
        },
        {
            "md": "oak_curriculum/workbooks/workbook_06_seconde_dp1.md",
            "pdf": "oak_curriculum/exports/pdf/workbook_06_seconde_dp1.pdf",
            "title": "Seconde / IB DP 1 Activity Workbook",
            "grade": "Seconde (2nde) / IB DP 1 (Ages 15–16)",
            "version": "OIS-WB-2NDE-DP1-V1.0",
            "code": "OIS-MATH-06-2NDE-DP1"
        },
        {
            "md": "oak_curriculum/workbooks/workbook_07_premiere_dp2.md",
            "pdf": "oak_curriculum/exports/pdf/workbook_07_premiere_dp2.pdf",
            "title": "Première / IB DP 2 Activity Workbook",
            "grade": "Première (1ère) / IB DP 2 (Ages 16–17)",
            "version": "OIS-WB-1ERE-DP2-V1.0",
            "code": "OIS-MATH-07-1ERE-DP2"
        },
    ]

    reports = [
        {
            "md": "oak_curriculum/01_research_report.md",
            "pdf": "oak_curriculum/exports/pdf/01_research_report.pdf",
            "title": "Curriculum Research Report",
            "grade": "Official Curriculum Research Report",
            "version": "OIS-MTH-RES-2026-V1.0",
            "code": "OIS-REP-01-RESEARCH"
        },
        {
            "md": "oak_curriculum/02_seven_level_curriculum_inventory.md",
            "pdf": "oak_curriculum/exports/pdf/02_seven_level_curriculum_inventory.pdf",
            "title": "Seven-Level Curriculum Inventory",
            "grade": "Seven-Level Mathematical Content Inventory",
            "version": "OIS-MTH-INV-2026-V1.0",
            "code": "OIS-REP-02-INVENTORY"
        },
        {
            "md": "oak_curriculum/03_curriculum_alignment_matrix.md",
            "pdf": "oak_curriculum/exports/pdf/03_curriculum_alignment_matrix.pdf",
            "title": "Curriculum Alignment Matrix",
            "grade": "Comparative Curriculum Alignment Matrix",
            "version": "OIS-MTH-ALN-2026-V1.0",
            "code": "OIS-REP-03-MATRIX"
        },
        {
            "md": "oak_curriculum/04_harmonisation_strategy.md",
            "pdf": "oak_curriculum/exports/pdf/04_harmonisation_strategy.pdf",
            "title": "Pedagogical Harmonisation Strategy",
            "grade": "Oak Harmonisation Strategy & Model",
            "version": "OIS-MTH-STR-2026-V1.0",
            "code": "OIS-REP-04-STRATEGY"
        },
        {
            "md": "oak_curriculum/05_harmonised_scope_and_sequence.md",
            "pdf": "oak_curriculum/exports/pdf/05_harmonised_scope_and_sequence.pdf",
            "title": "Harmonised Scope and Sequence Plans",
            "grade": "Seven-Level Scope & Sequence Plans",
            "version": "OIS-MTH-SCQ-2026-V1.0",
            "code": "OIS-REP-05-SCOPE"
        },
        {
            "md": "oak_curriculum/07_quality_assurance_report.md",
            "pdf": "oak_curriculum/exports/pdf/07_quality_assurance_report.pdf",
            "title": "Quality Assurance Report",
            "grade": "Final Quality Assurance & Audit Report",
            "version": "OIS-MTH-QAR-2026-V1.0",
            "code": "OIS-REP-07-QA"
        },
    ]

    for item in workbooks + reports:
        print(f"Building Premium PDF for: {item['md']}")
        try:
            build_premium_pdf(item['md'], item['pdf'], item)
        except Exception as e:
            print(f"Error building {item['pdf']}: {e}")

if __name__ == '__main__':
    main()
