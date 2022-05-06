import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="employees"
)

mycursor = mydb.cursor()

sql = "INSERT INTO emp (name,age,salary,desig) VALUES (%s, %s,%s,%s)"
val = ("John", "35","50000","Clerk")

mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
