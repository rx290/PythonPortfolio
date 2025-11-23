"""Write a Python program to create a FIFO queue. 
Expected Output:
0 1 2 3 """ 

queue = [5,4,8,9,1]

print("Fifo implemented: \n")
for i in range(len(queue)):
    print(queue.pop(0))