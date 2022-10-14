import pytest


def name(x:str):
    y ="Your Name is "+x
    return y

# This one will Pass
def TestCase1():
    assert name("Asad") == "Your Name is Asad"

# This one will fail
# def TestCase2():
#     assert name("Asad") == "Your Name is "
    

name("Asad")
TestCase1()
# TestCase2()