import pytest

@pytest.fixture
def numbers():
    x = 2
    return [2*x for x in range(1,11)]

def test_method1(numbers):
    x = 30
    assert numbers[-1] == x
    

def test_method2(numbers):
    y = 20
    assert numbers[-1] == y
