---
name: illustrate-note
description: "Create a new visual that explains an idea in this knowledge base and add it to the right note: a concept explainer, a step-by-step mechanism diagram, or a mind map, as a text diagram, table, Mermaid diagram, or SVG. Use when the user asks to draw, diagram, map, visualize, or illustrate a concept or how something works, including for the note being studied. For an existing image file, use add-note-image instead."
---

# Illustrate Note

Make a visual that helps the reader see how an idea works and why, then place it next to the explanation it supports. A good visual in this repo is accurate, easy to maintain, and still useful when read as plain Markdown.

Read [AGENTS.md](../../../AGENTS.md) for note rules and explanation style.

## Inputs And Scope

- One idea to show: a concept, one mechanism, or one comparison that uses the same starting situation.
- A target note and section, when the visual should be saved. Infer them from the conversation or current study topic when clear. Ask one short question only when the idea or target is ambiguous.
- A requested format or style, if any.

When a target note is named or implied, the request authorizes creating the visual and inserting it, even during a [learning-tutor](../learning-tutor/SKILL.md) session. Without a target, show the visual in the conversation and offer to save it. For a preview-only request, do not edit notes. Do not create a new note, flashcards, or other material unless asked.

## 1. Understand The Idea And Its Sources

- Read the relevant section, its neighbors, existing visuals, and the note's `Sources`. Check linked source notes when a claim needs support.
- Choose the one main point the reader should see. If one visual would need several unrelated points, make it smaller or propose separate visuals.
- Keep sourced facts, your own examples, analogies, and assumptions distinct. Do not put an unverified claim into a visual as fact; narrow it, or mark it with `OPEN QUESTION:` in the caption or note.
- Do not turn "important" into "always", or one variant into the definition of the whole idea.

## 2. Choose The Form

| Form | Use when the reader needs to see | Avoid |
| --- | --- | --- |
| Concept explainer | What the idea is, why it matters, and how its parts relate | A poster that copies the whole note |
| Mechanism | Which part acts, what it acts on, and what changes step by step | Decorative icons or a list of step names that hides what happens inside |
| Mind map | The core definition and main ideas to remember and review | Implying time order, or mapping a whole subject |

A comparison, before-and-after, or timeline fits inside these forms. Choose the layout from the content instead of forcing every idea into problem and solution or right and wrong.

## 3. Choose The Medium

Use the lightest medium that shows the idea accurately:

1. **Text diagram or table** in a `text` block or Markdown table: for short flows, layers, and comparisons. Easy to edit and always readable.
2. **Mermaid**: for flows, sequences, state changes, and mind maps (`mindmap`) where boxes and arrows are enough. It stays diffable and renders on GitHub.
3. **SVG file**: when position, shape, cutaways, several states of the same system, or exact labels matter, or when the user asks for an image.

If the user asks for an image, do not deliver only Mermaid or text in its place. Use a raster image tool only if one is actually available in the current session and the user wants an illustrated style. Do not install software, fetch packages, or use paid APIs without asking. When a needed tool is missing, say so and offer a working alternative instead of a fake link.

## 4. Plan The Content Before Drawing

Write the labels, example values, and steps first, then draw. Recalculate every number and check every step.

### Concept Explainer

- Follow the note's reasoning: context or intuition, a small concrete example, then the rule. Keep long explanations and analogy limits in the note or caption.
- Use a concrete case with real quantities or objects instead of placeholders such as "A" and "B" when that helps.
- End with one takeaway line when it adds value.

### Mechanism

List briefly:

- **Parts:** what takes part and where it sits.
- **Start:** the initial state of the relevant material, data, or resources.
- **Trigger:** what makes the next step happen.
- **Steps:** which part acts, what changes, and what condition causes a different branch.
- **Result:** what changed, what stayed the same, and whether the next cycle differs.

Draw the real parts of the model and number the steps or show states before, during, and after. Keep each part in the same position, color, and name across frames. Give each arrow type one meaning, such as fluid flow, a signal, or a reference, and label ambiguous arrows. Do not invent intermediate steps to make the picture look complete.

Example: for [engine oil and filter care](../../../knowledge/automobile-engineering/concepts/engine-oil-and-filter-care.md), a mechanism diagram could show oil in the sump, the pump drawing it, flow through the filter, galleries reaching the crankshaft bearings and valve train, and oil draining back. The note says real engines can add branches, so label the route as simplified.

### Mind Map

- Put the concept name in the center. Make one branch a short answer to "What is it?"
- Choose about three to six main branches that fit this concept, such as purpose, parts, types, core rules, or common confusions. Keep each branch one or two levels deep.
- Make each node a keyword or short phrase. Keep conditions that change the meaning.
- Add an example or formula only when it helps remember a main idea.

## 5. Build And Look At The Result

- Use the note's language, which is usually simple English. Add Vietnamese terms only when the user asks or the note already pairs terms.
- Make labels short and readable at the size shown in Markdown. Use a light background and clear contrast. Do not rely on color alone. Include correct units.
- For SVG, set `viewBox`, `width`, and `height`, use a common font stack, and keep text as text instead of paths so it stays editable.
- Look at the actual result, not only the source code. Render SVG to a PNG in a temporary folder and open it. For example, use headless Chrome or Chromium with `--screenshot`, or `qlmanage -t` on macOS. Check text, numbers, arrow directions, step order, parent-child links, clipping, and overlap.
- For Mermaid, render it when a renderer is already available. Otherwise, check the syntax carefully and report that it was not rendered.
- Test a mechanism by covering the explanatory text: can the reader still follow it from the parts and arrows? If not, fix the layout instead of adding text.
- Fix errors and look again. Do not insert a visual known to be wrong or use the caption to excuse a wrong arrow or state.

## 6. Save And Insert

- Put a text diagram, table, or Mermaid block directly in the note.
- Save an SVG using the existing asset pattern `knowledge/<domain>/assets/<note-slug>/<idea>-<form>.svg`, such as `oil-circulation-mechanism.svg` or `engine-oil-mindmap.svg`. Link the SVG directly. Keep the PNG only if the user needs a raster copy. Do not overwrite an existing visual unless the user asks to replace it.
- Insert the visual right after the explanation or example it supports. A summary-level visual, such as a mind map, can go in `Visual Representation` or near `Mental Model And Summary`. Keep `Practice Question`, `Sources`, and `Related Notes` at the end. Do not change the note's explanation just to fit the visual.
- For an image file, follow the placement, alt-text, and duplicate checks in [add-note-image](../add-note-image/SKILL.md). Use a caption that states its origin honestly:

```markdown
![Oil moving from the sump through the pump and filter to the bearings, then draining back](../assets/engine-oil-and-filter-care/oil-circulation-mechanism.svg)

*Simplified diagram drawn for this note, based on [source]. The example values are illustrative.*
```

- For a complex visual, add a short list after the caption for reading steps or limits. Each bullet should cover one area or step.
- Update the note's `Table Of Contents` only if you add or change a heading.

## 7. Check And Report

- Confirm that the visual covers one idea, matches the note and sources, and keeps assumptions visible.
- Confirm that relative links resolve to files inside the repo. Run `git diff --check`. Say you checked rendered Markdown only if you actually viewed it; viewing an image file is a separate check.
- Unless this is a preview, commit and push as described in [AGENTS.md](../../../AGENTS.md#commit-and-push). Include the note and any new asset files together.
- Report what the visual shows, where it was inserted, and which checks ran. If it is only a preview or a step is unfinished, say so.
