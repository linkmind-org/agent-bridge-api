from pydantic import BaseModel, Field
from typing import List
from uuid import uuid4

class Agent(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    type: str  # e.g. 'chatgpt', 'gemini', 'human'

class Message(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    sender_id: str
    receiver_id: str
    content: str
    timestamp: str
