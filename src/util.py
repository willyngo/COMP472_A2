# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:35:40 2020

@author: NgoWi
"""

puzzle_filepath = "../puzzles/initial_puzzle.txt"

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
