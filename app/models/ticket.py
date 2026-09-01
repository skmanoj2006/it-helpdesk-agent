from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class TicketCategory(str, Enum):
    ACCESS = "access"
    HARDWARE = "hardware"
    NETWORK = "network"
    SOFTWARE = "software"
    SECURITY = "security"


class TicketPriority(str, Enum):
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"
    P4 = "P4"


class TicketStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    ESCALATED = "escalated"


@dataclass
class Ticket:
    ticket_id: str
    requester_id: str
    description: str
    priority: TicketPriority

    category: TicketCategory | None = None
    status: TicketStatus = TicketStatus.OPEN

    created_at: datetime = field(default_factory=datetime.utcnow)

    conversation_history: list[str] = field(default_factory=list)
    tool_call_log: list[dict] = field(default_factory=list)