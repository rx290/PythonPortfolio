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

# Connection code
databaseURL = 'https://uberriderapp-ccb13-default-rtdb.firebaseio.com/'
cred_obj = firebase_admin.credentials.Certificate('D:\python_workarea\PythonPortfolio\Database\Firebase\Firebase_Admin\google-services.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':databaseURL
	})

# Writing to DB with set function
ref =db.reference('/')
with open("D:\python_workarea\PythonPortfolio\Database\Firebase\Firebase_Admin\sample_data.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)

#