"""
Write a Python program to sort a given list of strings(numbers) numerically using lambda.  
Original list:
['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
Sort the said list of strings(numbers) numerically:
['-500', '-12', '0', '4', '7', '12', '45', '100', '200']
""" 
lst = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
int_sorter = lambda x : int(x)
str_con = lambda x: str(x)
_lst = sorted(list(map(int_sorter,lst)))
_lst2 = list(map(str_con,_lst))
print("String sorted list: ",_lst2)