"""Write a Python program to create a SQLite database connection to a database that resides in the memory.  """ 
import sqlite3
from sqlite3 import Error


def Establish_Connection():
    """ This function is to establish a connection with the database of SQLite which resides in memory"""
    connection = None
    try:
        connection = sqlite3.connect(':memory:')
        #Checking the version of sqlite 
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()


if __name__ == '__main__':
    database_name = input("Please enter database name: ")
    Establish_Connection()