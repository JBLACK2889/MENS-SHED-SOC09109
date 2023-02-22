import sqlite3

PRAGMA foreign_keys = ON;

connection = sqlite3.connect('database.db')


with open('CreationDataBase.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

connection.commit()
connection.close()