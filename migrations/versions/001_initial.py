from app.models.user import User


def run(db, migrate):
    # Create tables for initial models
    if not User.table_exists():
        User.create_table()
