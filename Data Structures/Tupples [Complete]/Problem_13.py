"""Write a Python program convert a given string list to a tuple. 
Original string: python 3.0
<class 'str'>
Convert the said string to a tuple:
('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
<class 'tuple'> """ 
input_string = "Python 3.0"
convertedTup = [*input_string.replace(' ','')]
convertedTup = tuple(convertedTup)
print(convertedTup)