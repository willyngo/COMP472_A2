# -*- coding: utf-8 -*-
puzzle_filepath = "../puzzles/initial_puzzle.txt"

"""
This function reads the filepath containing the input file and returns
a list containing each line of the input file as an array of ints

Created on Thu Nov 12
@author: WilliamNgo, ShifatKhan, Tahn
"""
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

goal_puzzle1 = []

"""
Checks if the given puzzle 
"""
def checkGoal(puzzle):
    length = len(puzzle.matrix)
    width = puzzle.width
    
    goal = list(range(1, length+1))
    goal[length-1] = 0
    
    goal2 = list(range(1, length+1))
    index = 0
    counter = 1
    for i in range(1, length+1):
        goal2[index] = i
        index += width
        if index >= length:
            index = 0 + counter
            counter += 1
    goal2[length-1] = 0