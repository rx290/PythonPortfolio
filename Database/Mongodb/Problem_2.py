"""Write a Python program to create a Collection inside of the MongoDB database and see if collection exist or not.""" 


import pymongo

db_client = pymongo.MongoClient("mongodb://localhost:27017/")
database = db_client["mydatabase"]

customer_column = database["customers"]

# Checking if the collection exist or not
collections_list = database.list_collection_names()
collection_name = input("Please enter the name for collection you want to search:")
if collection_name in collections_list:
  print("The {} collection exists.".format(collection_name))