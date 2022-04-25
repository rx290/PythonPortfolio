"""
Write a Python program to create a function that takes one argument, 
and that argument will be multiplied with an unknown given number.
Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75
""" 

def num_mul(x):
    print("""
        Double the number of {} = {}
        Triple the number of {} = {}
        Quadruple the number of {} = {}
        Quintuple the number {} = {}
          """.format(x,x*2,x,x*3,x,x*4,x,x*5))
    
    
num = int(input("Enter some number: "))
num_mul(num)