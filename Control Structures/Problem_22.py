"""
Drivers are concerned with mileage obtained by their automobiles. One driver has kept track of several tips by recording miles
driven and gallons used for each trip.
The program should calculate and display the miles per gallon obtained for each trip and print the combined miles per gallon obtained
for all tankful up to this point.

Example:
    Enter miles driver: 287
    Enter gallons used: 13
    MPG this trip: 22.076923
    Total MPG: 22.076923
"""

trips = int(input("How many trips have you done?\n"))
_trips = []
for i in range(trips):
    miles = float(input("Please enter miles driven for trip {}: ".format(i+1)))
    gallons = float(input("Please enter gallons used for trip {}: ".format(i+1)))
    mpg = miles/gallons
    print("Total MPG for trip {} is: ".format(i+1), mpg)
    _trips.append(mpg)
    
print("Total mog: {}".format(sum(_trips)))