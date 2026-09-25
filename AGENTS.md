# AGENTS.md

Guidance for AI tools working in this personal knowledge base.

## Purpose

This repo supports long-term learning, research, thinking, and synthesis across AI, software engineering, business, and future domains.

Optimize for high information value with low maintenance cost.

## Core Rules

- Use simple English.
- Use examples and practical scenarios when they improve understanding.
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

### First-Principles Explanation

- Before explaining a concept, statement, or fact, consider what the reader needs to understand it. Abstract, complex, technical, or unfamiliar ideas often need context first.
- When context is needed, build a mental model before giving a full definition. Start with the problem or need that makes the concept useful.
- For straightforward, self-explanatory ideas, explain them directly. Do not force extra steps or examples.

When more context is needed, use this progression:

1. Context: Explain the problem, need, or situation behind the concept and why it matters. Do not invent a historical origin.
2. Foundation: Identify the basic principles, assumptions, or building blocks the reader needs. Keep assumptions distinct from established facts.
3. First Principles: Explain the root idea, why it works, and what must be true for it to work.
4. Derivation: Show step by step how the concept follows from those foundations. Introduce its definition once the reasoning gives it meaning.
5. Concrete Example: Immediately follow the explanation with a simple, realistic example connected to the concept. Show how it works in practice, rather than repeating the definition in different words.
6. Mental Model And Summary: End with a simple way to remember and reason about the concept, plus a concise key takeaway. Combine these when they would repeat each other.

Keep the depth proportional to the reader's needs. Combine or skip steps that add no value. The goal is deeper, more intuitive understanding that the reader can reason from independently, not a longer answer or a fixed set of headings for every response.

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

Include a linked `## Table Of Contents` near the top of every note you create. List the note's sections and subsections using normal Markdown heading links. Keep the contents aligned with the final headings when editing a note; exclude the title, the contents heading itself, and headings inside code examples.

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

## Project Skills

- Keep shared Codex and Claude Code skills in `.claude/skills/<skill-name>/SKILL.md`.
- `.agents/skills` is a relative symlink to `../.claude/skills`. Preserve this link so new skills reach both tools automatically.
- Create and edit skills only in `.claude/skills/`; do not maintain separate copies for each tool.
- Use [templates/agent-skill.md](templates/agent-skill.md). Skill frontmatter starts with `name` and `description`; the note metadata rules apply to knowledge notes.
- Keep shared instructions usable by both tools. Add tool-specific settings only when needed.
- Follow the [skill management guide](.claude/README.md) when adding, updating, or removing a skill.

## Uncertainty Markers

Use direct labels when needed:

```text
ASSUMPTION:
OPEN QUESTION:
INFERENCE:
```

Do not remove these labels unless the note has been updated with better evidence.

## Git Safety

- Git username: `papercoding22`
- Git email: `john.ly997@gmail.com`
- Do not commit `private/`.
- Do not overwrite unrelated user changes.
- Keep edits narrow and easy to review.
- Prefer adding or improving focused notes over reorganizing the whole repo.
