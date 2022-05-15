"""Write a Python program to square the elements of a list using map() function.""" 
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
square = lambda x: x**2
square_nums = list(map(square,lst)) 

print("Normal List: ",lst)
print("Square List: ",square_nums)
