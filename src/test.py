# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:04:35 2020

@author: NgoWi
"""

from Puzzle import Puzzle
import util

puzzle_arr = util.read_puzzle()
puzzle_1 = puzzle_arr[1]

p = Puzzle(2, 4, puzzle_1, 0)

print(p.regularMoveUp())