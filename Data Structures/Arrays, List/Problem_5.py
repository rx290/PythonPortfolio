"""
Find the minimum and maximum out of the array/list/list!
a)  use built-in functions
b)  Don't use built-in functions
"""

lst = [0.425,1,2,85,45854,0.1112,-85452,-0.5658,1000,23,-90000,666]
print("Max: {}, Min: {}".format(max(lst),min(lst)))

# B to be implemented

counter = 0
min = lst[counter]
sorted = []

for i in range(len(lst)):
    if lst[i] < min:
        min = lst[i]
        sorted.insert(0,min)
        print(sorted)
    else:
        pass
print(min)