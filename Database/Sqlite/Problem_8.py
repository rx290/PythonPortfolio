""" Write a Python program to count the number of rows of a given SQLite table.""" 
import sqlite3 
from sqlite3 import Error
from sre_parse import State 

connection = None
database_name = input("Please enter database name: ")
try:
    connection = sqlite3.connect(database_name+'.db')
    cursor = connection.cursor()
    
    statement_exec = cursor.execute('select count( * ) From products;')
    print(statement_exec)
except Error as e:
      print(e)
finally:
    if connection:
        connection.close()
 
