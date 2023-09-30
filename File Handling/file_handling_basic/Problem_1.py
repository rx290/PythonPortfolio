"""
a. Write a Python program to read an entire text file.

b. Write a Python program to read first n lines of a file.

c. Write a Python program to append text to a file and display the text.

d. Write a Python program to read last n lines of a file.

e. Write a Python program to read a file line by line and store it into a list. 

f. Write a Python program to read a file line by line store it into a variable.
""" 

# Task a
with open("./File Handling/file_handling_basic/sample.txt", 'r') as f:
    print(f.read())
    
# Task b
with open("./File Handling/file_handling_basic/sample.txt",mode='r')as f:
    lines = [lines for lines in f][:3]
    print("N number of lines are as follows: \n",lines)
    
#