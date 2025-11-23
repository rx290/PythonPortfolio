""" Write a Python program to convert a list of tuples into a dictionary. """ 

_list = [(1,2,3),(4,5,6),(7,8,9)]
_list2 = [('dict 1'),('dict 2'),('dict 3')]

_dict = zip(_list2,_list)
print(dict(_dict))