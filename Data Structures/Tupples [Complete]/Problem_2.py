"""
a. Write a Python program to add an item in a tuple.

b. Write a Python program to convert a tuple to a string. 

c. Write a Python program to get the 4th element and 4th element from last of a tuple.

d.  Write a Python program to create the clone of a tuple.

e. Write a Python program to find the repeated items of a tuple. 
""" 
# Method 1
from copy import deepcopy


c = 25.5
tup = (1,'a',c)
tup = list(tup)

tup.append("b")
tup.append('a')
tup = tuple(tup)
print(tup)


# Method 2

_tup = ("some value",)
tup = tup + _tup
print(tup)

#b
print("String: ",str(tup))

#c
print("Fourth element: ",tup[4])
# reverse Index
print("Fourth element: ",tup[-4])

#tupple copy 
#d
_tup_copy = deepcopy(tup)

if tup == _tup_copy:
    print("full copy!")
else:
    print("Nope!")

#e
repeated_ele = []
for i in tup:
    if tup.count(i) > 1:
        if i in repeated_ele:
            pass
        else:
            repeated_ele.append(i)
    else:
        pass
print(repeated_ele)