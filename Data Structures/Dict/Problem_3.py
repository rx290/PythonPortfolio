"""
There is a structure called employee that holds information like employee code, name and date of joining
Write a program to create an array of the structure and enter some data into it.
Then ask the user to enter current date, display the names of those employees whose tenure is 3 r more than 3 years according 
to the current date
"""

import random

# Re to use for parsing
# ((0?[0-9]|[0-2])-([0-2][0-9]|3[0-1])-([1900-2025]{4}))


def employee(name,date_of_joining,sex):
    
    return{
        "employee_name": name,
        "employee_code": random(),
        "date_of_joining": date_of_joining,
        "gender": sex,   
    }
    
    