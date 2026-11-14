import sqlite3

connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()
print(connection)
print(cur)

cur.execute("INSERT INTO first_table (name) VALUES ('Vasya');")

connection.commit()

connection.close()