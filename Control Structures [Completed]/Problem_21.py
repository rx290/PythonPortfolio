"""
Write a program using while loop to convert alphabets from A-Z to their corresponding ASCII values
"""
from string import ascii_letters

print("Alphabets : ASCII Value")
for i in ascii_letters:
    print(i, ' : ', ord(i))