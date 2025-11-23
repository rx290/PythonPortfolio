" Write a Python program to write a list to a file." 

with open("./File Handling/file_handling_basic/sample1.txt",'a') as f:
    newList = [1,2,3,4,5,'This is a sample list']
    f.write("Here is the list that was appended to this file: ",str(newList))