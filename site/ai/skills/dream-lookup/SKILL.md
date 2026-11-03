# Dream Symbol Lookup — Skill

Read verified classical dream-interpretation pages from teethdreammeaning.com and answer with checkable source citations.

## When to use

A user asks what a dream symbol means according to classical Islamic sources (Ibn Sirin, Al-Nabulsi) or the Chinese Zhou Gong tradition, and wants the answer traceable to printed pages or library locations.

## How to find

1. List available symbols: `GET https://teethdreammeaning.com/api/agent/symbols`
2. Read one symbol: `GET https://teethdreammeaning.com/api/agent/symbols/{slug}`

## How to interpret the response

- `title` — the page's plain-language headline reading
- `lede` — the one-paragraph summary of what both books say
- `sourceLocations` — exact printed-page / library-page citations for the quotes

## How to compose an answer

- Answer in the visitor's language.
- Cite the relevant /dream/ page URL and the printed-page locations from `sourceLocations`.
- Preserve identifiers, slugs, printed-page numbers and dates exactly as returned.
- Where the two books disagree, present the disagreement — do not smooth it over.
- Treat unknown facts as unknown: if a symbol is not in the list, say the verified corpus does not cover it. Do not extrapolate beyond the cited sources.
