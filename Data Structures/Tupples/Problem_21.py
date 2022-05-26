"""  Write a Python program to convert a given list of tuples to a list of lists. Go to the editor
Original list of tuples: [(1, 2), (2, 3), (3, 4)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]""" 
lst_of_tup = [(1, 2), (2, 3), (3, 4)]
lister = lambda x: list(x)
converted = list(map(lister,lst_of_tup))
print(converted)