"""
Take an input of nuMbers from the user and read those numbers individually and convert them as intergers.
Then display their sum, subtraction and multiplication.
"""

from re import sub


numbers= input("Please enter your desired numbers so that arithmetic operations can be applied on them: ")

sum =0
multiplication = 1
subtraction = 0
for i in range(len(numbers)):
    sum = sum + int(numbers[i])
    multiplication = multiplication * int(numbers[i])
    if i == 0:
        subtraction = subtraction + int(numbers[i])
    else:
        subtraction = subtraction - int(numbers[i])
    
print("Sum: {}\nMultiplication: {}\nSubtraction: {}".format(sum,multiplication,subtraction))