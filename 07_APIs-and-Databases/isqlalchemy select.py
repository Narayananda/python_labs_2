import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine("mysql+pymysql://root:password@localhost/sakila")
connection = engine.connect()
metadata = sqlalchemy.MetaData()

film = sqlalchemy.Table('film', metadata, autoload_with=engine)

query = sqlalchemy.select(film).where(film.c.title=="AFRICAN EGG")

result_proxy = connection.execute(query)

result = result_proxy.fetchall()

pprint(result)