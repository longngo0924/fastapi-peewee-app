import sys
from pathlib import Path
import importlib

# Add the project root directory to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from playhouse.migrate import PostgresqlMigrator, migrate
from app.core.database import db

MIGRATION_DIR = Path(__file__).parent / "versions"


def run_migration(version: str):
    migration_file = MIGRATION_DIR / f"{version}.py"
    if not migration_file.exists():
        print(f"Migration script {migration_file} not found.")
        sys.exit(1)

    module_name = f"migrations.versions.{version}"
    migration_module = importlib.import_module(module_name)

    with db:
        migrator = PostgresqlMigrator(db)
        migration_module.run(migrator, migrate)
        print(f"Migration {version} applied successfully!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python migrate.py <migration_version>")
        sys.exit(1)

    migration_version = sys.argv[1]
    run_migration(migration_version)
