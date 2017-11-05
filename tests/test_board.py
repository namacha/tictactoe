# -*- coding: utf-8 -*-

import unittest
from src.ttt import Board
from src.ttt import (
    EMPTY,
    CIRCLE,
    CROSS,
)


class TestBoard(unittest.TestCase):
    """Test class of ttt.Board"""

    def setUp(self):
        self.scene = [
            CIRCLE, CROSS, EMPTY,
            CIRCLE, CROSS, EMPTY,
            CIRCLE, CROSS, EMPTY,
        ]

    def test_init_board(self):
        """test initial board state"""
        board = Board()
        self.assertEqual(board.board, [EMPTY for _ in range(9)])

    def test_row(self):
        b = Board(self.scene)
        self.assertEqual([CIRCLE, CROSS, EMPTY], b.row(0))
        self.assertEqual([CIRCLE, CROSS, EMPTY], b.row(1))
        self.assertEqual([CIRCLE, CROSS, EMPTY], b.row(2))

    def test_col(self):
        b = Board(self.scene)
        self.assertEqual([CIRCLE, CIRCLE, CIRCLE], b.col(0))
        self.assertEqual([CROSS, CROSS, CROSS], b.col(1))
        self.assertEqual([EMPTY, EMPTY, EMPTY], b.col(2))

    def test_diag(self):
        b = Board(self.scene)
        self.assertEqual([CIRCLE, CROSS, EMPTY], b.diag(0))
        self.assertEqual([EMPTY, CROSS, CIRCLE], b.diag(1))

    def test_is_full(self):
        b = Board([CROSS for _ in range(9)])
        self.assertTrue(b.is_full())
        b2 = Board()
        self.assertFalse(b2.is_full())

    def test_put_cross(self):
        b = Board()
        self.assertTrue(b.put_cross(1, 1))
        self.assertEqual(b.board,
                         [EMPTY, EMPTY, EMPTY, EMPTY, CROSS, EMPTY, EMPTY, EMPTY, EMPTY])
        self.assertFalse(b.put_cross(1, 1))

    def test_put_circle(self):
        b = Board()
        self.assertTrue(b.put_circle(1, 1))
        self.assertEqual(b.board,
                         [EMPTY, EMPTY, EMPTY, EMPTY, CIRCLE, EMPTY, EMPTY, EMPTY, EMPTY])
        self.assertFalse(b.put_circle(1, 1))

    def test_is_exists(self):
        b = Board(self.scene)
        self.assertTrue(b.is_exists(0, 0))
        self.assertTrue(b.is_exists(1, 2))
        self.assertFalse(b.is_exists(2, 0))

    def test_row_invalid(self):
        b = Board()
        self.assertRaises(ValueError, b.row, -1)
        self.assertRaises(ValueError, b.row, 4)

    def test_col_invalid(self):
        b = Board()
        self.assertRaises(ValueError, b.col, -1)
        self.assertRaises(ValueError, b.col, 4)

    def test_diag_invalid(self):
        b = Board()
        self.assertRaises(ValueError, b.diag, -1)
        self.assertRaises(ValueError, b.diag, 2)


if __name__ == '__main__':
    unittest.main()
