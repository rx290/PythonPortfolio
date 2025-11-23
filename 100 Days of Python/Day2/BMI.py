import time

print("Welcome to BMI Calculator.")
height_in_meter = height_in_inches = 0.0, 0.0 
weight_in_kg = weight_in_lbs = 0.0, 0.0
constant = 703

choice = int(input("1. Standard Scale(kg, meter) \n2. International Scale(pound, inches)\nPlease Enter Your Choice:"))
if (choice == 1):
    weight_in_kg = float(input("Please enter weight in KGs: "))
    height_in_meter = float(input("Please enter weight in Meter: "))
    bmi = (weight_in_kg / height_in_meter**2 )
    print(round(bmi,2))
elif (choice == 2):
    weight_in_lbs = float(input("Please enter weight in Pounds: "))
    height_in_inches = float(input("Please enter weight in inches: "))
    bmi = (weight_in_lbs / height_in_inches**2) * constant
    print(round(bmi,2))
else:
    time.sleep(3)
    print("invalid Selection. Program will terminate shortly")
    