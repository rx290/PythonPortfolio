"""
According to a study, the approximate level of intelligence of a person can be calculated using the following formula:

i = 2 + ( Y + 0.5 X )

Write a program that will produce a table of values i, y and x.
Where y varies from 1 to 6 and for each value of y, x varies from 5.5 to 12.5 in steps of 0.5
"""

for y in range(1,7):
    for x in range(5.5,12.5,0.5):
        i = 2 + (y + 0.5(x))
        print(i)
        
