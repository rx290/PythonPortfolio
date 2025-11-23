"""Write a Python code to check the status code issued by a server in response to a client's request made to the server. 
Print all of the methods and attributes available to objects on successful request.""" 
import  requests
getter  = requests.get('https://api.github.com/events')
print("Status Code: ",getter.status_code)
print("All Methods: ",dir(getter))


"""
Types of requests
    getter  = requests.get('https://api.github.com/events')
    Creator = requests.post("https://httpbin.org/post", data=payload)
    Editor = requests.put('https://httpbin.org/put', data={'key': 'value'})
    Eliminator = requests.delete('https://httpbin.org/delete')
    Essentials = requests.head('https://httpbin.org/get')
    Options = requests.options('https://httpbin.org/get')

Code:
    1xx informational response: the request was received, continuing process
    2xx successful: the request was successfully received, understood, and accepted
    3xx redirection: further action needs to be taken in order to complete the request
    4xx client error: the request contains bad syntax or cannot be fulfilled
    5xx server error: the server failed to fulfil an apparently valid request
    
Most Used Examples:

    200:    Read or okay
    201:    Created or posted
    301:    Moved Permanently
    400:    Bad Request
    401:    Unauthorized
    404:    Not Found
    500:    Internal Server error
    501:    Not Implemented
    502:    Bad Gateway    
    503:    Service Unavailable

"""