"""
Take 10 inputs into an array/list and print that array/list in reverse
"""
arr = []
for i in range(0,10):
    var=input("please {}st/nd/rd enter an element: ".format(i))
    arr.append(var)

print(arr[::-1])