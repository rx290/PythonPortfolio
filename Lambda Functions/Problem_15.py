"""
Write a Python program to find the values of length six in a given list using Lambda.
Sample Output:
Monday
Friday
Sunday
""" 
lst = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
value_finder = lambda x: print(x,"is a value of length 6.") if len(x)==6 else print(x, "is not a value of length 6.")
list(map(value_finder,lst))