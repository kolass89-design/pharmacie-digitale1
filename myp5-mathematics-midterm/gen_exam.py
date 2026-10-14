#!/usr/bin/env python3
"""Generate the MYP 5 Mathematics Mid-Term Test (Oak International School).

Outputs:
  1. MYP5_Mathematics_MidTerm_Test.pdf    (print-ready student paper, exactly 1 x A4 portrait)
  2. MYP5_Mathematics_MidTerm_Test.docx   (editable student paper, 1 x A4 portrait)
  3. MYP5_Mathematics_MidTerm_Mark_Scheme.docx (teacher's mark scheme, separate document)

All mathematics pre-verified independently.
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HERE, "assets", "ois-logo-trimmed.png")

# ------------------------------------------------------------------ palette
GREEN      = HexColor("#008968")   # official Oak brand green (sampled from logo)
GREEN_DARK = HexColor("#006B52")
INK        = HexColor("#1A1A1A")
DARK       = HexColor("#1F2A24")
GREY       = HexColor("#6B7280")
LIGHTLINE  = HexColor("#9CA3AF")
DOTCOL     = HexColor("#B3BAC2")
TINT       = HexColor("#E6F4EE")
BARTEXT    = white

W, H = A4                            # 595.28 x 841.89 pt
ML = 34; MR = 34                     # margins
CW = W - ML - MR                     # content width
XR = W - MR                          # right edge

# ================================================================== STUDENT PAPER (PDF)
BODY, LEAD = 9.4, 11.3

def rich_width(parts, size):
    w = 0.0
    for text, st in parts:
        f, s = ("Helvetica-Bold", size) if st == "b" else \
               ("Helvetica-Oblique", size) if st == "i" else \
               ("Helvetica", size * 0.68) if st == "sub" else ("Helvetica", size)
        w += stringWidth(text, f, s)
    return w

def draw_rich(c, x, y, parts, size=BODY, color=INK):
    c.setFillColor(color)
    cur = x
    for text, st in parts:
        y_use = y
        if st == "b":
            c.setFont("Helvetica-Bold", size)
        elif st == "i":
            c.setFont("Helvetica-Oblique", size)
        elif st == "sub":
            c.setFont("Helvetica", size * 0.66)
            y_use = y - 2.4
        else:
            c.setFont("Helvetica", size)
            y_use = y
        c.drawString(cur, y_use, text)
        cur += stringWidth(text, c._fontname, c._fontsize)
    return cur

def wrap_parts(parts, size, maxw):
    """Split rich parts into lines fitting maxw (word-level)."""
    lines, cur, curw = [], [], 0.0
    for text, st in parts:
        words = text.split(" ")
        for i, wd in enumerate(words):
            piece = wd + (" " if i < len(words) - 1 else "")
            pw = stringWidth(piece, "Helvetica-Bold" if st == "b" else "Helvetica", size)
            if cur and curw + pw > maxw:
                lines.append(cur); cur, curw = [], 0.0
            cur.append((piece, st)); curw += pw
    if cur: lines.append(cur)
    return lines

class Paper:
    def __init__(self, path):
        self.c = c = canvas.Canvas(path, pagesize=A4)
        c.setTitle("MYP 5 Mathematics - Mid-Term Test")
        c.setAuthor("Oak International School")
        c.setSubject("Linear Sequences and Arithmetic Sequences - Criterion A and Criterion D")
        self.y = H - ML

    # ---------------- header -------------------------------------------------
    def header(self):
        c = self.c
        logo_h = 42.0
        logo_w = logo_h * 0.787
        c.drawImage(LOGO, ML, self.y - logo_h, width=logo_w, height=logo_h,
                    mask="auto", preserveAspectRatio=True)
        tx = ML + logo_w + 10
        c.setFillColor(GREEN)
        c.setFont("Helvetica-Bold", 14.5)
        c.drawString(tx, self.y - 12, "OAK INTERNATIONAL SCHOOL", charSpace=1.1)
        c.setFillColor(DARK)
        c.setFont("Helvetica-Bold", 10.3)
        c.drawString(tx, self.y - 26, "MYP 5 MATHEMATICS — MID-TERM TEST", charSpace=0.3)
        c.setFillColor(GREY)
        c.setFont("Helvetica-Oblique", 7.2)
        c.drawString(tx, self.y - 37, "Bilingual Excellence in Education & Leadership")

        # meta box (right)
        bw, bh = 132, 41
        bx, by = XR - bw, self.y - bh - 1
        c.setStrokeColor(GREEN); c.setLineWidth(0.9)
        c.roundRect(bx, by, bw, bh, 2.5, stroke=1, fill=0)
        rows = [("DURATION", "30 minutes"), ("TOTAL MARKS", "20"),
                ("CALCULATOR", "Not permitted")]
        yy = by + bh - 11.5
        for lab, val in rows:
            c.setFont("Helvetica-Bold", 6.4); c.setFillColor(GREY)
            c.drawString(bx + 7, yy, lab)
            c.setFont("Helvetica-Bold", 7.5); c.setFillColor(DARK)
            c.drawRightString(bx + bw - 7, yy, val)
            yy -= 10.2

        # name / class / date
        yl = by - 13
        c.setFont("Helvetica-Bold", 8.4); c.setFillColor(DARK)
        segs = [("Name:", 30, 205), ("Class:", 250, 385), ("Date:", 430, XR)]
        for lab, x0, x1 in segs:
            c.drawString(x0, yl, lab)
            lw = stringWidth(lab, "Helvetica-Bold", 8.4)
            c.setStrokeColor(LIGHTLINE); c.setLineWidth(0.6)
            c.line(x0 + lw + 4, yl - 1.5, x1, yl - 1.5)
        # green rule
        self.y = yl - 8
        c.setStrokeColor(GREEN); c.setLineWidth(1.3)
        c.line(ML, self.y, XR, self.y)
        self.y -= 9

    # ---------------- instructions -------------------------------------------
    def instructions(self):
        c = self.c
        lines = [
            "Answer ALL questions on this paper. Show all working clearly — marks are awarded for method, justification and clear communication.",
            "Write final answers on the dotted lines. Give non-exact decimal answers correct to 2 decimal places. Aim for about 90 seconds per mark.",
        ]
        h = 5.5 + LEAD * len(lines) + 3.5
        c.setFillColor(TINT)
        c.roundRect(ML, self.y - h, CW, h, 2, stroke=0, fill=1)
        c.setFillColor(GREEN)
        c.rect(ML, self.y - h, 2.6, h, stroke=0, fill=1)
        yy = self.y - 5.5 - 8
        c.setFillColor(DARK); c.setFont("Helvetica", 7.35)
        for ln in lines:
            c.drawString(ML + 10, yy, ln)
            yy -= 9.6
        self.y -= h + 10

    # ---------------- task building blocks ------------------------------------
    def task_bar(self, title, crit, marks):
        c = self.c
        bh = 13.6
        c.setFillColor(GREEN)
        c.roundRect(ML, self.y - bh, CW, bh, 2, stroke=0, fill=1)
        c.setFillColor(BARTEXT)
        c.setFont("Helvetica-Bold", 7.7)
        c.drawString(ML + 8, self.y - bh + 4.2, title, charSpace=0.2)
        right = f"{crit}  •  {marks} MARKS"
        c.setFont("Helvetica-Bold", 7.2)
        c.drawRightString(XR - 8, self.y - bh + 4.3, right)
        self.y -= bh + 4.6

    def para(self, parts, size=BODY, color=INK, indent=0, hang=0):
        lines = wrap_parts(parts, size, CW - indent - hang)
        for i, ln in enumerate(lines):
            self.y -= LEAD
            draw_rich(self.c, ML + indent + (hang if i > 0 else 0), self.y, ln, size, color)
        return lines

    def seq_display(self, groups):
        """Centered sequence terms. groups = [(label, [terms...]), ...]"""
        c = self.c
        parts = []
        for gi, (lab, terms) in enumerate(groups):
            if gi: parts.append(("          ", ""))
            parts.append((lab + ":   ", "b"))
            parts.append((",    ".join(terms) + ",   …", ""))
        wd = rich_width(parts, BODY + 0.6)
        self.y -= LEAD + 1.6
        draw_rich(c, ML + (CW - wd) / 2, self.y, parts, BODY + 0.6)
        self.y -= 1.5

    def subq(self, label, parts, marks, dots=1):
        """A labelled sub-question line with [marks] at right + dotted answer lines."""
        c = self.c
        parts = [(f"({label})  ", "b")] + parts
        lw = stringWidth(f"({label})  ", "Helvetica-Bold", BODY)
        self.para(parts, hang=lw)
        for i in range(dots):
            self.y -= 10.8
            c.setStrokeColor(DOTCOL); c.setLineWidth(0.7)
            c.setDash(0.6, 2.6)
            c.line(ML + lw, self.y, XR - 52, self.y)
            c.setDash()
        c.setFont("Helvetica-Oblique", 7.6); c.setFillColor(GREY)
        c.drawRightString(XR, self.y + 1.2, f"[{marks} mark{'' if marks == 1 else 's'}]")
        self.y -= 3.4

    def footer(self):
        c = self.c
        c.setStrokeColor(HexColor("#D5DBE0")); c.setLineWidth(0.6)
        c.line(ML, 40, XR, 40)
        c.setFont("Helvetica", 6.7); c.setFillColor(GREY)
        c.drawString(ML, 30.5, "Oak International School — MYP 5 Mathematics — Mid-Term Test")
        c.drawRightString(XR, 30.5, "Page 1 of 1")

    def space(self, pts):
        self.y -= pts

    def save(self):
        self.c.save()


p = Paper(os.path.join(HERE, "MYP5_Mathematics_MidTerm_Test.pdf"))
p.header()
p.instructions()

MIN = "−"  # en dash used as minus glyph (WinAnsi-safe)

# ---------------------------------------------------------------- TASK 1
p.task_bar("TASK 1 — RECOGNISING AND UNDERSTANDING SEQUENCES", "Criterion A", 4)
p.para([("Two sequences are shown below.", "")])
p.seq_display([("P", ["5", "11", "17", "23"]), ("Q", ["2", "6", "18", "54"])])
p.subq("a", [("For sequence P, write down the common difference.", "")], 1, dots=1)
p.subq("b", [("Determine whether sequence Q is ", ""), ("linear", "b"),
             (". Justify your answer by considering the differences between consecutive terms.", "")],
       2, dots=2)
p.subq("c", [("Write down the next term of Q.", "")], 1, dots=1)
p.space(8.5)

# ---------------------------------------------------------------- TASK 2
p.task_bar("TASK 2 — ARITHMETIC SEQUENCES AND GENERAL TERMS", "Criterion A", 6)
p.para([("The first four terms of an arithmetic sequence ", ""), ("U", "b"),
        (" are:", "")])
p.seq_display([(MIN + "4", [])] and [("U", ["23", "19", "15", "11"])])
p.subq("a", [("Find ", ""), ("u", ""), ("25", "sub"),
             (", the 25th term of U.", "")], 2, dots=1)
p.subq("b", [("A different arithmetic sequence ", ""), ("V", "b"),
             (" has fourth term 19 and common difference " + MIN + "3. Find the first term of V, and write down the first four terms of V.", "")],
       2, dots=2)
p.subq("c", [("Explain, with clear working, why " + MIN + "60 cannot be a term of U.", "")], 2, dots=2)
p.space(8.5)

# ---------------------------------------------------------------- TASK 3
p.task_bar("TASK 3 — APPLYING SEQUENCES: THEATRE SEATING", "Criterion D", 6)
p.para([("A theatre in Cotonou is hosting the school arts showcase. ", ""),
        ("Row 1 (the front row) contains 12 seats, and each row behind it contains exactly 3 more seats than the row in front of it. There are 20 rows in total.", "")])
p.subq("a", [("Show that the number of seats in row ", ""), ("n", "i"),
             (" is  ", ""), ("u", ""), ("n", "sub"),
             (" = 3", ""), ("n", "i"), (" + 9.", "")], 2, dots=1)
p.subq("b", [("Find the number of seats in row 15.", "")], 1, dots=1)
p.subq("c", [("Calculate the total number of seats in the theatre.", "")], 2, dots=2)
p.subq("d", [("A full-school performance requires 795 seats. Determine whether ", ""),
             ("one performance", "b"),
             (" in this theatre is enough for the whole school. Justify your answer.", "")], 1, dots=2)
p.space(8.5)

# ---------------------------------------------------------------- TASK 4
p.task_bar("TASK 4 — REASONING CHALLENGE: TWO PATTERNS", "Criterion A", 4)
p.para([("Pattern X begins at 100 and decreases by 8 each time. Pattern Y begins at 10 and increases by 12 each time. The patterns are compared term by term (term 1 with term 1, term 2 with term 2, and so on). A student claims: ", ""),
        ("“From the 5th term onwards, Y is always greater than X.”", "i")])
p.subq("a", [("Write down a formula for the ", ""), ("n", "i"),
             ("th term of each pattern.", "")], 1, dots=1)
p.subq("b", [("Investigate the student’s claim. Find, with full justification, the first paired term for which Y is greater than X.", "")],
       3, dots=3)

p.footer()
p.save()
print("PDF written")

# ================================================================== STUDENT PAPER (DOCX)
GREEN_HEX = "008968"

def set_shading(par, hexfill):
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), hexfill)
    par._p.get_or_add_pPr().append(shd)

def bottom_border(par, color=GREEN_HEX, size=12):
    pPr = par._p.get_or_add_pPr()
    pbdr = OxmlElement('w:pBdr')
    b = OxmlElement('w:bottom')
    b.set(qn('w:val'), 'single'); b.set(qn('w:sz'), str(size))
    b.set(qn('w:space'), '2'); b.set(qn('w:color'), color)
    pbdr.append(b); pPr.append(pbdr)

def dotted_line(par, pos_twips=9900):
    pPr = par._p.get_or_add_pPr()
    tabs = OxmlElement('w:tabs'); tab = OxmlElement('w:tab')
    tab.set(qn('w:val'), 'right'); tab.set(qn('w:leader'), 'dot'); tab.set(qn('w:pos'), str(pos_twips))
    tabs.append(tab); pPr.append(tabs)
    r = par.add_run('\t'); r.font.size = Pt(9)

def add_rich(par, parts, size=10):
    for text, st in parts:
        r = par.add_run(text)
        r.font.size = Pt(size * (0.66 if st == "sub" else 1.0))
        r.font.bold = (st == "b")
        r.font.italic = (st == "i")
        if st == "sub":
            r.font.subscript = True
    return par

def styled_par(doc, space_after=2, space_before=0, align=None, line=1.0):
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.space_after = Pt(space_after); pf.space_before = Pt(space_before)
    pf.line_spacing = line
    if align: par.alignment = align
    return par

def build_student_docx(path):
    doc = Document()
    for sec in doc.sections:
        sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
        sec.top_margin = Cm(1.15); sec.bottom_margin = Cm(1.0)
        sec.left_margin = Cm(1.35); sec.right_margin = Cm(1.35)
    st = doc.styles['Normal']
    st.font.name = 'Calibri'; st.font.size = Pt(10)
    st.paragraph_format.space_after = Pt(2)

    # ---- header table: logo + identity
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Cm(1.9); tbl.columns[1].width = Cm(16.4)
    c0 = tbl.cell(0, 0).paragraphs[0]
    run = c0.add_run(); run.add_picture(LOGO, height=Cm(1.5))
    c1 = tbl.cell(0, 1)
    p1 = c1.paragraphs[0]; p1.paragraph_format.space_after = Pt(0)
    r = p1.add_run("OAK INTERNATIONAL SCHOOL")
    r.font.bold = True; r.font.size = Pt(15); r.font.color.rgb = RGBColor(0x00, 0x89, 0x68)
    p2 = c1.add_paragraph(); p2.paragraph_format.space_after = Pt(0)
    r = p2.add_run("MYP 5 MATHEMATICS — MID-TERM TEST")
    r.font.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = RGBColor(0x1F, 0x2A, 0x24)
    p3 = c1.add_paragraph(); p3.paragraph_format.space_after = Pt(0)
    r = p3.add_run("Bilingual Excellence in Education & Leadership")
    r.font.italic = True; r.font.size = Pt(7.5); r.font.color.rgb = RGBColor(0x6B, 0x72, 0x80)

    meta = styled_par(doc, space_before=3, space_after=2, align=WD_ALIGN_PARAGRAPH.RIGHT)
    r = meta.add_run("Duration: 30 minutes   |   Total: 20 marks   |   Calculator: not permitted")
    r.font.size = Pt(8.5); r.font.bold = True; r.font.color.rgb = RGBColor(0x00, 0x6B, 0x52)

    nd = styled_par(doc, space_after=4)
    r = nd.add_run("Name: _____________________________        Class: ________________        Date: ______________")
    r.font.size = Pt(9)

    rule = styled_par(doc, space_after=5); bottom_border(rule)

    ins = styled_par(doc, space_after=2)
    set_shading(ins, "E6F4EE")
    r = ins.add_run("Answer ALL questions on this paper. Show all working clearly — marks are awarded for method, justification and clear communication. "
                    "Write final answers on the dotted lines. Non-exact decimal answers: 2 d.p. Aim for about 90 seconds per mark.")
    r.font.size = Pt(7.6)

    def task(title, crit, marks):
        par = styled_par(doc, space_before=5, space_after=3)
        set_shading(par, GREEN_HEX)
        r = par.add_run(f"  {title}")
        r.font.bold = True; r.font.size = Pt(9); r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r2 = par.add_run(f"   —   {crit} • {marks} MARKS  ")
        r2.font.bold = True; r2.font.size = Pt(8); r2.font.color.rgb = RGBColor(0xD9, 0xF2, 0xE9)

    def subq(label, parts, marks, dots=1):
        par = styled_par(doc)
        add_rich(par, [(f"({label})  ", "b")] + parts)
        mr = par.add_run(f"\t[{marks} mark{'' if marks == 1 else 's'}]")
        mr.font.size = Pt(8); mr.font.italic = True; mr.font.color.rgb = RGBColor(0x6B, 0x72, 0x80)
        pPr = par._p.get_or_add_pPr()
        tabs = OxmlElement('w:tabs'); tab = OxmlElement('w:tab')
        tab.set(qn('w:val'), 'right'); tab.set(qn('w:pos'), '10100')
        tabs.append(tab); pPr.append(tabs)
        for _ in range(dots):
            d = styled_par(doc, space_after=1)
            d.paragraph_format.left_indent = Cm(0.45 if dots == 1 else 0.3)
            dotted_line(d)

    task("TASK 1 — RECOGNISING AND UNDERSTANDING SEQUENCES", "Criterion A", 4)
    par = styled_par(doc); par.add_run("Two sequences are shown below.")
    sq = styled_par(doc, space_after=3, align=WD_ALIGN_PARAGRAPH.CENTER)
    r = sq.add_run("P:   5,     11,     17,     23,   …          Q:   2,     6,     18,     54,   …")
    r.font.size = Pt(10)
    subq("a", [("For sequence P, write down the common difference.", "")], 1, dots=1)
    subq("b", [("Determine whether sequence Q is ", ""), ("linear", "b"),
               (". Justify your answer by considering the differences between consecutive terms.", "")], 2, dots=2)
    subq("c", [("Write down the next term of Q.", "")], 1, dots=1)

    task("TASK 2 — ARITHMETIC SEQUENCES AND GENERAL TERMS", "Criterion A", 6)
    par = styled_par(doc)
    add_rich(par, [("The first four terms of an arithmetic sequence ", ""), ("U", "b"), (" are:", "")])
    sq = styled_par(doc, space_after=3, align=WD_ALIGN_PARAGRAPH.CENTER)
    r = sq.add_run("U:   23,     19,     15,     11,   …"); r.font.size = Pt(10)
    subq("a", [("Find ", ""), ("u", ""), ("25", "sub"), (", the 25th term of U.", "")], 2, dots=1)
    subq("b", [("A different arithmetic sequence ", ""), ("V", "b"),
               (" has fourth term 19 and common difference −3. Find the first term of V, and write down the first four terms of V.", "")], 2, dots=2)
    subq("c", [("Explain, with clear working, why −60 cannot be a term of U.", "")], 2, dots=2)

    task("TASK 3 — APPLYING SEQUENCES: THEATRE SEATING", "Criterion D", 6)
    par = styled_par(doc)
    par.add_run("A theatre in Cotonou is hosting the school arts showcase. Row 1 (the front row) contains 12 seats, and each row behind it contains exactly 3 more seats than the row in front of it. There are 20 rows in total.")
    subq("a", [("Show that the number of seats in row ", ""), ("n", "i"),
               (" is  ", ""), ("u", ""), ("n", "sub"), (" = 3", ""), ("n", "i"), (" + 9.", "")], 2, dots=1)
    subq("b", [("Find the number of seats in row 15.", "")], 1, dots=1)
    subq("c", [("Calculate the total number of seats in the theatre.", "")], 2, dots=1)
    subq("d", [("A full-school performance requires 795 seats. Determine whether ", ""),
               ("one performance", "b"),
               (" in this theatre is enough for the whole school. Justify your answer.", "")], 1, dots=2)

    task("TASK 4 — REASONING CHALLENGE: TWO PATTERNS", "Criterion A", 4)
    par = styled_par(doc)
    add_rich(par, [("Pattern X begins at 100 and decreases by 8 each time. Pattern Y begins at 10 and increases by 12 each time. The patterns are compared term by term (term 1 with term 1, term 2 with term 2, and so on). A student claims: ", ""),
                   ("“From the 5th term onwards, Y is always greater than X.”", "i")])
    subq("a", [("Write down a formula for the ", ""), ("n", "i"), ("th term of each pattern.", "")], 1, dots=1)
    subq("b", [("Investigate the student’s claim. Find, with full justification, the first paired term for which Y is greater than X.", "")], 3, dots=3)

    ftr = styled_par(doc, space_before=4)
    r = ftr.add_run("Oak International School — MYP 5 Mathematics — Mid-Term Test — Page 1 of 1")
    r.font.size = Pt(7); r.font.color.rgb = RGBColor(0x6B, 0x72, 0x80)
    ftr.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.core_properties.title = "MYP 5 Mathematics — Mid-Term Test"
    doc.core_properties.author = "Oak International School"
    doc.save(path)
    print("Student DOCX written")

build_student_docx(os.path.join(HERE, "MYP5_Mathematics_MidTerm_Test.docx"))
