""" Write a Python program to add two given lists and find the difference between lists. Use map() function.""" 
adder, subtractor = lambda x,y : x+y , lambda x,y: x-y
l1 = [1,15,187,69,75]
l2=[2,89,785,14,2]

addition, subtraction = list(map(adder,l1,l2)),list(map(subtractor,l1,l2))
print("Sum of two lists: ",addition,'\n',"Difference of two lists: ",subtraction)