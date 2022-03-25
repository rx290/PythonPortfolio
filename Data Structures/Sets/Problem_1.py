"""
a. Write a Python program to create a set.

b. Write a Python program to iteration over sets.

c. Write a Python program to add member(s) in a set.

d. Write a Python program to remove item(s) from a given set.

e. Write a Python program to remove an item from a set if it is present in the set. 
""" 

# a. Creating a SET
fruits = {'Banana', 'Apple','Pineapple'}

# b. Iteration
for item in fruits:
    print(item)
    
#c. Adding Member
fruits.add("Pear")
print(fruits)

#d. Remove Items
fruits.remove("Banana")
print(fruits)

#e. if element in set remove element
f_t_r = input("Please enter the fruit you want to remove: ")
fruits.add("Banana")
if f_t_r in fruits:
    fruits.remove(f_t_r)
    print("{} has been removed!".format(f_t_r))
    print("Remaining fruits are: {}".format(fruits))
    