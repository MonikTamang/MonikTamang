# Function name must include 'test' at the beginning if you want to test the function
# pytest will run all the test if name is not specified

import math

def test_sqrt():
    num = 25
    # assert are used to check if the actual result match the expected result
    # assertion will generate exception automatically when test donot match the result
    # You can also provide message for AssertionError

    assert math.sqrt(num) == 5  # test passed as square root of 25 is 5

def testsquare():
    num = 7
    assert 7*7 == 40  # test failed as 7*7 == 49 

def testquality():
    assert 10 == 11  # test failed as 10 is not equal to 11


# Notes
# pytest 'for all test to run at once'
# pytest -v 'all test with more details'
# pytest testname.py -v 'individual test files'
# pytest -k <substring> -v 'files with substring only'
