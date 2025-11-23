"""Write a Python program to Display everthing in ascending and decending orders. """ 
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
    # Ordering names alphabetically
    sql_statement = "SELECT * FROM customers ORDER BY name"
    cur.execute(sql_statement)
    results = cur.fetchall()
    # Ordering names in decending order
    sql_statement = "SELECT * FROM customers ORDER BY name DESC"
    desc_results = cur.fetchall()
    print("Names in Alphabeticall Order are as folloews: ", results)
    print("Names in Alphabetically decending order: ",desc_results)
    


except Error as e:
    print(e)
    
finally:
    if connection:
        connection.close()
    