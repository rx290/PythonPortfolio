"""Write a Python program to delete a specific value and prevent sql injection""" 
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
    # escaping user entered values with %S
    sql_statement = "DELETE FROM customers WHERE address = %s"
    address = ("some value",)
    cur.execute(sql_statement,address)
    # commit is important without it there would be no change
    cur.commit()
    print("record(s) are deleted!")
    
except Error as e:
    print(e)
    
finally:
    if connection:
        connection.close()
    