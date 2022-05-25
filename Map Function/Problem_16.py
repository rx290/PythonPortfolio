"""Write a Python program to convert a given list of strings into list of lists using map function.""" 
lst = ['a','b','c','d','e']
lst_con = lambda x:list(x)
mapper = list(map(lst_con,lst))
print(mapper)