"""If a four digit number is input through the keybard, write a program to obtain the sum of the first and last digit of this number"""

from os import wait


digit = input("Enter any 5 digits: ")
t_sum = 0

if (len(digit) > 4) or (len(digit)<4):
    print("Length of the digits entered are not 4, Program is terminating, please enter 4 digits next time!")
else:
    t_sum = int(digit[0]) + int(digit[-1])
    print("Sum of first and last digits is: {}".format(t_sum))
    
#revision 22nd Nov 2025
dig = input("Please enter your 5 digit number: ")
print("Thank you for entering 5 digit number!") if len(dig)==5 else print("Program Terminating as digit length was incorrect.",wait(2),quit())
ld= [int(x) for x in dig]
n_s = ld[0]+ld[-1]
print("sum of first and last digit is: ",n_s)
