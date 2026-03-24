# Learnclew

Independent web learning product built with Vue 3 and FastAPI.

## Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- Docker and Docker Compose
- pnpm (recommended) or npm

### Setup

1. Clone the repository:
```bash
git clone https://github.com/llamapw/learnclew.git
cd learnclew
```

2. Copy environment file:
```bash
cp .env.example .env
```

3. Start PostgreSQL:
```bash
docker compose up -d postgres
```

4. Setup backend:
```bash
cd backend
pip install -e ".[dev]"
```

5. Setup frontend:
```bash
cd frontend
pnpm install
```

### Run Development Servers

Backend:
```bash
cd backend
python -m uvicorn app.main:app --reload
```

Frontend:
```bash
cd frontend
pnpm dev
```

### Run Tests

Backend:
```bash
cd backend
pytest
```

Frontend:
```bash
cd frontend
pnpm test
```

## Architecture

- **Frontend**: Vue 3 + Vite + Pinia + Vue Router
- **Backend**: FastAPI + SQLAlchemy + PostgreSQL
- **Storage**: Local file storage (upgradeable to S3-compatible)
- **Jobs**: In-process background tasks (upgradeable to worker queue)

## Project Structure

```
learnclew/
├── frontend/          # Vue 3 application
├── backend/           # FastAPI application
├── docs/              # Specifications and plans
└── docker-compose.yml # Local development services
```
