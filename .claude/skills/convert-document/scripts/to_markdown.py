#!/usr/bin/env python3
"""Convert a document or URL to Markdown with Microsoft MarkItDown.

Output is a reading and search aid saved under .cache/markitdown/ (ignored by
Git). Cite the original document, not this output.

Usage:
  python3 .claude/skills/convert-document/scripts/to_markdown.py <file-or-url>
      [--out PATH | --stdout] [--force]

PDFs are converted page by page with "## Page N" headings so that notes can
cite page numbers. Pages with almost no text are flagged as image pages.
Everything else (.docx .pptx .xlsx .epub .html .csv .json .xml, web URLs,
YouTube URLs when the extra is installed) goes through MarkItDown directly.

MarkItDown needs Python 3.10+. This wrapper runs on the system python3 and
re-runs itself with the Python of the MarkItDown tool installed by uv:
  uv tool install --python 3.12 'markitdown[pdf,docx,pptx,xlsx]'
Set MARKITDOWN_PYTHON to use a different interpreter.
"""

import argparse
import datetime
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

INSTALL_HINT = (
    "MarkItDown is not installed. Install it once with:\n"
    "  brew install uv\n"
    "  uv tool install --python 3.12 'markitdown[pdf,docx,pptx,xlsx]'"
)
IMAGE_PAGE_CHARS = 40  # pages with less text than this are probably images
URL_RE = re.compile(r"^(https?|file|data):", re.I)


def tool_python():
    env = os.environ.get("MARKITDOWN_PYTHON")
    if env and Path(env).exists():
        return env
    tool_dir = None
    if shutil.which("uv"):
        try:
            tool_dir = subprocess.run(["uv", "tool", "dir"], capture_output=True,
                                      text=True, check=True).stdout.strip()
        except (subprocess.CalledProcessError, OSError):
            pass
    tool_dir = tool_dir or str(Path.home() / ".local/share/uv/tools")
    py = Path(tool_dir) / "markitdown" / "bin" / "python"
    return str(py) if py.exists() else None


def repo_root():
    here = Path(__file__).resolve().parent
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=here,
                             capture_output=True, text=True, check=True)
        return Path(out.stdout.strip())
    except (subprocess.CalledProcessError, OSError):
        return here.parents[3]


def slugify(text):
    text = re.sub(r"^[a-z]+://", "", text.lower())
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:80].strip("-") or "document"


def default_output(source):
    if URL_RE.match(source):
        name = slugify(source)
    else:
        path = Path(source)
        name = slugify(path.stem) + ("-" + path.suffix.lstrip(".").lower() if path.suffix else "")
    return repo_root() / ".cache" / "markitdown" / (name + ".md")


# ---- worker: runs inside the MarkItDown tool's Python -----------------------

def pdf_to_markdown(path):
    from pdfminer.high_level import extract_text

    pages = extract_text(path).split("\f")
    if pages and not pages[-1].strip():
        pages.pop()
    body, image_pages = [], []
    for number, text in enumerate(pages, 1):
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        flag = ""
        if sum(len(l) for l in lines) < IMAGE_PAGE_CHARS:
            image_pages.append(number)
            flag = " (mostly images: view the original page)"
        body.append(f"## Page {number}{flag}\n\n" + "\n".join(lines))
    notes = [f"{len(pages)} pages."]
    if pages and len(image_pages) == len(pages):
        notes.append("No text layer found: read the original PDF as images.")
    elif image_pages:
        notes.append("Mostly-image pages: " + ", ".join(map(str, image_pages)) + ".")
    return " ".join(notes), "\n\n".join(body) + "\n"


def worker(source):
    if not URL_RE.match(source) and source.lower().endswith(".pdf"):
        return pdf_to_markdown(source)
    from markitdown import MarkItDown

    return "", MarkItDown().convert(source).markdown


# ---- entry point -------------------------------------------------------------

def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--worker":
        try:
            info, text = worker(sys.argv[2])
        except ImportError as error:
            sys.exit(f"missing MarkItDown dependency: {error}. {INSTALL_HINT}")
        except Exception as error:  # report conversion failures in one line
            sys.exit(f"conversion failed: {type(error).__name__}: {error}")
        sys.stdout.write(info + "\n\x00\n" + text)
        return

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("source", help="file path or URL")
    target = parser.add_mutually_exclusive_group()
    target.add_argument("--out", help="output file (default: .cache/markitdown/<name>.md)")
    target.add_argument("--stdout", action="store_true", help="print instead of saving")
    parser.add_argument("--force", action="store_true", help="convert again even if cached")
    args = parser.parse_args()

    is_url = bool(URL_RE.match(args.source))
    source = args.source if is_url else str(Path(args.source).expanduser().resolve())
    if not is_url and not Path(source).is_file():
        sys.exit(f"error: file not found: {args.source}")

    out = None if args.stdout else Path(args.out).expanduser() if args.out else default_output(source)
    if out and out.exists() and not args.force and not is_url \
            and out.stat().st_mtime >= Path(source).stat().st_mtime:
        print(f"cached {out}")
        return

    python = tool_python()
    if not python:
        sys.exit(INSTALL_HINT)
    result = subprocess.run([python, str(Path(__file__).resolve()), "--worker", source],
                            capture_output=True, text=True)
    if result.returncode != 0:
        lines = result.stderr.strip().splitlines() or ["unknown error"]
        sys.exit("error: " + lines[-1])
    info, _, text = result.stdout.partition("\n\x00\n")

    label = args.source if is_url else Path(source).name
    header = (
        f"<!-- Converted from {label} with MarkItDown on {datetime.date.today()}. "
        f"Reading aid only; cite the original.{' ' + info.strip() if info.strip() else ''} -->\n\n"
    )
    if out is None:
        sys.stdout.write(header + text)
        return
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(header + text, encoding="utf-8")
    words = len(text.split())
    print(f"saved  {out}  (~{words:,} words{'; ' + info.strip() if info.strip() else ''})")


if __name__ == "__main__":
    main()
