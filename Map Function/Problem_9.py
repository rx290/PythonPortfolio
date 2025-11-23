"""Write a Python program to create a new list taking specific elements from a tuple and convert a string value to integer.""" 
tup = (1,2,3,4,5,6,7,8,9,10)
lst = []
str_lst = ['101','202','303']
picker = lambda x: lst.append(x) if tup.index(x)%2 == 0 else print(x)
changer = lambda  x: int(x)
selected_lst = tuple(map(picker,tup))
changed = list(map(changer,str_lst))

print(selected_lst,changed)