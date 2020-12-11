import sqlite3
def insert(t):
    

    con=sqlite3.connect("mysql.db")
    obj=con.cursor()


    
    obj.execute("insert into online1 values(?,?,?,?)",t)
    obj.execute("select *from online1")
    row=obj.fetchall()
    print(row)
  

    con.commit()
def check(uid):

    con=sqlite3.connect("mysql.db")
    obj=con.cursor()
    obj.execute("select * from online ")
    row1=obj.fetchall()
    for i in row1:
        if(i[2]==uid):
            return i[9]
    

con=sqlite3.connect("mysql.db")


obj=con.cursor()
obj.execute("select * from online ")
row1=obj.fetchall()
print(row1)
obj.execute("create table online1(uid TEXT(20),name TEXT(20),address TEXT(20),status TEXT(20))")
obj.execute("PRAGMA table_info(online1)")
print(obj.fetchall())
obj.execute("select * from online1 ")
row1=obj.fetchall()
print(row1)
