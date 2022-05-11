"""Uf the total selling price of 15 items and the total profit earned on them is input through the keybard,
write a program to find the cost price of one item"""



total_price = input("Please enter the total price of 15 items sold: ")
profit = input("Please enter the total profit gained on 15 items: ")

actual_cost = float(total_price ) - float(profit)

print("Price of one item is: ",actual_cost/15)