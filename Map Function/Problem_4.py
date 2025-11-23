"""Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.""" 
lst = [1,2,3,4,5]
power_raiser = lambda x: x**lst.index(x)
raised= list(map(power_raiser,lst))

print(raised)