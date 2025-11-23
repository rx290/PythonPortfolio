"""Write a Python program to listify the list of given strings individually using Python map.""" 
lst = ['a','b','c','d','e']
lister = lambda x: print(list(x))
print("List or strings: ",lst)
mapper = list(map(lister,lst))
