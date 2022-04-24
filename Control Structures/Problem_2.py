"""Write a program that prints the minimum of four input integers"""
numbers = []
min = 0
for i in range(4):
    numbers.append(int(input("Please enter {} number: ".format(i+1))))
    if i == 0:
        min = numbers[i]
    else:
        pass
# print("Minimum of these {} numbers is: {}".format(numbers, min(numbers)))

