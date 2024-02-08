import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

newTable = sqlalchemy.Table('newTable',metadata, autoload_with=engine)

query = sqlalchemy.insert(newTable)
new_records = [{'Id':'2','name':'record1','salary':20000, 'active':False},{'Id':'3', 'name':'FRILL', 'salary':50000, 'active':True}]

sqlalchemy.insert(newTable).values(Id=1, name = "PAT", salary = 40000, active=True)
result_proxy = connection.execute(query,new_records)
connection.commit()