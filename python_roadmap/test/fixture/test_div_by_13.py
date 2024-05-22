# calling fixture function value (input_value)
# creating test cases/ functions
import pytest

def test_divisible_by_13(input_value):
    assert input_value % 13 == 0, f"{input_value} is not divisible by 3."  # You can also provide the message for AssertionError

# using the substring method to run test
# pytest -k divisible <substring> -v