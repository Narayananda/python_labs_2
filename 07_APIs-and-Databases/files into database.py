from pathlib import Path
import sqlalchemy as db

current_location = Path("C:\\users\\lucas\\Desktop")

# dict_files = {}

# # Filter for different extentions eg: .py .txt .jpg etc...
# for file in current_location.iterdir():
#     if file.suffix not in dict_files.keys():
#         dict_files[file.suffix] = 1
#     else:
#          dict_files[file.suffix] += 1

engine = db.create_engine('mysql+pymysql://root:password@localhost/python')
connection = engine.connect()
metadata = db.MetaData()
Table = db.Table('files_on_desktop', metadata, autoload_with=engine)

query = db.select(Table.columns.name)
result_proxy = connection.execute(query)
results = result_proxy.fetchall()



for file in current_location.iterdir():
    if tuple([file.suffix]) in results:
        query = db.select(Table.columns.number_of_files).where(Table.columns.name ==f'{file.suffix}')
        result_proxy = connection.execute(query)
        result = result_proxy.fetchall()
        result1 = int(str(result)[3:-4])+1
        print(file.suffix)

        # update = db.update(Table).values(number_of_files=result1).where(Table.columns.name ==f'{file.suffix}')
        # result_proxy = connection.execute(update)
        # connection.commit()
    else:
        print('no')
        # insert = db.insert(Table).values(name= f'{file.suffix}',number_of_files=1)
        # result_proxy = connection.execute(insert)
        # connection.commit()

query = db.select(Table.columns.name,Table.columns.number_of_files,)
result_proxy = connection.execute(query)
result = result_proxy.fetchall()

print(result)


