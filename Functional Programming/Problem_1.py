"""
Write a recursive function to obtain the running sum of first 25 natural numbers.
"""
sum = 0

def nn_sum(x):
    #using global variaable
    global sum 
    sum = sum + x
    print("Sum is equal to: ",sum) if x==0 else nn_sum(x-1)

# Modified it to take input and return answer
num = int(input("Please enter the natural number to find sum of: "))
nn_sum(num)