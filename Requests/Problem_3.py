"""Write a Python code to send a request to a web page, and print the response text and content. Also get the raw socket response from the server.""" 
import  requests
getter  = requests.get('https://api.github.com/events')
print("Status Code: ",getter.status_code)
print("Content: ",getter.content)
print("Raw socket response: ",getter.raw)
