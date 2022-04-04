"""Two numbers are input through the keyboard into two locations C and D. Write a program to interchange the contents of C and D"""

c = int(input("Please enter first number: "))
d= int(input("Please enter second number: "))

print("Before shuffling value of c is {} and value of d is {}.".format(c,d))
c , d = d , c
print("After shuffling value of c is {} and value of d is {}.".format(c,d))