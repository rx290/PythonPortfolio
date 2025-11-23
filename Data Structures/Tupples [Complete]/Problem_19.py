"""Write a Python program to compute element-wise sum of given tuples. 
Original lists:
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)
Element-wise sum of the said tuples:
(6, 9, 8, 6) """ 
t,u,p = (1, 2, 3, 4),(3, 5, 2, 1),(2, 2, 3, 1)
total = []
if len(t) == len(u) == len(p):
    for i in range(len(t)):
        total.append(t[i]+u[i]+p[i])
    print(total)
else:
    print("Tuples are not equal in length!")