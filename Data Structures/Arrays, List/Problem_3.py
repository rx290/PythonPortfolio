"""
Find the smallest number index from a randomly generated array/list.
"""
from random import randint

arr= []
for i in range(0,25):
    arr.append(randint(1,5855))

print("The array/list: ",arr)
print("The smallest digit of the above given list is as follows: ", min(arr))