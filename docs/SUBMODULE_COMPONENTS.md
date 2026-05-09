# Submodule Component Mapping for MEMBRA

This document maps which parts from each submodule can be used for MEMBRA.

## Core Infrastructure Submodules

### DockOS
**Purpose:** FastAPI backend infrastructure for space booking with auth, payments, booking engine

**Components for MEMBRA:**
- **Auth system** (`packages/auth/`) — JWT authentication, user registration, login, role management (guest/host)
- **Booking engine** (`packages/booking-engine/`) — Overlap prevention, booking lifecycle, check-in/check-out
- **Payments** (`packages/payments/`) — Platform fee calculation, host payout settlement, payment ledger
- **Database** (`packages/database/`) — SQLAlchemy models, Alembic migrations, seed data
- **Realtime** (`packages/realtime/`) — WebSocket support for live updates
- **API** (`apps/api/`) — FastAPI endpoints, Pydantic schemas, exception handling
- **Docker Compose** — Local development setup with PostgreSQL, Redis
- **Render deployment** (`render.yaml`) — Production deployment configuration

**MEMBRA Modules:** MEMBRA Spaces, MEMBRA Requests, MEMBRA Delivery

---

### Couchify
**Purpose:** Next.js app for booking private seating capacity by the minute

**Components for MEMBRA:**
- **Next.js App Router** — `/explore` marketplace grid, `/spaces/[id]` detail pages, `/host` dashboard
- **Neumorphic UI components** — Cards, selectors, pills, pricing calculators
- **Pricing logic** (`lib/pricing.ts`) — Seat × minute × price calculation
- **Capacity helpers** (`lib/capacity.ts`) — Seat availability management
- **Mock data** (`lib/mock-data.ts`) — Sample spaces for development
- **Vercel deployment** — Production-ready configuration

**MEMBRA Modules:** MEMBRA Spaces (MEMBRA by Couchify)

---

## AI/ML & LLM Submodules

### Repo 19 (Speculative Signal Research Lab)
**Purpose:** Research operating system for discovering and evaluating signal classes with AI/ML

**Components for MEMBRA:**
- **Feedback ingestion** (`feedback_ingest/`) — Parse and classify user feedback for improvement
- **Prompt versions** (`prompt_versions/`) — Versioned prompts and hypothesis templates
- **Evaluation reports** (`evaluation_reports/`) — LLM evaluation outputs and scorecards
- **Simulation runs** (`simulation_runs/`) — Non-execution simulation artifacts
- **Improvement proposals** (`improvement_proposals/`) — Structured improvement suggestions
- **Safety policies** (`safety_policies/`) — Hard safety requirements for AI operations

**MEMBRA Modules:** MEMBRA Assess, MEMBRA AdAgent, MEMBRA Requests (LLM interpretation)

---

### -google-voice-orders
**Purpose:** Voice-based order processing integration

**Components for MEMBRA:**
- **Voice-to-text processing** — Convert voice requests to structured demand
- **Order parsing** — Extract item, quantity, urgency from voice input
- **Backend API** (`backend/`) — FastAPI service for voice order processing

**MEMBRA Modules:** MEMBRA Requests (chat-first interface), MEMBRA Skills (voice-based service requests)

---

## Credits & Rewards Submodules

### Repo 1 (KPI Factory)
**Purpose:** Full-stack scaffold for tokenized KPIs with Solidity contracts, FastAPI backend, Streamlit frontend

**Components for MEMBRA:**
- **Smart contracts** (`contracts/`) — ERC-20 KPI tokens, oracle contracts, registry
- **Backend API** (`backend/`) — FastAPI with REST endpoints, WebSocket streaming
- **LLM integration placeholder** — Where LLM would score prompts and propose KPIs
- **Oracle feeder** (`scripts/oracle_feeder.py`) — Off-chain data ingestion

**MEMBRA Modules:** MEMBRA Credits (tokenized rewards system)

---

### Repo 5 (KPI Factory)
**Purpose:** Similar to repo 1 — KPI Factory system

**Components for MEMBRA:**
- Same as repo 1 (duplicate or variant)

**MEMBRA Modules:** MEMBRA Credits (alternative implementation)

---

## Security & Payment Submodules

