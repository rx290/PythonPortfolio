"""Write a Python program to use diffrent types of joins. """ 

from getpass import getpass
from mysql.connector import connect, Error
connection = None
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="name of database")
    cur = connection.cursor()
    # Inner Join
    sql_statement_join = """SELECT users.name AS user, products.name AS favorite FROM users  INNER JOIN products ON users.fav = products.id"""
    cur.execute(sql_statement_join)
    print(cur.fetchall())

    # Right Join
    sql_statement_left_join = """SELECT users.name AS user, products.name AS favorite FROM users  Left JOIN products ON users.fav = products.id"""
    cur.execute(sql_statement_left_join)
    print(cur.fetchall())

    # Right Join
    sql_statement_right_join = """SELECT users.name AS user, products.name AS favorite FROM users  Right JOIN products ON users.fav = products.id"""
    cur.execute(sql_statement_right_join)
    print(cur.fetchall())

except Error as e:
    print(e)
    
finally:
    if connection:
        connection.close()