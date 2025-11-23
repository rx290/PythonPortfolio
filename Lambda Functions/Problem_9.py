"""
Write a Python program to check whether a given string is number or not using Lambda.
Sample Output:
True
True
False
True
False
True
Print checking numbers:
True
True
""" 
_str = input("Please enter a string; ")
int_checker = lambda x: print(True) if _str.isdigit() else print(False)
int_checker(_str)
