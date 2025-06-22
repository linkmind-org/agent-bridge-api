from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.db.database import SessionLocal
from app.db import models
from app.models.agent import Agent
from app.models.message import Message

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Agent endpoints
@router.post("/agents", response_model=Agent)
def create_agent(agent: Agent, db: Session = Depends(get_db)):
    # Convert UUID to bytes for SQLite BLOB primary key
    db_agent = db.execute(models.agents.select().where(models.agents.c.id == agent.id.bytes)).first()
    if db_agent:
        raise HTTPException(status_code=400, detail="Agent already exists")
    db.execute(
        models.agents.insert().values(
            id=agent.id.bytes,
            name=agent.name,
            description=agent.description,
            is_human=agent.is_human,
        )
    )
    db.commit()
    return agent

@router.get("/agents", response_model=List[Agent])
def list_agents(db: Session = Depends(get_db)):
    agents = db.execute(models.agents.select()).fetchall()
    result = []
    for a in agents:
        result.append(Agent(
            id=UUID(bytes=a.id),
            name=a.name,
            description=a.description,
            is_human=a.is_human,
        ))
    return result

# Message endpoints
@router.post("/messages", response_model=Message)
def create_message(message: Message, db: Session = Depends(get_db)):
    db.execute(
        models.messages.insert().values(
            id=message.id.bytes,
            sender_id=message.sender_id.bytes,
            thread_id=message.thread_id.bytes,
            content=message.content,
            timestamp=message.timestamp,
            reply_to_id=message.reply_to_id.bytes if message.reply_to_id else None,
        )
    )
    db.commit()
    return message

@router.get("/threads/{thread_id}/messages", response_model=List[Message])
def get_thread_messages(thread_id: UUID, db: Session = Depends(get_db)):
    rows = db.execute(models.messages.select().where(models.messages.c.thread_id == thread_id.bytes)).fetchall()
    messages = []
    for r in rows:
        messages.append(Message(
            id=UUID(bytes=r.id),
            sender_id=UUID(bytes=r.sender_id),
            thread_id=UUID(bytes=r.thread_id),
            content=r.content,
            timestamp=r.timestamp,
            reply_to_id=UUID(bytes=r.reply_to_id) if r.reply_to_id else None,
        ))
    return messages