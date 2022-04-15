""" Write a Python program to count the number of rows of a given SQLite table.""" 
import sqlite3 
from sqlite3 import Error
from sre_parse import State 

connection = None
root_dir = "D:\python_workarea\PythonPortfolio\Database\Sqlite\db"
database_name = input("Please enter database name: ")
try:
    connection = sqlite3.connect(root_dir+"\\"+database_name+'.db')
    cursor = connection.cursor()
    
    statement_exec = cursor.execute("SELECT count(*) FROM products;")
    print(statement_exec.fetchall())
    connection.commit()
except Error as e:
      print(e)
finally:
    if connection:
        connection.close()
 
