"""Write a Python program to create a LIFO queue. 
Expected Output:
3 2 1 0 """ 

lifo = [8,4,9,2,7]
print("LIFO implemented: ")
for i in range(len(lifo)):
    print(lifo.pop())