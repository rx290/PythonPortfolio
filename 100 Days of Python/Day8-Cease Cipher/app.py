import string

print ("""  ___|                             ___|_)       |               
 |      _ \  _` |  __|  _ \  __|  |     | __ \  __ \   _ \  __| 
 |      __/ (   |\__ \  __/ |     |     | |   | | | |  __/ |    
\____|\___|\__,_|____/\___|_|    \____|_| .__/ _| |_|\___|_|    
                                         _|                     
""")

con = True
while True:
    choice = input("what do you want to do? \n 'encode' or 'decode': ")
    phrase = ""
    shift_number = 0
    if choice == 'encode':
        phrase = input("Please enter a phrase: ")
        shift_number = int(input("Please enter shift number: "))
    elif choice == 'decode':
        pass
    else:
        print("Please enter only encode or decode: ")
        choice

