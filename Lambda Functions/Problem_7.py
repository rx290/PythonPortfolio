"""
Write a Python program to find if a given string starts with a given character using Lambda.
Sample Output:
True
False
""" 
_str = "Some String"
char_finder = lambda x: True if x == _str[0] else False
char = input("Please input a character to match first element of the string: ")
print(char_finder(char))