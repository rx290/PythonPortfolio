"""You can convert temperature from degree celsius to degree fahrenheit by multiplying
by 9/5 and adding 32. write a program that takes users input in float representing Celsius and
then convert it and display the corresponding degree in Fahrenheit"""

celsius = float(input("Please enter temperature in Celsius: "))

fahrenheit = (9/5 * celsius) + 32

print("{} celsius is {} in fahrenheit.".format(celsius,fahrenheit))