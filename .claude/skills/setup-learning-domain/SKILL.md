---
name: setup-learning-domain
description: "Make sure a new learning topic has a home under knowledge/: interview the user when the request is unclear, then map the topic to an existing domain or create the domain folders, README, and index links when none fits. Use when the user wants to start learning a new topic or subject, or asks to add a knowledge domain. Not for writing individual concept or application notes."
---

# Setup Learning Domain

Give a new topic a place in the knowledge base before learning starts, so saved notes land in the right folder. Most topics belong in an existing domain. Create a new domain only when none fits.

Read [AGENTS.md](../../../AGENTS.md) for folder and note rules.

## 1. Check Whether The Request Is Clear

A request is clear when you can name the topic, what the user means by it, and the domain it belongs in. For example, "I want to learn how sourdough fermentation works" is clear. Go straight to step 3 for a clear request.

Interview the user first when any of these is true:

- **The topic is vague or very broad**, such as "I want to learn something about money" or "teach me design".
- **The term has several meanings**, such as "Rust" (programming language or corrosion) or "Spark" (Apache Spark or something else).
- **The scope is unclear:** it could be one topic in an existing domain or the start of a whole new field.
- **The goal changes where the topic belongs.** For example, "learn negotiation" could be for salary talks (`business`) or for everyday life (`cross-domain`).

## 2. Interview To Understand

Ask only what you need to place the topic well. This is a short conversation, not a form.

- Ask one or two short questions per turn, then wait for the answer. Do not create folders until the unclear points are settled.
- Offer concrete choices when they help, based on what is already in `knowledge/`. For example: "Do you mean Rust the programming language? That would go in `software-engineering`." Leave room for an answer you did not list.
- Cover only the gaps, in this order:
  1. **What:** the exact topic and what the user means by it.
  2. **Why:** what the user wants to understand or be able to do, such as for work, a project, an exam, or curiosity.
  3. **How broad:** one focused topic, or a field they expect to keep learning over time.
  4. **Where:** whether an existing domain fits, or which name a new domain should have.
- Do not ask what the user has already said, what you can find in the repository, or teaching questions such as their current level or study time. Those belong to [learning-tutor](../learning-tutor/SKILL.md).
- Once the answers are clear, restate the plan in one or two sentences and wait for confirmation. For example: "I'll create `knowledge/cooking/` for home cooking, starting with sourdough." Skip this step when the user already chose the domain.
- If the user wants to skip the interview, use your best guess, state it, and continue.

## 3. Map The Topic To A Domain

List the folders in `knowledge/` and read the domain indexes that might fit.

- A **domain** is a broad field that can hold many concept notes over time, such as `cooking` or `personal-finance`. A **topic** is something to learn inside it, such as sourdough bread or emergency funds.
- If an existing domain fits, use it and create nothing. Examples: Kubernetes goes in `software-engineering`, prompt caching in `ai`, and turbochargers in `automobile-engineering`.
- If the topic mainly connects several domains, use `cross-domain`.
- If no domain fits, choose a broad, stable, lowercase kebab-case slug. Name the field, not the first topic: use `cooking`, not `sourdough-bread`.
- A clear request to learn a topic that fits no domain counts as a request for a new domain, so create it without asking. If mapping raises a new doubt, go back to step 2.

## 4. Create The Folders

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

## 5. Adjust The Domain README

- Keep the generated structure unless the domain needs something specific. For example, if the topic involves personal data, add a line saying that real numbers or private details belong in `private/`, as [personal finance](../../../knowledge/personal-finance/README.md) does.
- Leave the `Learning Roadmap` placeholder until the learner's goal and starting point are known. Then replace it with the plan from [learning-tutor](../learning-tutor/SKILL.md), or a short Mermaid flow and checklist like the existing domains.
- Do not create empty topic subfolders or placeholder notes. Add notes and index links when there is real content to save.

## 6. Finish

- Commit and push as described in [AGENTS.md](../../../AGENTS.md#commit-and-push). Include the new domain folder and both index files.
- Report the domain used or created, and which files changed.
- If the user wants to learn now, continue with [learning-tutor](../learning-tutor/SKILL.md). Pass on what the interview found, especially the goal, so the user is not asked again.
