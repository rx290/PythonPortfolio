"""
Assume that you want to generate a table of multiples of any given number, Write a program that allows the user to enter the number and 
then generates the table, formatting it into 10 columns and 20 lines interaction with the program should look like this 

Enter a number: 7

    7   14  21  28  35  42  49  56  63  70
    77  84  91  98  105 112 119 126 133 140
    147 154 161 168 175 182 189 196 203 210
    .....
"""

num = int(input("Please enter a number: "))
line_count = 0
i = 1
while line_count != 20:
    print(num * i,end =' ')
    if i % 10 == 0:
        line_count += 1
        print(" ")
    i = i + 1
        
    