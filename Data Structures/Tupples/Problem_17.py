""" Write a Python program to convert a given tuple of positive integers into an integer. 
Original tuple:
(1, 2, 3)
Convert the said tuple of positive integers into an integer:
123
Original tuple:
(10, 20, 40, 5, 70)
Convert the said tuple of positive integers into an integer:
102040570""" 
tup = (10, 20, 40, 5, 70)
adder = lambda x: str(x)
mapper = list(map(adder,list(tup)))
combo =''
for i in mapper: combo = combo + i
print(combo)