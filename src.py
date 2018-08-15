"""
Penniless pilgrim riddle recursive brute force solution.

See:
    https://www.youtube.com/watch?v=6sBB-gRhfjE
"""

MOVES = {
    'N': (-1, 0),
    'E': (0, +1),
    'S': (+1, 0),
    'W': (0, -1)
}

TAXES = {
    'N': lambda tax: tax / 2,
    'E': lambda tax: tax + 2,
    'S': lambda tax: tax * 2,
    'W': lambda tax: tax - 2
}

MIN_X = MIN_Y = 0
MAX_X = MAX_Y = 4


class WalkError(ValueError):
    pass


class Pilgrim(object):

    def __init__(self, pos=(MIN_Y, MIN_X), tax=0):
        self.pos = pos
        self.tax = tax
        self.path = []
        self.visited_edges = set()

    def __repr__(self):
        return f'{self.__class__.__name__}(pos={self.pos}, tax={self.tax})'

    def find_path(self, target_pos, target_tax):
        for direct in MOVES:
            clone = self._clone()

            try:
                clone.walk(direct)
            except WalkError:
                continue

            if clone.pos == target_pos and clone.tax == target_tax:
                return clone.path

            path = clone.find_path(target_pos, target_tax)

            if path is not None:
                return path

        return None

    def walk(self, direct):
        new_pos = self._calc_new_pos(direct)

        if self._can_reach(new_pos):
            edge = self._make_edge(new_pos)

            if edge not in self.visited_edges:
                self.pos = new_pos
                self.path.append(direct)
                self.visited_edges.add(edge)
                self.tax = self._calc_tax(direct)

            else:
                raise WalkError(f'Edge already visited: {edge}')

        else:
            raise WalkError(f'Invalid pos: {new_pos}')

    def _clone(self):
        clone = self.__class__()

        clone.pos = self.pos
        clone.tax = self.tax
        clone.path = self.path.copy()
        clone.visited_edges = self.visited_edges.copy()

        return clone

    def _calc_new_pos(self, direct):
        return tuple(map(sum, zip(self.pos, MOVES[direct])))

    @staticmethod
    def _can_reach(pos):
        y, x = pos
        return MIN_X <= x <= MAX_X and MIN_Y <= y <= MAX_Y

    def _make_edge(self, new_pos):
        return frozenset([self.pos, new_pos])

    def _calc_tax(self, direct):
        return TAXES[direct](self.tax)


def main():
    pilgrim = Pilgrim()

    pilgrim.walk('E')
    pilgrim.walk('E')

    path = pilgrim.find_path(
        target_pos=(4, 4),
        target_tax=0
    )
    print(path)


if __name__ == '__main__':
    main()
