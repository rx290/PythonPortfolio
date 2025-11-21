"""
Write a program that converts a string to an int using array/list
"""
entered_string = input("please enter a string of numbers: ")
ls = list(map(int,entered_string))
print("Your entered number string was: ",entered_string,"\nYour converted list is: ",ls)