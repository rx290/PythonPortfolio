"""
Write a a recursive function that finds and returns the sum of the elements of an array.
Also test that function!
"""
elements =input("Please enter comman seprated values you want to add in an array:\n")
arr = int(elements.split(sep=','))
sum = 0
def array_element_adder(some_list):
    global sum
    