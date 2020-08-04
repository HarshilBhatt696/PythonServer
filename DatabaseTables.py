import sqlite3


connection = sqlite3.connect('NewData.db')

cursor = connection.cursor()

createTable = "CREATE TABLE IF NOT EXISTS ford (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(createTable)

connection.commit()
connection.close()
