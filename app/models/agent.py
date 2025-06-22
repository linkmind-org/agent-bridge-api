from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4

class Agent(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None
    is_human: bool = False
