"""
Create a structure to specify data of customers in a bank, the data to be stored is 
Account number, Amount, Name.
There are 200 bank account in bank

Write a function to print the data of all 200 accounts
Write a function to print data of any given account number
Write a menu to deposit or withdraw money
"""
customerData = {
   'asadwaseem32@gmail.com': {
        'Account': 0,
        'Name': 'Asad Waseem',
        'Amount':2500.0,
    },
'waseem_asad@live.co.uk':    {
        'Account': 1,
        'Name': 'Muhammad Asad Waseem',
        'Amount':85000.0,
    }
}

def ReturnAllData():
    return customerData

def AccountFinder(email):
    #index = customerData.get(email)
    accountDetails = customerData[email]
    return accountDetails

print(ReturnAllData())
print(AccountFinder('asadwaseem32@gmail.com'))