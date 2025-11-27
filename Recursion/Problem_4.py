"Write a Python program to get the factorial of a non-negative integer." 

num = int(input("Any positive number: "))

def fac(num):
    fac = 1
    for i in range(1,num+1):
        fac = fac *i
    return fac    
        
fac_5 = fac(num)
print(fac_5)