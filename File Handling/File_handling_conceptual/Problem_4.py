"""
Write a function in Python to read lines from a text file "notes.txt". Your function should find and display the occurrence of the word "the".

For example: If the content of the file is:
"India is the fastest-growing economy. India is looking for more investments around the globe. The whole world is looking at India as a great market. Most of the Indians can foresee the heights that India is capable of reaching."

The output should be 5.
""" 

import re
corpus = "India is the fastest-growing economy. India is looking for more investments around the globe. The whole world is looking at India as a great market. Most of the Indians can foresee the heights that India is capable of reaching."
with open(file='/run/media/drago/Fast Drive/PythonPortfolio/File Handling/File_handling_conceptual/sample.txt',mode='a+') as file:
    file.write(corpus)
    file.close
    
with open(file='/run/media/drago/Fast Drive/PythonPortfolio/File Handling/File_handling_conceptual/sample.txt',mode='r') as of:
    read_corpus = of.read()
    checker = re.compile(r'\b[tT]he\b')
    _str_checker = checker.findall(read_corpus)
    print("Number of the in the corpus is: ",_str_checker)
    of.close()