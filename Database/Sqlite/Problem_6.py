""" Write a Python program to insert a list of records into a given SQLite table.""" 
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
          INSERT INTO products (product_name)

                VALUES
                ('Olpers 1.5L'),
                ('Olpers Cream'),
                ('Bunnys Rusk'),
                ('Bunnys Rusk Large'),
                ('Bunnys Bread Small')
          ''')
        cur.execute('''
          INSERT INTO prices (price)

                VALUES
                (240),
                (160),
                (80),
                (140),
                (85)
          ''')
        # cur.execute("Select * from products")
        # print(cur.fetchall())
        # cur.execute("SELECT * from prices")
        cur.execute('''
          SELECT
          a.product_name,
          b.price
          FROM products a
          LEFT JOIN prices b ON a.product_id = b.product_id
          ''')
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