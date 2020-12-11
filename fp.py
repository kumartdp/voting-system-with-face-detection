import sqlite3
con=sqlite3.connect("mysql.db")
obj=con.cursor()
obj.execute("select * from facepoll")
rows=obj.fetchone()
print(rows)
obj.execute("PRAGMA table_info(facepoll)")
print(obj.fetchall())
obj.close()
con.close()
    
