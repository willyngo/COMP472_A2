# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16

@author: ShifatKhan
"""
import util
import time
import threading
from myQueue import myQueue
from Puzzle import Puzzle

puzzle_arr = util.read_puzzle()
puzzle_50 = util.read_50_puzzles()

"""
Runs the A* algorithm for a given Puzzle with a chosen Heuristic.

Parameters:
    puzzle: Puzzle class to solve
    goal1: list representation of first goal
    goal2: list representation of 2nd goal
    heuristic: int heuristic index 0, 1 or 2
"""
def run_a_star(puzzle, goal1, goal2, heuristic):
    # Create open and closed lists
    open_list = myQueue()
    open_list.push_a_star(puzzle)
    closed_list = []
    
    goalReached = False
    
    time_start = time.time()
    time_limit = time_start + 60
    
    if heuristic == 0:
        puzzle.h0()
    elif heuristic == 1:
        puzzle.h1(goal1, goal2)
    else:
        puzzle.h2(goal1, goal2)
    
    # Loop until goal is reached.
    while open_list._data:
        if time.time() > time_limit:
            break
        
        current = open_list.pop()
        closed_list.append(current)
        
        # Check if we reached the goal
        if util.checkIfGoalState(current, goal1, goal2):
            goalReached = True
            break
        
        # Loop through successors
        successors = util.find_successors(current)
        
        for neighbour in successors:
            
            # Check if child is in Closed list
            foundInClosed = False
            for c in closed_list:
                if neighbour == c:
                    foundInClosed = True
                    if neighbour.g_cost < c.g_cost:
                        c.g_cost = neighbour.g_cost
                        c.parent = current
            
            if foundInClosed:
                continue
            
            # if neighbour in closed_list: #TODO: add check for "not traversable"
            #     continue
            
            if heuristic == 0:
                neighbour.h0()
            elif heuristic == 1:
                neighbour.h1(goal1, goal2)
            else:
                neighbour.h2(goal1, goal2)
            
        
            # Check if child is in Open list
            foundInOpen = False
            for o in open_list._data:
                openPuzzle = o[-1]
                if neighbour == openPuzzle:
                    foundInOpen = True
                    break
             
            if not foundInOpen: #TODO: Add check for new path is shorter
                neighbour.parent = current
                open_list.push_a_star(neighbour)
    
    print("GOAL REACHED? ", goalReached)
    return closed_list, goalReached, (time.time() - time_start)

def run_50(heuristic):
    total_solution_path = 0
    total_search_path = 0
    total_number_no_solution = 0
    total_cost = 0
    total_time = 0
    
    for i in range(50):
        currPuzzle = Puzzle(2, 4, puzzle_50[i], 0, None)
        
        # Get goal states
        goal1, goal2 = util.createGoalStates(currPuzzle)
        
        # Run A*
        search_list, goalReached, time_taken = run_a_star(currPuzzle, goal1, goal2, heuristic)

        # Get Solution path
        solution_list = util.create_solution_list(search_list[-1])
        
        # Calculate total values
        total_solution_path += len(solution_list)
        total_search_path += len(search_list)
        total_number_no_solution += 1 if not goalReached else 0
        total_cost += search_list[-1].g_cost
        total_time += time_taken
    
    util.output_analysis_50(total_solution_path, total_search_path, total_number_no_solution, total_cost, total_time, "astar", "h"+str(heuristic))

def run(heuristic):
    for i in range(3):
        currPuzzle = Puzzle(2, 4, puzzle_arr[i], 0, None)
        
        # Get goal states
        goal1, goal2 = util.createGoalStates(currPuzzle)
        
        # Run A*
        search_list, goalReached, time_taken = run_a_star(currPuzzle, goal1, goal2, heuristic)

        # Get Solution path
        solution_list = util.create_solution_list(search_list[-1])
        
        if goalReached:
            util.output_solution_list(solution_list, i, time_taken, search_list[-1].g_cost, "astar", "h"+str(heuristic))
            util.output_search_list(search_list, i, "astar", "h"+str(heuristic))
        else:
            util.output_no_solution(i, "astar", "h"+str(heuristic))

# Run for 1st heuristic
run(1)
run_50(1)

# Run for 2nd heuristic
run(2)
run_50(2)