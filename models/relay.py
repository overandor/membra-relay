"""
MEMBRA Relay Data Models
"""
from enum import Enum
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class RelayMode(str, Enum):
    """Relay fulfillment modes"""
    PICKUP_ONLY = "pickup_only"
    MEET_HALFWAY = "meet_halfway"
    LOCAL_DELIVERY = "local_delivery"
    RETURN_RUN = "return_run"
    HUB_TRANSFER = "hub_transfer"
    ERRAND_RELAY = "errand_relay"
    BATCH_ROUTE = "batch_route"
    STORAGE_TO_DELIVERY = "storage_to_delivery"
    ON_DEMAND_COURIER = "on_demand_courier"


class RelayStatus(str, Enum):
    """Relay status states"""
    AVAILABLE = "available"
    ACCEPTED = "accepted"
    IN_PROGRESS = "in_progress"
    PICKED_UP = "picked_up"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    FAILED = "failed"


class RiskLevel(str, Enum):
    """Risk level for items"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    FRAGILE = "fragile"
    HIGH_VALUE = "high_value"


class NodeType(str, Enum):
    """Types of nodes in the network"""
    HERO_HOUSE = "hero_house"
    ALPHA_HUB = "alpha_hub"
    USER = "user"
    STORE = "store"
    WAREHOUSE = "warehouse"
    COURIER_HUB = "courier_hub"


class RelayNode(BaseModel):
    """A node in the MEMBRA network (pickup or dropoff location)"""
    node_id: str
    node_type: NodeType
    name: str
    address: str
    latitude: float
    longitude: float
    capacity_items: Optional[int] = None
    hours: Optional[str] = None
    contact: Optional[str] = None


class RelayItem(BaseModel):
    """Item being moved through the Relay network"""
    item_id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    weight_lb: Optional[float] = None
    dimensions: Optional[str] = None  # e.g., "12x8x4"
    value_usd: Optional[float] = None
    fragile: bool = False
    perishable: bool = False
    restricted: bool = False
    image_url: Optional[str] = None


class RelayRequest(BaseModel):
    """Request for a Relay fulfillment"""
    request_id: str = Field(default_factory=lambda: str(uuid4()))
    item: RelayItem
    pickup_node: RelayNode
    dropoff_node: RelayNode
    mode: RelayMode
    distance_miles: float
    estimated_minutes: int
    risk_level: RiskLevel = RiskLevel.LOW
    proof_required: bool = True
    insurance_required: bool = False
    special_instructions: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class RelayOffer(BaseModel):
    """Offer from a Relay agent to fulfill a request"""
    offer_id: str = Field(default_factory=lambda: str(uuid4()))
    request_id: str
    agent_id: str
    agent_name: str
    agent_rating: float
    vehicle_type: Optional[str] = None  # car, bike, walk, etc.
    estimated_arrival_minutes: int
    quoted_payout: float
    available_immediately: bool = True
    message: Optional[str] = None


class Relay(BaseModel):
    """Active Relay fulfillment"""
    relay_id: str = Field(default_factory=lambda: str(uuid4()))
    request_id: str
    offer_id: Optional[str] = None
    agent_id: str
    pickup_node: RelayNode
    dropoff_node: RelayNode
    mode: RelayMode
    distance_miles: float
    estimated_minutes: int
    actual_minutes: Optional[int] = None
    payout_to_agent: float
    platform_fee: float
    insurance_reserve: float = 0.0
    hub_fee: float = 0.0
    referral_fee: float = 0.0
    proof_required: bool = True
    risk_level: RiskLevel = RiskLevel.LOW
    status: RelayStatus = RelayStatus.AVAILABLE
    created_at: datetime = Field(default_factory=datetime.utcnow)
    accepted_at: Optional[datetime] = None
    picked_up_at: Optional[datetime] = None
    delivered_at: Optional[datetime] = None
    proof_photo_url: Optional[str] = None
    proof_signature: Optional[str] = None
    notes: Optional[str] = None


class RelayBatch(BaseModel):
    """Batched Relay routes for efficiency"""
    batch_id: str = Field(default_factory=lambda: str(uuid4()))
    relay_ids: List[str]
    agent_id: str
    total_payout: float
    total_distance_miles: float
    estimated_total_minutes: int
    status: RelayStatus = RelayStatus.AVAILABLE
    created_at: datetime = Field(default_factory=datetime.utcnow)


class RelayProof(BaseModel):
    """Proof of delivery/pickup"""
    proof_id: str = Field(default_factory=lambda: str(uuid4()))
    relay_id: str
    type: str  # "pickup" or "dropoff"
    photo_url: str
    location_latitude: float
    location_longitude: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    signature: Optional[str] = None
    notes: Optional[str] = None
