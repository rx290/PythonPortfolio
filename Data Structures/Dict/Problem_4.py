"""
Write aa program that compares two given dates. To store data use structures say date that contains three members namely,
date, month and years. If the dates are equal then display messages as "Equal" otherwise "Unequal"
"""

def dates(day, month,year):
    return{
        "Day": day,
        "Month": month,
        "Year": year
    }
names= ['day','month','year']
date_1= list(input("Please input date in following pattern (days Month Year):").split(sep=' '))
date_2= list(input("Please input date in following pattern (days Month Year):").split(sep=' '))
date_1 = dates(date_1[0],date_1[1],date_1[2])
date_2 = dates(date_2[0],date_2[1],date_2[2])

if (date_1==date_2):
    print("Dates are equal!")
else:
    print("Dates are not equal")