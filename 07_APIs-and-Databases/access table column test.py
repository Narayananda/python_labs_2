from pathlib import Path
import sqlalchemy as db


engine = db.create_engine('mysql+pymysql://root:Tattvamasi&108@localhost/python')
connection = engine.connect()
metadata = db.MetaData()
Table = db.Table('files_on_desktop', metadata, autoload_with=engine)


# for name in Table.columns.name:
#     print(name)

query = db.select(Table.columns.name)
result_proxy = connection.execute(query)
result = result_proxy.fetchall()
print(type(result))
