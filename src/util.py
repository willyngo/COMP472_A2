# -*- coding: utf-8 -*-
puzzle_filepath = "../puzzles/initial_puzzle.txt"
puzzle_50_filepath = "../puzzles/50_random_puzzles.txt"
"""
This function reads the filepath containing the input file and returns
a list containing each line of the input file as an array of ints

Created on Thu Nov 12
@author: WilliamNgo, ShifatKhan, Tahn
"""

import random

#=============== Input Output ===============#


def read_puzzle():
    puzzle_arr = []
    
    try:    
        with open(puzzle_filepath, 'r') as puzzlefile:
            for line in puzzlefile:
                #splits each int into a list but split() returns a list of str
                split_list = line.split()
                
                #turn the str content into a list of ints
                int_list = list(map(int, split_list))
                
                #append each line(puzzle) to the puzzle_array
                #so that we have an array containing all our puzzles
                puzzle_arr.append(int_list)
    except FileNotFoundError:
        print(f"File not found: {puzzle_filepath}")
    
    return puzzle_arr

def read_50_puzzles():
    puzzle_arr = []
    
    try:    
        with open(puzzle_50_filepath, 'r') as puzzlefile:
            for line in puzzlefile:
                #splits each int into a list but split() returns a list of str
                split_list = line.split()
                
                #turn the str content into a list of ints
                int_list = list(map(int, split_list))
                
                #append each line(puzzle) to the puzzle_array
                #so that we have an array containing all our puzzles
                puzzle_arr.append(int_list)
    except FileNotFoundError:
        print(f"File not found: {puzzle_filepath}")
    
    return puzzle_arr

"""
Creates a list of the solution path by traversing each node bottom to top.

Return:
    List of Puzzles (solution path)
"""
def create_solution_list(goal_puzzle):
    #new_block_file.write(json.dumps(spimi_index))
    backToRoot = False
    current = goal_puzzle  
    solution_list = [goal_puzzle]
    
    while not backToRoot:
        #go to parent
        parent = current.parent
        
        #if reached root, stop
        if not parent:
            backToRoot = True
            break
        #else check the parent
        current = parent
        solution_list.append(parent)
        
    return solution_list[::-1]

"""
Output the solution path to a file.
"""
def output_solution_list(solution_list, puzzle_num, time_taken, solution_cost, algorithmName):
    with open(f"../outputs/{puzzle_num}_{algorithmName}_solution.txt", "w") as output_file:     
        #write down time and total cost
        for puzzle in solution_list:
            output_file.write(f"{puzzle.moveTile} {puzzle.moveCost} {puzzle.matrix}\n")
        output_file.write("Total cost: " + str(solution_cost) + "\n")
        output_file.write("Execution time: " + str(time_taken))

def output_search_list(search_list, puzzle_num, algorithmName):
    #output block into a new file
    with open(f"../outputs/{puzzle_num}_{algorithmName}_search.txt", "w") as output_file:
        #new_block_file.write(json.dumps(spimi_index))
        for result in search_list:
            str_out = str(result.g_cost + result.h_cost) + " " + str(result.g_cost) + " " + str(result.h_cost) + " " + str(result.matrix) + "\n"
            output_file.write(str_out)

def output_no_solution(puzzle_num, algorithmName):
    with open(f"../outputs/{puzzle_num}_{algorithmName}_solution.txt", "w") as sol_file:
        sol_file.write("NO SOLUTION")
        
    with open(f"../outputs/{puzzle_num}_{algorithmName}_search.txt", "w") as output_file:
        output_file.write("NO SOLUTION")

def output_analysis_50(total_solution_path, total_search_path, total_number_no_solution, total_cost, total_time, algorithmName):
    avg_solution_path = total_solution_path / 50
    avg_search_path = total_search_path / 50
    avg_number_no_solution = total_number_no_solution / 50
    avg_cost = total_cost / 50
    avg_time = total_time / 50
    
    with open(f"../outputs/{algorithmName}_analysis_50.txt", "w") as output_file:
        output_file.write("total solution length: " + str(total_solution_path) + "\n")
        output_file.write("avg solution length: " + str(avg_solution_path) + "\n\n")
        
        output_file.write("total search length: " + str(total_search_path) + "\n")
        output_file.write("avg search length: " + str(avg_search_path) + "\n\n")
        
        output_file.write("total no solutions: " + str(total_number_no_solution) + "\n")
        output_file.write("avg no solutions: " + str(avg_number_no_solution) + "\n\n")
        
        output_file.write("total cost: " + str(total_cost) + "\n")
        output_file.write("avg cost: " + str(avg_cost) + "\n\n")
        
        output_file.write("total execution time: " + str(total_time) + "\n")
        output_file.write("avg execution time: " + str(avg_time) + "\n")

#=============== Puzzle Utils ===============#

"""
Takes in a Puzzle reference and tries to perform any possible moves 
and returns a list of its successors
"""
def find_successors(puzzle):
    
    successors = []
    
    p = puzzle.moveUp()
    if (p is not None): successors.append(p)
    p = puzzle.moveDown()
    if (p is not None): successors.append(p)
    p = puzzle.moveRight()
    if (p is not None): successors.append(p)
    p = puzzle.moveLeft()
    if (p is not None): successors.append(p)
    p = puzzle.moveRightWrap()
    if (p is not None): successors.append(p)
    p = puzzle.moveLeftWrap()
    if (p is not None): successors.append(p)
    p = puzzle.moveUpWrap()
    if (p is not None): successors.append(p)
    p = puzzle.moveDownWrap()
    if (p is not None): successors.append(p)
    p = puzzle.moveUpRight()
    if (p is not None): successors.append(p)
    p = puzzle.moveUpLeft()
    if (p is not None): successors.append(p)
    p = puzzle.moveDownRight()
    if (p is not None): successors.append(p)
    p = puzzle.moveDownLeft()
    if (p is not None): successors.append(p)
    p = puzzle.moveUpRightWrap()
    if (p is not None): successors.append(p)
    p = puzzle.moveUpLeftWrap()
    if (p is not None): successors.append(p)
    p = puzzle.moveDownRightWrap()
    if (p is not None): successors.append(p)
    p = puzzle.moveDownLeftWrap()
    if (p is not None): successors.append(p)
    
    return successors

"""
Creates the goal states. 
Call this once only in the begining.

Return:
    A tuple of both goal states (2 arrays)
"""
def createGoalStates(puzzle):
    length = len(puzzle.matrix)
    width = puzzle.width
    
    # Create 1st goal state
    goal_puzzle1 = list(range(1, length+1))
    goal_puzzle1[length-1] = 0
    
    # Create 2nd goal state
    goal_puzzle2 = list(range(1, length+1))
    index = 0
    counter = 1
    for i in range(1, length+1):
        goal_puzzle2[index] = i
        index += width
        if index >= length:
            index = 0 + counter
            counter += 1
    goal_puzzle2[length-1] = 0
    
    return goal_puzzle1, goal_puzzle2

def checkIfGoalState(puzzle, goal1, goal2):
    if puzzle.matrix == goal1:
        return True
    if puzzle.matrix == goal2:
        return True
    
    return False