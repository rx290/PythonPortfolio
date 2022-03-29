"""Write a Python program to create a queue and display all the members and size of the queue. 
Expected Output:
Members of the queue:
0 1 2 3
Size of the queue:
4 """ 

queue = [0,1,2,3]

print("Size of the queue is: {}".format(len(queue)))
print("Members of queue are: ",queue)

print("Lifo: ")
for i in range(len(queue)):
    print(queue.pop())

queue = [0,1,2,3]

print("Fifo: ")
for j in range(len(queue)):
    print(queue.pop(0))