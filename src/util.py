# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:35:40 2020

@author: NgoWi
"""

puzzle_filepath = "../puzzles/initial_puzzle.txt"

"""
This function reads the filepath containing the input file and returns
a list containing each line of the input file as an array of ints
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
