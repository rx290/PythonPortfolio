""" Write a Python program to remove an empty tuple(s) from a list of tuples. 
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']""" 

sample_data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# stringComprehension = [sample_data.pop(sample_data.index(sample_data[i])) if len(sample_data[i]) is 0 else print('Skipping',sample_data[i]) for i in range(0, len(sample_data)-1    )]
stringComprehension = [element for element in sample_data if len(element)>0]
print(stringComprehension)