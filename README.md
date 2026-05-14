# MEMBRA Relay

**MEMBRA Relay is the local fulfillment and movement expansion module for MEMBRA Labs and the MEMBRA Proof Network.**

It turns Hero Houses, Alpha Hubs, and local agents into proof-backed micro-fulfillment, storage, handoff, and delivery capacity.

## Company Context

- Company: **MEMBRA Labs**
- Flagship product: **MEMBRA Proof Network**
- Module: **MEMBRA Relay**
- Category: local fulfillment, storage, handoff, delivery proof, route attribution

## One-Line Thesis

Store locally. Move locally. Fulfill locally. Prove every handoff.

## Product Role

MEMBRA Relay is phase-two expansion after the first Membra Ads / QR proof wedge.

It supports:

- local delivery
- meet-halfway handoffs
- returns/drop-offs
- hub transfers
- errand relay
- batch routes
- storage-to-delivery flows
- route proof and custody evidence

## Core Concept

MEMBRA aggregates three physical capacities:

1. **Inventory** — what people already own or stock locally
2. **Storage** — where goods can sit temporarily
3. **Movement** — who can carry items from one node to another

Instead of competing directly with last-mile networks, MEMBRA Relay can become overflow micro-storage, local handoff, proof-route, and long-tail fulfillment infrastructure.

## Relay Workflow

1. User or operator needs an item moved.
2. MEMBRA checks inventory, storage, and route options.
3. Hero can self-handoff, meet halfway, or request Relay.
4. Relay agent accepts route.
5. Item moves from Hero House, Alpha Hub, store, or user.
6. Proof is captured at pickup and dropoff.
7. Payment eligibility is split across owner, hub, courier, and MEMBRA.
8. KPI and ProofBook records are generated.

## Relay Object

```json
{
  "relay_id": "relay_001",
  "item_id": "usb_c_cable_123",
  "pickup_node": "hero_house_456",
  "dropoff_node": "user_789",
  "mode": "local_delivery",
  "distance_miles": 1.2,
  "estimated_minutes": 18,
  "payout_to_agent": 8,
  "platform_fee": 2,
  "proof_required": true,
  "risk_level": "low",
  "status": "available"
}
```

## Integration Points

| Repo | Relationship |
|---|---|
| `overandor/membra` | company hub, doctrine, KPI runtime |
| `overandor/Membra_ads` | campaigns and local physical media assets that may need kit movement |
| `overandor/membra-qr-gateway` | dashboard view for route proof and local fulfillment activity |
| `overandor/Membra_wallet` | reward eligibility and payout state boundary |
| `overandor/Membra_proofbook` | pickup/dropoff proof records and custody hashes |
| `overandor/Membra_kpi` | relay performance, route cost, proof approval, payout reporting |

## Safety and Compliance Rules

- no restricted goods without policy review
- no unverified courier payout eligibility
- no route completion without proof event
- no hidden custody chain
- fragile/high-value items require deposit, insurance, or rejection
- perishable, regulated, illegal, or unsafe categories must be blocked or reviewed
- no guaranteed courier earnings

## Productization Priority

This is not the first resale wedge. The first wedge is Membra Ads / QR proof media.

Relay should be positioned as expansion value after the proof-commerce dashboard is live.

## Current Stage

Product doctrine and module architecture. Suitable for buyer narrative and phase-two roadmap; not yet production fulfillment software.