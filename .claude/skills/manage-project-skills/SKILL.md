---
name: manage-project-skills
description: "Create, update, rename, or remove repository-local skills shared by Codex and Claude Code. Use when the user asks to manage skills in this project."
---

# Manage Project Skills

Maintain one shared copy of each skill in this repository.

## Project Layout

Read [AGENTS.md](../../../AGENTS.md) and the [skill management guide](../../README.md) before changing a skill.

- The source of truth is `.claude/skills/<skill-name>/SKILL.md`, relative to the repository root.
- `.agents/skills` points to `../.claude/skills`. Preserve this shared-directory link; new skills need no separate Codex copy.
- Use the [agent skill template](../../../templates/agent-skill.md) for new skills.

## Create or Update

1. Inspect existing skills and the worktree. Improve the matching skill when one already covers the requested task.
2. Identify the task, when the skill should apply, the required inputs, and the expected result. Ask only for missing details that materially affect the workflow.
3. Create or edit the skill under `.claude/skills/`. Match the folder and frontmatter `name`, using lowercase letters, digits, and single hyphens. Keep the name under 64 characters and avoid `synced`.
4. Write a specific `description` so either tool can select the skill. Keep shared instructions independent of one tool's command syntax or unavailable integrations. Use `name` and `description` as the initial frontmatter; add tool-specific settings only when needed and preserve existing settings when updating.
5. Describe only the task-specific workflow. Refer to existing project rules and templates instead of duplicating them. Add scripts or supporting files only when they have a concrete use, and link them from `SKILL.md`.
6. Update the available-skills table in `.claude/README.md` when the catalog changes.

Keep this task within the repository unless the user requests a wider installation. A request to create a skill authorizes writing its instructions; any actions performed by that skill still need to fit the user's task and permissions.

## Rename or Remove

Rename or remove only the skill the user identifies. For a rename, update the folder, frontmatter name, guide entry, and affected references. For removal, remove its folder and guide entry. Preserve the shared-directory link and unrelated skills.

## Validate

- Validate the YAML frontmatter with an available YAML parser or skill validator. Confirm `name` and `description` are non-empty and the name matches the folder.
- Confirm both `.claude/skills/<skill-name>/SKILL.md` and `.agents/skills/<skill-name>/SKILL.md` resolve to the same file for each added or changed skill.
- Check local links and run `git diff --check`.
- Review one request that should use the skill and one nearby request that should not. Run any new helper scripts with safe sample input when practical.
- Report the changed files and invocation examples: `$skill-name` in Codex and `/skill-name` in Claude Code. State which checks ran and whether actual invocation in each tool was tested.
