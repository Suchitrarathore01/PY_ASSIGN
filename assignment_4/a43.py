import sqlite3

conn1=sqlite3.connect("db2.db")

data=conn1.execute("Select * FROM user_a")
for x in data:
    print(x)
    
id=input("id to delete")
conn1.execute("DELETE FROM user_a where usid="+id)
conn1.commit()
data=conn1.execute("Select* FROM user_a ")
for x in data:
    print(x)

conn1.close()
