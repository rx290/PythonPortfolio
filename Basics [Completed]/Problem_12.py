"""
Write a program that generates following table:
    1990    135
    1991    7290
    1992    11300
    1993    16200
    
use a single count statement for all the outputs
"""
table = "{0} {1:15}\n{2} {3:15}\n{4} {5:15}\n{6} {7:15}".format(1990,135,1991,7290,1992,11300,1993,16200)
table_2 = "{0}\t{1}\n{2}\t{3}\n{4}\t{5}\n{6}\t{7}".format(1990,135,1991,7290,1992,11300,1993,16200)
print(table)
print(table_2)
