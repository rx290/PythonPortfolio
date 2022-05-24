"""
Write a Python program to remove None value from a given list using lambda function.  
Original list:
[12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
Remove None value from the said list:
[12, 0, 23, -55, 234, 89, 0, 6, -12]
""" 
lst =[None,1,None,2,None,3,None,4,None,5]
print("Actual List: ",lst)
remover = lambda x: lst.pop(lst.index(x)) if x== None else print("Next index of None is: ",lst.index(None)) 
list(map(remover,lst))
print("Filtered List: ",lst)