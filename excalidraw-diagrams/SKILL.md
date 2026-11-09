---
name: excalidraw-diagrams
description: >-
  Create clean, minimal Excalidraw diagrams (.excalidraw files) in Nate's house
  style: Geist dark colors picked by role, sharp Architect-style shapes on a
  4 px grid, very few words. Use when the user asks for an Excalidraw file, a
  diagram, a data flow, a sequence or architecture sketch, or an algorithm
  visual saved as .excalidraw.
---

# Excalidraw diagrams

Write a valid `.excalidraw` JSON file that someone understands in a few seconds, with as few words as possible. The style guide is Nate's `geist-colors.excalidraw`: Geist dark colors plus a sample diagram marked "Sloppiness: Architect, Edges: Sharp, Grid Step: 4". This skill is that guide in usable form, for Excalidraw's native dark theme. All ten steps of every hue are in [references/geist-palette.md](references/geist-palette.md), converted for dark theme. Read it before you use teal, purple, pink, gray-alpha, or any step not listed under Tokens.

## Principles

- Draw the idea as a picture: rails, lifelines, buckets, stacks, and branches beat a row of text boxes.
- Few words. Titles of 2 to 5 words, labels of 1 to 3 words, at most one short caption per section.
- One idea per section, stacked top to bottom.
- Gray carries structure; a hue carries meaning. One hue means one thing. Use gray plus at most three hues in a diagram.
- Show emphasis by moving up the gray steps, not by adding a color.
- Flat and sharp: Architect sloppiness, square corners, solid fills, no shadows, gradients, icons, or emoji.

## Color roles

Each Geist scale has ten steps, and each step has one job. Pick the step by its job, then the hue by its meaning.

| Steps | Job in Geist | Job in a diagram |
| --- | --- | --- |
| 100 to 300 | Component backgrounds | Fills: 100 for large regions, 300 for nodes and badges |
| 400 to 600 | Borders | Strokes: 400 structure, 500 ordinary shapes, 600 focus and colored nodes |
| 700 | High-contrast background | Solid fill for the one element the diagram is about, at most one |
| 900, 1000 | Text and icons | 1000 primary text and main arrows, 900 secondary text, return arrows, and marks |

## Native dark theme

Diagrams are always viewed in Excalidraw's native dark theme. Dark theme filters every canvas color, including the background: it inverts 93% and rotates the hue 180deg. So the file stores the color that becomes Geist after the filter, never the Geist hex itself. A Geist value written straight into the file renders wrong: `#0a0a0a` shows up almost white.

- Write colors from the Write column below or from "File values" in the reference. The Renders column is what appears on screen.
- The canvas is `"viewBackgroundColor": "#ffffff"`, which renders as the native dark background `#121212`. Nothing renders darker, so Geist Background 2 has no equivalent. The canvas is also the default surface, so a neutral shape with a `transparent` fill reads as the canvas.
- Gray renders exactly. Vivid hues render a little softer than Geist because the filter caps saturation. That is expected, so don't chase exact Geist values.
- Write every color as 6-digit lowercase hex.

## Tokens

Neutral (gray):

| Role | Write | Renders | Step |
| --- | --- | --- | --- |
| Canvas, `viewBackgroundColor` | `#ffffff` | #121212 | native dark background |
| Neutral fill when a shape needs one | `#f6f6f6` | #1a1a1a | gray-100 |
| Structure: section rules, group boundaries, notes | `#dedede` | #2e2e2e | gray-400 |
| Ordinary shapes, lifelines, rails | `#c4c4c4` | #454545 | gray-500 |
| Focus shape (the neutral node that matters) | `#777777` | #878787 | gray-600 |
| Secondary text, return arrows | `#595959` | #a1a1a1 | gray-900 |
| Primary text, main arrows | `#000000` | #ededed | gray-1000 |

Meaning (hues), as values to write:

| Hue | Meaning | Node fill 300 | Node stroke 600 | Text and marks 900 | Region fill 100 | Region stroke 400 | Solid 700 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| blue | selected, info, main path | `#c0ddff` | `#1489ff` | `#0172d7` | `#e5f2ff` | `#b3d1ff` | `#4f8dff` |
| red | error, failure, danger | `#ffd1d1` | `#ff655f` | `#ff5559` | `#ffeff3` | `#ffc2be` | `#ff6664` |
| amber | in progress, warning | `#ffd6ab` | `#a54c00` | `#bd4500` | `#fff2d8` | `#ffcf8f` | `#8d3c00` |
| green | done, kept, passed | `#b1f4c1` | `#14c249` | `#007e00` | `#d4ffdc` | `#9cedb4` | `#00a921` |

Teal, purple, and pink mark categories that carry no status (owners, services, data kinds). Take them from the reference with the same step pattern.

Text color:

