# Test using mark (group test case using mark)
# must import pytest to use mark

import pytest
import math

# creating marker
@pytest.mark.square
def test_sqrt():
    num = 25
    # assert are used to check if the actual result match the expected result
    # assertion will generate exception automatically when test donot match the result

    assert math.sqrt(num) == 5  # test passed as square root of 25 is 5

@pytest.mark.square
def testsquare():
    num = 7
    assert 7*7 == 40  # test failed as 7*7 == 49 

@pytest.mark.others
def testquality():
    assert 10 == 11  # test failed as 10 is not equal to 11


# Notes
# pytest -m <markername> -v 'files with the marker'
