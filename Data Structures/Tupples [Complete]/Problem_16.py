"""Write a Python program to convert a tuple of string values to a tuple of integer values. 
Original tuple values:
(('333', '33'), ('1416', '55'))
New tuple values:
((333, 33), (1416, 55)) """ 

ogTuple = (('333', '33'), ('1416', '55'))
ogTuple = list([list(i) for i in ogTuple])
for i in range(0,len(ogTuple)):
    for j in range(0,len(ogTuple[i])):
        # i[j].replace(i[j], int(i[j]))
        ogTuple[i][j] = int(ogTuple[i][j]) 
    ogTuple[i]= tuple(ogTuple[i])
ogTuple = tuple(ogTuple)
print(ogTuple)
