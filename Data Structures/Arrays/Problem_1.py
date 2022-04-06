"""
Twenty five numbers are entered from the keyboard into an array.
The number searched is entered through the keyboard by the user.
Write a program to find if the number to be searched is present in the array.
"""

arr = []

for i in range(5):
    
    arr.append(input("Please enter {} number: ".format(i+1)))
    
num = input("Please enter a number to search in array: ")

if num in arr:
    print("Number is in array!")
else:
    print("Number not found!")