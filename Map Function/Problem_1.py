"""Write a Python program to triple all numbers of a given list of integers. Use Python map """ 
triple = lambda x: x+x+x
lst = [1,2,3,4,5]

tripler = list(map(triple,lst))
print(tripler)