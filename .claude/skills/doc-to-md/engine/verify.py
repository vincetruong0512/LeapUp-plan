#!/usr/bin/env python3
"""/doc-to-md fidelity gate — prove no content was lost, don't assert it.

For every file in <out>/_manifest.json:
  1. Re-extract the source text by an INDEPENDENT path (raw OOXML text nodes, pdfminer for PDFs,
     raw bytes for text formats) — not the library convert.py used.
  2. Token coverage: share of source tokens (Unicode NFC, case-folded, multiset) present in the .md.
     Lists source paragraphs that are (mostly) missing.
  3. Structure counts: pages / slides / sheets / embedded images vs what the .md + assets contain.
  4. Vision: required `vision-pending` blocks still open -> INCOMPLETE (Claude must transcribe them).

Status per file: PASS · INCOMPLETE (vision pending) · FAIL (coverage < threshold or count mismatch)
· UNVERIFIED-TEXT (no independent extractor for this type — structure checks only). Text formats
that report UNVERIFIED-TEXT say so explicitly instead of printing a bare OK.

Writes <out>/_conversion-report.md and stamps fidelity fields into each .md frontmatter.
Usage: PYTHONUTF8=1 .tools/convert/Scripts/python.exe .claude/skills/doc-to-md/engine/verify.py <out> [--threshold 99.5]
Exit: 0 = no FAIL, 1 = at least one FAIL, 2 = bad input.
"""
from __future__ import annotations

import argparse
import email
import email.policy
import html
import json
import re
import sys
import unicodedata
import zipfile
from collections import Counter
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET

TOKEN = re.compile(r"\w+", re.UNICODE)


def tokens(text: str) -> list[str]:
    return TOKEN.findall(unicodedata.normalize("NFC", text).casefold())


# ------------------------------------------------------------------ independent extractors -> list of paragraphs
BOUNDARY = {"ins", "del", "moveFrom", "moveTo"}  # tracked-change edges are word breaks for a reader


def para_text(el) -> str:
    out = []
    for child in el:
        local = child.tag.rsplit("}", 1)[-1]
        if local in ("t", "delText") and child.text:
            out.append(child.text)
        if local == "p":  # nested paragraph (text box): root.iter() visits it on its own — don't count twice
            continue
        if local == "fld" and child.get("type") == "slidenum":  # auto slide-number field, not content
            continue
        inner = para_text(child)
        out.append(f" {inner} " if local in BOUNDARY else inner)
    return "".join(out)


def ooxml_paragraphs(path: Path, part_patterns: list[str]) -> list[str]:
    """Join text nodes per paragraph (runs split words mid-way, so never tokenize run-by-run)."""
    paras = []
    with zipfile.ZipFile(path) as z:
        for name in sorted(z.namelist()):
            if not any(re.fullmatch(p, name) for p in part_patterns):
                continue
            root = ET.fromstring(z.read(name))
            for el in root.iter():
                local = el.tag.rsplit("}", 1)[-1]
                if local == "p":  # w:p, a:p
                    t = para_text(el)
                    if t.strip():
                        paras.append(t)
                elif local == "c" and "spreadsheetml" in el.tag:
                    # worksheet cell: formula text + value. For t="s" the <v> is an INDEX into sharedStrings
                    # (its text is counted via <si>), so never count it as content.
                    for x in el:
                        xl = x.tag.rsplit("}", 1)[-1]
                        if xl == "f" and x.text:
                            paras.append(x.text)
                        elif xl == "v" and x.text and el.get("t") != "s":
                            paras.append(x.text)
                elif local == "v" and "drawingml/2006/chart" in el.tag and el.text and el.text.strip():
                    paras.append(el.text)  # chart cached values
                elif local in ("formula1", "formula2", "definedName") and el.text and el.text.strip():
                    paras.append(el.text)  # data validations, defined names
                elif local in ("si", "is", "comment", "threadedComment") and "spreadsheetml" in el.tag or local == "threadedComment":
                    # shared/inline strings + xlsx comments (Word's w:comment holds w:p, already counted above)
                    t = "".join(x.text or "" for x in el.iter() if x.tag.rsplit("}", 1)[-1] == "t")
                    if t.strip():
                        paras.append(t)
                elif local == "text" and el.text and el.text.strip():  # pptx comments
                    paras.append(el.text)
    return paras


