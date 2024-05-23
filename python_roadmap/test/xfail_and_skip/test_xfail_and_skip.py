# Conditions
# Test is not relevant due to some reason
# New feature is being implemented but already added a test for that feature
# pytest will execute 'xfailed' test, but it will not consider test as 'passed' or 'failed' and doesnot provide details
# 'skip' is used to skip the test
# @pytest.mark.xfail
# @pytest.mark.skip

import pytest

# if xfail is failed, output: 'XFAIL'
@pytest.mark.xfail
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100

# if xfail is passed, output: 'XPASS'
@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

# skip, output: 'SKIP'
@pytest.mark.skip
@pytest.mark.other
def test_less():
   num = 100
   assert num < 200