# DRACO Frequently Asked Questions

## Does DRACO run the commands it suggests?

No. DRACO only **prints** the suggested command. Executing it is always a deliberate human action — copy, read, then paste. This is a hard design boundary, not a missing feature.

## Which model powers DRACO?

Llama 3.3-70B-Instruct-Turbo, served by Together AI. The API key in your `.env` is a Together AI key; no other provider is contacted.

## Is my query data stored anywhere?

DRACO itself stores nothing — there is no local history file, no telemetry, and no analytics. Queries go to the Together AI inference API and are subject to Together AI's data policy. In interactive mode, session history lives only in process memory and is gone when you exit.

## Why does DRACO refuse some questions?

The system prompt constrains the model to CLI tasks. If you ask something that is not a terminal task ("what is the meaning of life"), DRACO answers with the refusal marker instead of improvising. This prevents the tool from becoming an unreliable general chatbot.

## Can I use a different model or provider?

Not via configuration today. The model and provider are fixed in `draco/llm.py`. Swapping providers means editing that one module — the rest of the tool is provider-agnostic.

## How much does it cost to run?

Together AI's free tier covers typical personal usage. A query consumes roughly 200–400 tokens round-trip; the free tier's monthly allowance is several thousand queries.

## Does DRACO work offline?

No. Every suggestion is a live model call. With no network, DRACO exits with code 2 and a clear message rather than hanging.

## Does it support Windows?

DRACO runs anywhere Python 3.8+ runs, including Windows. Suggested commands, however, follow the conventions of the shell you describe in the query — say "in PowerShell" if you want PowerShell syntax.
