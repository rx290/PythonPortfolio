"""Write a Python code to send some sort of data in the URL's query string. """ 
import requests
payload = {'key1': 'value1', 'key2': 'value2'}

creator = requests.post("https://httpbin.org/post", data=payload)
print(creator.text)