#!/usr/bin/env python3
"""
Oak International School - Document Generation Script
Generates editable Word documents (.docx) and print-ready PDFs (.pdf)
for all curriculum reports and workbooks.
"""

import os
import sys
import glob
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def markdown_to_docx(md_path, docx_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    doc = Document()
    
    # Page setup - A4
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10.5)
    normal_style.font.color.rgb = RGBColor(0x22, 0x22, 0x22)

    in_table = False
    table_rows = []

    def flush_table():
        nonlocal in_table, table_rows
        if not table_rows:
            in_table = False
            return
        
        num_cols = max(len(r) for r in table_rows)
        table = doc.add_table(rows=len(table_rows), cols=num_cols)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.style = 'Table Grid'

        for row_idx, r in enumerate(table_rows):
            is_header = (row_idx == 0)
            for col_idx in range(num_cols):
                cell_text = r[col_idx] if col_idx < len(r) else ""
                cell = table.cell(row_idx, col_idx)
                cell.text = cell_text.strip()
                p = cell.paragraphs[0]
                p.paragraph_format.space_before = Pt(3)
                p.paragraph_format.space_after = Pt(3)
                if p.runs:
                    p.runs[0].font.size = Pt(9.5)
                    if is_header:
                        p.runs[0].font.bold = True
                        p.runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                        set_cell_background(cell, "1F497D")
                    else:
                        if row_idx % 2 == 1:
                            set_cell_background(cell, "F2F5F8")
                        else:
                            set_cell_background(cell, "FFFFFF")
        
        doc.add_paragraph() # Spacing
        table_rows = []
        in_table = False

    for line in lines:
        raw = line.rstrip('\r\n')
        trimmed = raw.strip()

        # Check for table
        if trimmed.startswith('|') and trimmed.endswith('|'):
            # Table divider line e.g. |---|---|
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

        if trimmed.startswith('# '):
            p = doc.add_paragraph()
            run = p.add_run(trimmed[2:])
            run.font.name = 'Calibri'
            run.font.size = Pt(20)
            run.font.bold = True
            run.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(6)
        elif trimmed.startswith('## '):
            p = doc.add_paragraph()
            run = p.add_run(trimmed[3:])
            run.font.name = 'Calibri'
            run.font.size = Pt(15)
            run.font.bold = True
            run.font.color.rgb = RGBColor(0x2E, 0x75, 0xB6)
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(4)
        elif trimmed.startswith('### '):
            p = doc.add_paragraph()
            run = p.add_run(trimmed[4:])
            run.font.name = 'Calibri'
            run.font.size = Pt(12.5)
            run.font.bold = True
            run.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(3)
        elif trimmed.startswith('#### '):
            p = doc.add_paragraph()
            run = p.add_run(trimmed[5:])
            run.font.name = 'Calibri'
            run.font.size = Pt(11)
            run.font.bold = True
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(2)
        elif trimmed.startswith('- ') or trimmed.startswith('* '):
            p = doc.add_paragraph(style='List Bullet')
            clean_text = trimmed[2:].replace('**', '')
            p.add_run(clean_text)
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
        elif trimmed.startswith('1. ') or (len(trimmed) > 2 and trimmed[1] == '.' and trimmed[0].isdigit()):
            p = doc.add_paragraph(style='List Number')
            clean_text = trimmed[3:].replace('**', '')
            p.add_run(clean_text)
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
        elif trimmed == '---':
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
        else:
            p = doc.add_paragraph()
            clean_text = trimmed.replace('**', '')
            p.add_run(clean_text)
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(4)

    if in_table:
        flush_table()

    os.makedirs(os.path.dirname(docx_path), exist_ok=True)
    doc.save(docx_path)
    print(f"Generated DOCX: {docx_path}")


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#555555"))
        
        # Header (Pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 800, "Oak International School | Dual Mathematics Continuum (IB & Benin APC)")
            self.setStrokeColor(colors.HexColor("#CCCCCC"))
            self.setLineWidth(0.5)
            self.line(54, 792, 541, 792)

        # Footer
        self.setStrokeColor(colors.HexColor("#CCCCCC"))
        self.setLineWidth(0.5)
        self.line(54, 50, 541, 50)
        self.drawString(54, 38, "Confidential & Proprietary — Oak International School (2026–2027)")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(541, 38, page_text)
        self.restoreState()


