"""Write a program to determine whether the seller has made profit or incurred loss.
Also determine how much profit he made or loss he incurred.
AlsoCost price and selling price of an item is input by the user"""

item_cost = float(input("Please enter item cost: "))
selling_cost = float(input("Please enter selling cost: "))

difference = selling_cost - item_cost

if difference > 0:
    print("Item was sold in profit!")
    print("Profit was: ",difference)
elif difference == 0:
    print("Item was sold on terms of no profit and no gain!")
else:
    print("Item was sild in loss")
    print("loss was: ",difference)