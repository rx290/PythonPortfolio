"""
Write a Python program to remove specific words from a given list using lambda.  
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']
Remove words:
['orange', 'black']
After removing the specified words from the said list:
['red', 'green', 'blue', 'white']
""" 
lst = ['orange', 'red', 'green', 'blue', 'white', 'black']

words_to_remove = ['orange', 'black']

remover = lambda x: lst.pop(lst.index(x))

list(map(remover,words_to_remove))
    
print(lst)

