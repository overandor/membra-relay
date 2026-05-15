# MEMBRA Module Contract — Relay

## Role

Local handoff and micro-fulfillment layer for MEMBRA. Converts eligible neighborhood movement, pickup/dropoff, return runs, media-kit delivery, hub transfers, and local handoff capacity into proof-based relay jobs.

## System inputs

- relay request records
- pickup node
- dropoff node
- requester ID
- mode
- proof requirements
- admin/operator decisions

## System outputs

- relay jobs
- relay status records
- pickup/dropoff proof requirements
- relay proof events
- payout-eligibility triggers after proof/review

## Health

```text
GET /api/health
```

## Replit role

`service`

Runs as the local fulfillment and handoff module behind the MEMBRA OS workspace.

## Production boundary

Relay jobs record intent, proof, and eligibility. They do not guarantee delivery, safety, earnings, or settlement. High-risk categories require operator review.
