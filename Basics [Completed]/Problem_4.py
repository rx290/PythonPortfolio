"""If a five digit number is input through the keyboard, write a program to calculate the sum of those digits"""

from os import system


digit = input("Enter any 5 digits: ")
t_sum = 0

if (len(digit) > 5) or (len(digit)<5):
    print("Length of the digits entered are not 5, Program is terminating, please enter 5 digits next time!")
else:
    for i in range(len(digit)):
        t_sum = t_sum + int(digit[i])
    print("Total sum of digits is: {}".format(t_sum))
    
# Revision 21st Nov, 2026
five_digit_num = input("Please enter 5 digit number: ")
print("Thank you for entering a five digit number!") if len(five_digit_num)==5 else print("Program is terminating because entered number is not 5 digit.",quit())
nl = [float(x) for x in five_digit_num ]
total = sum(nl)
print("Total sum of 5 digits is: ",total)

