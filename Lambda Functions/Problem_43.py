"""
Write a Python program to multiply all the numbers in a given list using lambda.  
Original list:
[4, 3, 2, 2, -1, 18]
Mmultiply all the numbers of the said list: -864
Original list:
[2, 4, 8, 8, 3, 2, 9]
Mmultiply all the numbers of the said list: 27648
""" 
import math


lst = [4, 3, 2, 2, -1, 18]
multiplier = lambda x: math.prod(lst)
print(multiplier(lst))