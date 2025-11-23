import  random

names_string = input("Please Enter Names of the individuals: ")
name_list = names_string.split(',')

name = name_list[random.randrange(0,len(name_list))]
print (name," is going to buy the meal today!")