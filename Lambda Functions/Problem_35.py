"""
Write a Python program to check whether a specified list is sorted or not using lambda.  
Original list:
[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
Is the said list is sorted!
True
Original list:
[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
Is the said list is sorted!
False
""" 
lst = [1, 2, 4, 9, 8, 6, 10, 12, 14, 16, 17]
checker = lambda x: print(True) if sorted(lst)==lst else print(False)
checker(lst)