# Tool Aggregator Backend

This is the production-ready backend for the AI Tool Aggregator SaaS platform. It supports orchestrated AI workflows, token-based authentication, encrypted data, and modular tool connectors.

---

## 🚀 Features

- FastAPI backend
- JWT-based authentication
- Modular orchestration engine
- Mock connectors for ChatGPT, ElevenLabs, RunwayML
- AES-style encryption via Fernet
- Dockerized with `docker-compose`
- Ready for CI/CD and production deployment

---

## 🛠 Setup

```bash
# Clone the repo
git clone https://github.com/your-repo-url.git
cd GPT1

# Build and run
docker-compose up --build
