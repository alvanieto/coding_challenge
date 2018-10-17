import pytest

from jumping_clouds import jumpingOnClouds


@pytest.mark.parametrize('data, expected', [
    ([0, 0, 1, 0, 0, 1, 0], 4),
    ([0, 0, 0, 1, 0], 2),
    ([0, 0, 0, 1, 0, 0], 3),
    ([0, 0], 1),
])
def test_jumping_clouds(data, expected):
    assert jumpingOnClouds(data) == expected
