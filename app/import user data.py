import sqlite3

conn = sqlite3.connect('Database.db')

c = conn.cursor()

user_data =[
    ('TestAdmin','Password123','tester','NULL','NULL','NULL',True,False,True),
    ('TestUser1','Password123','tester','NULL','NULL','NULL',False,False,True),
	('TestUser2','Password123','tester','NULL','NULL','NULL',False,True,False),
	('TestUser3','Password123','tester','NULL','NULL','NULL',False,True,True),
	('TestUser4','Password123','tester','NULL','NULL','NULL',False,False,False),
]

c.executemany("INSERT INTO Users VALUES (?,?,?,?,?,?,?,?,?)", user_data)

conn.commit()
conn.close()