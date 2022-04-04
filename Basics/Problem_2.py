"""The length & the breadth of a rectangle and radius of a circle are input through the keyboard.
Write a program to calculate the area & perimeter of the rectangle and the area & circumference of the circle"""

from math import pi


length = float(input("Please enter the length of the rectangle: "))
breadth = float(input("Please enter the breadth of the rectangle: "))
radius = float(input("Please enter the radius of the circle:"))

area = length * breadth
perimeter= 2*(length+breadth)

circumference = 2 * pi * radius

print("Area of the rectangle is {} and it's perimeter is {}.\nCircumference of the circle is {:.2f}".format(area,perimeter,circumference))