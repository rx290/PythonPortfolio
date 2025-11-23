"""
Write a temperature conversion program but with a menu.
"""

from os import system


print("We offer following conversions:\n1. Fahrenheit to Celsius Conversion\n2. Celsius to Fahrenheit Conversion\n3, Quit\n")

choice = int(input("Please enter your choice: "))

if choice == 3:
    exit()
elif choice ==2:
    celsius = float(input("Please enter temperature in Celsius: "))
    fahrenheit = (9/5 * celsius) + 32
    print("{} celsius is {} in fahrenheit.".format(celsius,fahrenheit))
elif choice == 1:
    fahrenheit = float(input("Please enter temperature in Fahrenheit: "))
    celsius = 5/9 * (fahrenheit - 32) 
    print("{} celsius is {} in fahrenheit.".format(celsius,fahrenheit))
else:
    print("Wrong choice entered!\nProgram is quitting!")
    exit()