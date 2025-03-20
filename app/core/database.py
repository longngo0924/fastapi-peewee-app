from peewee import PostgresqlDatabase
from app.core.config import settings

db = PostgresqlDatabase(
    database=settings.DATABASE_URL.split('/')[-1],
    user=settings.DATABASE_URL.split(':')[1].split('@')[0].split('//')[1],
    password=settings.DATABASE_URL.split(':')[2].split('@')[0],
    host=settings.DATABASE_URL.split('@')[1].split(':')[0],
    port=int(settings.DATABASE_URL.split(':')[-1].split('/')[0])
)
