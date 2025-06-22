from sqlalchemy import Table, Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.sqlite import BLOB
from sqlalchemy.orm import registry
from datetime import datetime
import uuid

from .database import metadata

mapper_registry = registry()

agents = Table(
    "agents",
    metadata,
    Column("id", BLOB, primary_key=True, default=lambda: uuid.uuid4().bytes),
    Column("name", String, nullable=False),
    Column("description", String, nullable=True),
    Column("is_human", Boolean, default=False),
)

messages = Table(
    "messages",
    metadata,
    Column("id", BLOB, primary_key=True, default=lambda: uuid.uuid4().bytes),
    Column("sender_id", BLOB, ForeignKey("agents.id"), nullable=False),
    Column("thread_id", BLOB, nullable=False),
    Column("content", String, nullable=False),
    Column("timestamp", DateTime, default=datetime.utcnow),
    Column("reply_to_id", BLOB, ForeignKey("messages.id"), nullable=True),
)
