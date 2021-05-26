import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="localhost",passwd="")
mycursor=mydb.cursor()
mycursor.execute("show database")
for i in mycursor:
    print(i)
