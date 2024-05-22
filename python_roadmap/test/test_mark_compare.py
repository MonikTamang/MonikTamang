import pytest # import pytest to user mark

# creating mark
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.other
def test_less():
   num = 100
   assert num < 200

