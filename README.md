# Sales prospecting skill for Claude Code

**Sales prospecting builds the B2B prospect list you are willing to write to.** The scorer refuses a title-only list.

Who to contact is the person a signal puts on this week's list. The score is the slot: call, hold, or drop. A title with no signal does not earn a slot.

[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-blue)](https://claude.ai/claude-code)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![No paid APIs](https://img.shields.io/badge/paid%20APIs-none-success)

The build guide teaches a human. This pack teaches an agent.

## Install

```bash
npx skills add cmj-hub/claude-prospect-list --all -g --full-depth
```

Installs into Claude Code, Cursor, Codex, Grok, Copilot, Windsurf, Cline, and OpenCode. The scorer is Python in this repo. It does not call a paid API, and it does not buy data.

## What you walk out with in 15 minutes

```bash
python3 scripts/score.py --file examples/list-good.json
python3 scripts/score.py --file examples/list-title.json
```

The good draft exits 0 and prints a list score from a signal. The title-only draft exits 1. Then drop in yours.

## What this pack will not do

It will not send the list. It does not buy data. It will not accept a title-only list.

## What is a prospect list?

The people a public signal puts on this week's list. A job title with no signal is not a prospect yet.

## Does this pull leads from a database?

No. You bring the signal. The pack scores the slot: call, hold, or drop.

## Companion packs

- [claude-psp](https://github.com/cmj-hub/claude-psp) — Ideal customer profile
- [claude-evp](https://github.com/cmj-hub/claude-evp) — Value proposition
- [claude-cold-email](https://github.com/cmj-hub/claude-cold-email) — Cold email
- [claude-founder-brand](https://github.com/cmj-hub/claude-founder-brand) — LinkedIn posts
- [claude-pricing](https://github.com/cmj-hub/claude-pricing) — Pricing strategy
- [claude-landing-page](https://github.com/cmj-hub/claude-landing-page) — Landing page
- [claude-geo](https://github.com/cmj-hub/claude-geo) — Generative engine optimization
- [claude-sales-offer](https://github.com/cmj-hub/claude-sales-offer) — Sales offer
- [claude-email-sequence](https://github.com/cmj-hub/claude-email-sequence) — Email sequence

## License

MIT. Python 3 standard library only.
