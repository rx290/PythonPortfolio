"""
Write a program to find the sum of the following series,
a
1 + 1/2 + 1/3 +1/4 + .... 1/n
"""
n = int(input("Please enter some integer: "))
sum_series = 0
if n <0:
    print("Please enter positive integer next time!")
else:
    for i in range(1,n+1):
        if i == 1:
            sum_series = sum_series+1
        else:
            sum_series = sum_series+ (1/n)
    
    print("Result is :",sum_series)