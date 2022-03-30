"""
Take an input from user.
Read each character individually display it's type and ascii code

Ascii code:
Chars                  Ascii Values
A - Z                  65 - 90
a - z                  97 - 122
0 - 9                  48 - 77
special character      0 - 47, 58 - 64 , 91 - 96, 123 - 127
"""
text = input("Please enter a string: ")
ascii_text = ''
for i in text:
    print("Char: ",i ," Ascii Representation: ",str(ord(i)))
    ascii_text += str(ord(i))
    
print(ascii_text)