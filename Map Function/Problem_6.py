"""Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function.""" 
_pass = False
_upper, _lower = lambda x: x.upper(), lambda x:x.lower()
l = ['a','s','a','d']
upper = list(map(_upper,l))
lower = list(map(_lower,upper))
print(upper,lower)
print(list(set(l)))