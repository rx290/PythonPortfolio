"""Write a Python program to update a specific column value of a given table and select all rows before and after updating the said table. """ 
import  sqlite3
from sqlite3 import Error

connection= None
root_dir = "D:\python_workarea\PythonPortfolio\Database\Sqlite\db"
database = input("Please enter the name of database you want to connect: ")

try:
    connection = sqlite3.connect(root_dir + "//"+database + '.db')
    cursor = connection.cursor()
    cursor.execute("select * from prices")
    print("Prices before update: ",cursor.fetchall())
    connection.commit()
    cursor.execute("update prices set price = 180 where product_id = 3; ")
    cursor.execute("select * from prices")
    print("Print Prices after update: ",cursor.fetchall())
    connection.commit()
    
except Error as e:
    print(e)
finally:
    if connection:
        connection.close()