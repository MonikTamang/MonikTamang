# calling fixture function value (input_value)
# creating test cases/ functions

def test_divisible_by_3(input_value):
    assert input_value % 3 == 0, f"{input_value} is not divisible by 3."  # You can also provide the message for AssertionError

def test_divisible_by_6(input_value):
    assert input_value % 6 == 0, f"{input_value} is not divisible by 6."

# using the substring method to run test
# pytest -k divisible <substring> -v