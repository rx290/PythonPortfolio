"""Write a Python program to sort a tuple by its float element. 
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')] """ 

ogTup = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# lambda function to parse second element as the key
sorter = lambda x:float(x[1])
#Sorted in ascending order
sortedTup = sorted(ogTup,key=sorter)
print(sortedTup)
#sorted in defending order
sortedTup = sorted(ogTup,key=sorter,reverse=True)
print(sortedTup)