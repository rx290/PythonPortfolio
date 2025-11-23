"""Write a Python program to create a file and write some text and rename the file name""" 
import os
file_name = input("Please enter filename that will be replace the initial one: ")
with open('Random.txt', 'a+') as file:
   file.write('Python program to create a symbolic link and read it to decide the original file pointed by the link.')
print('\nInitial file/dir name:', os.listdir())
with open('Random.txt', 'a+') as file:
   print('\nContents of Random.txt:', repr(file.read()))
   file.write("\nThis is some text added before renaming the file")   
os.rename('Random.txt', file_name+'.txt')
print('\nAfter renaming initial file/dir name:', os.listdir())
with open(file_name+'.txt', 'r') as file:
   print('\nContents of {}.txt:'.format(file_name), repr(file.read()))
   
   
"""
File Modes:

r:   Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.

rb:  Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.

r+:  Opens a file for both reading and writing. The file pointer will be at the beginning of the file.

rb+: Opens a file for both reading and writing in binary format. The file pointer will be at the beginning of the file.

w:   Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

wb:  Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

w+:  Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

wb+: Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

a:   Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

ab:  Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

a+:  Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

ab+: Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
"""