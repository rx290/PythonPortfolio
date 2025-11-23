"""Write a Python program to convert a given list of tuples to a list of strings using map function.""" 
lst = [('a'),('b'),('c'),('d'),('e')]
str_con = lambda x:str(x)
mapper= list(map(str_con,lst))
print(mapper)