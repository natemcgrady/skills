# Geist dark palette

Every Geist dark color, transcribed from the style guide `~/workspace/natemcgrady/geist-colors.excalidraw`. `scripts/check_style.py` reads the hex values in this file as the allowed set, so edit colors here and nowhere else.

## Step roles

| Steps | Geist job | Diagram use |
| --- | --- | --- |
| 100, 200, 300 | Component backgrounds: default, hover, active | Fills. 100 for large regions, 300 for nodes and badges. |
| 400, 500, 600 | Borders: default, hover, active | Strokes. 400 for structure, 500 for ordinary shapes, 600 for focus and colored nodes. |
| 700, 800 | High-contrast backgrounds (800 is the hover of 700) | 700 as the solid fill of the one element a diagram is about. 800 is unused. |
| 900, 1000 | Text and icons: secondary, primary | Text, arrows, check marks, Xs. |

Notes from the guide:

- If a component's default background is Background 1, Color 1 is its hover background and Color 2 its active background. Small elements like badges use Color 2 or Color 3.
- Borders: use solid gray by default. Use the matching gray-alpha step only when the edge must blend with its surface.
- Use Background 1 in most cases, especially under color. Use Background 2 sparingly, for a subtle separation.

## Backgrounds

| Token | Hex | Use |
| --- | --- | --- |
| background-100 (Background 1) | `#0a0a0a` | Canvas and default surface |
| background-200 (Background 2) | `#000000` | Recessed panel, sparingly |

## Scales

| Hue | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 1000 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gray | `#1a1a1a` | `#1f1f1f` | `#292929` | `#2e2e2e` | `#454545` | `#878787` | `#8f8f8f` | `#7d7d7d` | `#a1a1a1` | `#ededed` |
| blue | `#06193a` | `#022248` | `#002f62` | `#003674` | `#00418b` | `#0090ff` | `#006efe` | `#005be7` | `#47a8ff` | `#eaf6ff` |
| red | `#330a11` | `#440d13` | `#5d0e17` | `#6f101b` | `#88151f` | `#f32e40` | `#f13242` | `#e2162a` | `#ff565f` | `#ffe9ed` |
| amber | `#2a1700` | `#361900` | `#502800` | `#5b3000` | `#703e00` | `#ed9a00` | `#ffae00` | `#ff9300` | `#ff9300` | `#fff3d5` |
| green | `#002608` | `#00320b` | `#003a0e` | `#004615` | `#006717` | `#00952d` | `#00ac3a` | `#009432` | `#00ca50` | `#d8ffe4` |
| teal | `#00231b` | `#002b22` | `#003d34` | `#004035` | `#006354` | `#009e86` | `#00aa95` | `#00927f` | `#00cfb7` | `#cbfff5` |
| purple | `#290c33` | `#341142` | `#47185e` | `#541a76` | `#642290` | `#9440d5` | `#9440d5` | `#7d2bba` | `#c472fb` | `#fbecff` |
| pink | `#310d1e` | `#420c25` | `#571032` | `#5d0c34` | `#76063f` | `#ba0056` | `#f12b82` | `#e7006d` | `#ff4d8d` | `#ffe9f4` |

The source repeats one value in two places: amber 800 and 900 are both `#ff9300`, and purple 600 and 700 are both `#9440d5`. Gray 800 is darker than gray 700 on purpose (it is the hover of 700).

## Gray-alpha

White at an opacity, for edges that must blend with a surface other than the canvas. Excalidraw opacity applies to the whole element, so put it on a separate unlabeled shape (`backgroundColor` or `strokeColor` `#ffffff`, `opacity` below) layered under or over the labeled one, as the source does.

| Step | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 1000 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| opacity | 6 | 9 | 13 | 14 | 24 | 51 | 54 | 47 | 61 | 92 |

Base color: `#ffffff`.

## Text on a 700 fill

| Hue | Text |
| --- | --- |
| blue, red, purple, pink | gray-1000 `#ededed` |
| gray, amber, green, teal | background-100 `#0a0a0a` |
