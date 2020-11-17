# -*- coding: utf-8 -*-
import unittest
from Puzzle import Puzzle

"""
This is a unit testing class for Puzzle.py
To run:
    python -m unittest

TODO: Add heuristic test

Created on Thu Nov 16
@author: ShifatKhan
"""
class TestPuzzle(unittest.TestCase):
    
    def test_moveUp(self):
        # 0 1 2 3
        # 4 5 6 7
        puzzle_3x3 = Puzzle(2, 4, [0, 1, 2, 3, 4, 5, 6, 7], 0)
        temp = puzzle_3x3.moveDownRight()
        self.assertEqual(None, temp)
        
        # 1 2 3 4
        # 0 5 6 7
        puzzle_3x3 = Puzzle(2, 4, [1, 2, 3, 4, 0, 5, 6, 7], 0)
        temp = puzzle_3x3.moveDownRight()
        self.assertEqual(None, temp)
        
        # 1 0 2
        # 3 4 5
        # 6 7 8
        puzzle_3x3 = [1, 0, 2, 3, 4, 5, 6, 7, 8]
