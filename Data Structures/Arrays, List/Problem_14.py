"""
Check if the string is palindrome or not!
"""
_str = input("enter some string: ")
if _str == _str[::-1]:
    print("string is palindrome!")
else:
    print("string is not palindrome!")