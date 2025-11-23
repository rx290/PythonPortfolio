print("Welcome to the tip Calculator.")
total_bill = float(input("What was the total bill?\n"))
number_of_people= int(input("How many people to split the bill?\n$"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
tip ,total_inclusive_of_tip ,per_person_share = 0.0 , 0.0 , 0.0
if (tip_percentage == 10):
    tip = total_bill*0.10
    total_inclusive_of_tip = total_bill + tip
    per_person_share = total_inclusive_of_tip / number_of_people
    print("Each person should pay: ${}".format(round(per_person_share,2)))
elif (tip_percentage == 12):
    tip = total_bill*0.12
    total_inclusive_of_tip = total_bill + tip
    per_person_share = total_inclusive_of_tip / number_of_people
    print("Each person should pay: ${}".format(round(per_person_share,2)))
elif(tip_percentage ==15 ):
    tip = total_bill*0.15
    total_inclusive_of_tip = total_bill + tip
    per_person_share = total_inclusive_of_tip / number_of_people
    print("Each person should pay: ${}".format(round(per_person_share, 2)))
else:
    print("invalid tip percentage!")