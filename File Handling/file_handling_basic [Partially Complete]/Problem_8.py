"Write a Python program to copy the contents of a file to another file " 


with open("./File Handling/file_handling_basic/sample.txt","r") as f:
    with open("./File Handling/file_handling_basic/DestinationFile.txt","a+") as e:
        lines = [lines for lines in f]
        for line in lines:
            e.write(line)