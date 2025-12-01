"Write a python program to find the longest words." 

with open(file='/run/media/drago/Fast Drive/PythonPortfolio/File Handling/file_handling_basic [Partially Complete]/DestinationFile.txt',mode='r') as file:
    corpus = file.read()
    words = corpus.split()
    len_longest_word = len(max(words,key=len))
    longest_word =  [word for word in words if len(word)==len_longest_word]
    print("corpus: ",corpus,"\nLongest Word: ",longest_word)
    