def markdown_to_pdf(md_path, pdf_path):
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

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor("#1F497D"),
        spaceAfter=10,
        spaceBefore=10
    )
    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#2E75B6"),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=colors.HexColor("#1F497D"),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )
    h3_style = ParagraphStyle(
        'H3',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#333333"),
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor("#222222"),
        spaceBefore=2,
        spaceAfter=3
    )
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10,
        spaceBefore=1,
        spaceAfter=1
    )
    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#222222")
    )
    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.white
    )

    story = []
    in_table = False
    table_rows = []

    def flush_pdf_table():
        nonlocal in_table, table_rows
        if not table_rows:
            in_table = False
            return
        
        num_cols = max(len(r) for r in table_rows)
        # Compute column widths
        avail_width = 487  # 595.27 - 108
        col_width = avail_width / num_cols
        col_widths = [col_width] * num_cols

        formatted_table = []
        for row_idx, r in enumerate(table_rows):
            formatted_row = []
            is_header = (row_idx == 0)
            for c_idx in range(num_cols):
                val = r[c_idx] if c_idx < len(r) else ""
                clean_val = val.replace('**', '').replace('$', '')
                p_style = table_header_style if is_header else table_cell_style
                p = Paragraph(clean_val, p_style)
                formatted_row.append(p)
            formatted_table.append(formatted_row)

        t = Table(formatted_table, colWidths=col_widths, repeatRows=1)
        t_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1F497D")),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('TOPPADDING', (0, 0), (-1, -1), 3),
            ('LEFTPADDING', (0, 0), (-1, -1), 3),
            ('RIGHTPADDING', (0, 0), (-1, -1), 3),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#D0D7DE")),
        ])
        for r_i in range(1, len(formatted_table)):
            if r_i % 2 == 1:
                t_style.add('BACKGROUND', (0, r_i), (-1, r_i), colors.HexColor("#F9FBFD"))
        t.setStyle(t_style)
        story.append(t)
        story.append(Spacer(1, 8))
        table_rows = []
        in_table = False

    for line in lines:
        raw = line.rstrip('\r\n')
        trimmed = raw.strip()

        if trimmed.startswith('|') and trimmed.endswith('|'):
            if set(trimmed.replace('|', '').replace('-', '').replace(':', '').strip()) == set():
                continue
            cells = [c.strip() for c in trimmed.split('|')[1:-1]]
            table_rows.append(cells)
            in_table = True
            continue
        else:
            if in_table:
                flush_pdf_table()

        if not trimmed:
            continue

        # Format markdown bold & symbols
        clean_text = trimmed.replace('**', '<b>', 1)
        while '**' in clean_text:
            clean_text = clean_text.replace('**', '</b>', 1)
            if '**' in clean_text:
                clean_text = clean_text.replace('**', '<b>', 1)
        
        # Clean latex dollars for readable display
        clean_text = clean_text.replace('$$', '').replace('$', '')
        clean_text = clean_text.replace('&', '&amp;')

        if trimmed.startswith('# '):
            story.append(Paragraph(clean_text[2:], title_style))
            story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1F497D"), spaceAfter=8))
        elif trimmed.startswith('## '):
            story.append(Paragraph(clean_text[3:], h1_style))
        elif trimmed.startswith('### '):
            story.append(Paragraph(clean_text[4:], h2_style))
        elif trimmed.startswith('#### '):
            story.append(Paragraph(clean_text[5:], h3_style))
        elif trimmed.startswith('- ') or trimmed.startswith('* '):
            story.append(Paragraph(f"&bull; {clean_text[2:]}", bullet_style))
        elif trimmed.startswith('1. ') or (len(trimmed) > 2 and trimmed[1] == '.' and trimmed[0].isdigit()):
            story.append(Paragraph(f"<b>{trimmed[:3]}</b> {clean_text[3:]}", bullet_style))
        elif trimmed == '---':
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#CCCCCC"), spaceBefore=6, spaceAfter=6))
        else:
            story.append(Paragraph(clean_text, body_style))

    if in_table:
        flush_pdf_table()

    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Generated PDF: {pdf_path}")

def main():
    root = "oak_curriculum"
    docs_to_build = [
        ("01_research_report.md", "exports/docx/01_research_report.docx", "exports/pdf/01_research_report.pdf"),
        ("02_seven_level_curriculum_inventory.md", "exports/docx/02_seven_level_curriculum_inventory.docx", "exports/pdf/02_seven_level_curriculum_inventory.pdf"),
        ("03_curriculum_alignment_matrix.md", "exports/docx/03_curriculum_alignment_matrix.docx", "exports/pdf/03_curriculum_alignment_matrix.pdf"),
        ("04_harmonisation_strategy.md", "exports/docx/04_harmonisation_strategy.docx", "exports/pdf/04_harmonisation_strategy.pdf"),
        ("05_harmonised_scope_and_sequence.md", "exports/docx/05_harmonised_scope_and_sequence.docx", "exports/pdf/05_harmonised_scope_and_sequence.pdf"),
        ("07_quality_assurance_report.md", "exports/docx/07_quality_assurance_report.docx", "exports/pdf/07_quality_assurance_report.pdf"),
        ("workbooks/workbook_01_cm2_myp1.md", "exports/docx/workbook_01_cm2_myp1.docx", "exports/pdf/workbook_01_cm2_myp1.pdf"),
        ("workbooks/workbook_02_sixieme_myp2.md", "exports/docx/workbook_02_sixieme_myp2.docx", "exports/pdf/workbook_02_sixieme_myp2.pdf"),
        ("workbooks/workbook_03_cinquieme_myp3.md", "exports/docx/workbook_03_cinquieme_myp3.docx", "exports/pdf/workbook_03_cinquieme_myp3.pdf"),
        ("workbooks/workbook_04_quatrieme_myp4.md", "exports/docx/workbook_04_quatrieme_myp4.docx", "exports/pdf/workbook_04_quatrieme_myp4.pdf"),
        ("workbooks/workbook_05_troisieme_myp5.md", "exports/docx/workbook_05_troisieme_myp5.docx", "exports/pdf/workbook_05_troisieme_myp5.pdf"),
        ("workbooks/workbook_06_seconde_dp1.md", "exports/docx/workbook_06_seconde_dp1.docx", "exports/pdf/workbook_06_seconde_dp1.pdf"),
        ("workbooks/workbook_07_premiere_dp2.md", "exports/docx/workbook_07_premiere_dp2.docx", "exports/pdf/workbook_07_premiere_dp2.pdf"),
    ]

    for src_rel, docx_rel, pdf_rel in docs_to_build:
        src = os.path.join(root, src_rel)
        docx_out = os.path.join(root, docx_rel)
        pdf_out = os.path.join(root, pdf_rel)
        
        print(f"Processing: {src}")
        try:
            markdown_to_docx(src, docx_out)
        except Exception as e:
            print(f"Error building docx for {src}: {e}")
            
        try:
            markdown_to_pdf(src, pdf_out)
        except Exception as e:
            print(f"Error building pdf for {src}: {e}")

if __name__ == "__main__":
    main()
