"""Write a Python program to check if a specified element presents in a tuple of tuples. 
Original list:
(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
Check if White present in said tuple of tuples!
True
Check if White present in said tuple of tuples!
True
Check if Olive present in said tuple of tuples!
False """ 
tup = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
# for checking single element
validator = lambda x,y: print(True) if x in y else print(False)
col = ['White','Blue','Green']
tup_ = tuple(map(validator,col,tup))
print(tup_)
pup = None

# # for all item list
# for i in range(len(col)):
#     for j in range(len(tup)):
#         if col[i] in tup[j]:
#             print(True)
#         else:
#             print(False)

# set something which will search for all items 