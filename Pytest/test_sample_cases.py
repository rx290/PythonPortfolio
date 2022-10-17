import pytest


def name(x:str):
    y ="Your Name is "+x
    return y

# This one will Pass
def test_func1():
    assert name("Asad") == "Your Name is Asad"

def func(x):
    return x + 5

def test_func3():
    assert func(3) == 8
    
    
test_func1()
test_func3()