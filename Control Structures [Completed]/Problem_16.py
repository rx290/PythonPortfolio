"""
Calculate the factorial of the number from 1-10
"""

def factorial(n):
    if n != 1:
        n = n * factorial(n-1)
        return n
    else:
        n = n * 1
        return n
    
print(factorial(10))