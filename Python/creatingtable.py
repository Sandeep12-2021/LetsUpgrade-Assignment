import mysql.connector as sqlcon

db = sqlcon.connect(host="localhost",user="root",passwd="system",database="essentials")

cur = db.cursor()

cur.execute("CREATE TABLE student(roll int,sname varchar(30), mark int)")

cur.execute("insert into student values(101,'Varun',87)")
cur.execute("insert into student values(102,'Arun',92)")

cur.execute("select * from student;")

for i in cur:
    print(i)



cur.execute("update student set mark = 89 where sname = 'Varun'")
cur.execute("select * from student")

for i in cur:
	print(i)
