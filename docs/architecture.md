# Architecture

ViSQL is a monorepo with independently deployable frontend and backend services. The frontend uses Next.js App Router; the backend exposes a versioned FastAPI REST API.

## Backend boundaries

`api` translates HTTP requests and responses. `services` contains application use cases. `repositories` owns data access through SQLAlchemy models. `schemas` defines Pydantic contracts. Cross-cutting configuration, logging, database setup, and AI clients are isolated from feature code.

## Frontend boundaries

`app` owns routing and layouts. `features` groups domain-specific UI and state. `components` contains reusable presentation components. `services` owns API clients and `lib` contains shared utilities and configuration.

No product-domain feature is implemented in this initialization.

