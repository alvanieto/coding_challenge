import pytest

from format_word_sentence import format_words


@pytest.mark.parametrize('words, expected', [
    (['one', 'two', 'three', 'four'], 'one, two, three and four'),
    (['one'], 'one'),
    (['one', '', 'three'], 'one and three'),
    (['one', 'two', ''], 'one and two'),
    ([], ''),
    (None, ''),
    ([''], '')
])
def test_format_words(words, expected):
    assert format_words(words) == expected
