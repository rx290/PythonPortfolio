import pytest

def even_odd(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

@pytest.mark.TestCase1
def test_Case1():
    assert even_odd(4) =="Even"

@pytest.mark.TestCase2
def test_Case2():
    assert even_odd(47) =="Odd"
    
    
#To run individual testcases go to the subdir and run this command filename.py -k markername -v
# For Custom markers initiate a pytest.ini and declare your custom markets there
