"""Write a Python program to find the ration of positive numbers, negative numbers and zeroes in an array of integers""" 

pos_count, neg_count, zero_count = 0,0,0
lst = [-5,-4,-3,-2,-1,0,1,2,3,0]
# counter = lambda x: pos_count + 1 if x > 0 else zero_count +1 if  x == 0 else neg_count+1
def counter(some_list):
    global pos_count,neg_count,zero_count
    if some_list > 0:
        pos_count = pos_count +1
    elif some_list < 0:
        neg_count = neg_count +1
    else:
        zero_count = zero_count +1
mapper = list(map(counter,lst))
print("Number of positive number: ",pos_count,"\nNumber of negative numbers: ",neg_count,"\nNumber of zeros: ",zero_count)
