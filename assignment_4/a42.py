import sqlite3
conn1=sqlite3.connect("db2.db")

conn1.execute('''
INSERT INTO user_a(name,pass1) VALUES("aaa","abc876"),("bbb","abc876"),("ccc","abc876")
            
             ''')
conn1.commit()
conn1.close()