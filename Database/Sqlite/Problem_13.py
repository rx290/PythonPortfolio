"""Write a Python program to create a backup of a SQLite database. """ 
import sqlite3


root_dir = "D:\python_workarea\PythonPortfolio\Database\Sqlite\db"
database = input("Please enter the name of database you want to connect: ")

def progress(status, remaining, total):
    print(f'Copied {total - remaining} of {total} pages...')

try:
    # existing DB
    sqliteCon = sqlite3.connect(root_dir+"\\"+database+'.db')
    # copy into this DB
    backupCon = sqlite3.connect('Sqlite_backup.db')
    with backupCon:
        sqliteCon.backup(backupCon, pages=3, progress=progress)
    print("backup successful")
except sqlite3.Error as error:
    print("Error while taking backup: ", error)
finally:
    if backupCon:
        backupCon.close()
        sqliteCon.close()