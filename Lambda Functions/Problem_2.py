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
  doubler = lambda x : x * 2
  triple = lambda x : x*3
  quadruplex = lambda x : x * 4
  quintupled = lambda x : x*5
  print("""
        Double the number of {} = {}
        Triple the number of {} = {}
        Quadruple the number of {} = {}
        Quintuple the number {} = {}
          """.format(doubler,triple,quadruplex,quintupled))
    
    
num = int(input("Enter some number: "))
num_mul(num)