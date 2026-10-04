---
name: who-to-contact
description: "Score who to contact this week from one public buying signal, and refuse a title-only list. Use when building or checking a B2B prospect list, lead list, or call sheet; when asked who to call, email, or prioritize this week; or when a list has job titles but no signal behind them."
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
- [ ] 3. Run `python3 scripts/score.py --file draft.json`.

Go back to step 2 if step 3 exits 1. Stop when it exits 0.

Paths are relative to this skill's directory. Use `--stdin` to pipe the object instead of writing a file, and `--json` for a machine-readable result.

## Run

```bash
python3 scripts/score.py --file examples/list-good.json
python3 scripts/score.py --file examples/list-title.json
```

| File | Exit | Why |
| --- | --- | --- |
| `examples/list-good.json` | 0 | Fresh signal, call this week. |
| `examples/list-hold.json` | 0 | Real but indirect signal, hold. |
| `examples/list-title.json` | 1 | A title-only list. |
| `examples/list-persona.json` | 1 | A persona label in place of a signal. |

Exit 2 means the input could not be read: missing file, not UTF-8, broken JSON, or not an object. A broken JSON does not echo the raw input.

Python 3 standard library only. No network. No send.
