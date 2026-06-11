# DRACO Architecture Overview

DRACO (Developer Resourceful AI Command Operator) is a lightweight command-line tool that translates plain-English task descriptions into executable terminal commands. This document describes how the pieces fit together.

## Design Goals

1. **Zero friction** — a single command, no daemon, no background service. You type what you want; DRACO prints the command.
2. **No hallucinated shell** — if a query is not CLI-related, DRACO refuses rather than inventing something dangerous.
3. **Minimal dependencies** — three runtime packages (`together`, `rich`, `python-dotenv`). The whole tool fits in three Python modules.

## Component Map

```
draco.py        Entry point. Parses CLI arguments, routes to quick-query
                or interactive mode, owns process exit codes.
draco/llm.py    Together AI integration. Builds the system prompt,
                calls Llama 3.3-70B, post-processes the response.
draco/options.py Interactive session loop. Maintains the prompt history
                for the current session and handles the exit commands.
```

## Request Lifecycle

1. The user invokes `draco "find all .log files modified today"`.
2. `draco.py` validates that an API key is present (loaded from `.env` via `python-dotenv`). A missing key aborts with a setup hint, never a stack trace.
3. `llm.py` wraps the query in a fixed system prompt that constrains the model to return **only** a command, or the literal refusal marker when the query is out of scope.
4. The response is rendered through `rich` with the `# DRACO AI Suggests:` banner.

## Model Choice

DRACO uses **Llama 3.3-70B-Instruct-Turbo** served by Together AI. The 70B size was chosen after testing smaller models (8B variants) produced incorrect flags for less common tools like `ffmpeg` and `jq`. Inference latency averages 1.2 seconds per query on the free tier, which is acceptable for an interactive developer tool.

## Failure Modes

| Failure | Behavior |
|---------|----------|
| No network | Exits with code 2 and a "check your connection" message |
| Invalid API key | Exits with code 3 and a link to api.together.xyz |
| Out-of-scope query | Prints `❌ The given query is not CLI related.` and exits 0 |
| Model timeout (>30s) | Retries once, then exits with code 4 |

## Non-Goals

DRACO deliberately does **not** execute the suggested command. Copy-paste is the safety boundary: a human reads every command before it touches the shell.
