"""
Ask user for an array/list input, then create a perfect shuffle for them and print that array/list.
Perfect shuffle is like this
Split the array/list into odd and evens then place two randomly odd and even number until you run out of elements

eg:

user: [11,22,33,44,55,66,77,88]
perfect shuffle step 1: [11,33,55,77] [22,44,66,88]
perfect shuffle step 2: [11,55,22,66,33,77,44,88] 
"""
num = int(input("Please enter the size of array: "))
ls = [int(input("Please enter {} number for your array: ".format(x+1))) for x in range(num)]
is_even = True if num%2==0 else False
perfect_shuffle =[]

if is_even:
    print("You have given us an even array split will be clean!")
    even_ls = [ x for x in ls if x%2==0 ]
    ls = [x for x in ls if x%2!=0]
    print("odd shuffle: ",ls,'\neven shuffle: ',even_ls)
    perfect_shuffle = [element for x in range(0,num//2) for element in [ls[x],even_ls[x]]]
    print("Perfect Shuffle: ",perfect_shuffle)
else:
    print("We will be dropping the last one as it will affect the clean split as the list provided is of Odd number.")
    ls.pop(-1)
    even_ls = [ x for x in ls if x%2==0 ]
    ls = [x for x in ls if x%2!=0]
    print("odd shuffle: ",ls,'\neven shuffle: ',even_ls)
    perfect_shuffle = [element for x in range(0,num//2) for element in [ls[x],even_ls[x]]]
    print("Perfect Shuffle: ",perfect_shuffle)
    