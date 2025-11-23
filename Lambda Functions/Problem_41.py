"""
Write a Python program to reverse strings in a given list of string values using lambda.  
Original lists:
['Red', 'Green', 'Blue', 'White', 'Black']
Reverse strings of the said given list:
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

""" 
lst = ['Red', 'Green', 'Blue', 'White', 'Black']
reverser = lambda x: x[::-1]
print(list(map(reverser,lst)))