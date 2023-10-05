"""
Create a structure to specify data of customers in a bank, the data to be stored is 
Account number, Amount, Name.
There are 200 bank account in bank

Write a function to print the data of all 200 accounts
Write a function to print data of any given account number
Write a menu to deposit or withdraw money
"""
customerData = {
    'customer1':{
        'Account': 000,
        'Name': '',
        'Amount':0.0,
    }
}

def ReturnAllData():
    return customerData

def AccountFinder(Key,accountNumber):
    index = customerData.get(Key,accountNumber)
    return index

print(ReturnAllData())
print(AccountFinder('Account',000))