import pytest # need to import pytest for fixture

# default fixture name conftest.py
# Fixtures are functions, which will run before each test function 
# Used to feed some data to the test such as database connections, urls, input data
# Insead of running same code for every test, we can attach fixture funcation to the tests and it will return the data before executing each test

# creating a fixture function the returns a value
@pytest.fixture
def input_value():
    input = 39
    return input

# Note: 'conftest' is the default name for naming a fixture
# confest.py need not be imported as pytest automatically discovers it.
# if you use other name you need to import them
