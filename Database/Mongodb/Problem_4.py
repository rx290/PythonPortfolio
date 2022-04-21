"""Write a Python program to find something in mongodb.  """ 
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Find All
for x in mycol.find():
  print(x)
  
# Find specific Record
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)
  
# Note
"""
You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field). 
If you specify a field with the value 0, all other fields get the value 1, and vice versa:
"""