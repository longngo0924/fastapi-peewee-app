import pytest
import importlib
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import these here to control when they are loaded
import app.core.database
from app.main import app as fastapi_app
from app.models.user import User
from app.core.db_test import test_db
from fastapi.testclient import TestClient

# Find migration files
MIGRATION_DIR = Path(__file__).parent.parent / "migrations" / "versions"


@pytest.fixture(scope="module")
def client():
    # Save the original database
    original_db = app.core.database.db

    # Replace the real database with our test database
    app.core.database.db = test_db

    # Connect to the test database
    if test_db.is_closed():
        test_db.connect()

    # Create tables for all models
    test_db.create_tables([User])

    # Apply migrations if needed
    for migration_file in sorted(os.listdir(MIGRATION_DIR)):
        if migration_file.endswith('.py') and not migration_file.startswith('__'):
            version = migration_file.replace('.py', '')
            module_name = f"migrations.versions.{version}"
            try:
                migration_module = importlib.import_module(module_name)
                if hasattr(migration_module, "run"):
                    print(f"Running migration: {version}")
                    migration_module.run(test_db, None)
            except Exception as e:
                print(f"Error running migration {version}: {e}")

    # Create a test client
    with TestClient(fastapi_app) as c:
        yield c

    # Cleanup
    test_db.drop_tables([User])
    test_db.close()

    # Restore the original database
    app.core.database.db = original_db
