""" Write a Python code to send a request to a web page and stop waiting for a response after a given number of seconds. In the event of times out of request, raise Timeout exception. """ 
import requests

_timeout = float(input("Please enter timeout duration: "))
try:
    getter = requests.get('https://github.com/events', timeout = _timeout)
    print(getter.text)
except requests.exceptions.RequestException as e:
    print(e)    