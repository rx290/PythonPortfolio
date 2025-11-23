"""
Write a program that reads in the size of the side of a square then prints a  hollow square if that size out of asterisk and blanks
Your programm should work for squares of all side sizes between 1 to 20 for example a 5 size square

*****
*   *
*   *
*   *
*****
"""

size = int(input("Please enter the size of square: "))
spacer = size -2
for i in range(size):
    if i ==0:
        print("*"*size)
    elif i == size-1:
        print("*"*size)
    else:
        print("*"+" "*spacer+"*")