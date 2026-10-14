#!/usr/bin/env python3
"""Generate the Teacher's Mark Scheme (separate document, not page-restricted)."""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HERE, "assets", "ois-logo-trimmed.png")

GREEN = RGBColor(0x00, 0x89, 0x68)
DARK  = RGBColor(0x1F, 0x2A, 0x24)
GREY  = RGBColor(0x6B, 0x72, 0x80)
GREEN_HEX = "008968"
TINT_HEX  = "E6F4EE"

doc = Document()
for sec in doc.sections:
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    sec.top_margin = Cm(1.3); sec.bottom_margin = Cm(1.2)
    sec.left_margin = Cm(1.5); sec.right_margin = Cm(1.5)
st = doc.styles['Normal']
st.font.name = 'Calibri'; st.font.size = Pt(10)
st.paragraph_format.space_after = Pt(3)

def shade(par, hexfill):
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), hexfill)
    par._p.get_or_add_pPr().append(shd)

def shade_cell(cell, hexfill):
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), hexfill)
    cell._tc.get_or_add_tcPr().append(shd)

def par(space_after=3, space_before=0, align=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    if align: p.alignment = align
    return p

def rich(p, parts, size=10):
    for text, stl in parts:
        r = p.add_run(text)
        r.font.size = Pt(size * (0.66 if stl == 'sub' else 1.0))
        r.font.bold = (stl == 'b'); r.font.italic = (stl == 'i')
        if stl == 'sub': r.font.subscript = True
    return p

# ---------------------------------------------------------------- header
tbl = doc.add_table(rows=1, cols=2)
tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl.columns[0].width = Cm(1.9); tbl.columns[1].width = Cm(16.1)
c0 = tbl.cell(0, 0).paragraphs[0]
c0.add_run().add_picture(LOGO, height=Cm(1.5))
c1 = tbl.cell(0, 1)
p = c1.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
r = p.add_run("OAK INTERNATIONAL SCHOOL"); r.font.bold = True; r.font.size = Pt(15); r.font.color.rgb = GREEN
p = c1.add_paragraph(); p.paragraph_format.space_after = Pt(0)
r = p.add_run("MYP 5 MATHEMATICS — MID-TERM TEST"); r.font.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = DARK
p = c1.add_paragraph(); p.paragraph_format.space_after = Pt(0)
r = p.add_run("TEACHER'S MARK SCHEME — CONFIDENTIAL"); r.font.bold = True; r.font.size = Pt(9); r.font.color.rgb = GREY

p = par(space_before=4, space_after=2, align=WD_ALIGN_PARAGRAPH.RIGHT)
r = p.add_run("Duration: 30 minutes   |   Total: 20 marks   |   Criteria: A and D")
r.font.size = Pt(8.5); r.font.bold = True; r.font.color.rgb = RGBColor(0x00, 0x6B, 0x52)

def band(text, right=""):
    p = par(space_before=8, space_after=4)
    shade(p, GREEN_HEX)
    r = p.add_run(f"  {text}"); r.font.bold = True; r.font.size = Pt(9.5)
    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    if right:
        r2 = p.add_run(f"   —   {right}  "); r2.font.bold = True; r2.font.size = Pt(8.5)
        r2.font.color.rgb = RGBColor(0xD9, 0xF2, 0xE9)

def note(text, bold_lead=None):
    p = par(space_after=3)
    if bold_lead:
        r = p.add_run(bold_lead + " "); r.font.bold = True; r.font.size = Pt(8.8); r.font.color.rgb = DARK
    r = p.add_run(text); r.font.size = Pt(8.8); r.font.color.rgb = GREY
    return p

def solution_table(rows):
    """rows = list of (working, marks, notes)"""
    t = doc.add_table(rows=1, cols=3)
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    widths = [Cm(8.6), Cm(1.7), Cm(7.7)]
    hdr = t.rows[0].cells
    for i, htxt in enumerate(["Answer / working", "Marks", "Marking notes"]):
        hdr[i].width = widths[i]
        p = hdr[i].paragraphs[0]; p.paragraph_format.space_after = Pt(0)
        r = p.add_run(htxt); r.font.bold = True; r.font.size = Pt(8.6)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        shade_cell(hdr[i], GREEN_HEX)
    for working, marks, notes in rows:
        cells = t.add_row().cells
        for i, val in enumerate((working, marks, notes)):
            cells[i].width = widths[i]
            p = cells[i].paragraphs[0]; p.paragraph_format.space_after = Pt(0)
            if isinstance(val, str) and val.startswith("RAW:"):
                rich(p, [("  ", "")] + eval(val[4:]), size=9)
            else:
                r = p.add_run(("  " if i != 1 else "") + str(val))
                r.font.size = Pt(9 if i != 1 else 9)
                if i == 1: p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    return t

# ================================================================ TASK 1
band("TASK 1 — RECOGNISING AND UNDERSTANDING SEQUENCES", "Criterion A • 4 marks")
solution_table([
    ("RAW: [('d = 6', '')]", "1", "A1. Accept '+6 each time'. Do not accept 'it goes up' without the value."),
    ("RAW: [('Q is ', ''), ('not', 'b'), (' linear. Differences: 6−2 = 4, 18−6 = 12, 54−18 = 36; since 4 ≠ 12 ≠ 36 there is no constant (common) difference, so Q is not linear.', '')]", "2",
     "M1 for computing at least two successive differences; A1 for the correct conclusion linked to the differences. (Q is in fact geometric, ×3 — accept but do not require this.)"),
    ("Next term of Q:  54 × 3 = 162.", "1", "A1 for 162 only. Accept 54 × 3 shown explicitly; '90' (continuing a difference of 36) reveals the misconception in (b) — award 0 and address in feedback."),
])
note("Many students see an increasing list and answer 'linear'. Award marks only when a difference check is shown. Computing a single gap is insufficient for M1.",
     "Misconception:")

# ================================================================ TASK 2
band("TASK 2 — ARITHMETIC SEQUENCES AND GENERAL TERMS", "Criterion A • 6 marks")
p = par(space_after=3)
rich(p, [("Sequence U:  ", "b"), ("23,  19,  15,  11, …    so    ", ""), ("a", "i"), (" = 23 and ", ""), ("d", "i"), (" = −4, giving ", ""),
         ("u", ""), ("n", "sub"), (" = 23 + (", ""), ("n", "i"), (" − 1)(−4) = 27 − 4", ""), ("n", "i"), (".", "")], size=9.5)
solution_table([
    ("RAW: [('u', ''), ('25', 'sub'), (' = 23 + 24(−4) = 23 − 96 = ', ''), ('−73', 'b')]", "2",
     "M1 for u₁ + (n − 1)d with correct substitution (24 × (−4)); A1 for −73. Accept equivalent listing-based methods only if fully shown."),
    ("First term of V:  u₄ = u₁ + 3d  →  19 = u₁ + 3(−3)  →  u₁ = 28.\nFirst four terms of V:  28,  25,  22,  19.", "2",
     "M1 for reversing the relation (u₁ = u₄ − 3d) or equivalent working backwards; A1 for u₁ = 28 and all four terms correct. Accept terms found by repeated subtraction if u₁ = 28 is justified."),
    ("RAW: [('27 − 4', ''), ('n', 'i'), (' = −60  →  4', ''), ('n', 'i'), (' = 87  →  ', ''), ('n', 'i'), (' = 21.75, which is not a positive integer, so −60 is not a term of U.', '')]", "2",
     "M1 for setting the nth-term expression equal to −60 and attempting to solve; A1 for n = 21.75 with the 'not an integer' conclusion. Alternative valid proof: 27 − 4n ≡ 3 (mod 4) but −60 ≡ 0 (mod 4) — accept."),
])
note("A bare 'no' scores 0. A numerical check of one or two terms without a general argument does not earn A1. Watch for sign slips giving n = −21.75, and for the uₙ = a + nd error in (a).",
     "Common errors:")

# ================================================================ TASK 3
band("TASK 3 — APPLYING SEQUENCES: THEATRE SEATING", "Criterion D • 6 marks")
p = par(space_after=3)
rich(p, [("Model: rows form an arithmetic sequence with ", ""), ("a", "i"), (" = 12 (row 1) and ", ""), ("d", "i"),
         (" = 3 (each row has 3 more seats than the row in front).", "")], size=9.5)
solution_table([
    ("Row 1: 12 seats ✓.  Common difference 3, so for row n:\nuₙ = 12 + (n − 1)(3) = 3n + 9.  ✓\nCheck: row 2 = 3(2) + 9 = 15 = 12 + 3 ✓.", "2",
     "M1 for identifying the arithmetic model and using uₙ = a + (n − 1)d with a = 12, d = 3; A1 for a correct derivation reaching 3n + 9. Verifying n = 1 and n = 2 alone, without the general form, scores M1 only."),
    ("u₁₅ = 3(15) + 9 = 54 seats.", "1", "A1. Accept 12 + 14(3) = 54."),
    ("Total for 20 rows:\nS₂₀ = 20⁄2 × (u₁ + u₂₀) = 10 × (12 + 69) = 10 × 81 = 810 seats.\n(Alternatively: S₂₀ = 20⁄2 × (2×12 + 19×3) = 810.)", "2",
     "M1 for a correct sum method (sum formula with consistent values, or summing all 20 row values 12+15+…+69); A1 for 810. '20 × 54' is a common error — 0 marks."),
    ("810 > 795, so one performance is enough; there are 810 − 795 = 15 spare seats.\nThis is reasonable: the model assumes the theatre is used for a single sitting, which matches a performance.", "1",
     "A1 for the explicit comparison 810 ≥ 795 with the decision 'yes'. The comparison must be stated; 810 alone does not answer the question."),
])
note("Criterion D rewards the full cycle: translate the situation into a sequence, apply the model, and interpret the answer in context (the '15 spare seats' or equivalent remark is the interpreting step for (d)).",
     "Contextual note:")
note("Using n instead of (n − 1) in (a) gives 3n + 12; forgetting that u₂₀ = 69 in (c); assuming 'total' means the largest row.",
     "Likely errors:")

# ================================================================ TASK 4
band("TASK 4 — REASONING CHALLENGE: TWO PATTERNS", "Criterion A • 4 marks")
solution_table([
    ("RAW: [('X:  ', 'b'), ('u', ''), ('n', 'sub'), (' = 100 − 8(', ''), ('n', 'i'), (' − 1) = 108 − 8', ''), ('n', 'i'), ('        Y:  ', 'b'), ('u', ''), ('n', 'sub'), (' = 10 + 12(', ''), ('n', 'i'), (' − 1) = 12', ''), ('n', 'i'), (' − 2', '')]", "1",
     "A1 for both correct nth-term formulae (either equivalent form). One correct formula only: no mark."),
    ("Test the claim:\n12n − 2 > 108 − 8n  →  20n > 110  →  n > 5.5\nFirst integer n satisfying this: n = 6.\nCheck: n = 5:  X₅ = 68,  Y₅ = 58  →  X still greater, so the claim fails at term 5.\nn = 6:  X₆ = 60,  Y₆ = 70  →  Y greater.\nVerdict: the claim is FALSE. Y becomes greater than X from the 6th paired term onwards, not the 5th.", "3",
     "M1 for forming the inequality (or equation 12n − 2 = 108 − 8n) or a systematic table of compared values; A1 for n = 6 as the first term where Y > X (n = 5.5 is not acceptable as a final answer — terms are counted in positive integers); R1 for an explicit verdict that the claim is false, supported by evidence at n = 5 and n = 6. A table alone with a correct verdict: M1 A1 R1 possible."),
])
note("Students who solve the equality and stop at n = 5.5, or who accept the claim without testing term 5, have not completed the reasoning. The mark scheme rewards the investigation and the justified verdict, not the arithmetic alone.",
     "Marking guidance:")

# ================================================================ CRITERION MAPPING
band("CRITERION MAPPING")
t = doc.add_table(rows=1, cols=4)
t.style = 'Table Grid'
widths = [Cm(2.2), Cm(1.6), Cm(3.2), Cm(10.0)]
hdr = t.rows[0].cells
for i, htxt in enumerate(["Task", "Marks", "Criterion", "Objective strands addressed"]):
    hdr[i].width = widths[i]
    p = hdr[i].paragraphs[0]; p.paragraph_format.space_after = Pt(0)
    r = p.add_run(htxt); r.font.bold = True; r.font.size = Pt(8.6); r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    shade_cell(hdr[i], GREEN_HEX)
mapping = [
    ("Task 1", "4", "A", "i–ii: knowing and using the concepts 'linear/common difference'; applying a difference test accurately; brief communication of a justified conclusion (iii)."),
    ("Task 2", "6", "A", "i–iii: using uₙ = a + (n − 1)d and its inverse; accurate technique; correct notation and a valid mathematical justification in (c)."),
    ("Task 3", "6", "D", "i–iv: identifying the arithmetic model in context; selecting/applying the strategy; accurate solution; interpreting the result (spare seats) and judging reasonableness."),
    ("Task 4", "4", "A", "ii–iii: applying algebraic techniques to compare sequences; communicating and justifying a reasoned verdict."),
    ("Total", "20", "A: 14   D: 6", "Criterion A ≈ 70%, Criterion D ≈ 30%."),
]
for row in mapping:
    cells = t.add_row().cells
    for i, val in enumerate(row):
        cells[i].width = widths[i]
        p = cells[i].paragraphs[0]; p.paragraph_format.space_after = Pt(0)
        r = p.add_run(val); r.font.size = Pt(8.8)
        if row[0] == "Total":
            r.font.bold = True; shade_cell(cells[i], TINT_HEX)

p = par(space_before=4, space_after=2)
r = p.add_run("Note on criterion levels: a single 30-minute test samples the criteria; it contributes evidence towards a criterion level but should not, alone, determine the final achievement level for Criterion A or D.")
r.font.italic = True; r.font.size = Pt(8.4); r.font.color.rgb = GREY

# ================================================================ MISCONCEPTIONS SUMMARY
band("COMMON MISCONCEPTIONS AND FEEDBACK NOTES")
misodes = [
    ("'Increasing means linear.'", "Growth alone does not establish linearity; a constant difference test (Task 1b) is required."),
    ("uₙ = a + nd confusion", "Students often omit the (n − 1); the first-term check u₁ = a catches this instantly."),
    ("Assuming −60 is 'too negative' to appear", "A decreasing sequence passes through every value in its range at some real n; only the integer test decides membership (Task 2c)."),
    ("Total = largest term × count", "In Task 3(c), multiplying u₂₀ by 20 ignores the growth; the mean × count structure (or the sum formula) is needed."),
    ("Answering n = 5.5", "Term numbers must be positive integers; n = 5.5 must be rounded up to n = 6 when locating the first term with Y > X (Task 4b)."),
    ("Answering without interpreting", "In Criterion D tasks, a bare number does not answer the contextual question; a decision in context ('yes, 15 seats spare') is required."),
]
t = doc.add_table(rows=1, cols=2)
t.style = 'Table Grid'
widths = [Cm(5.6), Cm(11.4)]
hdr = t.rows[0].cells
for i, htxt in enumerate(["Misconception", "Guidance / feedback point"]):
    hdr[i].width = widths[i]
    p = hdr[i].paragraphs[0]; p.paragraph_format.space_after = Pt(0)
    r = p.add_run(htxt); r.font.bold = True; r.font.size = Pt(8.6); r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    shade_cell(hdr[i], GREEN_HEX)
for a, b in misodes:
    cells = t.add_row().cells
    cells[0].width = widths[0]; cells[1].width = widths[1]
    p = cells[0].paragraphs[0]; p.paragraph_format.space_after = Pt(0)
    r = p.add_run(a); r.font.size = Pt(8.8); r.font.bold = True
    p = cells[1].paragraphs[0]; p.paragraph_format.space_after = Pt(0)
    r = p.add_run(b); r.font.size = Pt(8.8)


# proper Word footer with page numbers (spans all pages)
footer = doc.sections[0].footer
fp = footer.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = fp.add_run("Oak International School — MYP 5 Mathematics — Mid-Term Test — Teacher's Mark Scheme    |    Page ")
r.font.size = Pt(7); r.font.color.rgb = GREY
fld = OxmlElement('w:fldSimple'); fld.set(qn('w:instr'), 'PAGE')
run_el = OxmlElement('w:r'); rpr = OxmlElement('w:rPr')
sz = OxmlElement('w:sz'); sz.set(qn('w:val'), '14'); rpr.append(sz)
col = OxmlElement('w:color'); col.set(qn('w:val'), '6B7280'); rpr.append(col)
run_el.append(rpr)
t_el = OxmlElement('w:t'); t_el.text = '1'; run_el.append(t_el)
fld.append(run_el)
fp._p.append(fld)
r = fp.add_run(" of ")
r.font.size = Pt(7); r.font.color.rgb = GREY
fld2 = OxmlElement('w:fldSimple'); fld2.set(qn('w:instr'), 'NUMPAGES')
run_el2 = OxmlElement('w:r'); rpr2 = OxmlElement('w:rPr')
sz2 = OxmlElement('w:sz'); sz2.set(qn('w:val'), '14'); rpr2.append(sz2)
col2 = OxmlElement('w:color'); col2.set(qn('w:val'), '6B7280'); rpr2.append(col2)
run_el2.append(rpr2)
t_el2 = OxmlElement('w:t'); t_el2.text = '2'; run_el2.append(t_el2)
fld2.append(run_el2)
fp._p.append(fld2)

doc.core_properties.title = "MYP 5 Mathematics — Mid-Term Test — Teacher's Mark Scheme"
doc.core_properties.author = "Oak International School"
out = os.path.join(HERE, "MYP5_Mathematics_MidTerm_Mark_Scheme.docx")
doc.save(out)
print("Mark scheme written:", out)
