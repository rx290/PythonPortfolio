import time

print("Welcome to BMI Calculator.")
height_in_meter = height_in_inches = 0.0, 0.0 
weight_in_kg = weight_in_lbs = 0.0, 0.0
constant = 703

def bmi_calc(rounded_bmi):
    if  rounded_bmi< 18.5:
        print("Your bmi is {bmi} you're underweight.".format(bmi=rounded_bmi))
    elif  rounded_bmi> 18.5 and rounded_bmi < 25:
        print("Your bmi is {bmi} you have a normal weight.".format(bmi=rounded_bmi))
    elif  rounded_bmi> 25 and rounded_bmi <30:
        print("Your bmi is {bmi} you're slightly overweight.".format(bmi=rounded_bmi))
    elif  rounded_bmi> 30 and rounded_bmi <35:
        print("Your bmi is {bmi} you're obese.".format(bmi=rounded_bmi))
    else:
        print("You're critically obese")

choice = int(input("1. Standard Scale(kg, meter) \n2. International Scale(pound, inches)\nPlease Enter Your Choice:"))
if (choice == 1):
    weight_in_kg = float(input("Please enter weight in KGs: "))
    height_in_meter = float(input("Please enter weight in Meter: "))
    bmi = (weight_in_kg / height_in_meter**2 )
    rounded_bmi = round(bmi,2)
    bmi_calc(rounded_bmi)

elif (choice == 2):
    weight_in_lbs = float(input("Please enter weight in Pounds: "))
    height_in_inches = float(input("Please enter weight in inches: "))
    bmi = (weight_in_lbs / height_in_inches**2) * constant
    rounded_bmi=(round(bmi,2))
    bmi_calc(rounded_bmi)
else:
    time.sleep(3)
    print("invalid Selection. Program will terminate shortly")
    