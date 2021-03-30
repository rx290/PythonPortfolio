def price(opt):
    if opt =='s':
        price = 15.00
        return price 
    elif opt =='m':
        price = 20.00
        return price
    elif opt == 'l':
        price = 25.00
        return price

def addon(price,pep,cheese):
    if pep == 'yes' and price == 15.00 and cheese =='yes':
        price += 3.00
        return price
    elif pep == 'yes' and (price == 20.00 or price == 25.00) and cheese =='yes':
        price += 4.00
        return price
    elif pep == 'no' and price == 15.00 and cheese =='yes':
        price += 1.00
        return price
    elif pep == 'no' and (price == 20.00 or price == 25.00) and cheese =='yes':
        price += 1.00
        return price
    elif pep == 'yes' and (price == 15.00) and cheese =='no':
        price += 2.00
        return price
    elif pep == 'yes' and (price == 20.00 or price == 25.00) and cheese =='no':
        price += 3.00
        return price
    else:
        return price


size = input("Please Enter Pizza Size (S, M, L): ").lower()
pep = input("Do you want pepperoni? (Yes or No)\n").lower()
cheese = input("Do you want extra cheese? (Yes or No)\n").lower()



p = price(size)
total=addon(p,pep,cheese)

print("Your Total Bill is ${total}".format(total=total))