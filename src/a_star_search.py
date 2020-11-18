# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16

@author: ShifatKhan
"""
import util
from myQueue import myQueue
from Puzzle import Puzzle

puzzle_arr = util.read_puzzle()

p4 = Puzzle(2, 4, [1,2,3,4,5,6,7,8], 4)
p5 = Puzzle(2, 4, [2,4,5,6,7,8,9,8], 2)

p6 = Puzzle(2, 4, [3,3,3,4,5,6,7,8], 4)
p7 = Puzzle(2, 4, [3,3,3,4,5,6,7,8], 4)

open_list= myQueue()

open_list.push_a_star(p7)
open_list.push_a_star(p4)
open_list.push_a_star(p5)
open_list.push_a_star(p6)

popped = open_list.pop()
print("popped: ", popped.matrix)
open_list.showQueue()