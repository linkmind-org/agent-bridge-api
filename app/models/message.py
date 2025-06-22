from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

class Message(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    sender_id: UUID
    thread_id: UUID
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    reply_to_id: Optional[UUID] = None

