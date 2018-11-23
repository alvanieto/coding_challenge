import pytest

from love_letter_mistery import theLoveLetterMystery


@pytest.mark.parametrize('data, expected', [
    ('abc', 2),
    ('abcba', 0),
    ('abcd', 4),
    ('cba', 2),
])
def test_love_letter_mistery(data, expected):
    assert theLoveLetterMystery(data) == expected
