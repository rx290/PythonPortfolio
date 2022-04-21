"""Write a Python program to connect to firebase and perform basic crud using firebase_admin  """ 

# install firebase_admin
# pip install firebase_admin

import  firebase_admin
from firebase_admin import db
import json

# Pre-req
"""
1. Install firebase_admin via pip
2. Generate a new api key
	To generate a private key file for your service account:
		a. In the Firebase console, open Settings > Service Accounts.
		b. Click Generate New Private Key, then confirm by clicking Generate Key.
		c. Securely store the JSON file containing the key.
3. Some Sample data in json file
"""

sample_data = "D:\python_workarea\PythonPortfolio\Database\Firebase\Firebase_Admin\sample_data.json"

# Connection code
databaseURL = 'https://uberriderapp-ccb13-default-rtdb.firebaseio.com/'
cred_obj = firebase_admin.credentials.Certificate('D:\python_workarea\PythonPortfolio\Database\Firebase\Firebase_Admin\google-services.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':databaseURL
	})

# Writing to DB with set function
ref =db.reference('/')
with open(sample_data, "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)

# Writing to DB with push function
ref.set({
	"Books":
	{
		"Best_Sellers": -1
	}
})

ref = db.reference("/Books/Best_Sellers")
with open(sample_data, "r") as f:
	file_contents = json.load(f)

for key, value in file_contents.items():
	ref.push().set(value)
 
 
# Note
"""
These Functions push() and set() aren't atomic. 
"""

# Updating firebase DB

ref = db.reference("/Books/Best_Sellers/")

best_sellers = ref.get()
print(best_sellers)
for key, value in best_sellers.items():
	if(value["Author"] == "J.R.R. Tolkien"):
		value["Price"] = 80
		ref.child(key).update({"Price":120})
updated_best_seller = ref.get()
print("Updated Prices:\n",updated_best_seller)


# Fetching / Accessing data

"""
To use ordered list from firebase DB please add .indexOn in the sample_data.json
"""

# Get method for ordered dictionary 
print(ref.order_by_child("Price").get())

# Get method for fecthing maximum price
print("Most Expensive book: ",ref.order_by_child("Price").limit_to_last(1).get())

# Get method for fecthing min price
print("Most Cheap Book: ", ref.order_by_child("Price").limit_to_first(1).get())

# Get method for fecthing exact price
print("Book which is exactly 100: ",ref.order_by_child("Price").equal_to(100).get())


# Deleting Data from Firebase Database
ref = db.reference("/Books/Best_Sellers")

for key, value in best_sellers.items():
	if(value["Author"] == "J.R.R. Tolkien"):
		ref.child(key).set({})