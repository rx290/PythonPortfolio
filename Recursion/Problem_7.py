"""
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).  
Test Data:
sum_series(6) -> 12
sum_series(10) -> 30
"""
#TO be fixed
def sum_series(n:int):
    sum = n
    k = 2
    if n-k <= 0:
        return sum
    else:
        sum = sum + (n-k)
        k = k+2
        sum_series(sum)

sum_series(6)