"""
Write a Python program that multiply each number of given list with a given number using lambda function. Print the result.
Original list: [2, 4, 6, 9, 11]
Given number: 2
Result:
4 8 12 18 22
""" 
lst = [2, 4, 6, 9, 11]
num = int(input("Please enter a number: "))
multiplier = lambda x : x*num
mapper = list(map(multiplier,lst))
print(mapper)