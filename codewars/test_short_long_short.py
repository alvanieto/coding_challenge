import pytest

from short_long_short import solution


@pytest.mark.parametrize('a, b, expected', [
    ('45', '1', '1451'),
    ('13', '200', '1320013'),
    ('Soon', 'Me', 'MeSoonMe'),
    ('U', 'False', 'UFalseU'),
    ('A', 'B', 'BAB'),
    ('', '', ''),
])
def test_short_long_short(a, b, expected):
    assert solution(a, b) == expected
