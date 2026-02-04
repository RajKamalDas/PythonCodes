import mysql.connector as MC

db = MC.connect(host="localhost", database="MyThings", user="root", passwd="r.3.a.j.")

sql = "create table Table1(RollNo varchar(20), Name varchar(50), course varchar(5));"

cur = db.cursor()

cur.execute(sql)

db.close()