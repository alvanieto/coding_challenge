import pytest

from minimum_absolute_difference import minimumAbsoluteDifference


@pytest.mark.parametrize('arr, expected', [
    ([3, -7, 0], 3),
    ([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75], 1),
    ([1, -3, 71, 68, 17], 3),
])
def test_minimum_absolute_difference(arr, expected):
    assert minimumAbsoluteDifference(arr) == expected
