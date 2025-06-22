from fastapi import APIRouter
from typing import List
from app.models.agent import Message
from app.services import agent_manager

router = APIRouter(prefix="/api")

@router.post("/message", response_model=Message)
def post_message(sender_id: str, receiver_id: str, content: str):
    return agent_manager.send_message(sender_id, receiver_id, content)

@router.get("/messages", response_model=List[Message])
def get_messages(sender_id: str, receiver_id: str):
    return agent_manager.get_messages_between(sender_id, receiver_id)

