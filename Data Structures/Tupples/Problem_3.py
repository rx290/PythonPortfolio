"""Write a Python program to check whether an element exists within a tuple. """ 
ele = input("Please input the element you want to search in tuple")
tup = ('1','2','3','4','5','a','b','c')

if tup.count(ele) >= 1:
    print("Element Exit!")
else:
    print("Element Doesn't Exist!")