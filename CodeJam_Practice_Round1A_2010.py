#! /usr/bin/env python
from AutoMeasure import AutoMeasure

__author__ = 'Mohamed.Elsherif'


@AutoMeasure
def main():
    with open('A-small-practice.in') as input_file:
        T = int(input_file.readline())
        result = []
        for i in xrange(T):
            N, K = input_file.readline().rstrip('\n').split(' ')
            lines = [input_file.readline().rstrip('\n') for x in xrange(int(N))]
            board = Board(lines, int(K))
            board.rotate_90_clockwise()
            board.apply_gravity()
            result.append(format("Case #%d: %s\n" % (i + 1, board.who_wins())))
        with open("output.txt", "w") as output_file:
            output_file.writelines(result)

class Board:
    def __init__(self, lines, k):
        self._board = []
        self.K = k
        self.N = len(lines)
        for l in lines:
            rows = [c for c in l]
            self._board.append(rows)

    def __repr__(self):
        lines = []
        for i in self._board:
            lines.append(" ".join(i))
        return "\n".join(lines)

    def rotate_90_clockwise(self):
        # Transpose and reverse each row
        t_board = [[None for x in xrange(self.N)] for y in xrange(self.N)]
        for r in xrange(self.N):
            for c in xrange(self.N):
                t_board[c][r] = self._board[r][c]
        self._board = [[x for x in reversed(r)] for r in t_board]

    def apply_gravity(self):
        for i in xrange(self.N):
            for r in reversed(xrange(self.N)):
                for c in xrange(self.N):
                    if self._board[r][c] == '.':
                        if r - 1 >= 0:
                            self._board[r][c], self._board[r - 1][c] = self._board[r - 1][c], self._board[r][c]

    def who_wins(self):
        p_wins = {"R":False, "B":False}
        for r in reversed(xrange(self.N)):
            for c in xrange(self.N):
                if self._board[r][c] != '.' and not p_wins[self._board[r][c]]:
                    if self.wins(r, c, self.K):
                        p_wins[self._board[r][c]] = True
        if p_wins["R"] and p_wins["B"]:
            return "Both"
        elif p_wins["R"]:
            return "Red"
        elif p_wins["B"]:
            return "Blue"
        else:
            return "Neither"

    def wins(self, r, c, k):
            return self.wins_dir(r, c,  1,  0, k) \
                or self.wins_dir(r, c,  0,  1, k) \
                or self.wins_dir(r, c,  1,  1, k) \
                or self.wins_dir(r, c, -1,  0, k) \
                or self.wins_dir(r, c,  0, -1, k) \
                or self.wins_dir(r, c, -1, -1, k) \
                or self.wins_dir(r, c,  1, -1, k) \
                or self.wins_dir(r, c, -1,  1, k)

    def wins_dir(self, r, c, dir_x, dir_y, k):
        if k == 1:
            return True
        if (self.N > r + dir_y >= 0 and self.N > c + dir_x >= 0) and self._board[r][c] == self._board[r + dir_y][c + dir_x]:
            return self.wins_dir(r + dir_y, c + dir_x, dir_x, dir_y, k - 1)
        return False


if __name__ == "__main__":
    main()