""" Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path. """ 
import os

path= input("Please enter a path: ")

if os.access(path,os.F_OK):
    print("File exists!")
    print("File is readable!") if (path,os.R_OK) else print("File is not readable!")
    print("File is writeable!") if (path,os.W_OK) else print("File is writeable!")
    print("File is executable!") if (path,os.X_OK) else print("File is not executable!")
else:
    print("File does not exist!")
