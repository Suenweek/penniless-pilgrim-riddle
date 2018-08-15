MOVES = {
    'N': (-1, 0),
    'E': (0, +1),
    'S': (+1, 0),
    'W': (0, -1)
}

TAXES = {
    'N': lambda tax: tax // 2,
    'E': lambda tax: tax + 2,
    'S': lambda tax: tax * 2,
    'W': lambda tax: tax - 2
}

MIN_X = MIN_Y = 0
MAX_X = MAX_Y = 4


class Pilgrim(object):

    def __init__(self, pos=(MIN_Y, MIN_X), tax=0):
        self.pos = pos
        self.tax = tax
        self.route = []
        self.visited_edges = set()

    def __repr__(self):
        return f'{self.__class__.__name__}(pos={self.pos}, tax={self.tax})'

    def walk(self, dir):
        new_pos = self._calc_new_pos(dir)

        if self._can_reach(new_pos):
            edge = self._make_edge(new_pos)

            if edge not in self.visited_edges:
                self.pos = new_pos
                self.route.append(dir)
                self.visited_edges.add(edge)
                self.tax = self._calc_tax(dir)

            else:
                raise ValueError(f'Road already walked: {edge}')

        else:
            raise ValueError(f'Invalid pos: {new_pos}')

    def _calc_new_pos(self, dir):
        return tuple(map(sum, zip(self.pos, MOVES[dir])))

    @staticmethod
    def _can_reach(pos):
        y, x = pos
        return MIN_X <= x <= MAX_X and MIN_Y <= y <= MAX_Y

    def _make_edge(self, new_pos):
        return frozenset([self.pos, new_pos])

    def _calc_tax(self, dir):
        return TAXES[dir](self.tax)


class Riddle(object):

    def __init__(self, pilgrim, target_pos=(MAX_Y, MAX_X), target_tax=0):
        self.pilgrim = pilgrim
        self.target_pos = target_pos
        self.target_tax = target_tax

    def solve(self):
        raise NotImplementedError

    def clone_pilgrim(self, orig):
        clone = Pilgrim()

        clone.pos = orig.pos
        clone.tax = orig.tax
        clone.route = orig.route.copy()
        clone.visited_edges = orig.visited_edges.copy()

        return clone


def create_initial_pilgrim():
    pilgrim = Pilgrim()
    for _ in range(2):
        pilgrim.walk('E')
    return pilgrim


def main():
    pilgrim = create_initial_pilgrim()
    riddle = Riddle(pilgrim)
    riddle.solve()


if __name__ == '__main__':
    main()
