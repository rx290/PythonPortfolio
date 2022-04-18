"""Write a Python program that checks a table and if it exists it first update some value and then drops the entire table. """ 

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
    # Updating the table
    sql_statement = "UPDATE customers SET address = %s WHERE address = %s"
    values = ("Valley 345", "Canyon 123")
    cur.execute(sql_statement,values)
    cur.commit()
    # Droping the table
    sql_statement = "DROP TABLE IF EXISTS %s"
    table_name = ("some value",)
    cur.execute(sql_statement,table_name)
    print("Table is dropped!")
    
except Error as e:
    print(e)
    
finally:
    if connection:
        connection.close()