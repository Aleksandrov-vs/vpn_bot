from peewee import *
import os

DATABASE_NAME = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")


database = PostgresqlDatabase(DATABASE_NAME, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT)


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    telegram_id = BigIntegerField(unique=True, primary_key=True)
    chat_id = BigIntegerField(unique=True)
    name = CharField(max_length=300, null=False)
    permission = CharField(max_length=30, default="user")
    has_vpn_conf = BooleanField(default=False)


class VpnConf(BaseModel):
    id = AutoField(primary_key=True)
    path = TextField(null=False)


def create_tables():
    with database:
        database.create_tables([User, VpnConf])
        return database.connect()
