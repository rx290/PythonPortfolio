"""Write a Python program to compute the sum of elements of a given array of integers, use map() function.""" 

lst = [1,2,3,4,5,6,7,8,9,10]

def summer(x):
    mapped_sum = map(lambda a:a,x)
    _sum = sum(mapped_sum)
    return _sum
total_sum = summer(lst)
print(total_sum)