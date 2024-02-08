import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

newTable = sqlalchemy.Table('newTable',metadata, autoload_with=engine)

query = sqlalchemy.update(newTable).values(salary=1000000.00).where(newTable.columns.name == 'FRILL')

result_proxy = connection.execute(query)
connection.commit()
