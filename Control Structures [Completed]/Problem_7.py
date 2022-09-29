"""
Any year is input by the user.
Write a program to determine whether the year is a leap or not!
"""
year = int(input("Please enter any year: "))
if year % 10 == 0:
    if year % 400 ==0:
        print("Leap year!")
    else:
        print("Regular year!")
else:
    if year % 4 == 0:
        print("Leap year!")
    else:
        print("Regular year!")  