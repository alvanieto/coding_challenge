import pytest

from making_anagram import makeAnagram


@pytest.mark.parametrize('a, b, expected', [
    ('cde', 'abc', 4),
    ('ccde', 'abc', 5),
    ('ab', 'a', 1),
    ('ab', 'ab', 0),
    ('abbbcdd', 'abbd', 3),
    ('abbbc', 'abbd', 3),
    ('abc', 'def', 6),
    ('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke', 30),
])
def test_make_anagram(a, b, expected):
    assert makeAnagram(a, b) == expected
