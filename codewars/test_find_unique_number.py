import pytest

from find_unique_number import find_uniq


@pytest.mark.parametrize('data, expected', [
    ([ 1, 1, 1, 2, 1, 1], 2),
    ([ 0, 0, 0.55, 0, 0], 0.55),
    ([ 3, 10, 3, 3, 3, 3], 10),
    ([ 1, 2, 2, 2, 2, 2], 1),
    ([ 5, 5, 4, 5, 5, 5], 4),
])
def test_find_unique_number(data, expected):
    assert find_uniq(data) == expected
