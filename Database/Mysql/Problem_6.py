"""Write a Python program to update a specific column value of a given table and prevents sql injection. """ 
from getpass import getpass
from unittest import result
from mysql.connector import connect, Error
connection = None
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="name of database")
    cur = connection.cursor()
    # escaping user entered values with %S
    sql_statement = "SELECT * FROM customers WHERE address = %s "
    address = ("some value",)
    cur.execute(sql_statement,address)
    results = cur.fetchall()
    print("records are as follows:\n")
    for x in results: print (x)

except Error as e:
    print(e)
    
finally:
    if connection:
        connection.close()
    