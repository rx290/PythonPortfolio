"""Write a Python program to list only directories, files and all directories, files in a specified path. """ 
import os
path = input("Please enter path: ")
directory = os.listdir(path)
dirs, files = [],[]
dir_finder = lambda x: dirs.append(x) if os.path.isdir(os.path.join(path, x)) else files.append(x)
lst = list(map(dir_finder,directory))
print("Directories: ",dirs,"\nFiles: ",files)