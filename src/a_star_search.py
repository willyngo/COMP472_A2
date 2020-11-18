# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16

@author: ShifatKhan
"""
import util
import heapq
from dataclasses import dataclass, field
from Puzzle import Puzzle

@dataclass(order=True)
class PrioritizedItem:
    item: object = field()
    
    

q = []

puzzle_arr = util.read_puzzle() #puzzle_arr contains all the initial puzzle in a list

puzzle1 = Puzzle(2,4,puzzle_arr[0],1)
puzzle2 = Puzzle(2,4,puzzle_arr[1],1)
puzzle3 = Puzzle(2,4,puzzle_arr[2],1)

puzzle1.h0()
puzzle2.h0()

A = (puzzle1.g_cost + puzzle1.h_cost, puzzle1.h_cost, puzzle1.g_cost, puzzle1)
B = (puzzle2.g_cost + puzzle2.h_cost, puzzle2.h_cost, puzzle2.g_cost, puzzle2)
C = (puzzle3.g_cost + puzzle3.h_cost, puzzle3.h_cost, puzzle3.g_cost, puzzle3)

print("\nA---------:")
print("g: ", A[2])
print("h: ", A[1])
print("f: ", A[0])

print("\nB---------:")
print("g: ", B[2])
print("h: ", B[1])
print("f: ", B[0])

print("\nC---------:")
print("g: ", C[2])
print("h: ", C[1])
print("f: ", C[0])

heapq.heappush(q, A)
heapq.heappush(q, B)
heapq.heappush(q, C)

print(heapq.heappop(q)[3].matrix)

open_list = [puzzle1]
empty_list = []

goal1, goal2 = util.createGoalStates(puzzle1)

def main():
    while not util.checkIfGoalState(puzzle1, goal1, goal2):
        print("")
    

def getPuzzleWithLowestFScore(open_list):
    lowest = open_list[0]
    
    for i in range(1, len(open_list)):
        lowest_f = lowest.g_cost + lowest.h_cost
        curr_f = open_list[i].g_cost + open_list[i].h_cost 
        
        # compare f scores
        if curr_f < lowest_f:
            lowest = open_list[i]
        elif curr_f == lowest_f:
            # compare h scores
            if open_list[i].h_cost < lowest.h_cost:
                lowest = open_list[i]
            # compare g scores
            elif open_list[i].g_cost < lowest.g_cost:
                lowest = open_list[i]