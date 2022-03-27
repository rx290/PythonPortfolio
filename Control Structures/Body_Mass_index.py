"""The Formulas for calculating, BMI is,C
BMI = W_in_pounds * 703 / (h_in_inc x h_in_inc)

BMI calc check:
Underweight     18.5 or less
Normal          18.5 to 24.9
Overweight      25 tp 29.9
Obese           30 or greater
"""

def Kilo_converstion():
    weight_in_kilos = float(input("Enter your weight is kilos: "))
    weight_in_pounds = weight_in_kilos * 2.205
    return weight_in_pounds
    
def feet_to_inches():
    feet = float(input("Please enter your height in feet (eg. 5.9 feet): "))
    inches = feet * 12
    return inches
    
def feet_to_centimeter(feet):
    centimeter = feet * 30.48
    return centimeter

def BMI():
    x = input("Do you have your weight in pounds? (yes/no): ")
    y = input("Do you have your height in feet? (yes/no): ")
    weight = float(input("Please enter your weight in pounds: ")) if x=="yes" else Kilo_converstion()
    height = float(input("Please enter your weight in inches: ")) if x=="yes" else feet_to_inches()
    
    bmi = ( weight * 703 ) / (height * height)
    
    if bmi < 18.5:
        print("You're underweight! Eat something will ya?")
    elif bmi > 18.5 and bmi < 24.9:
        print("You're normal!")
    elif bmi > 25 and bmi < 30:
        print("You're overweight! Get a grip!")
    else:
        print("You're Obese, Shred some weight bruh!")