### Repo 25 (Vault Protocol)
**Purpose:** Enterprise IP collateralization with blockchain, security, rate limiting, ERC-3643 compliance

**Components for MEMBRA:**
- **Async blockchain service** — Non-blocking Web3 operations with gas optimization
- **Enterprise compliance service** — Multi-layer KYC verification
- **Security config** — Encrypted private key storage, rate limiting
- **Audit logger** — Cryptographic audit trail
- **Redis rate limiting** — Abuse mitigation
- **Health monitoring** — Comprehensive health checks

**MEMBRA Modules:** MEMBRA Payments, MEMBRA Delivery (escrow), MEMBRA Assess (compliance verification)

---

### Repo 6 (SuperpositionNFT)
**Purpose:** NFT observation economy with Hardhat contracts, Next.js 14 UI, wallet connectivity

**Components for MEMBRA:**
- **Smart contracts** (`packages/contracts/`) — Hardhat project with NFT contracts
- **Next.js 14 UI** (`apps/web/`) — Neomorphic design system, wallet connectivity
- **Signed edge APIs** — HMAC-signed API routes
- **Observability** — Sentry and OTEL instrumentation
- **Rate limiting** — CSP headers, signed entropy APIs

**MEMBRA Modules:** MEMBRA Shelf (NFT-based inventory tracking), MEMBRA Skills (capability NFTs)

---

## Infrastructure & Tools

### Repo 14 (Repository Factory)
**Purpose:** Flask app for spinning up pre-initialized Git repositories

**Components for MEMBRA:**
- **Repository initialization** — Git repo creation with standardized metadata
- **Launch destination templates** — Multi-platform deployment links

**MEMBRA Modules:** Not directly applicable (could be used for MEMBRA template/host provisioning)

---

## Less Relevant Submodules

### Repo 12 (Paradox Liquidity)
**Purpose:** Solana Anchor and Foundry smart contracts for liquidity

**Components for MEMBRA:** Not directly relevant (DeFi/liquidity focused)

### Repo 15 (Live Alpha Signals)
**Purpose:** Price edge mining for trading

**Components for MEMBRA:** Not directly relevant (trading focused)

### Repo 30 (DEX Sniper Agent)
**Purpose:** Solana DEX routing for price comparison

**Components for MEMBRA:** Not directly relevant (DeFi focused)

### Repo 18 (Anchor)
**Purpose:** Solana Anchor programs

**Components for MEMBRA:** Not directly relevant (Solana smart contracts)

---

## Minimal/Empty Submodules

### Repos 2, 3, 7, 8, 10, 11, 13, 16, 17, 20, 22, 23, 24, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38
**Status:** Minimal or no README documentation
**Recommendation:** Need manual inspection to determine relevance

---

## Integration Strategy

### Phase 1: Core Infrastructure (Immediate)
1. **DockOS** — Use as backend foundation for MEMBRA Spaces, Requests, Delivery
2. **Couchify** — Use as frontend template for MEMBRA Spaces module
3. **Repo 19** — Extract AI/ML components for MEMBRA Assess and AdAgent

### Phase 2: Credits & Security (Short-term)
1. **Repo 1 or 5** — Adapt KPI Factory for MEMBRA Credits system
2. **Repo 25** — Integrate security and compliance features for payments
3. **-google-voice-orders** — Add voice interface to MEMBRA Requests

### Phase 3: Advanced Features (Medium-term)
1. **Repo 6** — Consider NFT-based inventory tracking for MEMBRA Shelf
2. **Inspect numbered repos** — Evaluate minimal repos for utility components

### Phase 4: Deferred
1. **DeFi-focused repos** (12, 15, 30, 18) — Not relevant unless MEMBRA adds financial products

---

## Summary

**High-value submodules for MEMBRA:**
- DockOS (backend infrastructure)
- Couchify (frontend template)
- Repo 19 (AI/ML components)
- Repo 1/5 (credits system)
- Repo 25 (security/payments)
- -google-voice-orders (voice interface)

**Medium-value submodules:**
- Repo 6 (NFT inventory)
- Minimal numbered repos (need inspection)

**Low-value submodules:**
- DeFi/liquidity repos (12, 15, 30, 18)
- Trading/signal repos
