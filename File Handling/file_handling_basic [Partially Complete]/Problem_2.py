"Write a Python program to read a file line by line store it into an array." 

with open('./File Handling/file_handling_basic/sample.txt','r') as f:
    arr = [lines for lines in f]
    print(arr)