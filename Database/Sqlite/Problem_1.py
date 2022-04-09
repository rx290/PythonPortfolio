"""Write a Python program to create a SQLite database and connect with the database and print the version of the SQLite database.  """ 
import sqlite3
from sqlite3 import Error


def Establish_Connection(database):
    """ This function is to establish a connection with the database of SQLite """
    conn = None
    try:
        conn = sqlite3.connect(database)
        #Checking the version of sqlite 
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    database_name = input("Please enter database name: ")
    Establish_Connection(database_name+".db")