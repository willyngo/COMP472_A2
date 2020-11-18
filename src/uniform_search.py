# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:36:04 2020

@author: NgoWi
"""
from Puzzle import Puzzle
import util
from myQueue import myQueue

open_list = myQueue()
closed_list = []
initial_states = util.read_puzzle() #reads the input file and returns a list of puzzles

#initial puzzle from input file
initial_puzzle_1 = Puzzle(2, 4, initial_states[0], 0)
initial_puzzle_2 = Puzzle(2, 4, initial_states[1], 0)
initial_puzzle_3 = Puzzle(2, 4, initial_states[2], 0)

#goal state for each input puzzle
p1_goal_state_1, p1_goal_state_2 = util.createGoalStates(initial_puzzle_1)
p2_goal_state_1, p2_goal_state_2 = util.createGoalStates(initial_puzzle_2)
p3_goal_state_1, p3_goal_state_2 = util.createGoalStates(initial_puzzle_3)

#current puzzle to solve, change value as needed
current_puzzle = initial_puzzle_1

def __remove_if_in_closed(success_list):
    new_success_list = []
    
    for success_list_item in success_list:
        for closed_item in closed_list:
            if not (success_list_item.matrix == closed_item.matrix):
                new_success_list.append(success_list_item)
                
    return new_success_list

        
    
def run_uniform_search():
    #add root to open list
    open_list.push(current_puzzle)
    foundGoalState = False
    
    while not foundGoalState:
        # open_list will pop the puzzle state with the lowest cost
        current_state = open_list.pop()
        
        #check if reached goal state, break if so
        if util.checkIfGoalState(current_state, p1_goal_state_1, p1_goal_state_2):
            foundGoalState = True
            break
        #else check the successors
        closed_list.append(current_state)
        successors = util.find_successors(current_state)
        
        # if there are successors, in other words, if not a leaf
        if successors:
            #remove successors that already appeared in closed_list
            successors = __remove_if_in_closed(successors)
            
            #add successor to open list
            for state in successors:
                open_list.push(state)
                
            #check if a successor state already appears in the open_list
            # if it does appear, retain the one with the lowest cost
            
            
    return closed_list
    
search_list = run_uniform_search()
for state in search_list:
    print(state.matrix)