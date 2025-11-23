"""Write a Python program to iterate over a root level path and print all its sub-directories and files, also loop over specified dirs and files.""" 
import os

print('Iterate over a root level path:')
path = '/tmp/'
for root, dirs, files in os.walk(path):
 print(root)