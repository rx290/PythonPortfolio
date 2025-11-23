""" Write a Python program to calculate the average value of the numbers in a given tuple of tuples. 
Original Tuple:
((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
Average value of the numbers of the said tuple of tuples:
[30.5, 34.25, 27.0, 23.25]
Original Tuple:
((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
Average value of the numbers of the said tuple of tuples:
[25.5, -18.0, 3.75]""" 

# solution to find average of each tuple within the list
ogTuple = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
averageOgTuple = []
average = 0
childTupleLength= 0
for i in range(0,len(ogTuple)):
    for j in ogTuple[i]:
        average = average + j
    averageOgTuple.append(average/len(ogTuple[i]))
    average = 0
print(averageOgTuple)

# Solution to find average of each corresponding element in the list
def averageCalc(tup):
    avgList = [sum(x)/len(x) for x in zip(*tup)]
    return avgList
print(averageCalc(ogTuple))