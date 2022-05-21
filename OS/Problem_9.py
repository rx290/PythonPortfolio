"""Write a Python program to retrieve the current working directory and change the dir (moving up one).""" 
import os
print('Current working directory:', os.getcwd())
print('Changing the directory moving to parent directory:', os.pardir)
os.chdir(os.pardir)
print('Current working directory after switching:', os.getcwd())
