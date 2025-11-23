"""
Take an array/list as an input find the largest number out of it and print that number
"""
lst = [1,85,75,7585,899,8445,754,2425,1451,0.11,52.22]
print(max(lst))

num = int(input("How many character long list do you want to create?\n"))
ls = [input("Please enter {} number: ".format(x+1)) for x in range(0,num+1)]
print("Largest number from the input list of {} numbers is: {}".format(num,max(ls)))