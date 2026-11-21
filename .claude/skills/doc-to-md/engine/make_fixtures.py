#!/usr/bin/env python3
"""Generate regression fixtures for /doc-to-md (no hand-crafted binaries in git).

Each fixture deliberately contains the details a naive converter LOSES:
  docx  - header, footer, comment, tracked insertion + deletion, merged-cell table, image, footnote-like text
  xlsx  - formula (value + formula), merged cells, cell comment, hidden sheet, defined name, data validation
  pptx  - title, body, table, image, speaker notes, hidden slide
  pdf   - page 1 real text layer, page 2 image-only (simulated scan -> must be queued for vision)

Usage: PYTHONUTF8=1 .tools/convert/Scripts/python.exe .claude/skills/doc-to-md/engine/make_fixtures.py [out_dir]
"""
import io
import sys
from pathlib import Path

from PIL import Image, ImageDraw

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "fixtures"
OUT.mkdir(parents=True, exist_ok=True)


def png(text: str, size=(420, 120)) -> bytes:
    img = Image.new("RGB", size, "white")
    d = ImageDraw.Draw(img)
    d.rectangle([2, 2, size[0] - 3, size[1] - 3], outline="black", width=2)
    d.text((16, 40), text, fill="black")
    buf = io.BytesIO()
    img.save(buf, "PNG")
    return buf.getvalue()


# ---------------------------------------------------------------- docx
def make_docx():
    from docx import Document
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Inches

    doc = Document()
    sec = doc.sections[0]
    sec.header.paragraphs[0].text = "HEADER-MARK Confidential draft v0.3"
    sec.footer.paragraphs[0].text = "FOOTER-MARK Page footer text"

    doc.add_heading("Product Query Handling", level=1)
    p = doc.add_paragraph("Cases filed as Other exceed 45 percent of logged product queries.")
    doc.add_comment(p.runs, text="COMMENT-MARK Please confirm the 45 percent figure", author="Reviewer", initials="RV")

    # Tracked changes: one insertion and one deletion (raw WordprocessingML)
    tp = doc.add_paragraph("Escalations have a ")
    for kind, txt in (("w:del", "2-hour"), ("w:ins", "4-hour")):
        el = OxmlElement(kind)
        el.set(qn("w:id"), "1" if kind == "w:del" else "2")
        el.set(qn("w:author"), "PO")
        el.set(qn("w:date"), "2026-08-10T00:00:00Z")
        r = OxmlElement("w:r")
        t = OxmlElement("w:delText" if kind == "w:del" else "w:t")
        t.set(qn("xml:space"), "preserve")
        t.text = txt
        r.append(t)
        el.append(r)
        tp._p.append(el)
    tp.add_run(" SLA TRACKED-MARK.")

    doc.add_heading("Category table", level=2)
    t = doc.add_table(rows=3, cols=3)
    t.style = "Table Grid"
    t.cell(0, 0).merge(t.cell(0, 2)).text = "MERGED-MARK Category overview"
    for i, row in enumerate([("Cards", "Loans", "Savings"), ("12", "7", "3")], start=1):
        for j, v in enumerate(row):
            t.cell(i, j).text = v

    doc.add_paragraph("Figure below shows the flow.")
    doc.add_picture(io.BytesIO(png("IMAGE-MARK flow diagram")), width=Inches(3))
    doc.add_paragraph("Tiếng Việt: Khách hàng tự phục vụ thành công.")
    doc.save(OUT / "sample.docx")


