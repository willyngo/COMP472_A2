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
            break
        
        # open_list will pop the puzzle state with the lowest cost
        current_state = open_list.pop()
        closed_list.append(current_state)
        
        #check if reached goal state, break if so
        if util.checkIfGoalState(current_state, goal_state_1, goal_state_2):
            foundGoalState = True
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

def create_solution_list(goal_puzzle):
    #new_block_file.write(json.dumps(spimi_index))
    backToRoot = False
    current = goal_puzzle  
    solution_list = []
    
    while not backToRoot:
        str_out = str(current.moveTile) + " " + str(current.moveCost) + " " + str(current.matrix) + "\n"
        solution_list.append(str_out)
        # output_file.write(str_out)
        
        #go to parent
        parent = current.parent
        
        #if reached root, stop
        if not parent:
            backToRoot = True
            break
        #else check the parent
        current = parent
        
    return solution_list

def output_search_list(search_list, puzzle_num):
    #output block into a new file
    with open(f"../outputs/{puzzle_num}_ucs_search.txt", "w") as output_file:
        #new_block_file.write(json.dumps(spimi_index))
        for result in search_list:
            str_out = str(0) + " " + str(result.moveCost) + " " + str(0) + " " + str(result.matrix) + "\n"
            output_file.write(str_out)

def output_solution_list(solution_list, puzzle_num, time_taken, solution_cost):
    with open(f"../outputs/{puzzle_num}_ucs_solution.txt", "w") as output_file:     
        #write down time and total cost
        r_solution_list = solution_list[::-1]
        for line in r_solution_list:
            output_file.write(line)
        output_file.write("Total cost: " + str(solution_cost) + "\n")
        output_file.write("Execution time: " + str(time_taken))
        
def output_no_solution(puzzle_num):
    with open(f"../outputs/{puzzle_num}_ucs_solution.txt", "w") as sol_file:
        sol_file.write("NO SOLUTION")
        
    with open(f"../outputs/{puzzle_num}_ucs_search.txt", "w") as output_file:
        output_file.write("NO SOLUTION")
            
def run_50():
    found_count = 0
    all_search_list = []
    all_solution_list = []
    all_time_taken = []
    
    for i in range(50):
        # initial_puzzle = Puzzle(2, 4, initial_states[i], 0, None)
        initial_puzzle = Puzzle(2, 4, initial_states_50[i], 0, None)
        goal_state_1, goal_state_2 = util.createGoalStates(initial_puzzle)
        
        search_list, found, time_taken = run_uniform_search(initial_puzzle, goal_state_1, goal_state_2)
        
        # if found:
        #     found_count += 1
        #     all_search_list.append(search_list)
        #     all_solution_list.append(solution_list)
        #     all_time_taken.append(time_taken)
            
        #     # output_solution_list(search_list[-1], i)
        #     # output_search_list(search_list, i)
        # # else:
        #     # output_no_solution(i)
            
def run():
    for i in range(3):
        initial_puzzle = Puzzle(2, 4, initial_states[i], 0, None)
        goal_state_1, goal_state_2 = util.createGoalStates(initial_puzzle)
        
        search_list, found, time_taken  = run_uniform_search(initial_puzzle, goal_state_1, goal_state_2)
       
        if found:
            solution_list = create_solution_list(search_list[-1])
            solution_cost = search_list[-1].g_cost
        
            output_solution_list(solution_list, i, time_taken, solution_cost)
            output_search_list(search_list, i)
        else:
            output_no_solution(i)
            
run()    