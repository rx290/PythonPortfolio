"""Evaluate the following expressions and show heir hierarchy

a)  g = big / 2 * 4 / big - big + abc /3;
    (abc =  2.5, big = 2 , assume g to be a float)
    
b)  on = ink * act /2 + 3 /2 * act + 2 + toh;
    (int = 4, act = 1, tig =3.2, assume on to be an int)
    
c)  s = qui * add / 4 - 6 / 2 + 2 / 3 * 6 / god;
    (qui = 4, add = 2, god =2, assume s to be an int)

d)  j = 1 / 3 * a / 4 - 6 / 2 + 2 /3 *6 / h;
    ( a = 4, h = 3, assume s to be an int)

"""

abc, big,g= 2.5,2 ,0.0

g = (big/2) * (4/big) - big + (abc/3)

print("Value for g: ",g)

ink, act,tig = 4,1,3.2

on = ink * (act/2) + (3/2) * (act+2) + tig
print("Value for on: ",int(on))

qui , add, god = 4,2,2
s = qui * (add / 4) - (6 / 2) + (2 / 3) * (6 / god)
print("Value for S: ",int(s))

a,h = 4,3
j = (1 / 3) * (a / 4) - (6 / 2) + (2 /3) * (6 / h)
print("Value for J: ",int(j))
