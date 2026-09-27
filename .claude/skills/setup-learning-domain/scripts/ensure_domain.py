#!/usr/bin/env python3
"""Create a knowledge domain scaffold if it does not exist yet.

Safe to run again: existing files are never overwritten, and index links
are added only when missing.

Usage:
  python3 .claude/skills/setup-learning-domain/scripts/ensure_domain.py <slug> \
      [--title "Title"] [--description "One sentence."] [--dry-run]
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def repo_root() -> Path:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=True,
            cwd=Path(__file__).resolve().parent,
        )
        root = Path(out.stdout.strip())
    except (subprocess.CalledProcessError, FileNotFoundError):
        root = Path(__file__).resolve().parents[4]
    if not (root / "knowledge").is_dir() or not (root / "templates").is_dir():
        sys.exit(f"error: {root} does not look like the knowledge base root")
    return root


def default_title(slug: str) -> str:
    return " ".join(word.capitalize() for word in slug.split("-"))


def add_index_link(index: Path, name: str, title: str, target: str, dry_run: bool) -> str:
    """Add '- [title](target)' to the '## Domains' list, before Cross-Domain."""
    if not index.exists():
        return f"skipped   {name} (missing)"
    lines = index.read_text(encoding="utf-8").splitlines(keepends=True)
    if any(f"]({target})" in line for line in lines):
        return f"exists    link in {name}"
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == "## Domains")
    except StopIteration:
        return f"skipped   {name} (no '## Domains' section; add the link by hand)"

    items = []
    i = start + 1
    while i < len(lines) and not lines[i].startswith("#"):
        if lines[i].startswith("- ["):
            items.append(i)
        i += 1
    entry = f"- [{title}]({target})\n"
    if not items:
        return f"skipped   {name} (empty '## Domains' list; add the link by hand)"
    cross = [n for n in items if "cross-domain/" in lines[n]]
    pos = cross[0] if cross else items[-1] + 1
    lines.insert(pos, entry)
    if not dry_run:
        index.write_text("".join(lines), encoding="utf-8")
    return f"{'would update' if dry_run else 'update'} {name}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("slug", help="lowercase kebab-case domain name, e.g. cooking")
    parser.add_argument("--title", help="display title (default: from slug)")
    parser.add_argument("--description", default="",
                        help="one sentence on what this domain is for")
    parser.add_argument("--dry-run", action="store_true",
                        help="print what would change without writing")
    args = parser.parse_args()

    if not SLUG_RE.fullmatch(args.slug) or len(args.slug) > 63:
        sys.exit("error: slug must be lowercase kebab-case, e.g. 'machine-learning'")

    root = repo_root()
    title = args.title or default_title(args.slug)
    description = args.description or (
        f"Use this domain to learn {title.lower()} and apply it in real situations."
    )
    domain = root / "knowledge" / args.slug
    prefix = "would " if args.dry_run else ""
    report = []

    for sub in ("concepts", "applications"):
        folder = domain / sub
        keep = folder / ".gitkeep"
        if folder.is_dir():
            report.append(f"exists    {folder.relative_to(root)}/")
            continue
        if not args.dry_run:
            folder.mkdir(parents=True)
            keep.touch()
        report.append(f"{prefix}create {keep.relative_to(root)}")

    readme = domain / "README.md"
    if readme.exists():
        report.append(f"exists    {readme.relative_to(root)}")
    else:
        template = (root / "templates" / "domain-readme.md").read_text(encoding="utf-8")
        text = template.replace("{title}", title).replace("{description}", description)
        if not args.dry_run:
            domain.mkdir(parents=True, exist_ok=True)
            readme.write_text(text, encoding="utf-8")
        report.append(f"{prefix}create {readme.relative_to(root)}")

    for index, target in (
        (root / "knowledge" / "README.md", f"{args.slug}/README.md"),
        (root / "README.md", f"knowledge/{args.slug}/README.md"),
    ):
        name = str(index.relative_to(root))
        report.append(add_index_link(index, name, title, target, args.dry_run))

    print("\n".join(report))


if __name__ == "__main__":
    main()
