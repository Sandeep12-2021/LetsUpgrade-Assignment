import mysql.connector as sqlcon

# creating a database 
db= sqlcon.connect(host="localhost",user="root",passwd="system")

cur = db.cursor()

cur.execute("CREATE DATABASE essentials")
