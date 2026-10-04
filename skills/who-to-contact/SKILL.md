---
name: who-to-contact
description: "Score who to contact this week from one public buying signal, and refuse a title-only list. Use when building or checking a B2B prospect list, lead list, or call sheet; when asked who to call, email, or prioritize this week; or when a list has job titles but no signal behind them. Not for deliverability, dedup, or hygiene of an existing send list (use cold-email's cold-email-list-quality)."
models: ""
---

# Who to contact

A list score names one person worth a slot this week, and the signal that put them there. A title with no signal is not a list. It is a directory of names.

The build guide teaches a human. This pack teaches an agent.

## What you hold

Write one JSON object per person:

```json
{
  "title": "Ops lead at Northwind",
  "signal": "Posted a role for an outbound lead this week.",
  "score": "call this week"
}
```

1. `title`. The person, in the words you would use on a call sheet: role and company.
2. `signal`. One observable fact from this window that someone could check: a role posted, a stack change, a public complaint, a hiring line, a funding note. Not a persona label.
3. `score`. The slot you give them: `call this week`, `hold`, or `drop`.

## Signal or label

| Signal (passes) | Label (refused) |
| --- | --- |
| Posted a role for an outbound lead this week. | Decision maker |
| Moved their CRM from HubSpot to Salesforce last month. | ICP fit |
| Complained in a public forum about lead routing. | Target account |
| Raised a Series A and named sales hiring as the use. | VP Sales at Fabrikam (the title again) |

A signal says what they did. A label says who they are. If you cannot point to where you saw it, it is not a signal yet.

## Signals from brand-config.json

If `brand-config.json` is at the project root, read it first.

- `psp.signal_anchors` names the kinds of signal worth a slot. Look for those first. Each person's `signal` is one concrete, checkable instance of an anchor, not the anchor text itself.
- `psp.primary_pain` is "the problem you solve" in the slot rules below.
- `icp.role_targets` and `icp.exclusion_criteria`, when present, decide who belongs on the list at all. Leave excluded people off.

A real signal that matches no anchor is `hold` at best. If there is no `psp` block, say the psp pack produces it (`/plugin install psp@gtm-operator-skills`, then `/psp:psp`) and ask the user for the signal. Never invent anchors.

## Picking the slot

- `call this week`. The signal is fresh and points at the problem you solve.
- `hold`. The signal is real but early, indirect, or a step removed from your problem. Look again next week.
- `drop`. The signal is stale or points away from your problem. Say so and move on.

## Refusal

The scorer refuses a title-only list. A title with no signal is the refusal. It also refuses a persona label in place of a signal, a signal that repeats the title, and a score that is not one of the three slots. Each refusal prints a `fix:` line. Do what it says and return to step 2.

Do not invent a signal to get past the refusal. If you have no signal for a person, leave them off the list and tell the user.

## Checklist

Copy this list and tick it in order.

- [ ] 1. Name the person in `title`.
- [ ] 2. Write the `signal` and the `score` into `draft.json`.
- [ ] 3. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/score.py --file draft.json`.

Go back to step 2 if step 3 exits 1. Stop when it exits 0.

The scorer runs from this skill's directory (`${CLAUDE_SKILL_DIR}`). Keep `draft.json` in a scratch directory, not the user's repo. Use `--stdin` to pipe the object instead of writing a file, and `--json` for a machine-readable result.

## Run

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/score.py --file ${CLAUDE_SKILL_DIR}/examples/list-good.json
python3 ${CLAUDE_SKILL_DIR}/scripts/score.py --file ${CLAUDE_SKILL_DIR}/examples/list-title.json
```

| File | Exit | Why |
| --- | --- | --- |
| `examples/list-good.json` | 0 | Fresh signal, call this week. |
| `examples/list-hold.json` | 0 | Real but indirect signal, hold. |
| `examples/list-title.json` | 1 | A title-only list. |
| `examples/list-persona.json` | 1 | A persona label in place of a signal. |

Exit 2 means the input could not be read: missing file, not UTF-8, broken JSON, or not an object. A broken JSON does not echo the raw input.

## Works with the suite

This is step 3 of the GTM operator suite (`/plugin marketplace add cmj-hub/gtm-operator-skills`).

- **Reads:** `psp.signal_anchors`, `psp.primary_pain`, and `icp` from `brand-config.json` if present.
- **Writes:** nothing outside `draft.json`. Never touches `brand-config.json`.
- **Before this:** psp (`/psp:psp`), when there is no `psp` block to say which signals count.
- **After this:** cold-email (`/cold-email:cold-email`) for a signal-anchored first touch to each `call this week` person; sales-offer (`/sales-offer:cold-offer`) when the first touch should hand over a leak instead.
- **Not this pack:** dedup or deliverability hygiene of a send list you already have is cold-email's `cold-email-list-quality`.

If a companion pack is not installed, name it and its install line (`/plugin install <name>@gtm-operator-skills`); do not do its job inline.

Python 3 standard library only. No network. No send.
