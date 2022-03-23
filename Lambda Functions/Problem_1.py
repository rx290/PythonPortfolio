""" 
Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
also create a lambda function that multiplies argument x with argument y and print the result.
Sample Output:
25
48
""" 
from audioop import add


adder = lambda a : a + 15
multiplier = lambda x,y : x*y

print(adder(15))
print(multiplier(20,400))