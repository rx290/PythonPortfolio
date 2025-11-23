"""
Write a program to add first seven terms of the following series using a for loop

1/1! + 2/2! + 3/3!

"""
sum = 0
fac = 1
def dem(k):
    for j in reversed(range(1,k+1)):
        global fac
        fac = fac * k
    return fac
        
for i in range(1,8):
    sum = sum + 1/dem(i)
print("Sum of 1/1! + 2/2! + 3/3! + 4/4! + 5/5! + 6/6! + 7/7! = ",sum)
    