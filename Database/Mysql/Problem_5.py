"""Write a Python program to create a table and insert some records in that table. Finally selects all rows from the table and display the records. """ 
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
    sql_statement = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    values = [
        ('Peter', 'Lowstreet 4'),
        ('Amy', 'Apple st 652'),
        ('Hannah', 'Mountain 21'),
        ('Michael', 'Valley 345'),
        ('Sandy', 'Ocean blvd 2'),
        ('Betty', 'Green Grass 1'),
        ('Richard', 'Sky st 331'),
        ('Susan', 'One way 98'),
        ('Vicky', 'Yellow Garden 2'),
        ('Ben', 'Park Lane 38'),
        ('William', 'Central st 954'),
        ('Chuck', 'Main Road 989'),
        ('Viola', 'Sideway 1633')]
    cur.executemany(sql_statement, values)
    #saving the sate of database after data transaction
    cur.commit()
    #Returning row count for inserted rows
    print("Number of rows that were inserted: ",cur.rowcount)
    #Selecting and printing all rows
    cur.execute("Select * from customers")
    results = cur.fetchall()
    print("records are as follows:\n",results)

except Error as e:
    print(e)
    
finally:
    if connection:
        connection.close()
    
    
