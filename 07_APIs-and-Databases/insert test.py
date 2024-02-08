import sqlalchemy as db

engine = db.create_engine('mysql+pymysql://root:password@localhost/python')
connection = engine.connect()
metadata = db.MetaData()
Table = db.Table('files_on_desktop', metadata, autoload_with=engine)

query = db.select(Table.columns.name)
result_proxy = connection.execute(query)
result = result_proxy.fetchall()


# insert = db.insert(Table).values(name= 'John')
# result_proxy = connection.execute(insert)
# connection.commit()


files_on_desk = db.Table('files_on_desktop', metadata, autoload_with=engine)

query = db.delete(files_on_desk).where(files_on_desk.columns.name == 'John')
results = connection.execute(query)
connection.commit()