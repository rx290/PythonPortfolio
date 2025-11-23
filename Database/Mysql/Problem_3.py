""" Write a Python program to connect a database and create a table within the database. """ 

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
    cur.execute("CREATE TABLE Product (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price VARCHAR(255))")
    cur.execute("Show tables")
    # Printing tables
    for x in cur:
        print("Can't Create table {} as it already exists".format(x))
    else:
        print("{} table is created!".format(x))
    
except Error as e:
    print(e)
    
finally:
    if connection:
        connection.close()
    
    
