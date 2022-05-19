from peewee import PostgresqlDatabase
from .models import User, VpnConf, BaseModel, database


# class DB:
#     pg_db: PostgresqlDatabase
#
#     def __init__(self):
#         try:
#             self.pg_db = db
#         except Exception as e:
#             print(e)
#
#     # def create_tables(self):
#     #     User.create()
#     #     VpnConf.create()
