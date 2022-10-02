"""
Say there are two randomly generated array/lists of different sizes.
Write a function which is like tis AddArr(a,n,b) where n is the length of array/list b to add to a.

for eg:

a = [2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9]
b = [6.0,5.0,4.0,3.0,2.0,1.0]
add(a,5,b)

returns: [8.2,8.3,8.4,8.5,8.6,8.7,8.8,9.9]
"""
a = [2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9]
b = [6.0,5.0,4.0,3.0,2.0,1.0]

def list_adder(a:list,b:list):
    larger, shorter = a,b
    if len(larger) > len(shorter):
        pass
    else:
        larger,shorter=shorter,larger
    c = []
    for i in range(len(shorter)):
        larger[i]= larger[i]+shorter[i]
    
    return(larger)

print(list_adder(a,b))