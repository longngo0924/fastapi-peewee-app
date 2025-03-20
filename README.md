# FastAPI Peewee App

A modern RESTful API built with FastAPI and Peewee ORM using PostgreSQL as the database backend.

## Features

- **FastAPI**: High-performance, easy-to-use framework for building APIs
- **Peewee ORM**: Lightweight ORM for interacting with PostgreSQL
- **JWT Authentication**: Secure user authentication with JWT tokens
- **PostgreSQL**: Robust relational database for production use
- **Migration System**: Database versioning with custom migration scripts
- **Testing**: In-memory SQLite database for fast test execution
- **Docker**: Containerized deployment for consistent environments
- **FastAPI CLI**: Application management using the official CLI tool

## Project Structure

```
.
├── app/                  # Application package
│   ├── api/              # API endpoints and routes
│   ├── core/             # Core configuration and database setup
│   ├── dependencies/     # Dependency injection functions
│   ├── models/           # Peewee database models
│   ├── schemas/          # Pydantic schemas for validation
│   └── services/         # Business logic layer
├── migrations/           # Database migration scripts
│   └── versions/         # Individual migration versions
├── tests/                # Test suite
├── .env                  # Environment variables
├── Dockerfile            # Docker container definition
└── requirements.txt      # Project dependencies
```

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL
- Virtual environment (recommended)
- Docker (optional)

### Installation

#### Option 1: Standard Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi_peewee_app.git
   cd fastapi_peewee_app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root with the following content:
   ```
   PROJECT_NAME=FastAPI Peewee App
   DATABASE_URL=postgresql://postgres:password@localhost:5432/fastapi-app
   SECRET_KEY=your-secret-key-should-be-changed-in-production
   ```
   **Important**: Replace the password with your actual PostgreSQL password, and generate a secure random secret key.

5. Run database migrations:
   ```bash
   python -m migrations.migrate 001_initial
   ```

#### Option 2: Docker Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi_peewee_app.git
   cd fastapi_peewee_app
   ```

2. Build the Docker image:
   ```bash
   docker build -t fastapi-peewee-app .
   ```

3. Run the container:
   ```bash
   docker run -d \
     --name fastapi-app \
     -p 8000:8000 \
     -e DATABASE_URL=postgresql://postgres:password@host.docker.internal:5432/fastapi_app \
     -e SECRET_KEY=your-secret-key \
     fastapi-peewee-app
   ```

   Note: 
   - Replace `postgres:password` with your PostgreSQL credentials
   - `host.docker.internal` refers to the host machine's localhost from inside the container
   - Make sure PostgreSQL is running on your host machine and is configured to accept connections

### Running the Application

#### Standard Method

Start the development server using uvicorn:

```bash
uvicorn app.main:app --reload
```

Or use the FastAPI CLI:

```bash
fastapi run app/main.py --reload
```

#### Using Docker

To run the application with Docker:

```bash
docker run -d -p 8000:8000 fastapi-peewee-app
```

The API will be available at `http://127.0.0.1:8000`.
API documentation is available at `http://127.0.0.1:8000/docs`.

## Testing

### Standard Method

Run the test suite:

```bash
pytest
```

For test coverage:

```bash
pytest --cov=app
```

### With Docker

To run tests in a Docker container:

```bash
docker run --rm fastapi-peewee-app pytest
```

## API Endpoints

- `POST /api/v1/users/`: Create a new user
- More endpoints coming soon...

## Database Migrations

To create a new migration:

1. Create a new file in `migrations/versions/` with a sequential number, e.g., `002_add_posts.py`
2. Implement the migration script following the pattern in existing migrations
3. Run the migration: `python -m migrations.migrate 002_add_posts`

## License

This project is licensed under the MIT License - see the LICENSE file for details. 