"""Write a program that prints the minimum of four input integers"""
numbers = []
for i in range(4):
    numbers.append(int(input("Please enter {} number: ".format(i+1))))
    
print("Minimum of these {} numbers is: {}".format(numbers, min(numbers)))