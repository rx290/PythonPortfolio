"""Write a Python program to create a SQLi database and connect with the database and print the version of the SQLite database.  """ 

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")