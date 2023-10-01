"""
a. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

b. Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line.
""" 
import os
from string import ascii_letters
directory = 'AlphabetFiles'
parentDirectory = "./File Handling/file_handling_basic/"
path=os.path.join(parentDirectory,directory)
os.mkdir(path)
path = path+'/'
global filename
filename = ''
for i in range(26,52):
    letter = ascii_letters[i]
    filename = path+letter+'.txt'
    with open(filename,'w') as e:
        pass