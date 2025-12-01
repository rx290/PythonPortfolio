"""
Write a Python program to get the class name of an instance in Python.
"""

class Person:
    pass  # An empty block
p = Person()
print(p.__class__.__name__)