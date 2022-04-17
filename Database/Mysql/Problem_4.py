"""Write a Python program to list the tables of given MySql database file.  """ 

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
    cur.execute("Show tables")
    # Printing tables
    for x in cur:
        print(x)
    
except Error as e:
    print(e)
    
finally:
    if connection:
        connection.close()
    