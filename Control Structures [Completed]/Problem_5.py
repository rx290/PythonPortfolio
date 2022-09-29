"""
Write a program to check whether a triangle is valid or not, when the three angles of the triangle are entered by the user.
TheA triangle is valid if the sum of all the three angles is equal to 180 degrees
"""

angle_1=  float(input("Please enter first angle: "))
angle_2=  float(input("Please enter second angle: "))
angle_3 = float(input("Please enter third angle: "))

if (angle_1+angle_2+angle_3) == 180.00:
    print("It is a valid triangle!")
else:
    print("it is not a valid triangle")