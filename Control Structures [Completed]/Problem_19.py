"""
Write a prgogram that takes a five digit number from the user and print its reverse using a while loop
"""
digits= input("Please enter a five characer long digit: ")

reverse_digits =""
i = 5
while i <= 1:
    reverse_digits = reverse_digits + digits[i]
    i = i - 1
    
print("digit: ",digits)
print("reversed digits: ",reverse_digits) 