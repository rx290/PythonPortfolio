""" Write a Python program calculate the product, multiplying all the numbers of a given tuple. 
Original Tuple:
(4, 3, 2, 2, -1, 18)
Product - multiplying all the numbers of the said tuple: -864
Original Tuple:
(2, 4, 8, 8, 3, 2, 9)
Product - multiplying all the numbers of the said tuple: 27648""" 
tup = (4, 3, 2, 2, -1, 18)
def TupleProduct(tup,i,length):
    product= 0
    if i == length-1:
        return product
    else:
        i += 1
        TupleProduct(tup,i,length)
    