"""If a five digit number is input through the keyboard write a program to reverse the number"""


from string import digits


digit = input("Input any 5 digit number: ")

if len(digit) > 5 or len(digit)<5:
    print ("Please enter a digit of length 5. Program is exiting")
else:
    print(digit[::-1])