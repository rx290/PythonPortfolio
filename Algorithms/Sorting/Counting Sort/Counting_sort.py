"""
Write a Python program for counting sort.
According to Wikipedia "In computer science, counting sort is an algorithm for sorting a collection of objects according 
to keys that are small integers; that is, it is an integer sorting algorithm. It operates by counting the number of objects 
that have each distinct key value, and using arithmetic on those counts to determine the positions of each key value in the output sequence. 
Its running time is linear in the number of items and the difference between the maximum and minimum key values, so it is only suitable for direct 
use in situations where the variation in keys is not significantly greater than the number of items. However, 
it is often used as a subroutine in another sorting algorithm, radix sort, that can handle larger keys more efficiently".
"""
sample = [0,2,8,9,9,4,7,5,3,1,0,5,6,7,8,8,8,5,4,0,1,0,0,3,2,4]
counter = {}
unique_elements = set(sample)
final_array = []

def occurrence_counter(unique_arr,sample_arr):
    global counter
    for i in unique_arr:
        counter[i] = sample_arr.count(i)
    #Sorting Occurrence Dictionary based on values
    # Another option dict(sorted(x.items(), key=lambda item: item[1]))
    counter = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1])}

def counting_sort_element_creator(element,iter):
    if iter == 0:
        return final_array
    else:
        final_array.append(element)
        counting_sort_element_creator(element,iter-1)
        
def counting_sort():
    for keys in counter:
        counting_sort_element_creator(keys,counter[keys])

occurrence_counter(unique_elements,sample)
counting_sort()
print("Counting Sort in Ascending order: ",final_array,"\nCounting Sort Descending Order: ",final_array[::-1])