- Labels inside any shape use gray-1000, including colored nodes.
- Use hue 900 only for colored text outside a shape (a status word, a count) and for check marks and Xs.
- On a 700 fill, use gray-1000 on blue and red, and `#ffffff` (renders #121212) on amber and green. The reference lists the other hues.
- Secondary text (subtitles, captions, notes) is gray-900.

## Element defaults

- Every element: `roughness: 0` (Architect), `fillStyle: "solid"`, `opacity: 100`, `angle: 0`, `roundness: null` (sharp edges). The only exception is opacity on gray-alpha shapes from the reference.
- `appState`: `{ "viewBackgroundColor": "#ffffff", "gridSize": 20, "gridStep": 4, "gridModeEnabled": true }`.
- Every `x`, `y`, `width`, and `height` is a multiple of 4. Text bound to a container is exempt because Excalidraw positions it.
- Shapes: `strokeWidth: 1`. The standard node is a 160 x 80 rectangle. Grow in 40 px steps for longer labels. Circles are 64 or 72 px.
- Main arrows: gray-1000, `strokeWidth: 2`, solid, `endArrowhead: "triangle"`, `startArrowhead: null`.
- Return, async, or optional arrows: gray-900, `strokeWidth: 1`, `strokeStyle: "dashed"`, `endArrowhead: "triangle"`.
- Lifelines and rails: gray-500, `strokeWidth: 1`, no arrowheads. A lifeline is an `elbowed: true` arrow bound to the centers of its two shapes.
- Dashed strokes mean not real yet: skipped, optional, not saved, a response, or a note.
- Check marks and Xs: 2 or 3 point `line` elements in hue 900, `strokeWidth: 2`.
- Every arrow starts and ends on a shape edge or a lifeline. Bind arrows to shapes with `startBinding` and `endBinding`, and list the arrow in the shape's `boundElements`.
- Bound text: set `containerId`, add `{ "type": "text", "id": ... }` to the container's `boundElements`, and use `textAlign: "center"`, `verticalAlign: "middle"`, `autoResize: true`, `lineHeight: 1.25`. To label an arrow, set `containerId` to the arrow and `labelPosition: 0.5`.

Binding shape, as Excalidraw writes it:

```json
"startBinding": { "elementId": "service-1", "mode": "orbit", "fixedPoint": [0.5001, 1.06875] },
"endBinding": { "elementId": "service-1-bottom", "mode": "orbit", "fixedPoint": [0.5001, -0.06875] }
```

## Type

| Text | `fontFamily` | Size | Color |
| --- | --- | --- | --- |
| Diagram title | 6 Nunito | 40 | gray-1000 |
| Section title | 6 Nunito | 22 | gray-1000 |
| Section subtitle | 6 Nunito | 16 | gray-900 |
| Row or side label | 5 Excalifont | 20 | gray-1000 |
| Shape and arrow label, including routes like `POST /path` | 5 Excalifont | 16 | gray-1000 |
| Number or value in a shape | 6 Nunito | 18 | gray-1000 |
| Caption or note | 6 Nunito | 14 | gray-900 |
| Code token shown alone (CSS variable, file path) | 3 Cascadia | 16 | gray-1000 |

Titles, subtitles, and captions are left-aligned and unbound. Labels are centered in their container.

## Layout

The layout unit is 40 px. Fine positions snap to the 4 px grid step.

- Section header: a title (22), a subtitle (16) 30 px below it, then a gray-400 rule (`line`, `strokeWidth: 2`) across the full section width. Content starts 40 px below the rule.
- Side labels go in a 160 px column at the left. Content starts 80 px to its right.
- Grids and matrices: 160 x 80 cells on a 200 x 120 pitch, which leaves 40 px gutters.
- Flows: put connected shapes 480 px apart, center to center, so arrow labels fit. Stack parallel messages 40 px apart.
- Notes: a dashed gray-400 rectangle with gray-900 text centered inside.
- Leave 120 px or more between sections. Align centers, and keep the spacing even.

## Patterns that work

- Sequence (the guide's sample): service boxes on top, the same boxes mirrored below, and gray-500 elbowed lifelines joining each pair. Requests are main arrows from one lifeline to another, labeled `POST /path`. Responses are dashed return arrows going back. Each message sits 40 px below the one before.
- Filter or decision: a rail of circles. A kept item is green 300/600 with a green-900 check. A skipped item is a dashed gray-500 circle with a gray-900 X.
- Process: one source shape, main arrows through the steps, then a fan out to outcome nodes colored by meaning.
- Storage or result: outcomes on the left and one destination card on the right. Outcomes that never land get a dashed X and the label "not saved".
- Parallelism or volume: a short caption such as "up to 10 at once" under one node instead of many repeated shapes.
- Comparison matrix: side labels on the left, a section header over each column group, and cells on the grid pitch.

## Workflow

1. Write the story first: 3 sections or fewer, each with one sentence of meaning. Assign each hue its single meaning.
2. Generate the JSON with a small script (Python or Node). Declare the tokens above, using their Write values, as named constants once at the top so no hex is typed inline. Give every element a unique `id`, `seed`, and increasing `index`.
3. Save the file to the repo or the path the user gives, with a descriptive kebab-case name.
4. Run `python3 <skill-dir>/scripts/check_style.py <file>.excalidraw` and fix every finding until it prints `ok`. The script checks colors against the dark-theme file values, the background, sloppiness, sharp edges, fonts, stroke widths, opacity, and the 4 px grid.
5. Render a preview of what dark theme shows: an SVG of the same elements with every color passed through `rendered()` from `scripts/check_style.py`. On macOS, `qlmanage -t -s 1600 -o <dir> <file>.svg` turns it into a PNG. Look at it. Done means: no overlaps, no clipped text, every arrow lands on a shape or lifeline, and every label is readable against its fill.
6. Reply with the file path and a short summary of each section. If the diagram was checked in a preview rather than in Excalidraw, say so.