DOCX_PARTS = [r"word/document\.xml", r"word/header\d*\.xml", r"word/footer\d*\.xml", r"word/footnotes\.xml",
              r"word/endnotes\.xml", r"word/comments\.xml", r"word/diagrams/data\d+\.xml", r"word/charts/chart\d+\.xml"]
PPTX_PARTS = [r"ppt/slides/slide\d+\.xml", r"ppt/notesSlides/notesSlide\d+\.xml", r"ppt/comments/.+\.xml",
              r"ppt/diagrams/data\d+\.xml", r"ppt/charts/chart\d+\.xml"]
XLSX_PARTS = [r"xl/sharedStrings\.xml", r"xl/worksheets/sheet\d+\.xml", r"xl/comments[^/]*\.xml", r"xl/comments/[^/]+\.xml",
              r"xl/threadedComments/[^/]+\.xml", r"xl/workbook\.xml",
              r"xl/charts/chart\d+\.xml", r"xl/diagrams/data\d+\.xml"]


def pdf_paragraphs(path: Path) -> list[str]:
    from pdfminer.high_level import extract_text  # independent of PyMuPDF used by convert.py
    return [p for p in re.split(r"\n\s*\n", extract_text(str(path))) if p.strip()]


def html_paragraphs(path: Path) -> list[str]:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(path.read_bytes(), "html.parser")
    for s in soup(["script", "style", "noscript"]):
        s.decompose()
    return [l for l in soup.get_text("\n").splitlines() if l.strip()]


def epub_paragraphs(path: Path) -> list[str]:
    from bs4 import BeautifulSoup
    paras = []
    with zipfile.ZipFile(path) as z:
        for name in sorted(n for n in z.namelist() if n.lower().endswith((".xhtml", ".html", ".htm"))):
            soup = BeautifulSoup(z.read(name), "html.parser")
            for s in soup(["script", "style", "nav"]):
                s.decompose()
            paras += [l for l in soup.get_text("\n").splitlines() if l.strip()]
    return paras


def text_paragraphs(path: Path) -> list[str]:
    return [l for l in path.read_text(encoding="utf-8", errors="replace").splitlines() if l.strip()]


def eml_paragraphs(path: Path) -> list[str]:
    msg = email.message_from_bytes(path.read_bytes(), policy=email.policy.default)
    paras = [str(msg[h]) for h in ("From", "To", "Cc", "Subject") if msg[h]]
    body = msg.get_body(preferencelist=("plain",))
    if body is not None:
        paras += [l for l in body.get_content().splitlines() if l.strip()]
    return paras


EXTRACTORS = {
    ".docx": lambda p: ooxml_paragraphs(p, DOCX_PARTS), ".docm": lambda p: ooxml_paragraphs(p, DOCX_PARTS),
    ".pptx": lambda p: ooxml_paragraphs(p, PPTX_PARTS), ".pptm": lambda p: ooxml_paragraphs(p, PPTX_PARTS),
    ".xlsx": lambda p: ooxml_paragraphs(p, XLSX_PARTS), ".xlsm": lambda p: ooxml_paragraphs(p, XLSX_PARTS),
    ".pdf": pdf_paragraphs,
    ".html": html_paragraphs, ".htm": html_paragraphs,
    ".md": text_paragraphs, ".markdown": text_paragraphs, ".txt": text_paragraphs, ".csv": text_paragraphs,
    ".tsv": text_paragraphs, ".json": text_paragraphs, ".xml": text_paragraphs, ".yaml": text_paragraphs, ".yml": text_paragraphs,
    ".eml": eml_paragraphs, ".epub": epub_paragraphs,
}


