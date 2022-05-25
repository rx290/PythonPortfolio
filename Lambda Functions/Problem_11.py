"""
Write a Python program to find intersection of two given arrays using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
[1, 2, 4, 8, 9]
Intersection of the said arrays: [1, 2, 8, 9]
""" 
intersection = []
lst = [1, 2, 3, 5, 7, 8, 9, 10]
lst_1 = [1, 2, 4, 8, 9]

intersected = lambda x: intersection.append(x) if lst.count(x) > 0 and lst_1.count(x) >0 else print("")
mapper = list(map(intersected,lst_1))
print(intersection)