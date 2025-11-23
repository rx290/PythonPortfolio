"""
Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
Original arrays:
[-1, 2, -3, 5, 7, 8, 9, -10]
Rearrange positive and negative numbers of the said array:
[2, 5, 7, 8, 9, -10, -3, -1]
""" 
lst = [-1, 2, -3, 5, 7, 8, 9, -10]

sorter = lambda x: sorted(x)
sorted_list = sorter(lst)
print("Ascending order: ",sorted_list, "Descending Order: ",sorted_list[::-1])