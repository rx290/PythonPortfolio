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

# Class based Test Suite

class TestCase:
    def Test_One(args):
        random_string = "He is a boy"
        assert 'e' in random_string
 
    def Test_Two(args):
        sum = 4+4
        assert 8 == sum
 