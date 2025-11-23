"""
Write a Python program to calculate the value of 'a' to the power 'b'.  
Test Data :
(power(3,4) -> 81
"""
def power(a:int,b:int):
    if b == 0 or b==1:
        return 1
    elif a == 0:
        return 0
    else:
        return a*power(a,b-1)

p=power(3,4)
print(p)