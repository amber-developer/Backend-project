# FastAPI Backend with Docker

A containerized FastAPI backend application with PostgreSQL and Redis, configured with Docker.

## 📋 Overview

This project provides a ready-to-use FastAPI backend environment running in Docker containers. It includes:

- FastAPI web server with hot reloading
- PostgreSQL database
- Redis for session management
- Alembic for database migrations
- Docker configuration for development

## 🚀 Quick Start

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Setup and Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. Create the Docker network:

```bash
docker network create backend-network
```

3. Start the services:

```bash
docker-compose -f DockerCompose.yml up --build
```

4. Access the API at http://localhost:8000 and API documentation at http://localhost:8000/docs

## 🏗️ Project Structure

```
├── DockerCompose.yml         # Docker Compose configuration
├── Dockerfile.local          # Docker configuration for the backend
├── README.md                 # This file
├── backend/                  # Backend application code
│   └── src/
│       ├── main.py           # FastAPI application entry point
│       ├── models.py         # SQLAlchemy models
│       ├── dependencies.py   # FastAPI dependencies
│       ├── api/              # API modules
│       │   ├── routes/       # API route definitions
│       │   └── schemas/      # Pydantic schemas
│       ├── alembic/          # Database migrations
│       └── requirements.txt  # Python dependencies
├── .volumes/                 # Persistent data volumes
│   ├── db/data/              # PostgreSQL data
│   └── redis_session/        # Redis data
```

## 🐳 Docker Configuration

The project uses Docker Compose to manage three services:

1. **Backend Service (FastAPI)**
   - Builds from `Dockerfile.local`
   - Exposes port 8000 for API access
   - Sets up hot reloading for development
   - Mounts the source code as a volume

2. **PostgreSQL Database**
   - Uses PostgreSQL 17
   - Persists data to `.volumes/db/data/`
   - Credentials: Username: `postgres`, Password: `postgres`
   - Database name: `backend-dev`
   - Exposes port 5432

3. **Redis Session**
   - Uses Redis 7.2
   - Persists data to `.volumes/redis_session/`

## 📊 API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 💾 Database Migrations with Alembic

Alembic is used for database migrations, allowing you to version control your database schema.

### Initialize Alembic (first time only)

```bash
# Access the backend container
docker exec -it backend-fastapi-app bash

# Inside the container
cd /app
alembic init alembic

# Edit alembic.ini - set database URL
# sqlalchemy.url = postgresql://postgres:postgres@db:5432/backend-dev

# Edit alembic/env.py to import your models
# import models
# target_metadata = models.Base.metadata
```

### Create and Apply Migrations

```bash
# After making changes to your SQLAlchemy models

# Create a migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head
```

## 🧰 Useful Commands

### Docker Commands

```bash
# Start services
docker-compose -f DockerCompose.yml up

# Start in detached mode
docker-compose -f DockerCompose.yml up -d

# Stop services
docker-compose -f DockerCompose.yml down

# View logs
docker-compose -f DockerCompose.yml logs -f

# View logs for a specific service
docker-compose -f DockerCompose.yml logs -f backend

# Restart a specific service
docker-compose -f DockerCompose.yml restart backend
```

### Database Access

```bash
# Connect to PostgreSQL
docker exec -it backend-db psql -U postgres -d backend-dev

# Basic PostgreSQL commands
\dt         # List tables
\d tablename # Describe table
\q          # Quit
```

### Redis CLI

```bash
# Connect to Redis
docker exec -it backend-redis-session redis-cli

# Basic Redis commands
KEYS *      # List all keys
GET keyname # Get value of a key
FLUSHALL    # Clear all data
EXIT        # Exit Redis CLI
```

## 🛠️ Development Workflow

1. **Start the services**: `docker-compose -f DockerCompose.yml up`
2. **Create your FastAPI routes**: Add files in `backend/src/api/routes/`
3. **Define models**: Update `backend/src/models.py`
4. **Create migrations**: Use Alembic when you change models
5. **Test endpoints**: Use the Swagger UI at http://localhost:8000/docs

## 📚 Adding Dependencies

To add a new Python package:

1. Add it to `backend/src/requirements.txt`
2. Restart the backend service:
   ```bash
   docker-compose -f DockerCompose.yml restart backend
   ```

## 🔒 Environment Variables

You can customize the configuration by modifying these environment variables in DockerCompose.yml:

- Database settings:
  - `POSTGRES_USER`: PostgreSQL username (default: postgres)
  - `POSTGRES_PASSWORD`: PostgreSQL password (default: postgres)
  - `POSTGRES_DB`: Database name (default: backend-dev)

- App settings (can be added to the backend service):
  - `DEBUG`: Enable debug mode (default: not set)
  - Add any other environment variables your application needs

## 🐛 Troubleshooting

### Container won't start

Check if ports are already in use:
```bash
sudo lsof -i :8000
sudo lsof -i :5432
```

### Database migration issues

If you encounter problems with migrations:
```bash
# Access the container
docker exec -it backend-fastapi-app bash

# Check migration history
alembic history

# Stamp the database with the current head without running migrations
alembic stamp head
```

## 📝 Notes

- The API server automatically reloads when you make changes to the code
- Database data persists between container restarts thanks to the mounted volumes
- The timezone is set to Asia/Calcutta in the Dockerfile

## 📄 License

[Add your license information here]

## 👥 Contributing

[Add contributing guidelines here]
