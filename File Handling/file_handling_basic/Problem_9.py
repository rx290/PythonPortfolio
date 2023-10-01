"Write a Python program to combine each line from first file with the corresponding line in second file." 

with open("./File Handling/file_handling_basic/sample.txt","r") as f:
    with open("./File Handling/file_handling_basic/DestinationFile.txt","r") as e:
        with open("./File Handling/file_handling_basic/Taks9File.txt","a+") as t:
            newLine = ""
            for i in f:
                for j in e:
                    newLine = i + j
                    t.write(newLine)
            print(t) 