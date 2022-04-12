"""Write a Python program to insert values to a table from user input. """ 
import sqlite3
from sqlite3 import Error


def Establish_Connection(database):
    """ create a database connection to a SQLite database """
    connection = None
    try:
        connection = sqlite3.connect(database)
        print(sqlite3.version)
        cur = connection.cursor()
        product = input("Please enter the product name: ")
        price = int(input("Please Enter the price of {}: ".format(product)))
        cur.execute('''
                    INSERT INTO products (product_name) VALUES ({})
                    '''.format(product))
        cur.execute('''
          INSERT INTO prices (price) VALUES ({})
          '''.format(price))
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