"Write a Python program to remove newline characters from a file" 

with open("./File Handling/file_handling_basic/sample.txt",'r') as f:
    lines = [lines for lines in f]
    global newcorpus
    newcorpus = ""
    for i in lines:
        newcorpus += i
    print(newcorpus.replace('\n', ''))