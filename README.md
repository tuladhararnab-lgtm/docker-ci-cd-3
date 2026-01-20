# Docker Demo

## Setup

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Update `.env` with your credentials

3. Run:
   ```bash
   docker-compose up --build
   ```

## CI/CD Setup

Add these secrets in GitHub repository settings (Settings → Secrets → Actions):

- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`