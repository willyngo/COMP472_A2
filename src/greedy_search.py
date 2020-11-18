# -*- coding: utf-8 -*-
import util
from Puzzle import Puzzle
from myQueue import myQueue

try: import operator
except ImportError: keyfun = lambda x: x.h_cost
else: keyfun = operator.attrgetter("h_cost")

puzzle_arr = util.read_puzzle() #puzzle_arr contains all the initial puzzle in a list
goal1, goal2 = util.createGoalStates()

def run_with_h0(puzzle):
    
    # init vars
    open_list = myQueue()
    closed_list = []
    reach_goal = False
    
    # get h(n) of root and add it to closed list
    puzzle.h0()
    closed_list.insert(0, puzzle)
    
    while not reach_goal:
        
        currentNode = closed_list[0]
        
        if util.checkIfGoalState(currentNode, goal1, goal2):
            reach_goal = True
        else:
            # find successors
            successors = util.find_successors(puzzle)
            
            # find best successor
            for s in successors:
                s.h0()
                # our priority queue will sort by h(n) and remove duplicates
                open_list.push_sort_gbfs(s)
                
            bestSuccessor = open_list[0]
                    
            if bestSuccessor.h_cost < currentNode.h_cost:
                closed_list.insert(0, bestSuccessor)
            else:
                reach_goal = True  # nothing can beat current node
        
        
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