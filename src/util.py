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