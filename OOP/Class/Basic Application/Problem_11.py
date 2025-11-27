"""
Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
"""

from math import pi

class Circle:
    def __init__(self, radius):
        self.pi = pi
        self.radius = radius
        
    def diameter(self):
        return 2 * self.radius
    
    def area(self):
        return pi * (self.radius**2)
    
    def perimeter(self):
        return 2 * pi * self.radius
    
c = Circle(5)
print("The diameter of the circle is {}, the area of the circler is {}, the circumference of a circle is {}.".format(c.diameter(),c.area(),c.perimeter()))


