"""Write a Python program to add three given lists using Python map and lambda. """ 
lst = [1,2,3,4,5]
lst2 = [3,6,9,12,15]
lst3 = [2,4,6,8,10]

adder = lambda x,y,z : x+y+z

sum = list(map(adder,lst,lst2,lst3))
print (sum)