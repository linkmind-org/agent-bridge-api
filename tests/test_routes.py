from fastapi.testclient import TestClient
from uuid import uuid4
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_agent_and_message_flow():
    # Create two agents
    agent_a_data = {"name": "agent-a", "is_human": False}
    agent_b_data = {"name": "agent-b", "is_human": False}

    res_a = client.post("/agents", json=agent_a_data)
    assert res_a.status_code == 200
    agent_a = res_a.json()

    res_b = client.post("/agents", json=agent_b_data)
    assert res_b.status_code == 200
    agent_b = res_b.json()

    # Create a thread ID (UUID)
    thread_id = str(uuid4())

    # Send a message from agent_a in this thread
    message_data = {
        "sender_id": agent_a["id"],
        "thread_id": thread_id,
        "content": "Hello there",
        "reply_to_id": None
    }

    res_msg = client.post("/messages", json=message_data)
    assert res_msg.status_code == 200
    message = res_msg.json()
    assert message["content"] == "Hello there"
    assert message["sender_id"] == agent_a["id"]
    assert message["thread_id"] == thread_id

    # Retrieve messages for the thread
    res_thread = client.get(f"/threads/{thread_id}/messages")
    assert res_thread.status_code == 200
    messages = res_thread.json()
    assert len(messages) >= 1
    assert messages[0]["content"] == "Hello there"
