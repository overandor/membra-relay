# MEMBRA Relay

MEMBRA Relay turns Hero Houses and local agents into flexible micro-fulfillment and delivery capacity for neighborhood commerce.

## Concept

MEMBRA aggregates three things at once:

1. **Inventory** — what people already own or stock locally
2. **Storage** — where goods can sit temporarily  
3. **Movement** — who can carry items from one node to another

Instead of competing directly with DoorDash or GoPuff, MEMBRA becomes the overflow, micro-storage, local handoff, and long-tail fulfillment layer.

## Key Product Line

**Store locally. Move locally. Fulfill locally.**

## Workflow

User needs item
→ MEMBRA finds local inventory
→ MEMBRA checks pickup/delivery options
→ Hero can self-handoff, meet halfway, or request Relay
→ Relay agent accepts route
→ item moves from Hero House / Alpha Hub / store / user
→ proof is captured
→ payment splits between owner, hub, courier, and MEMBRA

## Product Modes

- **Instant Local Delivery** — bring an item from a nearby Hero to a user
- **Meet Halfway** — both parties move less, lowering cost
- **Return Run** — agents handle returns/drop-offs
- **Hub Transfer** — move inventory between Hero Houses and Alpha Hubs
- **Errand Relay** — simple compliant errands
- **Batch Route** — bundle several low-value deliveries into one route
- **Storage-to-Delivery** — Alpha Hub holds item until a Relay agent delivers
- **On-Demand Courier** — host needs something brought across town

## Pricing

- Pickup only: $0
- Meet halfway: $2–$5
- Under 0.5 mile delivery: $4–$7
- 0.5–2 miles: $7–$12
- 2–5 miles: $12–$25
- Cross-city: quote required
- Heavy/bulky: surcharge
- Fragile/high-value: deposit or insurance required

## Payment Split Example

For a local delivery:
- User pays: $18
- Inventory Hero: $7
- Relay Agent: $6
- Alpha Hub: $2
- User cashback: $1
- MEMBRA fee: $2

For cross-city:
- Sender pays: $24
- Relay Agent: $17
- MEMBRA fee: $4
- Insurance/proof reserve: $1
- Referral/Hub fee: $2

## Relay Object Structure

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

## AI Dispatch Role

MEMBRA AI doesn't just match inventory — it chooses the fulfillment path:

- Can the buyer pick it up?
- Can the Hero meet halfway?
- Is there an Alpha Hub nearby?
- Is there a Relay agent already moving that direction?
- Can this be batched with other deliveries?
- Is the item restricted, fragile, perishable, or high value?
- Does this need proof, deposit, insurance, or rejection?

## System Stack

- **Ask MEMBRA** — user asks for need
- **MEMBRA Inventory** — detects supply
- **MEMBRA Marketplace** — creates listing
- **MEMBRA House** — local node
- **MEMBRA Alpha Hub** — storage/fulfillment node
- **MEMBRA Relay** — delivery/transfer layer
- **MEMBRA Pay** — payment split
- **MEMBRA Trust** — proof, risk, reputation
- **MEMBRA Supply** — predicts what to stock

## Partnership Angle

MEMBRA can approach larger delivery or quick-commerce companies as a local overflow inventory and micro-fulfillment partner.

**To DoorDash-like partners:**
"MEMBRA gives you distributed neighborhood inventory, pickup nodes, local storage, and low-friction demand signals. Your couriers can fulfill MEMBRA orders during idle time, and MEMBRA Heroes can create new hyperlocal order volume."

**To GoPuff-like partners:**
"MEMBRA extends micro-fulfillment beyond warehouses by turning trusted homes into light Alpha Hubs for long-tail inventory, returns, local storage, and neighborhood replenishment."

## Investor Pitch

MEMBRA combines local inventory, Hero Houses, Alpha Hubs, and Relay agents into a distributed fulfillment network where AI decides whether an item should be picked up, delivered, stored, transferred, batched, returned, or sold locally.

**AI-operated neighborhood commerce infrastructure.**

## Combined Repositories

This repo combines and references earlier work from GitHub submodules. See `/submodules/` for linked projects.

## Documentation

- [MEMBRA Master Summary](docs/MEMBRA_MASTER_SUMMARY.md) — Complete overview of MEMBRA as a chat-first, LLM-operated local sharing marketplace
- [Pricing & Payment Splits](docs/pricing.md) — Distance-based pricing, surcharges, and payment distribution logic
- [Submodule Components](docs/SUBMODULE_COMPONENTS.md) — Which parts from each submodule can be used for MEMBRA
