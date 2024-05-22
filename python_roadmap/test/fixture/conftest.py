import pytest # need to import pytest for fixture

# Fixtures are functions, which will run before each test function 
# Used to feed some data to the test such as database connections, urls, input data
# Insead of running same code for every test, we can attach fixture funcation to the tests and it will return the data before executing each test

# creating a fixture function the returns a value
@pytest.fixture
def input_value():
    input = 39
    return input


