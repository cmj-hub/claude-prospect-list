---
name: who-to-contact
description: "Score who to contact from one buying signal. Use when a list needs a list score, and when a title with no signal must be refused."
models: ""
---

# Who to contact

A list score names one person worth a slot this week, and the signal that put them there. A title with no signal is not a list. It is a directory of names.

The build guide teaches a human. This pack teaches an agent.

## What you hold

1. Title. The person, in the words you would use on a call sheet.
2. Signal. One observable fact from this window: a role posted, a stack change, a public complaint, a hiring line. Not a persona label.
3. Score. The slot you give them: call this week, hold, or drop.

## Refusal

The scorer refuses a title-only list. A title with no signal is the refusal. Add the signal and return to step 2.

## Checklist

Copy this list and tick it in order.

- [ ] 1. Name the person.
- [ ] 2. Write the signal and the score in the shell.
- [ ] 3. Run `python3 scripts/score.py --file draft.json`.

Check again until the script exits 0.

Go back to step 2 if step 3 fails.

## Run

```bash
python3 scripts/score.py --file examples/list-good.json
python3 scripts/score.py --file examples/list-title.json
```

The good file exits 0 and prints a list score from a signal. The title-only file exits 1.

The JSON object has `title`, `signal`, and `score`. A broken JSON exits non-zero and does not echo the raw input.

Python 3 standard library only. No network. No send.
