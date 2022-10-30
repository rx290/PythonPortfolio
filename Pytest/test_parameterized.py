import pytest

@pytest.mark.parametrize("x,y",[(3,4)])
def test_method(x,y):
    assert [3,6,9] == [x*i for i in range(1,4)]
    # assert [4,8,12] == [y*i for i in range(1,4)]
    
# use @pytest.mark.skip for skipping the test case
# use @pytest.mark.xfail for avoiding the failed test case count increment