import pytest
import src


@pytest.fixture(name='pilgrim')
def fixture_pilgrim():
    return src.Pilgrim()


@pytest.fixture(name='riddle')
def fixture_riddle(pilgrim):
    return src.Riddle(pilgrim)


class TestPilgrim(object):

    def test_sanity(self, pilgrim):
        assert pilgrim.pos == (0, 0)
        assert pilgrim.tax == 0

    def test_unreachable_pos(self, pilgrim):
        with pytest.raises(ValueError):
            pilgrim.walk('W')
        assert pilgrim.tax == 0

        with pytest.raises(ValueError):
            pilgrim.walk('N')
        assert pilgrim.tax == 0

    def test_walk_by_unvisited_edges(self, pilgrim):
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

    def test_walk_by_visited_edges(self, pilgrim):
        pilgrim.walk('E')
        assert pilgrim.pos == (0, 1)
        assert pilgrim.tax == 2

        with pytest.raises(ValueError):
            pilgrim.walk('W')
        assert pilgrim.pos == (0, 1)
        assert pilgrim.tax == 2

        pilgrim.walk('E')
        assert pilgrim.pos == (0, 2)
        assert pilgrim.tax == 4


class TestRiddle(object):

    def test_sanity(self, riddle):
        assert riddle.pilgrim.pos == (0, 0)
        assert riddle.pilgrim.tax == 0
        assert riddle.target_pos == (4, 4)
        assert riddle.target_tax == 0

    def test_clone(self, riddle):
        orig = riddle.pilgrim
        clone = riddle.clone_pilgrim(orig)

        orig.walk('E')
        assert orig.pos == (0, 1)
        assert orig.tax == 2
        assert orig.route == ['E']
        assert orig.visited_edges == {frozenset([(0, 0), (0, 1)])}
        assert clone.pos == (0, 0)
        assert clone.tax == 0
        assert clone.route == []
        assert clone.visited_edges == set()

        clone.walk('S')
        assert orig.pos == (0, 1)
        assert orig.tax == 2
        assert orig.route == ['E']
        assert orig.visited_edges == {frozenset([(0, 0), (0, 1)])}
        assert clone.pos == (1, 0)
        assert clone.tax == 0
        assert clone.route == ['S']
        assert clone.visited_edges == {frozenset([(0, 0), (1, 0)])}
