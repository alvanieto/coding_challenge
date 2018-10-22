import pytest

from ransom_note import checkMagazine


@pytest.mark.parametrize('magazine, note, expected', [
    ('give me one grand today night', 'give one grand today', True),
    ('two times three is not four', 'two times two is four', False),
    ('two times three is not four', 'two times is four', True),
    ('Two times', 'two times', False),
    ('times', 'two times', False),
])
def test_ransom_note(magazine, note, expected):
    assert checkMagazine(magazine, note) == expected
