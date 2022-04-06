"""
Twenty five numbers are entered from the keyboard into an array.
Find out count of positive and negative numbers.
Find out count of even and odd numbers.
"""
from re import A
from turtle import pos

from torch import negative


arr = []
for i in range(1,26):
    arr.append(int(input("Please enter {} number: ".format(i))))
    
pos_count, neg_count, even_count, odd_count = 0,0,0,0

for i in arr:
    if i > 0:
        pos_count = pos_count + 1
    else:
        neg_count = neg_count + 1
        
    if i % 2 == 0:
        even_count =even_count + 1
    else:
        odd_count = odd_count + 1
        
print("There are {} positive numbers, {} negative numbers, {} even numbers and {} odd numbers in the array.".format(pos_count,neg_count,even_count,odd_count))