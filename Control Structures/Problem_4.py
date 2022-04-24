"""
If the ages of Mark, David, and Tom are input by the user, write a program to determine the youngest of the three.
"""

mark_age = int(input("Hey Mark, Please enter your age: "))
david_age = int(input("Hey David, Please enter your age: "))
tom_age = int(input("Hey Tom, Please enter your age: "))

if (mark_age<david_age and mark_age<tom_age):
    print("Mark is the youngest!")
elif (david_age<mark_age and david_age<tom_age):
    print("David is the youngest!")
else:
    print("Tom is the youngest")
# ages = {mark_age:"Mark",david_age:"David",tom_age:"Tom"}

# print("The youngest one is: {}".format(ages[min(ages)]))