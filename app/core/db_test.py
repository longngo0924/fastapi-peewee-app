from peewee import SqliteDatabase

# Create an in-memory SQLite database for testing
test_db = SqliteDatabase(':memory:') 