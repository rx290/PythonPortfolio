""" Convert the following equations into corresponding python statements according to operators precedence.

a)      8.8 ( a+ b) 2 / c - 05 + a a / (q + r)
    Z= ___________________________________________
                     (a + b ) * (1/m)

b)      - b + (b * b) + 2 4ac
    X = ______________________
                2a

c)      2v + 6.22 (c + d)
    R = _________________
                g + v

d)      7.7b (xy + a) / c - 0.8 + 2b
    h = ______________________________
                (x + a)( 1 / y)
    
"""
a, b, c, q, r, v , x, y, m, g, d = 1,2,3,4,5,6,7,8,9,10,11
z_nom = ((8.8 * (a + b)) * 2 / c - 5 + (a * (a / (q + r))))
z_denom = (a + b) * (1 / m)

x_nom = - b + (b * b) + (2*(4*a*c))
x_denom= 2*a

r_nom = 2 * v + (6.22 *(c+d))
r_denom= g + v

h_nom = ((7.7 * b *((x*y) + a)) / (c - 0.8 + 2*b)) 
h_denom = (x + a) * (1 / y)

z = z_nom / z_denom
X = x_nom / x_denom
r = r_nom / r_denom
h = h_nom / h_denom


print(z,x,r,h)