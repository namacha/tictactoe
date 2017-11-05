# -*- coding: utf-8 -*-

import unittest
from src.ttt import Board, Game, Summary 
from src.ttt import (
    EMPTY,
    CIRCLE,
    CROSS,
)


class TestGame(unittest.TestCase):
    """Test class of ttt.Game"""

    def setUp(self):
        self.scene = [
            CIRCLE, CROSS, CROSS,
            CIRCLE, CIRCLE, EMPTY,
            CROSS, CROSS, CIRCLE,
        ]

    def test_is_finished(self):
        g = Game()
        g.judge()
        self.assertFalse(g.finished)
        g2 = Game(self.scene)
        g2.judge()
        self.assertTrue(g2.finished)

    def test_judge_0(self):
        g = Game()
        self.assertEqual(g.judge(), Summary.NOT_FINISHED)
        self.assertFalse(g.finished)

    def test_judge_cross_wins(self):
        scene = [
            EMPTY, EMPTY, CROSS,
            EMPTY, CROSS, EMPTY,
            CROSS, EMPTY, EMPTY,
        ]
        g = Game(scene)
        self.assertEqual(g.judge(), Summary.CROSS_WINS)
        self.assertTrue(g.finished)

    def test_judge_circle_wins(self):
        scene = [
            EMPTY, EMPTY, CIRCLE,
            EMPTY, CIRCLE, EMPTY,
            CIRCLE, EMPTY, EMPTY,
        ]
        g = Game(scene)
        self.assertEqual(g.judge(), Summary.CIRCLE_WINS)
        self.assertTrue(g.finished)

    def test_judge_draw(self):
        scene = [
            CROSS, CROSS, CIRCLE,
            CIRCLE, CIRCLE, CROSS,
            CROSS, CIRCLE, CROSS,
        ]
        g = Game(scene)
        self.assertEqual(g.judge(), Summary.DRAW)
        self.assertTrue(g.finished)

    def test_judge_invalid_0(self):
        scene = [
            CROSS, CIRCLE, CROSS,
            CROSS, CIRCLE, CROSS,
            CROSS, CIRCLE, CROSS,
        ]
        g = Game(scene)
        self.assertEqual(g.judge(), Summary.INVALID)
        self.assertFalse(g.finished)

    def test_is_winner_0(self):
        g = Game()
        self.assertEqual(g._is_winner(CIRCLE), 0)
        self.assertEqual(g._is_winner(CROSS), 0)

    def test_is_winner_1(self):
        scene = [
            EMPTY, CROSS, CIRCLE,
            EMPTY, CROSS, CIRCLE,
            EMPTY, CROSS, CIRCLE,
        ]
        g = Game(scene)
        self.assertEqual(g._is_winner(CIRCLE), 1)
        self.assertEqual(g._is_winner(CROSS), 1)

    def test_is_winner_2(self):
        scene = [CROSS for _ in range(9)]
        g = Game(scene)
        self.assertEqual(g._is_winner(CROSS), 8)
        self.assertEqual(g._is_winner(CIRCLE), 0)

    def test_is_all(self):
        g = Game()
        self.assertTrue(g._is_all([0, 0, 0], 0))
        self.assertFalse(g._is_all([0, 0, 1], 0))

if __name__ == '__main__':
    unittest.main()
