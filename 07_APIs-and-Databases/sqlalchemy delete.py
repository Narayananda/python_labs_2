import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

newTable = sqlalchemy.Table('newTable', metadata, autoload_with=engine)

query = sqlalchemy.delete(newTable).where(newTable.columns.salary < 30000)
results = connection.execute(query)
connection.commit()
