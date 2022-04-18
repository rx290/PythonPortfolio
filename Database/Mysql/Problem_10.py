"""Write a Python program to manipulate the output of the results. """ 

from getpass import getpass
from mysql.connector import connect, Error
connection = None
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="name of database")
    cur = connection.cursor()
    # Limiting the values and starting from 25th value
    sql_statement = "SELECT * FROM customers LIMIT 5 OFFSET 25"
    cur.execute(sql_statement)
    print(cur.fetchall())

    
except Error as e:
    print(e)
    
finally:
    if connection:
        connection.close()