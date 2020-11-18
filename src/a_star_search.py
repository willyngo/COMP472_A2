# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16

@author: ShifatKhan
"""
import util
from myQueue import myQueue
from Puzzle import Puzzle

puzzle_arr = util.read_puzzle()

puzzle1 = Puzzle(2, 4, puzzle_arr[0], 0)
puzzle1.h0()
goal1, goal2 = util.createGoalStates(puzzle1)

# Create open and closed lists
open_list = myQueue()
open_list.push_a_star(puzzle1)
closed_list = []

goalReached = False
while not goalReached:
    currentPuzzle = open_list.pop()
    
    if util.checkIfGoalState(puzzle1, goal1, goal2):
        goalReached = True
    else:
        closed_list.append(currentPuzzle)
        successors = util.find_successors(currentPuzzle)
        
        for p in successors:
            if 