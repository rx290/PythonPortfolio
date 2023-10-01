"Write a Python program to count the number of lines in a text file. " 

with open("./File Handling/file_handling_basic/sample.txt","r") as f:
    wordCount = 0
    for i in f:
        wordCount = wordCount+1
    print(wordCount)