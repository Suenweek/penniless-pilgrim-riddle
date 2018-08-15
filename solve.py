class Pilgrim(object):

    GRID = [
        [0.0, 0.1, 0.2, 0.3, 0.4],
        [1.0, 1.1, 1.2, 1.3, 1.4],
        [2.0, 2.1, 2.2, 2.3, 2.4],
        [3.0, 3.1, 3.2, 3.3, 3.4],
        [4.0, 4.1, 4.2, 4.3, 4.4]
    ]

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
    MAX_X = MAX_Y = len(GRID) - 1

    def __init__(self, pos=(0, 0), tax=0):
        self._pos = pos
        self.tax = tax

    def __repr__(self):
        return f'Pilgrim(pos={self.pos}, tax={self.tax})'

    def move(self, dir):
        move = self.MOVES[dir]
        self.pos = tuple(map(sum, zip(self.pos), move))
        self.tax = self.TAXES[dir](self.tax)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, new_pos):
        y, x = new_pos
        if self.MIN_X <= x <= self.MAX_X and self.MIN_Y <= y <= self.MAX_Y:
            self._pos = new_pos
        else:
            raise ValueError(f'Unreachable pos: {new_pos}')


def main():
    pass


if __name__ == '__main__':
    main()
