"""Write a Python program to delete values. """ 
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Mountain 21" }

# To delete single Entry
mycol.delete_one(myquery)

# To delete multiple entry
multi_del_query = { "address": {"$regex": "^S"} }
x = mycol.delete_many(multi_del_query)
print(x.deleted_count, " documents deleted.")

# To delete everything

y = mycol.delete_many({})

print(y.deleted_count, " documents deleted.")