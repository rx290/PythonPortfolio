"Write a Python program to create an instance of a specified class and display the namespace of the said instance." 

class MySampleClass:
    def SampleMethod(*args):
        pass
    def HelloWorld(*args):
        return print("Hello World!")
    
instance = MySampleClass()
print(dir(instance))