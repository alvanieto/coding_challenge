import pytest

from two_strings import twoStrings


@pytest.mark.parametrize('s1, s2, expected', [
    ('hello', 'world', 'YES'),
    ('hi', 'world', 'NO'),
    ('a', 'art', 'YES'),
])
def test_two_strings(s1, s2, expected):
    assert twoStrings(s1, s2) == expected
