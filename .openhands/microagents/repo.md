---
name: repo
type: repo
agent: CodeActAgent
---
This repository contains the code for ProjectTimeTracker, a time tracking application built with Python and API Logic Server. It provides a RESTful API and web interface for managing projects, time entries, and related data.

## Server Configuration:
- Available ports: 50815, 58270
- Host: 0.0.0.0 (allow all hosts)
- CORS: Enabled for all origins
- Iframe: Allowed
- Default database: SQLite (PostgreSQL supported)

## Initial Setup:
1. Create and activate virtual environment:
```bash
# Create virtual environment
python -m venv venv
# Activate it (Linux/Mac)
source venv/bin/activate
# Or on Windows
# .\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Server Start Commands:
1. Using run.sh (recommended):
```bash
# Make script executable
chmod +x run.sh
# Set the port
export APILOGICPROJECT_PORT=50815
# Start with Flask (development)
./run.sh
# Or start with Gunicorn (production)
./run.sh gunicorn
```

2. Alternative direct Python command:
```bash
python api_logic_server_run.py --host=0.0.0.0 --port=50815 --cors-allow-origins='*' --allow-iframe
```

The run.sh script handles:
- Virtual environment activation (must exist first)
- Python hash seed setting
- Directory navigation
- Gunicorn configuration (when specified)
- Environment-specific setup (Docker/Codespaces)

## Repository Structure
- `api/`: API endpoints and configurations
  - `api_logic_server_run.py`: Main server entry point
  - Endpoints defined in `api/expose_api_models.py`
- `database/`: Models and migrations
  - SQLAlchemy models in `database/models.py`
  - Migration scripts in `database/alembic/`
- `logic/`: Business rules in `logic/declare_logic.py`
- `ui/`: Web interface components
- `test/`: Test files
  - Run with: `python -m pytest test/`
- `security/`: Auth configuration in `security/authentication.py`
- `devops/`: Container and deployment configs
- `docs/`: Documentation
- `integration/`: Integration components
- `system/`: System configs and utilities

## API Endpoints:
Base URLs:
- http://localhost:50815/api (primary)
- http://localhost:58270/api (alternate)

Common endpoints:
- GET /api/docs: Swagger documentation
- GET /api/[resource]: List resources
- POST /api/[resource]: Create resource
- GET /api/[resource]/{id}: Get resource
- PATCH /api/[resource]/{id}: Update resource
- DELETE /api/[resource]/{id}: Delete resource

## Error Handling:
- HTTP 400: Bad Request - Invalid input
- HTTP 401: Unauthorized - Authentication required
- HTTP 403: Forbidden - Insufficient permissions
- HTTP 404: Not Found - Resource doesn't exist
- HTTP 500: Server Error - Check logs in `logs/`

## Development Guidelines:
1. Database Changes:
   - Add models to `database/models.py`
   - Generate migration: `alembic revision --autogenerate`
   - Apply migration: `alembic upgrade head`

2. Business Logic:
   - Add rules to `logic/declare_logic.py`
   - Use LogicBank decorators for constraints
   - Test rules with `test/test_logic.py`

3. API Changes:
   - Modify `api/expose_api_models.py`
   - Update Swagger docs
   - Test with `test/api_test.py`

## Testing:
- Unit tests: `python -m pytest test/unit/`
- API tests: `python -m pytest test/api/`
- Integration: `python -m pytest test/integration/`
- Coverage: `coverage run -m pytest && coverage report`

## Logging:
- Application logs: `logs/api_logic_server.log`
- Debug logs: `logs/debug.log`
- Error logs: `logs/error.log`
