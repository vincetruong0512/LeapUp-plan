# Leap Up Portal: design rules

Scope: `MVP` (applies to Login, Project Files, Video Review first). Status: **draft v1, 2026-11-22**.
Mirror of the design system generated into the Figma file "Untitled", page `DS · System` (Reqwise,
audit compliance 1.00). Figma is the source of truth for exact values; this file records the
decisions and where each value came from.

> Wireframes (`/wireframe-html`) and prototypes (`/prototype-html`) stay neutral greyscale by
> convention. These rules are for visual design / hi-fi screens, not for the pipeline wireframes.

## 1. Sources and decisions

| Item | Value | Source |
|---|---|---|
| Brand primary | `#2DC75C` | **Sampled** from the Sign In / Approve buttons on the Miro board image (login column). Confirmed by the user 2026-11-22. |
| Font | Inter | **User decision** 2026-11-22. Not identifiable from the board screenshot. |
| Style | Neutral, light theme only, web + mobile | User accepted the tool's defaults 2026-11-22. |
| Success colour | Keeps green (`success/600`) | User decision 2026-11-22: matches the board's colour meaning (green = done/approved, `leapup-website-miro-board.md` L128). |
| Logo | Not in Figma yet | Board shows it as an image only (L131); the client provides the logo (`bao-gia-leapup-mvp.md` L144). |

## 2. Colour

### Board colours (sampled pixel values, for reference)

