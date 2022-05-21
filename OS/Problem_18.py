"""Write a Python program to start a new process replacing the current process.""" 
import os
import sys
program = "python"
arguments = ["problem_1.py"]
print(os.execvp(program, (program,) + tuple(arguments)))
print("Goodbye")