"""
a. Write a Python program to slice a tuple.

b. Write a Python program to find the index of an item of a tuple.

c. Write a Python program to find the length of a tuple.

d. Write a Python program to convert a tuple to a dictionary. 

e.Write a Python program to unzip a list of tuples into individual lists. 

f.  Write a Python program to reverse a tuple. 
""" 
tup = (1,2,3,4,5,'a','b','c')

#a
tup = tup[1:]

#b
print("Index of element 5 is:",tup.index(5))

#c 
print("Length of tuple:",len(tup))

#f
print(tup[::-1])

#d
dic = dict(tup)
print("Converted dict: ",type(dict),dict)

#e to be implemented