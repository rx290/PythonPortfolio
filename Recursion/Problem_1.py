"Write a Python program to calculate the sum of a list of numbers." 


l = [1,5,9,7,5,3,8,5,2,4,5,6]

# length = len(l)
# sum=0
# def adder(x):
#     if x != length:
#         global sum
#         sum = sum + l[x]
#         adder(x+1)
#     else:
#         print(sum)
# adder(0)

# Revision 26th November 2025


def adder(x):
    _length = len(x)
    _total_sum = 0
    return print(sum(x)) if len(x) > 0 else print("list is empty")

adder(l)