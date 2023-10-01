" Write a Python program to get the file size of a plain file." 
import os

stats=os.stat("./File Handling/file_handling_basic/sample.txt")
print("File size is: ",stats[6])