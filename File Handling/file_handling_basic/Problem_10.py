"Write a Python program to read a random line from a file." 

from random import randint
with open("./File Handling/file_handling_basic/sample.txt","r") as f:
    Line = f.readline(randint(0,30))
    words = Line.split(sep=' ')
    print(words[randint(0,len(words))])