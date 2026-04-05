from peewee import CharField

from app.database import BaseModel


class Link(BaseModel):
    original_url = CharField()
    short_code = CharField()