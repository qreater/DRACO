# Incident Response Runbook

How we detect, triage, and resolve production incidents.

## Severity Levels

- **SEV-1**: Full outage or data-loss risk. Page the on-call immediately; incident commander assigned within 10 minutes.
- **SEV-2**: Degraded service affecting multiple customers. Response within 30 minutes during business hours.
- **SEV-3**: Single-customer or cosmetic issues. Triaged in the next business day's queue.

## On-Call Rotation

The engineering on-call rotates weekly on Mondays at 09:00 UTC. The rotation is staffed by two people: a primary responder and a shadow.

## Communication

- Internal updates every 30 minutes in the incident channel until resolution.
- Customer-facing status page updated within 15 minutes of a SEV-1 being declared.

## Post-Incident

Every SEV-1 and SEV-2 gets a blameless retrospective within 5 business days, with action items tracked to closure.
