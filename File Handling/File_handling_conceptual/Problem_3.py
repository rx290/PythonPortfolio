"""
Write a function in Python to count and display the total number of words in a text file
""" 
with open(file='/run/media/drago/Fast Drive/PythonPortfolio/File Handling/File_handling_conceptual/sample.txt', mode='r') as file:
    corpus= file.read()
    words = corpus.split()
    print("Total number of words in the corpus are: ",len(words))