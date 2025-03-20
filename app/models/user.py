from peewee import CharField, AutoField
from .base import BaseModel


class User(BaseModel):
    id = AutoField()
    email = CharField(unique=True, index=True)
    hashed_password = CharField()

    class Meta:
        table_name = "users"
