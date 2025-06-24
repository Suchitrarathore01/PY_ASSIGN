import sqlite3


conn1= sqlite3.connect("db2.db")

conn1.execute(''' 
create table user_a(
usid INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(255),
pass VARCHAR(255),
mobile VARCHAR(255),  
email varchar(10)
             )''')
conn1.close()