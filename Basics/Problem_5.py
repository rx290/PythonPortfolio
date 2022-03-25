"""If a four digit number is input through the keybard, write a program to obtain the sum of the first and last digit of this number"""

digit = input("Enter any 5 digits: ")
sum = 0

if (len(digit) > 4) or (len(digit)<4):
    print("Length of the digits entered are not 4, Program is terminating, please enter 4 digits next time!")
else:
    sum = int(digit[0]) + int(digit[-1])
    print("Sum of first and last digits is: {}".format(sum))