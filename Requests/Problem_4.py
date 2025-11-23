"""Write a Python code to send a request to a web page, and print the information of headers. Also parse these values and print key-value pairs holding various information. """ 
import  requests

getter = requests.get('https://api.github.com/events')
print("Headers: ",getter.headers)
print("Date: ",getter.headers['date'])
print("server: ",getter.headers['server'])