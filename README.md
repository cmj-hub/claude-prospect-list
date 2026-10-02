# Who to contact

You hold a list score from a signal. The scorer refuses a title-only list.

Who to contact is the person a signal puts on this week's list. The score is the slot: call, hold, or drop. A title with no signal does not earn a slot.

The build guide teaches a human. This pack teaches an agent.

Give the instrument. Sell the compounding.

## Install

```bash
npx skills add cmj-hub/claude-list --all -g --full-depth
```

## What you walk out with

```bash
python3 scripts/score.py --file examples/list-good.json
python3 scripts/score.py --file examples/list-title.json
```

The good draft exits 0 and prints a list score from a signal. The title-only draft exits 1. Then drop in yours.

## What this pack will not do

It will not send the list. It does not buy data. It will not accept a title-only list.

This pack drafts and scores. The course keeps the signal map current.

## License

MIT. Python 3 standard library only.
