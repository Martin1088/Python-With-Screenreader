## Probe mit Mysql Connector
import mysql.connector
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "",
	database = "lgb"
)
mycursor = mydb.cursor()
mycursor.execute("Select * From level01")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)