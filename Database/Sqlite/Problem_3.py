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
          CREATE TABLE IF NOT EXISTS products
          ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
          ''')
        cur.execute('''
          CREATE TABLE IF NOT EXISTS prices
          ([product_id] INTEGER PRIMARY KEY, [price] INTEGER)
          ''')
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