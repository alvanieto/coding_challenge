import pytest

from alternating_characters import alternatingCharacters


@pytest.mark.parametrize('data, expected', [
    ('AAAA', 3),
    ('BBBBB', 4),
    ('ABABABAB', 0),
    ('BABABA', 0),
    ('AAABBB', 4),
])
def test_alternating_characters(data, expected):
    assert alternatingCharacters(data) == expected
