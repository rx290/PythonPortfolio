"""
Take 10 inputs into an array/list and print that array/list in reverse
"""
# arr = []
# for i in range(0,10):
#     var=input("please {}st/nd/rd enter an element: ".format(i))
#     arr.append(var)

# print(arr[::-1])

# Revision 22nd Nov 2025
ls = [input("Please Enter {} number: ".format(x+1)) for x in range(10)]
print("list in reverse order: ",ls[::-1])