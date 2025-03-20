from peewee import Model
from app.core.database import db


class BaseModel(Model):
    class Meta:
        database = db
