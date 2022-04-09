"""Write a Python program to list the tables of given SQLite database file.  """ 
from multiprocessing import connection
import sqlite3
from sqlite3 import Error

from matplotlib.pyplot import connect

def Establish_Connection(database):
    
    connection = None
    
    try:
        connection = sqlite3.connect(database)
        cur = connection.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(cur.fetchall())
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

if __name__ == '__main__':
    root_dir = "D:\python_workarea\PythonPortfolio\Database\Sqlite\db"
    database_name = input("Please enter database name: ")
    Establish_Connection(root_dir+"\\"+database_name+".db")