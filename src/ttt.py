# -*- coding: utf-8 -*-

EMPTY = '.'
CROSS = 'x'
CIRCLE = 'o'

ROW = 3
COL = 4
DIAG = 5


class Board(object):

    def __init__(self, board=None):
        self.board = [EMPTY for _ in range(9)] if board is None else board

    def _validate_pos(self, row, col):
        if row < 0 or row > 8:
            raise ValueError
        if col < 0 or col > 8:
            raise ValueError

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

    def is_exists(self, row, col):
        self._validate_pos(row, col)
        return self.board[row+col*3] is not EMPTY
    
    def _put(self, row, col, hand):
        if self.is_exists(row, col):
            return False
        self._validate_pos(row, col)
        self.board[row+col*3] = hand
        return True

    def put_cross(self, row, col):
        return self._put(row, col, CROSS)

    def put_circle(self, row, col):
        return self._put(row, col, CIRCLE)


class Summary(object):

    CIRCLE_WINS = 'o_wins'
    CROSS_WINS = 'x_wins'
    DRAW = 'draw'
    INVALID = 'invalid'
    NOT_FINISHED = 'not_finished'

    LINE_ROW_0 = 'row0'
    LINE_ROW_1 = 'row1'
    LINE_ROW_2 = 'row2'
    LINE_COL_0 = 'col0'
    LINE_COL_1 = 'col1'
    LINE_COL_2 = 'col2'
    LINE_DIAG_0 = 'diag0'
    LINE_DIAG_1 = 'diag1'

    ROWS = {
        0: LINE_ROW_0,
        1: LINE_ROW_1,
        2: LINE_ROW_2,
    }

    COLS = {
        0: LINE_COL_0,
        1: LINE_COL_1,
        2: LINE_COL_2,
    }

    DIAGS = {
        0: LINE_DIAG_0,
        1: LINE_DIAG_1,
    }


class Game(object):

    def __init__(self, board=None):
        self._board = Board(board=board)
        self._finished = False

    @property
    def finished(self):
        return self._finished

    def is_full(self):
        return self._board.is_full()

    def _is_winner(self, hand):
        count = 0
        for i in range(3):
            row = self._board.row(i)
            if self._is_all(row, hand):
                count += 1

            col = self._board.col(i)
            if self._is_all(col, hand):
                count += 1

        if self._is_all(self._board.diag(0), hand):
            count += 1

        if self._is_all(self._board.diag(1), hand):
            count += 1

        return count

    def judge(self):
        """Judge and returns `Summary` of Game"""
        c_cross = self._is_winner(CROSS)
        c_circle = self._is_winner(CIRCLE)
        if c_cross > 1 or c_circle > 1:
            situation = Summary.INVALID
        elif c_cross == 0 and c_circle == 0:
            situation = Summary.NOT_FINISHED
        elif c_cross == 1:
            situation = Summary.CROSS_WINS
            self._finished = True
        elif c_circle == 1:
            situation = Summary.CIRCLE_WINS
            self._finished = True
        
        return situation

    @staticmethod
    def _is_all(arr, value):
        for v in arr:
            if v != value:
                return False
        return True
