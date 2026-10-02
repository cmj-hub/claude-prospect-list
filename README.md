<p align="center">
  <img src="./assets/lockup.png" width="880" alt="Sales prospecting skill for Claude Code. Sales prospecting builds the B2B prospect list you are willing to write to.">
</p>

# Sales prospecting skill for Claude Code

Sales prospecting builds the B2B prospect list you are willing to write to.

Ops lead at Northwind posted a role for an outbound lead this week.

The good draft says call this week. A title-only list fails the score.

<p align="center">
  <img src="./assets/demo.gif" alt="Sales prospecting skill — a signal earns a call, a title-only list fails" width="100%">
</p>

The build guide teaches a human. The pack teaches an agent.

## Install

```bash
npx skills add cmj-hub/claude-prospect-list --all -g --full-depth
```

`--all` writes this pack for every host the installer knows. One host:

```bash
npx skills add cmj-hub/claude-prospect-list --skill '*' -g --full-depth -y -a claude-code
```

Swap `claude-code` for `cursor`, `codex`, `grok`, `github-copilot`, `windsurf`, `cline`, or `opencode`. The scorer is Python in this repo. It does not call a paid API, and it does not buy data.

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

## On the site

- [Sales prospecting pack](https://jaymountconsulting.com/skills/claude-prospect-list) — this pack's page
- [Skill packs catalog](https://jaymountconsulting.com/skills) — install paths + every pack

## Free, no signup

[All free tools](https://jaymountconsulting.com/prototypes)

## Free, by email

[**Growth Audit**](https://jaymountconsulting.com/growth-audit) — architecture gaps in the GTM you already run. Free written report.

[**Friday Signal**](https://jaymountconsulting.com/newsletter/signal) — one Friday GTM read. No pitch in it.

## Next

Previous: [Email sequence](https://github.com/cmj-hub/claude-email-sequence)

Next: [GTM skills for Claude Code](https://github.com/cmj-hub/gtm-operator-skills)

## License

MIT. Python 3 standard library only.
