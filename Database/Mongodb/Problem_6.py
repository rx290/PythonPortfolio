""" Write a Python program to perform sorting on mongo db.""" 
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydoc_asc = mycol.find().sort("name")
mydoc_des = mycol.find().sort("name",-1)

for x in mydoc_asc:
  print(x)
  
for y in mydoc_des:
    print(y)