# ---------------------------------------------------------------- xlsx
def make_xlsx():
    from openpyxl import Workbook
    from openpyxl.comments import Comment
    from openpyxl.workbook.defined_name import DefinedName
    from openpyxl.worksheet.datavalidation import DataValidation

    wb = Workbook()
    ws = wb.active
    ws.title = "Queries"
    ws.append(["Category", "Count", "Share"])
    ws.append(["Cards", 12, "=B2/B5"])
    ws.append(["Loans", 7, "=B3/B5"])
    ws.append(["Other", 26, "=B4/B5"])
    ws.append(["Total", "=SUM(B2:B4)", None])
    ws["A7"] = "MERGED-MARK Notes spanning three columns"
    ws.merge_cells("A7:C7")
    ws["A2"].comment = Comment("COMMENT-MARK Cards includes credit and debit", "BA")
    dv = DataValidation(type="list", formula1='"Open,Closed,Needs Review"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add("D2:D4")
    ws["D1"] = "Status"
    ws["D2"] = "Open"
    wb.defined_names["TotalQueries"] = DefinedName("TotalQueries", attr_text="Queries!$B$5")

    hidden = wb.create_sheet("HiddenLookup")
    hidden.append(["Code", "Label"])
    hidden.append(["HIDDEN-MARK OTH", "Other - user captured text"])
    hidden.sheet_state = "hidden"
    wb.save(OUT / "sample.xlsx")


# ---------------------------------------------------------------- pptx
def make_pptx():
    from pptx import Presentation
    from pptx.util import Inches

    prs = Presentation()
    s1 = prs.slides.add_slide(prs.slide_layouts[1])
    s1.shapes.title.text = "Reduce Other classification"
    s1.placeholders[1].text = "Route unclassified cases to Needs Review"
    s1.notes_slide.notes_text_frame.text = "NOTES-MARK Mention the 45 percent baseline here"
    tbl = s1.shapes.add_table(2, 2, Inches(1), Inches(4.5), Inches(4), Inches(1)).table
    for (r, c), v in {(0, 0): "Metric", (0, 1): "Target", (1, 0): "Other rate", (1, 1): "TABLE-MARK under 10%"}.items():
        tbl.cell(r, c).text = v
    s1.shapes.add_picture(io.BytesIO(png("IMAGE-MARK slide image")), Inches(6), Inches(4.5), width=Inches(3))

    s2 = prs.slides.add_slide(prs.slide_layouts[5])
    s2.shapes.title.text = "HIDDEN-MARK Backup slide"
    s2._element.set("show", "0")
    prs.save(OUT / "sample.pptx")


# ---------------------------------------------------------------- pdf
def make_pdf():
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfgen import canvas

    c = canvas.Canvas(str(OUT / "sample.pdf"), pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, 780, "Case lifecycle summary")
    c.setFont("Helvetica", 11)
    c.drawString(72, 750, "TEXT-MARK A case moves from Open to Resolved or Needs Review.")
    c.drawString(72, 734, "Recontact within 7 days reopens the original case.")
    c.showPage()
    c.drawImage(ImageReader(io.BytesIO(png("SCAN-MARK scanned page, no text layer", (600, 200)))), 72, 500, width=450, height=150)
    c.showPage()
    c.save()


def make_board():
    """Miro/FigJam-style export: one oversized page, coloured stickies with small text, curved connectors,
    a frame — the text layer exists, but the meaning (groups, colours, arrows) is in the layout.
    Expect: page classified visual, positioned item table with fills, overview + tiles, 1 required vision item.
    Also a large PNG of the same kind (image route must tile it)."""
    from reportlab.lib.colors import HexColor
    from reportlab.pdfgen import canvas
    W, H = 4000, 2400
    c = canvas.Canvas(str(OUT / "sample-board.pdf"), pagesize=(W, H))
    c.setStrokeColor(HexColor("#999999"))
    c.rect(100, 100, 3800, 2100)                                   # frame
    c.setFont("Helvetica-Bold", 28)
    c.drawString(120, 2230, "BOARD-MARK Onboarding journey")
    stickies = [("Sign up", "#fff9b1", 300, 1700), ("Verify email", "#fff9b1", 1100, 1700),
                ("Pick goals", "#a6ccf5", 1900, 1700), ("Pain: too many steps", "#f5a9b8", 1100, 1100),
                ("Idea: social login", "#d5f692", 300, 1100), ("Dashboard", "#a6ccf5", 2700, 1700)]
    for label, col, x, y in stickies:
        c.setFillColor(HexColor(col))
        c.rect(x, y, 400, 300, fill=1, stroke=0)
        c.setFillColor(HexColor("#000000"))
        c.setFont("Helvetica", 7)                                  # small: unreadable in a single downscaled render
        c.drawString(x + 20, y + 260, label)
    c.setStrokeColor(HexColor("#333333"))
    c.setLineWidth(3)
    for (x1, y1), (x2, y2) in [((700, 1850), (1100, 1850)), ((1500, 1850), (1900, 1850)), ((2300, 1850), (2700, 1850)),
                               ((1300, 1700), (1300, 1400)), ((500, 1400), (500, 1700))]:
        p = c.beginPath()
        p.moveTo(x1, y1)
        p.curveTo(x1 + 50, y1 + 40, x2 - 50, y2 - 40, x2, y2)
        c.drawPath(p)
    for k in range(12):                                            # extra connector noise like real boards
        p = c.beginPath()
        p.moveTo(200 + k * 300, 400)
        p.curveTo(260 + k * 300, 500, 340 + k * 300, 300, 400 + k * 300, 400)
        c.drawPath(p)
    c.showPage()
    c.save()
    from PIL import Image, ImageDraw
    img = Image.new("RGB", (3200, 1800), "white")
    d = ImageDraw.Draw(img)
    for i, col in enumerate(("#fff9b1", "#a6ccf5", "#f5a9b8")):
        d.rectangle([200 + i * 1000, 600, 800 + i * 1000, 1100], fill=col)
        d.text((230 + i * 1000, 630), f"IMG-MARK sticky {i + 1}", fill="black")
    img.save(OUT / "sample-board.png")


if __name__ == "__main__":
    for fn in (make_docx, make_xlsx, make_pptx, make_pdf, make_board):
        fn()
    print(f"fixtures written to {OUT}")
