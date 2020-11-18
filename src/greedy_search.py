# -*- coding: utf-8 -*-
import util
from Puzzle import Puzzle

try: import operator
except ImportError: keyfun = lambda x: x.h_cost
else: keyfun = operator.attrgetter("h_cost")

puzzle_arr = util.read_puzzle() #puzzle_arr contains all the initial puzzle in a list


def run_with_h0(puzzle):
    
    # init vars
    open_list = []
    closed_list = []
    reach_goal = False;
    
    # get h(n) of root and add it to closed list
    puzzle.h0()
    closed_list.insert(0, puzzle)
    
    while not reach_goal:
        # find successors
        currentNode = closed_list[0]
        successors = util.find_successors(puzzle)
        # find best successor
        lowestCost = float("inf")
        bestSucessor = None
        
        for s in successors:
            s.h0()
            
            # check for dups in open list
            for p in open_list:
                if (s == p and s.h_cost < p.h_cost):
                    open_list.remove(p)
            open_list.append(s)
            
            # find lowest h(n)
            if (s.h_cost < lowestCost):
                bestSuccessor = s
                lowestCost = s.h_cost
                
        if lowestCost >= closed_list[0].h_cost:
            
        
        
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