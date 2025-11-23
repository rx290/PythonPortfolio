"""Write a Python program to insert items into a list in sorted order.  
Expected Output:
Original List:
[25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
Sorted List:
[14, 25, 36, 36, 45, 47, 48, 68, 69, 78] """ 

num = int(input("Please enter the number of elements you want to add: "))

_list = []

for x in range(0,num):
    a = int(input("Please enter your "+str(x+1)+ " element: "))
    _list.append(a)
    
print("Original List: ", _list)
print("Sorted List: ", sorted(_list))