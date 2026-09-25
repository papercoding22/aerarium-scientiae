# Project Skills

Keep one copy of each skill and use it with Codex and Claude Code in this repository.

## Layout

```text
.claude/skills/                 Shared skill files; edit here.
  manage-project-skills/
    SKILL.md
.agents/skills -> ../.claude/skills
                               Codex reads the same directory.
templates/agent-skill.md        Starter for a new skill.
```

The relative symlink works when the repository moves. Preserve it as a symlink when cloning or copying the project. Future skills need no extra links or sync step.

[AGENTS.md](../AGENTS.md) holds the project rules. [CLAUDE.md](../CLAUDE.md) imports those rules for Claude Code.

## Available Skills

| Skill | Purpose |
| --- | --- |
| [manage-project-skills](skills/manage-project-skills/SKILL.md) | Create, update, or remove shared project skills. |

## Use a Skill

Open this project in Codex or Claude Code, then include the skill name in your request:

| Tool | Example |
| --- | --- |
| Codex | `$manage-project-skills Create a skill for turning an article into a source note.` |
| Claude Code | `/manage-project-skills Create a skill for turning an article into a source note.` |

Both tools can also select a skill when its description matches your request. If a new or changed skill does not appear, restart the session from this repository.

## Add a Skill

Ask either tool to use `manage-project-skills`, or create the files yourself from the repository root:

```sh
mkdir -p .claude/skills/my-skill
cp templates/agent-skill.md .claude/skills/my-skill/SKILL.md
```

Then:

1. Replace the template text. Match `name` to the folder name. Use lowercase letters, digits, and single hyphens, with fewer than 64 characters. Avoid the reserved name `synced`.
2. Write a description that says what the skill does and when to use it.
3. Keep the workflow focused on one repeatable task, with clear inputs and an expected result.
4. Add `scripts/`, `references/`, or `assets/` inside the skill only when useful. Link supporting files from `SKILL.md`.
5. Add a link to the available-skills table above.

Use standard `name` and `description` frontmatter for shared skills. Tool-specific options and syntax may behave differently across tools; add them only when the workflow needs them.

## Update or Remove a Skill

Edit its files under `.claude/skills/`. Both tools read those changes through the shared directory.

When removing a skill, remove only its folder and its link in the table above. Preserve `.agents/skills` for the remaining skills. When renaming a skill, update its folder, frontmatter `name`, and references together.

## Check the Setup

From the repository root:

```sh
readlink .agents/skills
test .claude/skills/manage-project-skills/SKILL.md -ef .agents/skills/manage-project-skills/SKILL.md
git diff --check
```

The first command should print `../.claude/skills`. The second succeeds silently when both paths reach the same file. For a new skill, replace `manage-project-skills` with its name.

Check each skill's YAML frontmatter and local links. Try a realistic request in each tool before relying on its behavior; matching file paths alone does not test invocation.

Keep the skill files, guide, template, and symlink in version control when committing this setup.

## Official References

- [Codex skills](https://developers.openai.com/codex/skills)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code project instructions and imports](https://code.claude.com/docs/en/memory)
