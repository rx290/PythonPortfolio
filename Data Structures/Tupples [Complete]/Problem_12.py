""" Write a Python program to count the elements in a list until an element is a tuple. """ 
lst = [1,2,3,(2,),4,5,[1],6,'a','v',(2,)]
counter =0
for i in lst:
    if type(i) == tuple:
        break
    else:
        counter = counter +1
        
print(counter)