"""
Write a Python program to sort a list of elements using the insertion sort algorithm.
Note : According to Wikipedia "Insertion sort is a simple sorting algorithm that builds 
the final sorted array (or list) one item at a time. It is much less efficient on large lists 
than more advanced algorithms such as quicksort, heapsort, or merge sort."
Sample Data: [14,46,43,27,57,41,45,21,70]
Expected Result : [14, 21, 27, 41, 43, 45, 46, 57, 70] 
"""
sample_data= [14,46,43,27,57,41,45,21,70]
minimum_val = sample_data[0]
for j in range(len(sample_data)-1,0,-1):
    for i in range(j):
        if minimum_val < sample_data[i]:
            sample_data[sample_data.index(minimum_val)], sample_data[i] = sample_data[i], sample_data[sample_data.index(minimum_val)]
            minimum_val = sample_data[sample_data.index(minimum_val)]
            
        else:
            pass
print("Newly sorted list: ",sample_data)