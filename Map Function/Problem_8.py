"""Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.""" 


l = [1,2,3,4,5]
tup = (4,5,6,)
str_changer = lambda x:str(x)
mapper = list(map(str_changer,l))
mapper_= tuple(map(str_changer,tup))
print(mapper,mapper_)
