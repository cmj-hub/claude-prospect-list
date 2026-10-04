# Changelog

## 0.3.1 — 2026-10-04

- Plugin icon: `.claude-plugin/icon.png`, set as `icon` in `plugin.json`.
- `SECURITY.md`: what runs locally, no network, how to report a vulnerability.
- README privacy and security section.

## 0.3.0 — 2026-10-04

- SKILL.md reads `psp.signal_anchors`, `psp.primary_pain`, and `icp`
  from a shared `brand-config.json` when present, and points to the psp
  pack when it is missing.
- New "Works with the suite" section. Description names what belongs
  to cold-email's list hygiene.
- Scorer and examples are called as `${CLAUDE_SKILL_DIR}/...`.
- `models: ""` restored in frontmatter (house rule).
- `marketplace.json` entry carries the version.

## 0.2.0

- Ship as a Claude Code plugin: `.claude-plugin/plugin.json` and a
  single-plugin `marketplace.json`, installable with
  `/plugin marketplace add cmj-hub/claude-prospect-list`.
- Move the skill to `skills/who-to-contact/` so the directory matches the
  skill name and the scorer and examples travel with it.
- Scorer refuses a persona label, a signal that repeats the title, a
  signal under three words, and a score that is not `call this week`,
  `hold`, or `drop`. `call` folds to `call this week`.
- Every refusal prints a `fix:` line naming the gap. A missing title is
  no longer reported as a title-only list.
- `--json` prints a machine-readable result.
- Exit codes are documented: 0 scored, 1 refused, 2 unreadable input.
- SKILL.md: sharper trigger description, signal-vs-label table, slot
  rubric, and a rule not to invent a signal to pass. Dropped the empty
  `models` field.
- New examples: `list-hold.json`, `list-persona.json`.
- Tests cover the new refusals, JSON output, and plugin layout. CI runs
  them on every push.

## 0.1.0

- First release: `who-to-contact` skill and `scripts/score.py`.
