import pytest

from criba_eratostenes import criba_eratostenes


@pytest.mark.parametrize('max_, expected', [
    (1, []),
    (2, [2]),
    (3, [2, 3]),
    (4, [2, 3]),
    (30, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
])
def test_criba_eratostenes(max_, expected):
    assert criba_eratostenes(max_) == expected
