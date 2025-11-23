"""
Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings.  
Original list:
[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
Sort the said mixed list of integers and strings:
[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
""" 
lst =[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
_int , color = [],[]
sorter = lambda x: _int.append(x) if type(x) ==int else color.append(x)
mapper = list(map(sorter,lst))
_sorted = lambda x: sorted(x)
_int =_sorted(_int)
color = _sorted(color)
sorted_list = _int +color
print(sorted_list)