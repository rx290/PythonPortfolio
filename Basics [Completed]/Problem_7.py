"""A cashier has currency notes of denominations 10, 50 and 100. if the amount to be withdrawn
is input through the keyboard in hundreds, find the total number of currency notes of each denomination
the cashier will have to give to the withdrawer"""

amount = int(input("Please enter currency: "))

hun, fif, ten = 0, 0, 0
loose = 0

while amount > 0:
    if amount > 100:
        amount = amount - 100
        hun = hun +1
    else:
        if amount < 100 and amount >= 50:
            amount = amount - 50
            fif = fif + 1
        else:
            if amount >= 10 and amount <50:
                amount = amount - 10
                ten = ten + 1
            else:
                loose = amount
                
print("Your currency notes are as follows:\nHundred Notes: {}\n\nFifty Notes: {}\nTen Notes: {}\nLoose: {}".format(hun,fif,ten,loose))
