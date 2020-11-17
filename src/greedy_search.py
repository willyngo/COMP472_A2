# -*- coding: utf-8 -*-
import util
from Puzzle import Puzzle

try: import operator
except ImportError: keyfun = lambda x: x.h_cost
else: keyfun = operator.attrgetter("h_cost")

puzzle_arr = util.read_puzzle() #puzzle_arr contains all the initial puzzle in a list


def run_with_h0(puzzle):
    
    open_list = []
    closed_list = []
    closed_list.insert(0, puzzle)
    # calc h(n) of root

    successors = util.find_successors(puzzle)
    # calc h(n) of each successors
    # add to list
    
    # sort by h_cost
    #successors.sort(key=keyfun, reverse=True)
    
    for s in successors:
        print(s.showState())

# end func


def run_gbfs(puzzle):
    
    run_with_h0(puzzle)
    

puzzle = Puzzle(2, 4, puzzle_arr[0], 0)
run_with_h0(puzzle)