| Board use | Hex | Maps to token (nearest) |
|---|---|---|
| Sign In / Approve buttons | `#2DC75C` | `primary/400` (exact) |
| "In Progress" pill, private-access chip, approve-final button | `#ADF0C7` | between `primary/200` and `primary/300` |
| Login brand panel / "Done" stage card | `#EAF9EF` / `#D9F8E5` | `primary/50` – `primary/100` |
| Logo lime accent | `#B1FF3B` | none (logo artwork only, not a UI token) |
| In review / current (Round 2 pill, warning note) | `#FFF6B6` | `warning-subtle` (inferred: tool's warning ramp is orange-amber, board is pale yellow; see open item O3) |
| Info box (feedback rule) / selected version | `#EAF2FF` / `#C6DCFF` | `info/50` / `info/200` |
| Attention outline (task list) | `#F9D8D8` | `error/100` |
| Dark surfaces (final sign-off card, video player) | `#1A1A1A` / `#313131` | `neutral/900` / `neutral/800` |
| Sidebar, inputs, upcoming stages | `#F7F7F7` | `neutral/50` |

`#067429` (dark-green section bars) is Miro board chrome, not app UI. Excluded.

### Brand ramp `primary`

| 50 | 100 | 200 | 300 | **400** | 500 | 600 | 700 | 800 | 900 |
|---|---|---|---|---|---|---|---|---|---|
| `#E7FCE9` | `#CDF7D2` | `#A7EDB2` | `#7AE28D` | **`#2DC75C`** | `#00AF48` | `#00913B` | `#00762E` | `#005F24` | `#004E1C` |

The brand green is light, so it anchors at step **400**, not 500. Semantic `primary` = `primary/600`
(`#00913B`), hover = 500, **pressed = 400 (the board green)**. Text on primary = `neutral/950` (dark).

### Semantic tokens (light)

| Job | Token → step |
|---|---|
| Page / surface | `bg` → neutral/0 · `bg-subtle` → neutral/50 · `surface-sunken` → neutral/100 |
| Text | `text` → neutral/900 · `text-muted` → neutral/600 · `text-subtle` → neutral/500 |
| Border | `border` → neutral/200 · `border-input` / `border-strong` → neutral/500 |
| Primary action | `primary` → primary/600 · `primary-subtle` → primary/50 · `focus` → primary/600 |
| Status | `success` → success/600 · `warning` → warning/600 · `error` → error/600 · `info` → info/600, each with a `-subtle` (step 50) and `-ink` (step 700) |

### Status colour rule (required)

Brand green and success green are 1° apart in hue. Therefore:

1. Every success / done / approved state carries an **icon or word** ("Approved", "Done", ✓), never colour alone.
2. Status meaning follows the board (L128): green = done/approved · yellow = in review/current · red = missing/attention.
3. Primary buttons and success badges never sit side by side without a label difference.

## 3. Typography (Inter, 20 text styles)

| Style | Size / line | Weight |
|---|---|---|
| Display L / M / S | 56/64 · 48/56 · 40/48 | 700 |
| Heading H1 | 32/40 | 700 |
| Heading H2 / H3 / H4 / H5 / H6 | 28/36 · 24/32 · 20/28 · 18/24 · 16/24 | 600 |
| Title L / M / S | 20/28 · 18/24 · 16/24 | 500 |
| Body L / M / S | 16/24 · 14/20 · 12/16 | 400 |
| Label L / M / S | 14/20 · 12/16 · 10/16 | 500 |
| Caption Regular / Small | 12/16 · 10/16 | 400 |

Vietnamese: Inter covers Vietnamese diacritics; check line height on stacked marks when copy is final.

## 4. Spacing, radius, elevation, sizes

- **Spacing** (4 px grid): 2 · 4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64 · 80 · 96.
- **Radius:** none 0 · xs 2 · sm 4 · md 8 · lg 12 · xl 16 · 2xl 20 · 3xl 24 · full · `radius/button` = 8.
- **Elevation:** `elevation/0`–`5`, soft two-layer shadows (cards 1–2, menus 3, dialogs 4–5).
- **Control heights:** sm 32 · md 44 · lg 56. **Icons:** 16 · 20 · 24.
  Rule: `sm` (32 px) controls on desktop only; on mobile every tap target ≥ 44 px.
- **Opacity:** disabled 0.4 · hover tint 0.08 · pressed 0.12 · backdrop 0.5.
- **Z-index:** dropdown 1000 · sticky 1100 · overlay 1300 · modal 1400 · popover 1500 · toast 1700 · tooltip 1800.

## 5. Layout grids and breakpoints

| Grid | Width | Columns | Gutter | Margin |
|---|---|---|---|---|
| Android / iPhone / iPhone Pro Max | 360 / 390 / 430 | 4 | 16 | 16 |
| Laptop | 1280 | 12 | 24 | 32 |
| Desktop | 1440 | 12 | 24 | 32 |
| Wide | 1920 | 12 | 32 | 64 |

Breakpoints: sm 640 · md 768 · lg 1024 · xl 1280 · 2xl 1536.

## 6. Components (Figma `DS · System`)

| Component | Variants | MVP use (inferred) |
|---|---|---|
| Atom/Status/Badge | Tone neutral·success·warning·error·info × Size sm·md | File status (Approved, Final, Shared…), round pill |
| Atom/Avatar | Size × initials·dot | Comment author, uploader |
| Molecule/Action/Button | primary·secondary·ghost·danger × sm·md·lg × default·hover·pressed·disabled | Sign In, Upload Files, Approve |
| Molecule/Input/TextField | default·focus·error·disabled × md·lg | User ID, password, search, comment |
| Molecule/Input/Select | default·focus·error·disabled | Folder / status filters |
| Molecule/Input/Checkbox, Switch | on/off × default/disabled | Remember me, file selection |
| Molecule/Display/Card | elevated·outlined·filled | Folder cards, comment cards |
| Molecule/Feedback/Alert, Toast | info·success·warning·error | Upload result, sign-in errors |
| Organism/Overlay/Dialog | default·danger | Confirm delete, upload dialog |

Screen-specific pieces (sidebar, file table row, video player, timecode marker, comment thread) are
**not** in the kit. Build them from these instances when hi-fi screens are drawn.

## 7. Open items

| # | Item | Owner |
|---|---|---|
| O1 | Official Leap Up brand green (hex) and font: confirm or replace the sampled `#2DC75C` / Inter | Leap Up |
| O2 | Logo files (SVG/PNG) for the login panel and sidebar | Client / Leap Up (quote L144) |
| O3 | Board's pale-yellow "in review" (`#FFF6B6`) vs the kit's amber warning ramp: keep, or add a yellow status tone | Design decision |
| O4 | Dark theme: not generated (light only); add later only if requested | — |

## Post-MVP

- Dashboard, timeline, approval screens (`P2`) reuse this kit; no extra components designed now.
- Material Library and Storyboard Review are `OUT` (change-request candidates); no rules designed for them.
