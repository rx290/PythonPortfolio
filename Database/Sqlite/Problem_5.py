"""Write a Python program to create a table and insert some records in that table. Finally selects all rows from the table and display the records. """ 
""" Write a Python program to connect a database and create a SQLite table within the database. """ 
import sqlite3
from sqlite3 import Error


def Establish_Connection(database):
    """ create a database connection to a SQLite database """
    connection = None
    try:
        connection = sqlite3.connect(database)
        print(sqlite3.version)
        cur = connection.cursor()
        cur.execute('''
                    INSERT INTO products (product_name) VALUES ("Olpers 1L")
                    ''')
        cur.execute('''
          INSERT INTO prices (price) VALUES (180)
          ''')
        cur.execute("Select * from products")
        print(cur.fetchall())
        cur.execute("SELECT * from prices")
        print(cur.fetchall())
        connection.commit()
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()


if __name__ == '__main__':
    root_dir = "D:\python_workarea\PythonPortfolio\Database\Sqlite\db"
    database_name = input("Please enter database name: ")
    Establish_Connection(root_dir+"\\"+database_name+".db")