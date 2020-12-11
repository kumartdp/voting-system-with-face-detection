import sqlite3

def insert(t):
    con=sqlite3.connect("mysql.db")
    obj=con.cursor()

    try:
        
        obj.execute("INSERT INTO facepoll (uid,name,address,status) VALUES (?,?,?,?)",t)
        print("try")
    except Error as e:
        print(e)
        print("error")
    obj.close()
    con.commit()
def insert1(t):
    con=sqlite3.connect("mysql.db")
    obj=con.cursor()
    enc=t[1]
    print(enc)
    for i in range(128):
        t1=(t[0],str(enc[i]))
        obj.execute("INSERT INTO faceid (uid,value) VALUES (?,?)",t1)
    obj.close()
    con.commit()   
def check(uid):
    con=sqlite3.connect("mysql.db")
    obj=con.cursor()
    obj.execute("select * from facepoll")
    row=obj.fetchall()
    for i in row:
        if(i[0]==uid):
            if(i[3]=="yes"):
                return True
            else:
                return False
    obj.close()
    con.commit()
 
con=sqlite3.connect("mysql.db")
obj=con.cursor()
obj.execute("PRAGMA table_info(faceid)")
print(obj.fetchall())
obj.execute("select * from facepoll")
row=obj.fetchall()
for i in row:
    print(i)

obj.execute("select * from faceid")
row=obj.fetchall()
for i in row:
    print(i)
obj.close()
con.commit()
