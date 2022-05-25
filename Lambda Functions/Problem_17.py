"""
Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
Orginal list:
[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
Numbers of the above list divisible by nineteen or thirteen:
[19, 65, 57, 39, 152, 190]
""" 
from numpy import append


lst = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
divides = []
divides_finder = lambda x: divides.append(x) if x%13 ==0 or x%19 == 0 else print(x, "is not a divide")
list(map(divides_finder,lst))
print("List of divides are: ",divides)