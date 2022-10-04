"""
Create an array/list of randomly generated numbers.
Find the last largest index.
Find the occurrence of the element present at the last largest index."""

lst = [1,85,75,7585,899,8445,754,2425,1451,0.11,52.22]
# len counts element and index start from 0 so len -1 is the formula to calc largest index
larget_index = len(lst) - 1
counter =0
for i in lst:
    if i == lst[larget_index]:
        counter = counter +1
    else:
        pass
print(counter)
    