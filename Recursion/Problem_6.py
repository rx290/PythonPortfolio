"""
Write a Python program to get the sum of a non-negative integer.  
Test Data:
sumDigits(345) -> 12
sumDigits(45) -> 9
""" 
def sumDigits(_str:str):
    sum = 0
    length = 0
    if length != len(_str):
        sum = sum +int(_str[length])
        length = length +1
        return sum
        