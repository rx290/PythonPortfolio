"""Write a Python program to get the name of the operating system (Platform independent), information of current operating system, 
current working directory, print files and directories in the current directory and raises error in the case of invalid or inaccessible file names and paths. """ 
import os

# Get Family name of Operating System
print(os.name)
# Get Distro Name 
print(os.uname())
# Get current Working directory
print(os.getcwd())
# List of all directories and files in the folder
print(os.listdir('.'))

# Checking if a file exist or not
try:
   filename = 'Problem_2.py'
   f = open(filename, 'r')
   text = f.read()
   f.close()
except IOError:
   print('Not accessed or problem in reading: ' + filename)