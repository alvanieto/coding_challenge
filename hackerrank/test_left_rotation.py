import pytest

from left_rotation import rotLeft


@pytest.mark.parametrize('data, num_rot, expected', [
    ([1, 2, 3, 4, 5], 4, [5, 1, 2, 3, 4]),
    ([1, 2, 3, 4, 5], 1, [2, 3, 4, 5, 1]),
    ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
])
def test_left_rotation(data, num_rot, expected):
    assert rotLeft(data, num_rot) == expected
