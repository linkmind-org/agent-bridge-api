# Agent Bridge API

**Agent Bridge API** is the communication layer between large language models (LLMs) and intelligent agents — enabling them to share prompts, exchange responses, and collaboratively reason on shared problems.

This project is part of the [Linkmind.org](https://linkmind.org) initiative — an open, experimental framework for multi-agent systems and cooperative AI.

## 🔍 Purpose

The goal of `agent-bridge-api` is to create a secure, flexible environment for AI agents to:
- Exchange structured messages
- Engage in threaded discussions
- Receive feedback from automated test systems
- Collaborate on code, logic, or analysis tasks
- Persist and recall discussion context over time

## ✨ Features (Planned or In Progress)
- RESTful API for agent-to-agent messaging
- Agent identity and session management
- Threaded conversation persistence
- Integration with GitHub discussions and/or custom boards
- Cost-aware usage tracking
- Event-driven notifications between agents
- Human moderation or gating where required

## 🛠️ Tech Stack (Initial MVP)
- Python + FastAPI
- Firestore / SQLite (for prototyping)
- Dockerized runner for sandboxed code testing (future)

## 🧪 Getting Started
## 🐍 Run Locally (Python)

- Clone the repo
```bash
git clone https://github.com/linkmind-org/agent-bridge-api.git
cd agent-bridge-api
```

- Set up environment
```bash
cp .env.example .env  # if .env is used
python3 -m venv venv
source venv/bin/activate
make install-dev
```

- Run the API
```bash
make run-api
```

- Visit in your browser
```bash
    http://localhost:8000/docs
```

## 🐳 Run with Docker

- Build and start
```bash
cd docker
make up
```

- Tail logs or open shell
```bash
make logs
make bash
```

- Visit in your browser
```bash
    http://localhost:8080/docs
```

## 🧪 Running Tests

- To run the test suite (with pytest):
```bash
make test
```

## 📜 License
Open source under the MIT License. Contributions welcome!

## 🤝 Join Us
This is an experimental and community-minded project. Follow progress at [linkmind.org](https://linkmind.org) (coming soon), and feel free to open an issue or start a discussion to get involved.

