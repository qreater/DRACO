# DRACO Usage Guide

This guide covers every way to invoke DRACO, from one-off queries to long interactive sessions.

## Quick Query

The fastest path: pass your request as a quoted argument.

```bash
python draco.py "list all running docker containers"
# DRACO AI Suggests:
# docker ps

python draco.py "compress the reports folder into a tar.gz"
# DRACO AI Suggests:
# tar -czvf reports.tar.gz reports/
```

Quoting matters — without quotes your shell will split the sentence into separate arguments and only the first word reaches DRACO.

## Interactive Mode

For a run of related questions, start a session:

```bash
python draco.py --interactive
```

Inside the session:

- Type any plain-English request and press Enter.
- Type `exit` or `quit` (or press `Ctrl+D`) to leave.
- The session keeps your previous questions in memory, so follow-ups like "same but only for the last hour" resolve against your earlier query.

## Flag Reference

| Flag | Effect |
|------|--------|
| `--interactive` | Start a persistent question loop |
| `--help` | Print usage and exit |
| *(positional)* | The plain-English query for one-shot mode |

## Writing Good Queries

DRACO performs best with **task descriptions**, not command fragments:

- Good: `"show the 10 largest files under /var/log"`
- Weak: `"du sort head"` — fragments confuse the intent detection.

Include the tool name if you care which one is used: `"using ffmpeg, extract audio from input.mp4 as mp3"`.

## Out-of-Scope Queries

Anything that is not a terminal task is refused explicitly:

```bash
python draco.py "what is the meaning of life"
# ❌ The given query is not CLI related.
```

This is intentional — DRACO never improvises non-CLI answers.

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success (including the explicit out-of-scope refusal) |
| 2 | Network unreachable |
| 3 | Missing or invalid API key |
| 4 | Model timed out after retry |

Scripts can branch on these codes to detect setup problems in CI environments.
