"""Write a Python program to replace last value of tuples in a list. 
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)] """ 

sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in range(0,len(sample_list)):
    x = list(sample_list[i])
    x[-1] = 100
    x = tuple(x)
    sample_list[i] = x

print(sample_list)

# Another way to do it is using string comprehension which is follows

example2= [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
stringComprehension = [eachElement[:-1]+(100,) for eachElement in example2]
print(stringComprehension)