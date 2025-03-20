from app.models.user import User


def run(migrator, migrate):
    # Create tables for initial models
    User.create_table()
