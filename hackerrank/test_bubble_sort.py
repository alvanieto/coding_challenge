import pytest

from bubble_sort import countSwaps


@pytest.mark.parametrize('a, swaps, expected', [
    ([3, 2, 1], 3, [1, 2, 3]),
    ([1, 2, 3], 0, [1, 2, 3]),
    ([4, 2, 3, 1], 5, [1, 2, 3, 4]),
])
def test_count_swaps(a, swaps, expected):
    assert countSwaps(a) == (swaps, expected)
