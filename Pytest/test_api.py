from urllib import response
import pytest
# import request for networking
import  requests
# import json for api data parsing
import  json


def main_url():
    x = "https://regress.in"
    return x

def test_login(main_url):
    url = main_url + "/api/login"
    data = {'email':'abc@xyz.com','password':'qwerty'}
    response = requests.get(main_url,data=data)
    token =json.loads(response.text)
    assert response.status_code == 404
    
test_login(main_url())