import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="ucantseeme", database="hotelmanagementsystem")
cur = mydb.cursor()