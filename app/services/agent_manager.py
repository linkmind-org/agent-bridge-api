from datetime import datetime
from app.models.agent import Message
from app.db.database import db

def send_message(sender_id: str, receiver_id: str, content: str) -> Message:
    msg = Message(
        sender_id=sender_id,
        receiver_id=receiver_id,
        content=content,
        timestamp=datetime.utcnow().isoformat()
    )
    db.save_message(msg)
    return msg

def get_messages_between(agent1: str, agent2: str):
    return db.get_conversation(agent1, agent2)
