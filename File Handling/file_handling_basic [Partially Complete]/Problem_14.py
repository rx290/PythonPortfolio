"Write a Python program to extract characters from various text files and puts them into a list." 
from random import randint

with open("./File Handling/file_handling_basic/sample.txt",'r') as f:
    with open("./File Handling/file_handling_basic/Taks9File.txt",'r') as e:
        with open("./File Handling/file_handling_basic/DestinationFile.txt",'r') as t:
            characterList = []
            charsFromFileOne, charsFromFileTwo, charsFromFileThree = '','',''
            for i in f:
                for chars in range(0,5):
                    randomline = f.readline(randint(0,30))
                    print(randomline)
                    # charsFromFileOne += randomline[] + ' '
            for j in e:
                for chars in range(0,5):
                    pass
                    # randomline1 = e.readline(randint(0,30))
                    # charsFromFileOne += randomline1[randint(0,12)] + ' '
            for k in t:
                for chars in range(0,5):
                    # randomline2 = t.readline(randint(0,30))
                    # charsFromFileOne += randomline2[randint(0,12)] + ' '
                    pass
                    
            characterList.append("Characters from file One: "+charsFromFileOne)
            characterList.append("Characters from file two: "+charsFromFileTwo)
            characterList.append("Characters from file three: "+charsFromFileThree)
            print(characterList)