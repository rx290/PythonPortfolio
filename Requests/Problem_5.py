"""Write a Python code to send a request to a web page, and print the JSON value of the response. Also print each key value of the response.""" 
from wsgiref.simple_server import server_version
import requests

getter = requests.get("https://api.github.com")
server_response = getter.json()
print("Json response: ",server_response)
print("Following Url: ",server_response['following_url'])
print("User Url: ",server_response['user_url'])