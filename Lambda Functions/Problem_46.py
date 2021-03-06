"""
Write a Python program to find index position and value of the maximum and minimum values in a given list of numbers using lambda.  
Original list:
[12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
Index position and value of the maximum value of the said list:
(5, 89)
Index position and value of the minimum value of the said list:
(3, 10.11)
""" 
lst =[12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
max_finder = lambda x: lst.index(max(x))
min_finder = lambda x: lst.index(min(x))
print('Index position and value of the maximum value of the said list:',(max_finder(lst),lst[max_finder(lst)]))
print('Index position and value of the minimum value of the said list:',(min_finder(lst),lst[min_finder(lst)]))