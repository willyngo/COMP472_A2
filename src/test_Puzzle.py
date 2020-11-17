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
        print("\n===================== test_moveUp =====================")
        #============ 3x2 ============#
        
        # 0 1
        # 2 3
        # 4 5
        puzzle = Puzzle(3, 2, [0,1,2,3,4,5], 0)
        temp = puzzle.moveUp()
        self.assertEqual(temp, None)
        
        # 1 2
        # 0 3
        # 4 5
        puzzle = Puzzle(3, 2, [1,2,0,3,4,5], 0)
        temp = puzzle.moveUp()
        self.assertEqual(temp.matrix, [0,2,1,3,4,5])
        self.assertEqual(temp.g_cost, 1)
        
        #============ 2x4 ============#
        
        # 0 1 2 3
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [0,1,2,3,4,5,6,7], 0)
        temp = puzzle.moveUp()
        self.assertEqual(temp, None)
        
        # 1 2 3 4
        # 0 5 6 7
        puzzle = Puzzle(2, 4, [1,2,3,4,0,5,6,7], 0)
        temp = puzzle.moveUp()
        self.assertEqual(temp.matrix, [0,2,3,4,1,5,6,7])
        
        #============ 3x3 ============#
        
        # 1 0 2
        # 3 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,0,2,3,4,5,6,7,8], 0)
        temp = puzzle.moveUp()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 0 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,0,5,6,7,8], 0)
        temp = puzzle.moveUp()
        self.assertEqual(temp.matrix, [1,0,3,4,2,5,6,7,8])
        self.assertEqual(temp.g_cost, 1)
        
        # 1 2 3
        # 4 5 6
        # 7 0 8
        puzzle = Puzzle(3, 3, [1,2,3,4,5,6,7,0,8], 0)
        temp = puzzle.moveUp()
        self.assertEqual(temp.matrix, [1,2,3,4,0,6,7,5,8])
        self.assertEqual(temp.g_cost, 1)
    
    def test_moveDown(self):
        print("\n===================== test_moveDown =====================")
        #============ 3x2 ============#
        
        # 1 2
        # 3 4
        # 0 5
        puzzle = Puzzle(3, 2, [1,2,3,4,0,5], 0)
        temp = puzzle.moveDown()
        self.assertEqual(temp, None)
        
        # 1 2
        # 0 3
        # 4 5
        puzzle = Puzzle(3, 2, [1,2,0,3,4,5], 0)
        temp = puzzle.moveDown()
        self.assertEqual(temp.matrix, [1,2,4,3,0,5])
        self.assertEqual(temp.g_cost, 1)
        
        #============ 2x4 ============#
        
        # 1 2 3 4
        # 0 5 6 7
        puzzle = Puzzle(2, 4, [1,2,3,4,0,5,6,7], 0)
        temp = puzzle.moveDown()
        self.assertEqual(temp, None)
        
        # 1 2 0 3
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [1,2,0,3,4,5,6,7], 0)
        temp = puzzle.moveDown()
        self.assertEqual(temp.matrix, [1,2,6,3,4,5,0,7])
        self.assertEqual(temp.g_cost, 1)
        
        #============ 3x3 ============#
        
        # 1 7 2
        # 3 4 5
        # 6 0 8
        puzzle = Puzzle(3, 3, [1,7,2,3,4,5,6,0,8], 0)
        temp = puzzle.moveDown()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 0 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,0,5,6,7,8], 0)
        temp = puzzle.moveDown()
        self.assertEqual(temp.matrix, [1,2,3,4,7,5,6,0,8])
        self.assertEqual(temp.g_cost, 1)
        
        # 1 0 3
        # 4 2 6
        # 7 5 8
        puzzle = Puzzle(3, 3, [1,0,3,4,2,6,7,5,8], 0)
        temp = puzzle.moveDown()
        self.assertEqual(temp.matrix, [1,2,3,4,0,6,7,5,8])
        self.assertEqual(temp.g_cost, 1)
        
    def test_moveRight(self):
        print("\n===================== test_moveRight =====================")
        #============ 3x2 ============#
        
        # 1 2
        # 3 4
        # 5 0
        puzzle = Puzzle(3, 2, [1,2,3,4,5,0], 0)
        temp = puzzle.moveRight()
        self.assertEqual(temp, None)
        
        # 1 2
        # 0 3
        # 4 5
        puzzle = Puzzle(3, 2, [1,2,0,3,4,5], 0)
        temp = puzzle.moveRight()
        self.assertEqual(temp.matrix, [1,2,3,0,4,5])
        self.assertEqual(temp.g_cost, 1)
        
        #============ 2x4 ============#
        
        # 1 2 3 0
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [1,2,3,0,4,5,6,7], 0)
        temp = puzzle.moveRight()
        self.assertEqual(temp, None)
        
        # 1 2 3 4
        # 0 5 6 7
        puzzle = Puzzle(2, 4, [1,2,3,4,0,5,6,7], 0)
        temp = puzzle.moveRight()
        self.assertEqual(temp.matrix, [1,2,3,4,5,0,6,7])
        self.assertEqual(temp.g_cost, 1)
        
        #============ 3x3 ============#
        
        # 1 2 0
        # 3 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,0,3,4,5,6,7,8], 0)
        temp = puzzle.moveRight()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 0 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,0,5,6,7,8], 0)
        temp = puzzle.moveRight()
        self.assertEqual(temp.matrix, [1,2,3,4,5,0,6,7,8])
        self.assertEqual(temp.g_cost, 1)
        
        # 1 2 3
        # 4 5 6
        # 0 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,5,6,0,7,8], 0)
        temp = puzzle.moveRight()
        self.assertEqual(temp.matrix, [1,2,3,4,5,6,7,0,8])
        self.assertEqual(temp.g_cost, 1)
        
    def test_moveLeft(self):
        print("\n===================== test_moveLeft =====================")
        #============ 3x2 ============#
        
        # 1 2
        # 3 4
        # 0 5
        puzzle = Puzzle(3, 2, [1,2,3,4,0,5], 0)
        temp = puzzle.moveLeft()
        self.assertEqual(temp, None)
        
        # 1 2
        # 3 0
        # 4 5
        puzzle = Puzzle(3, 2, [1,2,3,0,4,5], 0)
        temp = puzzle.moveLeft()
        self.assertEqual(temp.matrix, [1,2,0,3,4,5])
        self.assertEqual(temp.g_cost, 1)
        
        #============ 2x4 ============#
        
        # 0 1 2 3
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [0,1,2,3,4,5,6,7], 0)
        temp = puzzle.moveLeft()
        self.assertEqual(temp, None)
        
        # 1 2 3 4
        # 5 6 0 7
        puzzle = Puzzle(2, 4, [1,2,3,4,5,6,0,7], 0)
        temp = puzzle.moveLeft()
        self.assertEqual(temp.matrix, [1,2,3,4,5,0,6,7])
        self.assertEqual(temp.g_cost, 1)
        
        #============ 3x3 ============#
        
        # 0 1 2
        # 3 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [0,1,2,3,4,5,6,7,8], 0)
        temp = puzzle.moveLeft()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 0 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,0,5,6,7,8], 0)
        temp = puzzle.moveLeft()
        self.assertEqual(temp.matrix, [1,2,3,0,4,5,6,7,8])
        self.assertEqual(temp.g_cost, 1)
        
        # 1 2 3
        # 4 5 6
        # 7 8 0
        puzzle = Puzzle(3, 3, [1,2,3,4,5,6,7,8,0], 0)
        temp = puzzle.moveLeft()
        self.assertEqual(temp.matrix, [1,2,3,4,5,6,7,0,8])
        self.assertEqual(temp.g_cost, 1)
        
    def test_moveRightWrap(self):
        print("\n===================== test_moveRightWrap =====================")
        #============ 3x2 ============#
        
        # 1 2
        # 3 0
        # 4 5
        puzzle = Puzzle(3, 2, [1,2,3,0,4,5], 0)
        temp = puzzle.moveRightWrap()
        self.assertEqual(temp, None)
        
        # 1 2
        # 3 4
        # 5 0
        puzzle = Puzzle(3, 2, [1,2,3,4,5,0], 0)
        temp = puzzle.moveRightWrap()
        self.assertEqual(temp.matrix, [1,2,3,4,0,5])
        self.assertEqual(temp.g_cost, 2)
        
        #============ 2x4 ============#
        
        # 1 0 2 3
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [1,0,2,3,4,5,6,7], 0)
        temp = puzzle.moveRightWrap()
        self.assertEqual(temp, None)
        
        # 0 1 2 3
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [0,1,2,3,4,5,6,7], 0)
        temp = puzzle.moveRightWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3 4
        # 5 6 7 0
        puzzle = Puzzle(2, 4, [1,2,3,4,5,6,7,0], 0)
        temp = puzzle.moveRightWrap()
        self.assertEqual(temp.matrix, [1,2,3,4,0,6,7,5])
        self.assertEqual(temp.g_cost, 2)
        
        # 1 2 3 0
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [1,2,3,0,4,5,6,7], 0)
        temp = puzzle.moveRightWrap()
        self.assertEqual(temp.matrix, [0,2,3,1,4,5,6,7])
        self.assertEqual(temp.g_cost, 2)
        
        #============ 3x3 ============#
        
        # 1 2 3
        # 4 5 0
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,5,0,6,7,8], 0)
        temp = puzzle.moveRightWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 0 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,0,4,5,6,7,8], 0)
        temp = puzzle.moveRightWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 5 6
        # 7 8 0
        puzzle = Puzzle(3, 3, [1,2,3,4,5,6,7,8,0], 0)
        temp = puzzle.moveRightWrap()
        self.assertEqual(temp.matrix, [1,2,3,4,5,6,0,8,7])
        self.assertEqual(temp.g_cost, 2)
        
        # 1 2 0
        # 3 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,0,3,4,5,6,7,8], 0)
        temp = puzzle.moveRightWrap()
        self.assertEqual(temp.matrix, [0,2,1,3,4,5,6,7,8])
        self.assertEqual(temp.g_cost, 2)
        
    def test_moveLeftWrap(self):
        print("\n===================== test_moveLeftWrap =====================")
        #============ 3x2 ============#
        
        # 1 2
        # 0 3
        # 4 5
        puzzle = Puzzle(3, 2, [1,2,0,3,4,5], 0)
        temp = puzzle.moveLeftWrap()
        self.assertEqual(temp, None)
        
        # 1 2
        # 3 4
        # 0 5
        puzzle = Puzzle(3, 2, [1,2,3,4,0,5], 0)
        temp = puzzle.moveLeftWrap()
        self.assertEqual(temp.matrix, [1,2,3,4,5,0])
        self.assertEqual(temp.g_cost, 2)
        
        #============ 2x4 ============#
        
        # 1 0 2 3
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [1,0,2,3,4,5,6,7], 0)
        temp = puzzle.moveLeftWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3 0
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [1,2,3,0,4,5,6,7], 0)
        temp = puzzle.moveLeftWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3 4
        # 0 5 6 7
        puzzle = Puzzle(2, 4, [1,2,3,4,0,5,6,7], 0)
        temp = puzzle.moveLeftWrap()
        self.assertEqual(temp.matrix, [1,2,3,4,7,5,6,0])
        self.assertEqual(temp.g_cost, 2)
        
        # 0 1 2 3
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [0,1,2,3,4,5,6,7], 0)
        temp = puzzle.moveLeftWrap()
        self.assertEqual(temp.matrix, [3,1,2,0,4,5,6,7])
        self.assertEqual(temp.g_cost, 2)
        
        #============ 3x3 ============#
        
        # 1 2 3
        # 0 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,0,4,5,6,7,8], 0)
        temp = puzzle.moveLeftWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 5 0
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,5,0,6,7,8], 0)
        temp = puzzle.moveLeftWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 5 6
        # 0 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,5,6,0,7,8], 0)
        temp = puzzle.moveLeftWrap()
        self.assertEqual(temp.matrix, [1,2,3,4,5,6,8,7,0])
        self.assertEqual(temp.g_cost, 2)
        
        # 0 1 2
        # 3 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [0,1,2,3,4,5,6,7,8], 0)
        temp = puzzle.moveLeftWrap()
        self.assertEqual(temp.matrix, [2,1,0,3,4,5,6,7,8])
        self.assertEqual(temp.g_cost, 2)
        
    def test_moveUpRight(self):
        print("\n===================== test_moveUpRight =====================")
        #============ 3x2 ============#
        
        # 1 2
        # 0 3
        # 4 5
        puzzle = Puzzle(3, 2, [1,2,0,3,4,5], 0)
        temp = puzzle.moveUpRight()
        self.assertEqual(temp, None)
        
        # 1 2
        # 3 4
        # 0 5
        puzzle = Puzzle(3, 2, [1,2,3,4,0,5], 0)
        temp = puzzle.moveUpRight()
        self.assertEqual(temp.matrix, [1,2,3,0,4,5])
        self.assertEqual(temp.g_cost, 3)
        
        #============ 2x4 ============#
        
        # 1 5 2 3
        # 4 0 6 7
        puzzle = Puzzle(2, 4, [1,5,2,3,4,0,6,7], 0)
        temp = puzzle.moveUpRight()
        self.assertEqual(temp, None)
        
        # 1 2 3 0
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [1,2,3,0,4,5,6,7], 0)
        temp = puzzle.moveUpRight()
        self.assertEqual(temp, None)
        
        # 1 2 3 4
        # 0 5 6 7
        puzzle = Puzzle(2, 4, [1,2,3,4,0,5,6,7], 0)
        temp = puzzle.moveUpRight()
        self.assertEqual(temp.matrix, [1,0,3,4,2,5,6,7])
        self.assertEqual(temp.g_cost, 3)
        
        #============ 3x3 ============#
        
        # 1 2 3
        # 0 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,0,4,5,6,7,8], 0)
        temp = puzzle.moveUpRight()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 5 0
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,5,0,6,7,8], 0)
        temp = puzzle.moveUpRight()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 5 6
        # 0 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,5,6,0,7,8], 0)
        temp = puzzle.moveUpRight()
        self.assertEqual(temp.matrix, [1,2,3,4,0,6,5,7,8])
        self.assertEqual(temp.g_cost, 3)
        
    def test_moveUpLeft(self):
        print("\n===================== test_moveUpLeft =====================")
        #============ 3x2 ============#
        
        # 1 2
        # 3 0
        # 4 5
        puzzle = Puzzle(3, 2, [1,2,3,0,4,5], 0)
        temp = puzzle.moveUpLeft()
        self.assertEqual(temp, None)
        
        # 1 2
        # 3 4
        # 5 0
        puzzle = Puzzle(3, 2, [1,2,3,4,5,0], 0)
        temp = puzzle.moveUpLeft()
        self.assertEqual(temp.matrix, [1,2,0,4,5,3])
        self.assertEqual(temp.g_cost, 3)
        
        #============ 2x4 ============#
        
        # 1 5 2 3
        # 4 0 6 7
        puzzle = Puzzle(2, 4, [1,5,2,3,4,0,6,7], 0)
        temp = puzzle.moveUpLeft()
        self.assertEqual(temp, None)
        
        # 1 2 3 4
        # 0 5 6 7
        puzzle = Puzzle(2, 4, [1,2,3,4,0,5,6,7], 0)
        temp = puzzle.moveUpLeft()
        self.assertEqual(temp, None)
        
        # 1 2 3 4
        # 5 6 7 0
        puzzle = Puzzle(2, 4, [1,2,3,4,5,6,7,0], 0)
        temp = puzzle.moveUpLeft()
        self.assertEqual(temp.matrix, [1,2,0,4,5,6,7,3])
        self.assertEqual(temp.g_cost, 3)
        
        #============ 3x3 ============#
        
        # 1 2 3
        # 0 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,0,4,5,6,7,8], 0)
        temp = puzzle.moveUpLeft()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 5 0
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,5,0,6,7,8], 0)
        temp = puzzle.moveUpLeft()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 5 6
        # 7 8 0
        puzzle = Puzzle(3, 3, [1,2,3,4,5,6,7,8,0], 0)
        temp = puzzle.moveUpLeft()
        self.assertEqual(temp.matrix, [1,2,3,4,0,6,7,8,5])
        self.assertEqual(temp.g_cost, 3)

    def test_moveDownRight(self):
        print("\n===================== test_moveDownRight =====================")
        #============ 3x2 ============#
        
        # 1 2
        # 3 0
        # 4 5
        puzzle = Puzzle(3, 2, [1,2,3,0,4,5], 0)
        temp = puzzle.moveDownRight()
        self.assertEqual(temp, None)
        
        # 0 1
        # 2 3
        # 4 5
        puzzle = Puzzle(3, 2, [0,1,2,3,4,5], 0)
        temp = puzzle.moveDownRight()
        self.assertEqual(temp.matrix, [3,1,2,0,4,5])
        self.assertEqual(temp.g_cost, 3)
        
        #============ 2x4 ============#
        
        # 1 0 2 3
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [1,0,2,3,4,5,6,7], 0)
        temp = puzzle.moveDownRight()
        self.assertEqual(temp, None)
        
        # 1 2 3 0
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [1,2,3,0,4,5,6,7], 0)
        temp = puzzle.moveDownRight()
        self.assertEqual(temp, None)
        
        # 0 1 2 3
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [0,1,2,3,4,5,6,7], 0)
        temp = puzzle.moveDownRight()
        self.assertEqual(temp.matrix, [5,1,2,3,4,0,6,7])
        self.assertEqual(temp.g_cost, 3)
        
        #============ 3x3 ============#
        
        # 1 2 3
        # 0 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,0,4,5,6,7,8], 0)
        temp = puzzle.moveDownRight()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 5 0
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,5,0,6,7,8], 0)
        temp = puzzle.moveDownRight()
        self.assertEqual(temp, None)
        
        # 0 1 2
        # 3 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [0,1,2,3,4,5,6,7,8], 0)
        temp = puzzle.moveDownRight()
        self.assertEqual(temp.matrix, [4,1,2,3,0,5,6,7,8])
        self.assertEqual(temp.g_cost, 3)
    
    def test_moveDownLeft(self):
        print("\n===================== test_moveDownLeft =====================")
        #============ 3x2 ============#
        
        # 1 2
        # 0 3
        # 4 5
        puzzle = Puzzle(3, 2, [1,2,0,3,4,5], 0)
        temp = puzzle.moveDownLeft()
        self.assertEqual(temp, None)
        
        # 1 0
        # 2 3
        # 4 5
        puzzle = Puzzle(3, 2, [1,0,2,3,4,5], 0)
        temp = puzzle.moveDownLeft()
        self.assertEqual(temp.matrix, [1,2,0,3,4,5])
        self.assertEqual(temp.g_cost, 3)
        
        #============ 2x4 ============#
        
        # 1 0 2 3
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [1,0,2,3,4,5,6,7], 0)
        temp = puzzle.moveDownLeft()
        self.assertEqual(temp, None)
        
        # 0 1 2 3
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [0,1,2,3,4,5,6,7], 0)
        temp = puzzle.moveDownLeft()
        self.assertEqual(temp, None)
        
        # 1 2 3 0
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [1,2,3,0,4,5,6,7], 0)
        temp = puzzle.moveDownLeft()
        self.assertEqual(temp.matrix, [1,2,3,6,4,5,0,7])
        self.assertEqual(temp.g_cost, 3)
        
        #============ 3x3 ============#
        
        # 1 2 3
        # 0 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,0,4,5,6,7,8], 0)
        temp = puzzle.moveDownLeft()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 5 0
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,5,0,6,7,8], 0)
        temp = puzzle.moveDownLeft()
        self.assertEqual(temp, None)
        
        # 1 2 0
        # 3 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,0,3,4,5,6,7,8], 0)
        temp = puzzle.moveDownLeft()
        self.assertEqual(temp.matrix, [1,2,4,3,0,5,6,7,8])
        self.assertEqual(temp.g_cost, 3)
        
    def test_moveUpRightWrap(self):
        print("\n===================== test_moveUpRightWrap =====================")
        #============ 3x2 ============#
        
        # 1 2
        # 0 3
        # 4 5
        puzzle = Puzzle(3, 2, [1,2,0,3,4,5], 0)
        temp = puzzle.moveUpRightWrap()
        self.assertEqual(temp, None)
        
        # 1 2
        # 3 4
        # 0 5
        puzzle = Puzzle(3, 2, [1,2,3,4,0,5], 0)
        temp = puzzle.moveUpRightWrap()
        self.assertEqual(temp.matrix, [1,0,3,4,2,5])
        self.assertEqual(temp.g_cost, 3)
        
        #============ 2x4 ============#
        
        # 1 5 2 3
        # 4 0 6 7
        puzzle = Puzzle(2, 4, [1,5,2,3,4,0,6,7], 0)
        temp = puzzle.moveUpRightWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3 0
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [1,2,3,0,4,5,6,7], 0)
        temp = puzzle.moveUpRightWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3 4
        # 0 5 6 7
        puzzle = Puzzle(2, 4, [1,2,3,4,0,5,6,7], 0)
        temp = puzzle.moveUpRightWrap()
        self.assertEqual(temp.matrix, [1,2,3,0,4,5,6,7])
        self.assertEqual(temp.g_cost, 3)
        
        #============ 3x3 ============#
        
        # 1 2 3
        # 0 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,0,4,5,6,7,8], 0)
        temp = puzzle.moveUpRightWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 5 0
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,5,0,6,7,8], 0)
        temp = puzzle.moveUpRightWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 5 6
        # 0 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,5,6,0,7,8], 0)
        temp = puzzle.moveUpRightWrap()
        self.assertEqual(temp.matrix, [1,2,0,4,5,6,3,7,8])
        self.assertEqual(temp.g_cost, 3)
    
    def test_moveUpLeftWrap(self):
        print("\n===================== test_moveUpLeftWrap =====================")
        #============ 3x2 ============#
        
        # 1 2
        # 3 0
        # 4 5
        puzzle = Puzzle(3, 2, [1,2,0,3,4,5], 0)
        temp = puzzle.moveUpLeftWrap()
        self.assertEqual(temp, None)
        
        # 1 2
        # 3 4
        # 5 0
        puzzle = Puzzle(3, 2, [1,2,3,4,5,0], 0)
        temp = puzzle.moveUpLeftWrap()
        self.assertEqual(temp.matrix, [0,2,3,4,5,1])
        self.assertEqual(temp.g_cost, 3)
        
        #============ 2x4 ============#
        
        # 1 5 2 3
        # 4 0 6 7
        puzzle = Puzzle(2, 4, [1,5,2,3,4,0,6,7], 0)
        temp = puzzle.moveUpLeftWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3 0
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [1,2,3,0,4,5,6,7], 0)
        temp = puzzle.moveUpLeftWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3 4
        # 5 6 7 0
        puzzle = Puzzle(2, 4, [1,2,3,4,5,6,7,0], 0)
        temp = puzzle.moveUpLeftWrap()
        self.assertEqual(temp.matrix, [0,2,3,4,5,6,7,1])
        self.assertEqual(temp.g_cost, 3)
        
        #============ 3x3 ============#
        
        # 1 2 3
        # 0 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,0,4,5,6,7,8], 0)
        temp = puzzle.moveUpLeftWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 5 0
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,5,0,6,7,8], 0)
        temp = puzzle.moveUpLeftWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 5 6
        # 7 8 0
        puzzle = Puzzle(3, 3, [1,2,3,4,5,6,7,8,0], 0)
        temp = puzzle.moveUpLeftWrap()
        self.assertEqual(temp.matrix, [0,2,3,4,5,6,7,8,1])
        self.assertEqual(temp.g_cost, 3)
        
    def test_moveDownRightWrap(self):
        print("\n===================== test_moveDownRightWrap =====================")
        #============ 3x2 ============#
        
        # 1 2
        # 0 3
        # 4 5
        puzzle = Puzzle(3, 2, [1,2,0,3,4,5], 0)
        temp = puzzle.moveDownRightWrap()
        self.assertEqual(temp, None)
        
        # 0 1
        # 2 3
        # 4 5
        puzzle = Puzzle(3, 2, [0,1,2,3,4,5], 0)
        temp = puzzle.moveDownRightWrap()
        self.assertEqual(temp.matrix, [5,1,2,3,4,0])
        self.assertEqual(temp.g_cost, 3)
        
        #============ 2x4 ============#
        
        # 1 0 2 3
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [1,0,2,3,4,5,6,7], 0)
        temp = puzzle.moveDownRightWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3 0
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [1,2,3,0,4,5,6,7], 0)
        temp = puzzle.moveDownRightWrap()
        self.assertEqual(temp, None)
        
        # 0 1 2 3
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [0,1,2,3,4,5,6,7], 0)
        temp = puzzle.moveDownRightWrap()
        self.assertEqual(temp.matrix, [7,1,2,3,4,5,6,0])
        self.assertEqual(temp.g_cost, 3)
        
        #============ 3x3 ============#
        
        # 1 2 3
        # 0 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,0,4,5,6,7,8], 0)
        temp = puzzle.moveDownRightWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 5 0
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,5,0,6,7,8], 0)
        temp = puzzle.moveDownRightWrap()
        self.assertEqual(temp, None)
        
        # 0 1 2
        # 3 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [0,1,2,3,4,5,6,7,8], 0)
        temp = puzzle.moveDownRightWrap()
        self.assertEqual(temp.matrix, [8,1,2,3,4,5,6,7,0])
        self.assertEqual(temp.g_cost, 3)
        
    def test_moveDownLeftWrap(self):
        print("\n===================== test_moveDownLeftWrap =====================")
        #============ 3x2 ============#
        
        # 1 2
        # 3 0
        # 4 5
        puzzle = Puzzle(3, 2, [1,2,3,0,4,5], 0)
        temp = puzzle.moveDownLeftWrap()
        self.assertEqual(temp, None)
        
        # 1 0
        # 2 3
        # 4 5
        puzzle = Puzzle(3, 2, [1,0,2,3,4,5], 0)
        temp = puzzle.moveDownLeftWrap()
        self.assertEqual(temp.matrix, [1,4,2,3,0,5])
        self.assertEqual(temp.g_cost, 3)
        
        #============ 2x4 ============#
        
        # 1 0 2 3
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [1,0,2,3,4,5,6,7], 0)
        temp = puzzle.moveDownLeftWrap()
        self.assertEqual(temp, None)
        
        # 0 1 2 3
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [0,1,2,3,4,5,6,7], 0)
        temp = puzzle.moveDownLeftWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3 0
        # 4 5 6 7
        puzzle = Puzzle(2, 4, [1,2,3,0,4,5,6,7], 0)
        temp = puzzle.moveDownLeftWrap()
        self.assertEqual(temp.matrix, [1,2,3,4,0,5,6,7])
        self.assertEqual(temp.g_cost, 3)
        
        #============ 3x3 ============#
        
        # 1 2 3
        # 0 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,0,4,5,6,7,8], 0)
        temp = puzzle.moveDownLeftWrap()
        self.assertEqual(temp, None)
        
        # 1 2 3
        # 4 5 0
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,3,4,5,0,6,7,8], 0)
        temp = puzzle.moveDownLeftWrap()
        self.assertEqual(temp, None)
        
        # 1 2 0
        # 3 4 5
        # 6 7 8
        puzzle = Puzzle(3, 3, [1,2,0,3,4,5,6,7,8], 0)
        temp = puzzle.moveDownLeftWrap()
        self.assertEqual(temp.matrix, [1,2,6,3,4,5,0,7,8])
        self.assertEqual(temp.g_cost, 3)