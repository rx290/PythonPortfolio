"""
Write and run a program that uses a while loop to compute and prints the sum of a given number of squares. For example,
if 5 is input then the program will print 55, which equals 1^2 + 2^2 + 3^2 +4^2 +5^2
"""
def SquareSumCalc(n):
    num = 0
    for i in range(1,n+1):
        num = num + i**2
    return num

print(SquareSumCalc(5))