""" Write a Python program to scan a specified directory and identify the sub directories and files."""
import  os
path = input("Please input path: ")
items = os.scandir(path)

print(items)
for item in items:
    if os.path.isdir(item):
        print(item,"is a directory.")
    elif os.path.isfile(item):
        print(item,"is a file.")
    elif os.path.is_symlink(item):
        print(item,"is a link.")
    else:
        print(item.name,"is an unknown file type.")
        