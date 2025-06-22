from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_message_flow():
    sender = "agent-a"
    receiver = "agent-b"
    content = "Hello there"

    res = client.post("/api/message", params={
        "sender_id": sender,
        "receiver_id": receiver,
        "content": content
    })

    assert res.status_code == 200
    msg = res.json()
    assert msg["sender_id"] == sender
    assert msg["receiver_id"] == receiver
    assert msg["content"] == content

    convo = client.get("/api/messages", params={
        "sender_id": sender,
        "receiver_id": receiver
    })
    assert convo.status_code == 200
    assert len(convo.json()) >= 1
