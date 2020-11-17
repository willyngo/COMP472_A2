# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16

@author: ShifatKhan
"""
import util
from Puzzle import Puzzle

def h0(puzzle):
    if puzzle.matrix[len(puzzle.matrix) - 1] == 0:
        return 0
    else:
        return 1

puzzle_arr = util.read_puzzle()
p1 = puzzle_arr[0]

puzzle1 = Puzzle(2, 4, p1, 0)

print(h0(puzzle1))

