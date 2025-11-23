"""
Write a program that inputs an array/list of N integers and displays sum of all elements.
"""
_str = input("input n numbers of integers with spaces: ").split(" ")
lst = map(int,_str)
print(sum(lst))
