# -*- coding: utf-8 -*-


EMPTY = '.'
CROSS = 'o'
CIRCLE = 'x'

ROW = 3
COL = 4
DIAG = 5


class Board(object):

    def __init__(self, board=None):
        self.board = [EMPTY for _ in range(9)] if board is None else board

    def _validate_pos(self, pos):
        if pos > 9:
            raise ValueError('Index out of range')
        return True

    def row(self, n):
        if n < 0 or n > 2:
            raise ValueError
        return self.board[n*3:n*3+3]

    def col(self, n):
        if n < 0 or n > 2:
            raise ValueError
        return self.board[n::3]

    def diag(self, n):
        if n < 0 or n > 1:
            raise ValueError
        if n == 0:
             return self.board[::4]
        if n == 1:
            return self.board[2:-1:2]

    def lines(self):
        l = []
        l.extend([self.row(i) for i in range(3)])
        l.extend([self.col(i) for i in range(3)])
        l.extend([self.diag(i) for i in range(2)])
        return l

    def is_full(self):
        for i in range(9):
            if self.board[i] is EMPTY:
                return False
        return True

    def is_exists(self, pos):
        row, col = pos
        return self.board[row+col*3] is not EMPTY
    
    def _put(self, pos, hand):
        if self.is_exists(pos):
            return False
        row, col = pos
        self.board[row+col*3] = hand
        return True

    def put_cross(self, pos):
        return self._put(pos, CROSS)

    def put_circle(self, pos):
        return self._put(pos, CIRCLE)


class Game(object):

    def __init__(self):
        self.board = Board()
        self._finished = False

    @property
    def finished(self):
        return self._finished

    def is_full(self):
        return self.board.is_full()

    def _check_hand_has_won(self, hand):
        for i in range(3):
            line = self.board.row(i)
            if self._is_all(line, hand):
                return ROW, i
            line = self.board.col(i)
            if self._is_all(line, hand):
                return COL, hand
            if i < 2:
                line = self.board.diag(i)
                if self._is_all(line, hand):
                    return DIAG, i
        return False

    @staticmethod
    def _is_all(arr, value):
        for v in arr:
            if v != value:
                return False
        return True
