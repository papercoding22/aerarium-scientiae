---
name: setup-learning-domain
description: "Make sure a new learning topic has a home under knowledge/: map the topic to an existing domain, or create the domain folders, README, and index links when none fits. Use when the user wants to start learning a new topic or subject, or asks to add a knowledge domain. Not for writing individual concept or application notes."
---

# Setup Learning Domain

Give a new topic a place in the knowledge base before learning starts, so saved notes land in the right folder. Most topics belong in an existing domain. Create a new domain only when none fits.

Read [AGENTS.md](../../../AGENTS.md) for folder and note rules.

## 1. Map The Topic To A Domain

List the folders in `knowledge/` and read the domain indexes that might fit.

- A **domain** is a broad field that can hold many concept notes over time, such as `cooking` or `personal-finance`. A **topic** is something to learn inside it, such as sourdough bread or emergency funds.
- If an existing domain fits, use it and create nothing. Examples: Kubernetes goes in `software-engineering`, prompt caching in `ai`, and turbochargers in `automobile-engineering`.
- If the topic mainly connects several domains, use `cross-domain`.
- If no domain fits, choose a broad, stable, lowercase kebab-case slug. Name the field, not the first topic: use `cooking`, not `sourdough-bread`.
- A clear request to learn a topic that fits no domain counts as a request for a new domain, so create it without asking. Ask one short question only when the topic fits an existing domain about as well as a new one, or when the right breadth for the slug is unclear.

## 2. Create The Folders

From the repository root, preview first and then run:

```sh
python3 .claude/skills/setup-learning-domain/scripts/ensure_domain.py <slug> --title "<Title>" --description "<One sentence on what this domain is for.>" --dry-run
python3 .claude/skills/setup-learning-domain/scripts/ensure_domain.py <slug> --title "<Title>" --description "<One sentence on what this domain is for.>"
```

The [script](scripts/ensure_domain.py) creates only what is missing:

- `knowledge/<slug>/concepts/.gitkeep` and `knowledge/<slug>/applications/.gitkeep`
- `knowledge/<slug>/README.md`, built from the [domain README template](../../../templates/domain-readme.md)
- a link in the `## Domains` lists of [knowledge/README.md](../../../knowledge/README.md) and the root [README.md](../../../README.md), placed before Cross-Domain

It never overwrites files, so it can safely repair a partly created domain. If it reports a skipped index, add the link by hand.

Use `--title` when capitalization matters, such as `UX Design`. Write the description in simple English, and say what the learner will be able to understand or do.

## 3. Adjust The Domain README

- Keep the generated structure unless the domain needs something specific. For example, if the topic involves personal data, add a line saying that real numbers or private details belong in `private/`, as [personal finance](../../../knowledge/personal-finance/README.md) does.
- Leave the `Learning Roadmap` placeholder until the learner's goal and starting point are known. Then replace it with the plan from [learning-tutor](../learning-tutor/SKILL.md), or a short Mermaid flow and checklist like the existing domains.
- Do not create empty topic subfolders or placeholder notes. Add notes and index links when there is real content to save.

## 4. Finish

- Commit and push as described in [AGENTS.md](../../../AGENTS.md#commit-and-push). Include the new domain folder and both index files.
- Report the domain used or created, and which files changed.
- If the user wants to learn now, continue with [learning-tutor](../learning-tutor/SKILL.md).
