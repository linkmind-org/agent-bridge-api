from typing import List, Dict
from app.models.agent import Message

# In-memory storage for now
class InMemoryDB:
    def __init__(self):
        self.messages: List[Message] = []

    def save_message(self, message: Message):
        self.messages.append(message)

    def get_conversation(self, agent_a: str, agent_b: str) -> List[Message]:
        return [m for m in self.messages if 
                (m.sender_id == agent_a and m.receiver_id == agent_b) or
                (m.sender_id == agent_b and m.receiver_id == agent_a)]

# Singleton instance
db = InMemoryDB()
