# ViSQL

ViSQL is an AI-powered SQL learning platform focused on making query execution understandable through visual, stage-by-stage data transformations.

## Quick start

1. Copy `.env.example` to `.env` and set secrets appropriate for your environment.
2. Start the local stack: `docker compose up --build`.
3. Open `http://localhost:3000`; the API health endpoint is at `http://localhost:8000/api/v1/health`.

## Repository layout

```text
frontend/     Next.js application
backend/      FastAPI application and database migrations
docs/         Architecture and contributor documentation
docker/       Container-related shared assets
.github/      CI workflows and repository automation
```

## Architecture principles

- Feature-oriented frontend modules with shared UI and infrastructure layers.
- API routes remain thin; business logic lives in services and persistence in repositories.
- Configuration is environment-driven and validated at startup.
- Database schema changes are versioned through Alembic.

## Next milestones

1. Define authentication, user, and learning-progress domain models.
2. Add SQL workspace execution sandbox and query-stage representation.
3. Build the schema explorer and execution visualizer interfaces.
4. Integrate the AI tutor and AI-generated database/challenge workflows.
5. Add authorization, observability, end-to-end tests, and deployment pipelines.

