# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:04:35 2020

@author: NgoWi
"""

from Puzzle import Puzzle
import util

puzzle_arr = util.read_puzzle()
puzzle_1 = puzzle_arr[1]
puzzle_2 = [0,1,2,3,4,5,6,7,8] #3x3
puzzle_3 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] #3x6

p = Puzzle(3, 3, puzzle_2, 0)

p.showState()
# p.moveDown()
# p.moveUp()
# p.moveLeft()
# p.moveRight()
# p.moveUpRight()
# p.moveUpLeft()
# p.moveDownRight()
# p.moveDownLeft()
p.showState()
