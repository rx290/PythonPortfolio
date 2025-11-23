"""
Find the absolute value of a number entered by the user
"""
choice = int(input("What sort of number are you going to enter:\n1. Integer\n2. Floating point\n3. Complex Number\nPlease Enter your choice: "))


if choice == 1:
    num = int(input("Please enter any number: "))
    print("absolute value: ",abs(num))
elif choice == 2:
    num = float(input("Please enter any number: "))
    print("absolute value: ",abs(num))
elif  choice ==3:
    num = complex(input("Please enter any number: "))
    print("absolute value: ",abs(num))
else:
    print("invalid Entry")