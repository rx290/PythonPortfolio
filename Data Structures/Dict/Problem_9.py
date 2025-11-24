""" Write a Python script to check whether a given key already exists in a dictionary.""" 

dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

_key = int(input("please enter the key you think is in the dictionary"))

print("The key is in the Dictionary") if _key in dict_1 else print("The key is not in the Dictionary")