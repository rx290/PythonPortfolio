""" Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples. 
Original list of tuples:
[(1, 2), (2, 3), (3, 4)]
Sum of all the elements of each tuple stored inside the said list of tuples:
[3, 5, 7]
Original list of tuples:
[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
Sum of all the elements of each tuple stored inside the said list of tuples:
[9, -1, 7, 8]""" 

lst =[(1, 2), (2, 3), (3, 4)]
lst_2 =[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
adder = lambda x: sum(list(x))
mapper = list(map(adder,lst))
mapper_2 = list(map(adder,lst_2))
print(mapper,mapper_2)