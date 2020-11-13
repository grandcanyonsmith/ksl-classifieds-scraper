from peewee import *
from urllib.parse import urlparse
import os


url = urlparse.urlparse(os.environ['DATABASE_URL'])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port


pg_db = PostgresqlDatabase(dbname, user=user, password=password,
                           host=host, port=port)


class Product(Model):

    title = CharField()
    price = CharField()
    views = CharField()
    favorites = CharField()
    seller_name = CharField()
    seller_phone = CharField()
    url = CharField()
    image_url = CharField()

    class Meta:
        database = pg_db


class Keyword(Model):
    item_name = CharField()
    minimum_price = CharField()
    maximum_price = CharField()

    class Meta:
        database = pg_db


# pg_db.connect()
# pg_db.create_tables([Product, Keyword])
# pg_db.close()


# print("Table Created...")
