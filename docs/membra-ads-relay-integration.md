# Membra Ads Relay Integration

Membra Relay is the fulfillment and proof-route layer for Membra Ads.

## Role

Membra Ads creates campaigns, media kits, QR/NFC identities, proof rules, and payout eligibility.

Membra Relay handles physical movement, pickup, delivery, receipt confirmation, route status, and delivery proof.

## Shared objects

- campaign id
- media kit id
- owner id
- asset id
- pickup node
- delivery node
- relay request
- relay proof
- payout eligibility state

## Media kit fulfillment flow

1. Membra Ads creates a media kit.
2. Media kit is assigned to an owner and asset.
3. Vendor order or manual kit package is prepared.
4. Membra Relay creates a delivery or pickup route.
5. Relay agent records pickup proof.
6. Relay agent records delivery proof.
7. Owner confirms receipt.
8. Membra Ads waits for install proof before campaign activation.

## Relay proof events

Relay proof should include:

- relay id
- media kit id
- proof type
- evidence URL
- location when permitted
- timestamp
- status
- reviewer notes

## Status bridge

Relay status should update media kit status:

- created -> kit ordered
- picked up -> kit in transit
- delivered -> kit delivered
- receipt confirmed -> receipt confirmed
- install proof approved -> active

## Payout rule

Delivery proof can unlock courier payout.

Install proof unlocks owner campaign reward eligibility.

They are separate payout triggers.
