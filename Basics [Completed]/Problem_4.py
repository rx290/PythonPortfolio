"""If a five digit number is input through the keyboard, write a program to calculate the sum of those digits"""

digit = input("Enter any 5 digits: ")
sum = 0

if (len(digit) > 5) or (len(digit)<5):
    print("Length of the digits entered are not 5, Program is terminating, please enter 5 digits next time!")
else:
    for i in range(len(digit)):
        sum = sum + int(digit[i])
    print("Total sum of digits is: {}".format(sum))