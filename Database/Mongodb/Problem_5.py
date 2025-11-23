"""Write a Python program to use queries in mongo db. """ 
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#Simple Query
myquery = { "address": "Park Lane 38" }

#Advance Query
# parts of the query "MOdifier here":"value here"
advquery = { "address": { "$gt": "S" } }

# Regex based query
# parts of the query "regex modified":"regex"
requery = { "address": { "$regex": "^S" } }

mysimpledoc = mycol.find(myquery)
myadvdoc = mycol.find(advquery)
myredoc = mycol.find(requery)

for x in mysimpledoc:
  print(x)
  
for y in myadvdoc:
    print(y)
    
for z in myredoc:
    print(z)