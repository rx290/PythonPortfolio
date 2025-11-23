"""
Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
Number of even numbers in the above array: 3
Number of odd numbers in the above array: 5
""" 
lst= [1,2,3,4,5,6,7,8,9,10]
even ,odd = 0,0
even_odd_checker = lambda x: 1 if x%2==0 else 0
mapper =list(map(even_odd_checker,lst))
print("Number of even numbers: ",mapper.count(1))
print("Number of odd numbers: ",mapper.count(0))
