import sqlite3

connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()
print(connection)
print(cur)

cur.execute("UPDATE first_table SET name = 'Dima' WHERE rowid=2;")

connection.commit()

connection.close()