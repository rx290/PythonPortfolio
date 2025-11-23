"""Write a Python code to verify the SSL certificate for a website which is certified.""" 

import requests   
# Making a get request 
response = requests.get('https://rigaux.org/', verify=False)
print(response) 

#Requests verifies SSL certificates for HTTPS requests, just like a web browser.
response1 = requests.get('https://google.com/')
print(response1)

#Requests ignore verifying the SSL certificate if you set verify to True (Default value)
response1 = requests.get('https://rigaux.org/', verify=True)
print(response1) 