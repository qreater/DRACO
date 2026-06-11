# DRACO Security Notes

## API Key Handling

The Together AI key is the only secret DRACO touches.

- It is read from `.env` in the project root via `python-dotenv` at startup.
- It is **never** logged, printed, or included in error messages — a failed authentication prints a setup hint with a link to api.together.xyz, not the key.
- `.env` is listed in `.gitignore`; only `.env.example` (with a placeholder) is committed.

## What Leaves Your Machine

Exactly one thing: the text of your query, sent over HTTPS to the Together AI inference endpoint. DRACO sends no environment details, no hostname, no file contents, and no command history.

## What DRACO Never Does

| Boundary | Detail |
|----------|--------|
| No execution | Suggested commands are printed, never run |
| No shell access | DRACO does not spawn subprocesses for suggestions |
| No persistence | No history file, no cache, no telemetry |
| No file reads | DRACO never reads files referenced in your query |

## Reviewing Suggestions Before Use

Treat every suggestion like a snippet from a forum answer: read it before running it. Pay particular attention to:

- **Destructive verbs** — `rm`, `dd`, `mkfs`, `truncate`. The model is instructed to prefer safe variants, but the human is the final gate.
- **Privilege escalation** — suggestions may include `sudo` when the task requires it; confirm the task really does.
- **Pipes to shell** — DRACO is instructed never to suggest `curl ... | sh` patterns; report it as a bug if you see one.

## Reporting a Vulnerability

Open a GitHub issue with the `security` label on the qreater/DRACO repository. For sensitive reports, contact the maintainer directly rather than filing a public issue.
