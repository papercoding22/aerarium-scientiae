# AGENTS.md

Guidance for AI tools working in this personal knowledge base.

## Purpose

This repo supports long-term learning, research, thinking, and synthesis across AI, software engineering, business, and future domains.

Optimize for high information value with low maintenance cost.

## Core Rules

- Use simple English.
- Prefer clear examples and practical scenarios.
- Keep notes atomic: one concept note per single idea.
- Preserve uncertainty instead of overstating confidence.
- Do not invent sources, facts, owners, dates, or conclusions.
- Use normal Markdown links.
- Avoid heavy metadata, tags, IDs, or deep folder nesting.
- Keep private thinking separate from polished or reusable knowledge.

## Explanation Style

- Use clear, everyday English.
- Prefer short sentences over complex ones.
- Avoid unnecessary jargon, academic language, and complicated words.
- Do not use difficult words just to sound sophisticated.
- Be friendly and conversational.
- Avoid sounding robotic, overly formal, or like a textbook.
- Use analogies when they help explain the idea.
- Build understanding step by step.

## Folder Rules

- `inbox/`: temporary capture only. Process during weekly review.
- `sources/`: one note per source, focused on what the source said.
- `knowledge/<domain>/concepts/`: reusable atomic concept notes.
- `knowledge/<domain>/applications/`: practical usage notes for life, work, or business.
- `learning/`: flashcards, questions, and weekly review notes.
- `outputs/`: essays, research reports, and synthesis documents.
- `private/`: local-only notes. Do not rely on this folder being committed to Git.
- `templates/`: reusable note templates.

## Initial Domains

- `ai`
- `software-engineering`
- `business`
- `cross-domain`

Ask before creating a new top-level area unless the user clearly requests it.

## Metadata

Keep metadata to 3-5 simple fields. Use these confidence values:

```text
high
medium
low
needs-review
```

Use usefulness ratings as numbers:

```text
1/5
2/5
3/5
4/5
5/5
```

## Note Creation

When adding a concept note:

1. Place it under the best domain.
2. Use `templates/concept-note.md`.
3. Include a visual representation when possible.
4. Add sources when practical.
5. Add related notes only when useful.
6. Update the domain `README.md` with a simple list link.

When adding a source note:

1. Place it under the correct source type.
2. Use `templates/source-note.md`.
3. Use filenames like `deep-work-cal-newport.md`.
4. Extract important ideas into concept notes when useful.

When adding an application note:

1. Place it under `knowledge/<domain>/applications/`.
2. Use `templates/application-note.md`.
3. Link related concept notes when useful.

## Uncertainty Markers

Use direct labels when needed:

```text
ASSUMPTION:
OPEN QUESTION:
INFERENCE:
```

Do not remove these labels unless the note has been updated with better evidence.

## Git Safety

- Do not commit `private/`.
- Do not overwrite unrelated user changes.
- Keep edits narrow and easy to review.
- Prefer adding or improving focused notes over reorganizing the whole repo.
