"""Write a Python code to send cookies to a given server and access cookies from the response of a server.""" 
import requests
# Url to hit
url = 'https://httpbin.org/cookies'
# Creating a custom cookie
_cookies = dict(custom_cookie='This is a custom cookie which says cookies are working!')
# Getting back cookies from server
getter = requests.get(url, cookies=_cookies)
print(getter.text)




# returning cookies
#Cookies are returned in a RequestsCookieJar, which acts like a dict but also offers a more complete interface, suitable for use over multiple domains or paths.
jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'https://httpbin.org/cookies'
getter = requests.get(url, cookies=jar)
print(getter.text)