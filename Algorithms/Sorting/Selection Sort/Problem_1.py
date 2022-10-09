"""
Write a Python program to sort a list of elements using the selection sort algorithm.
Note : The selection sort improves on the bubble sort by making only one exchange for every pass through the list. 
Sample Data: [14,46,43,27,57,41,45,21,70]
Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70]

According to Wikipedia "In computer science, selection sort is a sorting algorithm, specifically an in-place comparison sort. 
It has O(n2) time complexity, making it inefficient on large lists, and generally performs worse than the similar insertion sort".
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