import pytest

from counting_valley import countingValleys


@pytest.mark.parametrize('data, expected', [
    ('UDDDUDUU', 1),
    ('UUUUUUUU', 0),
    ('DUDUUUDDDU', 3),
    ('DUDU', 2),
    ('DU', 1),
    ('UD', 0),
    ('UDDDDUU', 0),
    ('DDDUDUDUUU', 1),
])
def test_counting_valley(data, expected):
    assert countingValleys(1, data) == expected
