"""
Write a Python program of recursion list sum.  
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21
"""

test_data = [1, 2, [3,4], [5,6]]

def elemental_summer(x):
    totalSum = 0
    for i in x:
        if type(i) == int:
            totalSum = totalSum+i
        elif type(i) == list:
            totalSum = totalSum + elemental_summer(i)
        else:
            pass
    return totalSum
        
t_sum = elemental_summer(test_data)
print("Total Sum of all the elements is: ",t_sum)