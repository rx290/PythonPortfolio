"""
A certain grade of steel is graded accordning to the following conditions:

i.   Hardness must be greater than 50
ii.  Carbon content must be less than 0.7
iii. Tensile strength must be greater than 5600

The grades are as follows:

Grade is 10 if all three conditions are met.
Grade is 9 if conditions (i) and (ii) are met.
Grade is 8 if conditions (ii) are (iii) met.
Grade is 7 if conditions (i) are (iii) met.
Grade is 6 if only one conditions met.
Grade is 5 if conditions are not met.

write a program for grading of steel
"""

hardness = int(input("Please Enter the Hardness of steel: "))
carbon_content = float(input("Please Enter the Carbon content of steel: "))
tensile_strength = int(input("Please Enter the Tensile strength of steel: "))

if hardness == 10 and carbon_content < 0.7 and tensile_strength > 5600:
    print("Steel is of grade 10!")
elif (hardness == 10 and carbon_content <0.7):
    print("Steel is of grade 9!")
elif (carbon_content <0.7 and tensile_strength > 5600):
    print("Steel is of grade 8!")
elif (hardness == 10 and tensile_strength > 5600):
    print("Steel is of grade 7!")
elif (hardness == 10 or carbon_content < 0.7 or tensile_strength > 5600):
    print("Steel is of grade 6!")
else:
    print("Steel is of grade 5")