# ------------------------------------------------------------------ checks
def md_body(md: str) -> str:
    if md.startswith("---"):
        end = md.find("\n---", 3)
        md = md[end + 4:] if end > 0 else md
    return html.unescape(md.replace("\\", ""))


def coverage(src_paras: list[str], md_text: str) -> tuple[float, list[str], list[str], int]:
    md_tok = Counter(tokens(md_text))
    md_set = set(md_tok)
    src_tok = Counter(t for p in src_paras for t in tokens(p))
    total = sum(src_tok.values())
    if total == 0:
        return 100.0, [], [], 0
    matched = sum(min(n, md_tok.get(t, 0)) for t, n in src_tok.items())
    missing_tokens = [f"{t} (×{n - md_tok.get(t, 0)})" for t, n in src_tok.most_common() if md_tok.get(t, 0) < n][:20]
    missing_paras = []
    for p in src_paras:
        pt = tokens(p)
        if pt and sum(t in md_set for t in pt) / len(pt) < 0.8:
            missing_paras.append(p.strip().replace("\n", " ")[:140])
    return 100.0 * matched / total, missing_tokens, missing_paras[:15], total


def structure_checks(entry: dict, src: Path, md: str, out: Path) -> list[str]:
    problems = []
    ext = src.suffix.lower()
    stem = entry["stem"]
    stats = entry.get("stats", {})
    asset_dir = out / "assets" / stem
    on_disk = len([p for p in asset_dir.rglob("*") if p.is_file() and not p.name.endswith("-render.png")]) if asset_dir.exists() else 0
    if ext in (".pptx", ".pptm"):
        with zipfile.ZipFile(src) as z:
            n = len([x for x in z.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", x)])
        got = len(re.findall(r"^## Slide \d+", md, re.M))
        if got != n:
            problems.append(f"slides: source {n}, markdown {got}")
    if ext in (".xlsx", ".xlsm"):
        with zipfile.ZipFile(src) as z:
            n = len(re.findall(r"<(?:\w+:)?sheet\s", z.read("xl/workbook.xml").decode("utf-8", "replace")))
        got = len(re.findall(r"^## Sheet: ", md, re.M))
        if got != n:
            problems.append(f"sheets: source {n}, markdown {got}")
    if ext == ".pdf":
        import pymupdf
        with pymupdf.open(str(src)) as d:
            n = len(d)
            xrefs = {img[0] for page in d for img in page.get_images(full=True)}
        got = len(re.findall(r"^## Page \d+", md, re.M))
        if got != n:
            problems.append(f"pages: source {n}, markdown {got}")
        if on_disk < len(xrefs):
            problems.append(f"images: source {len(xrefs)} unique, extracted {on_disk}")
    if ext in (".docx", ".docm", ".xlsx", ".xlsm"):
        prefix = "word/media/" if ext.startswith(".doc") else "xl/media/"
        with zipfile.ZipFile(src) as z:
            n = len([x for x in z.namelist() if x.startswith(prefix)])
        if on_disk < n:
            problems.append(f"images: source {n}, extracted {on_disk}")
    return problems


def stamp_frontmatter(md_path: Path, fields: dict):
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return
    end = text.find("\n---", 3)
    lines = [l for l in text[4:end].splitlines() if l.split(":", 1)[0] not in fields]
    lines += [f"{k}: {json.dumps(v, ensure_ascii=False) if isinstance(v, str) else v}" for k, v in fields.items()]
    md_path.write_text("---\n" + "\n".join(lines) + text[end:], encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--threshold", type=float, default=99.5)
    a = ap.parse_args()
    out = Path(a.out)
    mf = out / "_manifest.json"
    if not mf.exists():
        print(f"no _manifest.json in {out}", file=sys.stderr)
        return 2
    manifest = json.loads(mf.read_text(encoding="utf-8"))
    rows, details, any_fail = [], [], False

    for e in manifest["files"]:
        name = e["source_name"]
        if e.get("status") == "failed":
            any_fail = True
            rows.append([name, "—", "—", "—", "—", "FAIL", e.get("error", "")])
            continue
        # legacy/ODF files are checked against the kept LibreOffice intermediate (assets/_intermediate/)
        src, md_path = Path(e.get("verify_path") or e["source_path"]), out / f"{e['stem']}.md"
        md = md_path.read_text(encoding="utf-8")
        body = md_body(md)
        pending = len(re.findall(r"<!-- vision-pending: [^|]+\| [^|]+\| required -->", md))
        optional = len(re.findall(r"<!-- vision-pending: [^|]+\| [^|]+\| if-text-visible -->", md))
        done = len(re.findall(r"<!-- vision-transcribed: ", md))
        ext = src.suffix.lower()
        problems = structure_checks(e, src, md, out) if src.exists() else ["source file no longer available — cannot verify"]

        extractor = EXTRACTORS.get(ext)
        cov_txt, cov_val = "n/a", None
        if extractor and src.exists():
            try:
                cov_val, miss_tok, miss_par, total = coverage(extractor(src), body)
                cov_txt = f"{cov_val:.2f}% of {total} tokens"
                if total == 0:  # nothing to check against (image-only source): never a vacuous PASS
                    cov_val, cov_txt = None, "n/a (source has no text layer)"
                if miss_tok or miss_par:
                    details.append(f"### {name}\n\n**Missing tokens:** {', '.join(miss_tok) or '—'}\n\n"
                                   + ("**Source paragraphs mostly absent from the .md:**\n\n" + "".join(f"- {p}\n" for p in miss_par) if miss_par else ""))
            except Exception as ex:
                problems.append(f"independent extraction failed: {type(ex).__name__}: {ex}")

        if (cov_val is not None and cov_val < a.threshold) or problems:
            status = "FAIL"
            any_fail = True
        elif pending:
            status = "INCOMPLETE"
        elif cov_val is None:
            status = "UNVERIFIED-TEXT"
        else:
            status = "PASS"
        warnings = e.get("warnings", []) + problems
        rows.append([name, f"{e['stem']}.md", e.get("engine", ""), cov_txt,
                     f"{pending} required open · {optional} optional · {done} done", status, "; ".join(warnings)])
        stamp_frontmatter(md_path, {"status": {"PASS": "verified", "INCOMPLETE": "needs-vision", "FAIL": "failed-verification",
                                               "UNVERIFIED-TEXT": "converted-unverified"}[status],
                                    "fidelity_coverage": round(cov_val, 2) if cov_val is not None else "n/a",
                                    "fidelity_checked": date.today().isoformat()})

    hdr = ["Source", "Markdown", "Engine", "Text coverage", "Vision", "Status", "Warnings / problems"]
    table = "| " + " | ".join(hdr) + " |\n|" + "---|" * len(hdr) + "\n" + "".join(
        "| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |\n" for r in rows)
    report = (f"---\ntype: source-conversion-report\nupdated: {date.today().isoformat()}\nthreshold: {a.threshold}\n---\n\n"
              f"# Conversion report\n\n{table}\n"
              "Status: PASS = independent re-extraction found ≥ threshold of source tokens and all structure counts match · "
              "INCOMPLETE = required vision transcription still open · FAIL = content or structure missing · "
              "UNVERIFIED-TEXT = no independent extractor for this type (structure only).\n\n"
              + ("## Gaps\n\n" + "\n".join(details) if details else ""))
    (out / "_conversion-report.md").write_text(report, encoding="utf-8")
    print(table)
    return 1 if any_fail else 0


if __name__ == "__main__":
    sys.exit(main())
