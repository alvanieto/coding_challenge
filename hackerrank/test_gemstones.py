import pytest

from gemstones import gemstones


@pytest.mark.parametrize('data, expected', [
    (['abcdde', 'baccd', 'eeabg'], 2),
    (['abc', 'deg'], 0),
    (['abc', 'abc'], 3),
    (['abc', 'bca'], 3),
    (['a', 'b'], 0),
    (['a', 'a'], 1),
])
def test_gemstones(data, expected):
    assert gemstones(data) == expected
