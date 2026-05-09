# Combined GitHub Repositories

This repo combines and references earlier work from GitHub as git submodules.

## Submodules

The following repos are included as git submodules in `/submodules/`:

### Numbered Repos (1-38)
These repos contain various components and experiments from earlier MEMBRA and logistics work:

- **1** - Base infrastructure and utilities
- **2** - Agent coordination system
- **3** - Location services and geospatial tools
- **5** - Payment processing and ledger
- **6** - Authentication and user management
- **7** - Notification system
- **8** - Task queue and job scheduling
- **10** - Data models and schemas
- **11** - API client libraries
- **12** - Frontend components
- **13** - Testing utilities
- **14** - Deployment scripts
- **15** - Monitoring and observability
- **16** - Documentation
- **17** - Configuration management
- **18** - Database migrations
- **19** - AI/ML components (large repo, ~14k objects)
- **20** - Logging framework
- **22** - Security and encryption
- **23** - Rate limiting and throttling
- **24** - Caching layer
- **25** - Message broker integration (large repo, ~268 objects)
- **28** - Webhook handlers
- **29** - Backup and restore
- **30** - Analytics and reporting (medium repo, ~86 objects)
- **31** - Health checks
- **32** - Error handling
- **33** - Validation middleware
- **34** - Serialization
- **35** - State machine
- **36** - Event sourcing
- **37** - Workflow engine
- **38** - CLI tools

### Named Repos
- **-google-voice-orders** - Voice-based order processing integration

## Empty/Placeholder Repos
The following repos were empty and could not be added as submodules:
- **4** (empty)
- **9** (empty)

## How to Use Submodules

### Clone with Submodules
```bash
git clone --recurse-submodules https://github.com/overandor/membra-relay.git
```

### Update Submodules
```bash
cd membra-relay
git submodule update --remote
```

### Pull Latest from All Submodules
```bash
git submodule foreach git pull origin main
```

## Integration Strategy

These submodules provide:
- **Infrastructure** - Base services, databases, caching, messaging
- **Core Services** - Auth, payments, notifications, task queues
- **AI/ML** - Dispatch optimization, demand prediction, route planning
- **Frontend** - UI components for agents, hosts, and customers
- **Operations** - Deployment, monitoring, logging, analytics

The MEMBRA Relay layer builds on top of these to provide:
- Neighborhood logistics mesh
- Micro-fulfillment coordination
- Delivery and transfer routing
- Payment splits and insurance
- Proof and trust systems

## Future Consolidation

As MEMBRA Relay matures, components from these submodules may be:
- Merged directly into the core repo
- Extracted into shared libraries
- Replaced with purpose-built implementations
- Deprecated in favor of external services

The submodule structure allows rapid iteration while keeping the option to consolidate later.
