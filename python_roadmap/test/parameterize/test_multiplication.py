# parameterizing of a test is done to run test agains multiple sets of inputs
# @pytest.mark.parametrize
# can create multiple parameters within the same file 

import pytest

# creating multiple set of inputs
@pytest.mark.parametrize("num, output",[(1, 11), (2, 22), (3, 33), (4, 44)])
def test_multiplication_11(num, output):
    assert num * 11 == output

@ pytest.mark.parametrize("num, output",[(1, 2),(2, 4), (3, 6), (4, 8), (5, 10)])
def test_multiplication_2(num, output):
    assert num * 2 == output