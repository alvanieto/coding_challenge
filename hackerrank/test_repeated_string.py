import pytest

from repeated_string import repeatedString


@pytest.mark.parametrize('data, length, expected', [
    ('aba', 10, 7),
    ('a', 1000000000000, 1000000000000),
    ('abaa', 100, 75),
    ('bbb', 100, 0),
    ('bbba', 3, 0),
    ('bbba', 4, 1),
])
def test_repetated_string(data, length, expected):
    assert repeatedString(data, length) == expected
