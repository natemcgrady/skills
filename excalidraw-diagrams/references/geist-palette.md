# Geist palette for native dark theme

Every Geist dark color from the style guide `geist-colors.excalidraw`, converted for Excalidraw's native dark theme. `scripts/check_style.py` reads the backticked hex values under "File values" as the allowed set, so edit colors there and nowhere else.

## How native dark theme changes colors

Excalidraw draws in light-theme colors. In dark theme it passes every canvas color, including the background, through a filter: invert 93%, then hue-rotate 180deg. So a `.excalidraw` file stores the color that turns into the Geist color after the filter, not the Geist color itself. Writing a Geist hex directly shows the wrong color: `#0a0a0a` would render almost white.

The filter has limits:

- Gray, most green, and most teal steps render exactly.
- The filter caps saturation, so vivid blue, red, amber, purple, and pink steps render as the closest reachable color, a little softer than Geist. Hue and lightness order still hold, so every role still reads.
- Nothing renders darker than `#121212`, the native dark background. That is the canvas, as close as Excalidraw gets to Geist background-100 `#0a0a0a`, and Background 2 `#000000` has no equivalent.

`rendered(hex)` in `scripts/check_style.py` returns what a stored color looks like in dark theme. Use it to draw previews.

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

## File values

Write these in the `.excalidraw` JSON.

Canvas and dark text:

| Role | Write | Renders as |
| --- | --- | --- |
| Canvas `viewBackgroundColor`, dark text on a light 700 fill | `#ffffff` | #121212 |

Scales:

| Hue | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 1000 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gray | `#f6f6f6` | `#f0f0f0` | `#e4e4e4` | `#dedede` | `#c4c4c4` | `#777777` | `#6d6d6d` | `#828282` | `#595959` | `#000000` |
| blue | `#e5f2ff` | `#d9ebff` | `#c0ddff` | `#b3d1ff` | `#9dc7ff` | `#1489ff` | `#4f8dff` | `#669cff` | `#0172d7` | `#000004` |
| red | `#ffeff3` | `#ffe2e1` | `#ffd1d1` | `#ffc2be` | `#ffb3ab` | `#ff655f` | `#ff6664` | `#ff746b` | `#ff5559` | `#110004` |
| amber | `#fff2d8` | `#ffead0` | `#ffd6ab` | `#ffcf8f` | `#f7bc76` | `#a54c00` | `#8d3c00` | `#bd4500` | `#bd4500` | `#0a0000` |
| green | `#d4ffdc` | `#bff9cc` | `#b1f4c1` | `#9cedb4` | `#63de81` | `#14c249` | `#00a921` | `#15c14f` | `#007e00` | `#000400` |
| teal | `#d5fef4` | `#c7f9ee` | `#96f9ee` | `#a0ebde` | `#5fd6c5` | `#00a88c` | `#009379` | `#0cb59f` | `#00623c` | `#000100` |
| purple | `#ffebff` | `#fde0ff` | `#f7cdff` | `#f3c0ff` | `#e5adff` | `#cf7eff` | `#cf7eff` | `#d694ff` | `#b150f1` | `#060013` |
| pink | `#ffecfa` | `#ffdff0` | `#ffd0ed` | `#ffcde7` | `#ffbcdf` | `#ff8dbb` | `#ff61a6` | `#ff6b9f` | `#ff4f92` | `#0e000b` |

## Rendered in dark theme

What each file value above looks like on screen.

| Hue | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 1000 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gray | #1a1a1a | #1f1f1f | #292929 | #2e2e2e | #454545 | #878787 | #8f8f8f | #7d7d7d | #a1a1a1 | #ededed |
| blue | #15202b | #172738 | #1c3552 | #243e65 | #264a7a | #2e93f8 | #477cde | #406ec3 | #47a8ff | #ededf0 |
| red | #27191d | #39201f | #4f2828 | #64302c | #793831 | #e25e59 | #e05d5b | #ce574f | #f76568 | #f5e7ea |
| amber | #261b05 | #311f09 | #4e2b06 | #5a3100 | #703e01 | #e29554 | #eaa471 | #f68f54 | #f68f54 | #f2eaea |
| green | #012608 | #00320b | #003a0e | #004615 | #006717 | #00952d | #1aab36 | #009432 | #53bf53 | #e9ece9 |
| teal | #00231b | #002b22 | #003d34 | #004035 | #006354 | #0e9e86 | #2aa892 | #00927f | #6ec2a1 | #ecedec |
| purple | #2a192a | #371e39 | #4b2752 | #592d63 | #69397f | #9953c2 | #9953c2 | #8148a4 | #c471fb | #eee9f9 |
| pink | #291925 | #3a1f2d | #4d253e | #52273e | #672e4c | #a6446c | #df5793 | #d35481 | #f76099 | #f3e7f0 |

## Geist source values

The targets, as defined in the guide. Never write these into a file.

| Hue | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 1000 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| background | #0a0a0a (Background 1) | #000000 (Background 2) | | | | | | | | |
| gray | #1a1a1a | #1f1f1f | #292929 | #2e2e2e | #454545 | #878787 | #8f8f8f | #7d7d7d | #a1a1a1 | #ededed |
| blue | #06193a | #022248 | #002f62 | #003674 | #00418b | #0090ff | #006efe | #005be7 | #47a8ff | #eaf6ff |
| red | #330a11 | #440d13 | #5d0e17 | #6f101b | #88151f | #f32e40 | #f13242 | #e2162a | #ff565f | #ffe9ed |
| amber | #2a1700 | #361900 | #502800 | #5b3000 | #703e00 | #ed9a00 | #ffae00 | #ff9300 | #ff9300 | #fff3d5 |
| green | #002608 | #00320b | #003a0e | #004615 | #006717 | #00952d | #00ac3a | #009432 | #00ca50 | #d8ffe4 |
| teal | #00231b | #002b22 | #003d34 | #004035 | #006354 | #009e86 | #00aa95 | #00927f | #00cfb7 | #cbfff5 |
| purple | #290c33 | #341142 | #47185e | #541a76 | #642290 | #9440d5 | #9440d5 | #7d2bba | #c472fb | #fbecff |
| pink | #310d1e | #420c25 | #571032 | #5d0c34 | #76063f | #ba0056 | #f12b82 | #e7006d | #ff4d8d | #ffe9f4 |

The source repeats one value in two places: amber 800 and 900 are both `#ff9300`, and purple 600 and 700 are both `#9440d5`. Gray 800 is darker than gray 700 on purpose (it is the hover of 700).

## Gray-alpha

Geist gray-alpha is white at an opacity, for edges that must blend with a surface other than the canvas. In dark theme, write gray-1000 `#000000` (renders #ededed) at the opacity below. Excalidraw opacity applies to the whole element, so put it on a separate unlabeled shape layered under or over the labeled one, as the guide does.

| Step | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 1000 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| opacity | 6 | 9 | 13 | 14 | 24 | 51 | 54 | 47 | 61 | 92 |

## Text on a 700 fill

| Hue | Write | Renders as |
| --- | --- | --- |
| blue, red, purple, pink | gray-1000 `#000000` | #ededed |
| gray, amber, green, teal | `#ffffff` | #121212 |
