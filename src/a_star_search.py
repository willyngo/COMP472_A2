# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16

@author: ShifatKhan
"""
import util
from Puzzle import Puzzle

puzzle_arr = util.read_puzzle() #puzzle_arr contains all the initial puzzle in a list

puzzle = Puzzle(3,3,[1,2,3,4,5,6,7,8,0],0)
goal_state1, goal_state2 = util.createGoalStates(puzzle)

print(goal_state1)
print(goal_state2)

print(util.checkIfGoalState(puzzle, goal_state1, goal_state2))