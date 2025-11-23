"""Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9). """ 
import re

some_str ='rx290 is cool'
string_checker = re.compile(r'[^a-zA-Z0-9]')
_Str= string_checker.search(some_str)

print(_Str)