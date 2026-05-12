# Quran Repository — AGENTS.md

## What this is

A front-end-only repo containing two standalone Quran meditation/reading web apps. No build system, no package manager, no tests.

## Files

- **`index.html`** — "Mirān" vanilla JS app. Fetches live data from the Quran Foundation API (`https://api.quran.com/api/v4`). All JS and CSS inline.
- **`index2.html`** — React+JSX variation using CDN-loaded React 18.3 and Babel standalone. Uses hardcoded verse data (`window.VERSE`) rather than live API calls. Also inline.
- **`llms.txt`** — Reference docs for the Quran Foundation Content/User/Search/OAuth APIs.

## Key conventions

- Both apps are self-contained single HTML files. There is no build step — open the file in a browser.
- No framework bundler. `index2.html` loads React and Babel from unpkg CDN via `<script>` tags and uses `type="text/babel"` for JSX (`<script type="text/babel" data-presets="react">`). Do not add npm/webpack/vite.
- All CSS and JS is inline within each HTML file. No external stylesheets or script files exist.

## API details (index.html)

- Base URL: `https://api.quran.com/api/v4`
- Audio base: `https://verses.quran.com/`
- Translation ID 20 (Sahih International), Recitation ID 7 (Mishary al-ʿAfāsy), Tafsir ID 168 (Maʿārif al-Qurʾān)
- App flow: `start → listen (verse picker) → prompt1 → prompt2 → prompt3 → done`
- The random verse endpoint may not return `text_uthmani`; the app explicitly re-fetches Arabic text via `/verses/by_key/{key}` to ensure it's available.

## Editing guidance

- Changes to `index.html` touch a single 1400+ line file with mixed CSS/JS/HTML. Be mindful of string template literals in JS that contain HTML.
- `index2.html` uses React hooks (`useState`, `useEffect`, `useRef`) with Babel JSX transformation at runtime. No JSX compile step needed.
- Theme system in `index2.html` is driven by `window.THEMES` — an array of 5 palettes applied as CSS custom properties. `index.html` uses hardcoded CSS variables in `:root`.
- The constellation/star background in both files is generated deterministically from loop indices, not randomly.

## What NOT to do

- Do not add `package.json`, node_modules, or a bundler.
- Do not refactor into separate JS/CSS files without explicit request.
- Do not introduce npm dependencies.