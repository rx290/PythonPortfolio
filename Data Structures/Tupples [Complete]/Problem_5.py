""" Write a Python program to remove an item from a tuple.""" 
tup = (1,2,3,4,5,'a','b','c')
print("Tup before removing: ",tup)
tup = tup[1:]
print("Tup after removing first element: ",tup)
tup = tup[:-1]
print("Tup after removing first element: ",tup)
