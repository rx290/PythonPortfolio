"Write a Python program to calculate the sum of a list of numbers." 

from operator import length_hint


l = [1,5,9,7,5,3,8,5,2,4,5,6]

length = len(l)
sum=0
def adder(x):
    if x != length:
        global sum
        sum = sum + l[x]
        adder(x+1)
    else:
        print(sum)
adder(0)