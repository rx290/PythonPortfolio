"""Write a Python program to create/connect to a MongoDB database, check all the databases and check if the desired database exist or not.""" 

import pymongo

# Initiating a client for mongo db
db_client = pymongo.MongoClient("mongodb://localhost:27017/")

# Connecting to or creating new database
database = db_client["Name of the database here!"]

# Displaying all databases
print(db_client.list_database_names())

# Checking if the database exist or not
databases = db_client.list_database_names()
db_name = input("Please enter the name for database you want to connect:")
if db_name in databases:
  print("The {} database exists.".format(db_name))
