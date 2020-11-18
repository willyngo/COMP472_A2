# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:36:04 2020

@author: William Ngo
"""
from Puzzle import Puzzle
import util
from myQueue import myQueue
import time


initial_states = util.read_puzzle() #reads the input file and returns a list of puzzles
initial_states_50 = util.read_50_puzzles()

# #initial puzzle from input file
# initial_puzzle_1 = Puzzle(2, 4, initial_states[0], 0, None)
# initial_puzzle_2 = Puzzle(2, 4, initial_states[1], 0, None)
# initial_puzzle_3 = Puzzle(2, 4, initial_states[2], 0, None)

#goal state for each input puzzle
# p1_goal_state_1, p1_goal_state_2 = util.createGoalStates(initial_puzzle_1)
# p2_goal_state_1, p2_goal_state_2 = util.createGoalStates(initial_puzzle_2)
# p3_goal_state_1, p3_goal_state_2 = util.createGoalStates(initial_puzzle_3)

def __remove_if_in_closed(success_list, closed_list):                
    return [item for item in success_list if item not in closed_list]

    
def run_uniform_search(current_puzzle, goal_state_1, goal_state_2):
    open_list = myQueue()
    closed_list = []
    #add root to open list
    open_list.push_sort_uniform(current_puzzle)
    foundGoalState = False
    
    time_start = time.time()
    time_limit = time_start + 60
    while not foundGoalState:
        if time.time() > time_limit:
            print("solution not found!")
            break
        
        # open_list will pop the puzzle state with the lowest cost
        current_state = open_list.pop()
        closed_list.append(current_state)
        
        #check if reached goal state, break if so
        if util.checkIfGoalState(current_state, goal_state_1, goal_state_2):
            foundGoalState = True
            print("solution found!")
            break
        
        #else check the successors
        successors = util.find_successors(current_state)
        
        # if there are successors, in other words, if not a leaf
        if successors:
            #remove successors that already appeared in closed_list
            successors = __remove_if_in_closed(successors, closed_list)
            
            #add successor to open list
            for state in successors:
                open_list.push_sort_uniform(state)
                
    return closed_list, foundGoalState, (time.time() - time_start)
            
def run_50():
    total_solution_path = 0
    total_search_path = 0
    total_number_no_solution = 0
    total_cost = 0
    total_time = 0
    
    for i in range(50):
        initial_puzzle = Puzzle(2, 4, initial_states_50[i], 0, None)
        goal_state_1, goal_state_2 = util.createGoalStates(initial_puzzle)
        
        search_list, found, time_taken = run_uniform_search(initial_puzzle, goal_state_1, goal_state_2)
        
        # Get Solution path
        solution_list = util.create_solution_list(search_list[-1])
        
        total_solution_path += len(solution_list)
        total_search_path += len(search_list)
        total_number_no_solution += 1 if not found else 0
        total_cost += search_list[-1].g_cost
        total_time += time_taken
    
    util.output_analysis_50(total_solution_path, total_search_path, total_number_no_solution, total_cost, total_time, "astar")
            
def run():
    algorithm_name = "ucs"
    
    for i in range(3):
        initial_puzzle = Puzzle(2, 4, initial_states[i], 0, None)
        goal_state_1, goal_state_2 = util.createGoalStates(initial_puzzle)
        
        search_list, found, time_taken  = run_uniform_search(initial_puzzle, goal_state_1, goal_state_2)
        if found:
            goal_puzzle = search_list[-1]
            solution_list = util.create_solution_list(goal_puzzle)
            solution_cost = goal_puzzle.g_cost
            
            util.output_solution_list(solution_list, i, time_taken, solution_cost, algorithm_name)
            util.output_search_list(search_list, i, algorithm_name)
        else:
            util.output_no_solution(i, algorithm_name)
            
run()
run_50() 