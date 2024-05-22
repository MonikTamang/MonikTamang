import pytest # need to import pytest for fixture

# Fixtures are functions, which will run before each test function 
# Used to feed some data to the test such as database connections, urls, input data
# Insead of running same code for every test, we can attach fixture funcation to the tests and it will return the data before executing each test

# creating a fixture function the returns a value
@pytest.fixture
def input_value():
    input = 39
    return input

# creating test cases/ functions
def test_divisible_by_3(input_value):
    assert input_value % 3 == 0, f"{input_value} is not divisible by 3."  # You can also provide the message for AssertionError

def test_divisible_by_6(input_value):
    assert input_value % 6 == 0, f"{input_value} is not divisible by 6."

# using the substring method to run test
# pytest -k divisible <substring> -v
