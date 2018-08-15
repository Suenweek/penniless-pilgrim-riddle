import pytest
from solve import Pilgrim


@pytest.fixture(name='pilgrim')
def fixture_pilgrim():
    return Pilgrim()


def test_sanity(pilgrim):
    assert pilgrim.pos == (0, 0)
    assert pilgrim.tax == 0


def test_unreachable_pos(pilgrim):
    with pytest.raises(ValueError):
        pilgrim.walk('W')
    assert pilgrim.tax == 0

    with pytest.raises(ValueError):
        pilgrim.walk('N')
    assert pilgrim.tax == 0


def test_walk_by_unvisited_edges(pilgrim):
    pilgrim.walk('E')
    assert pilgrim.pos == (0, 1)
    assert pilgrim.tax == 2

    pilgrim.walk('E')
    assert pilgrim.pos == (0, 2)
    assert pilgrim.tax == 4

    pilgrim.walk('S')
    assert pilgrim.pos == (1, 2)
    assert pilgrim.tax == 8

    pilgrim.walk('S')
    assert pilgrim.pos == (2, 2)
    assert pilgrim.tax == 16

    pilgrim.walk('W')
    assert pilgrim.pos == (2, 1)
    assert pilgrim.tax == 14

    pilgrim.walk('N')
    assert pilgrim.pos == (1, 1)
    assert pilgrim.tax == 7


def test_walk_by_visited_edges(pilgrim):
    pilgrim.walk('E')
    assert pilgrim.pos == (0, 1)
    assert pilgrim.tax == 2

    with pytest.raises(ValueError):
        pilgrim.walk('W')
    assert pilgrim.pos == (0, 1)
    assert pilgrim.tax == 2
