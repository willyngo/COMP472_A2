# -*- coding: utf-8 -*-
import util
from Puzzle import Puzzle
from myQueue import myQueue

puzzle_arr = util.read_puzzle() #puzzle_arr contains all the initial puzzle in a list
puzzle = Puzzle(2, 4, puzzle_arr[0], 0, None)
goal1, goal2 = util.createGoalStates(puzzle)


def __remove_if_in_closed(success_list, closed_list):
    return [item for item in success_list if item not in closed_list]

def run_with_h0(puzzle):
    
    # init vars
    open_list = myQueue()
    closed_list = []
    reach_goal = False
    
    # get h(n) of root and add it to closed list
    puzzle.h1(goal1, goal2)
    closed_list.insert(0, puzzle)
    
    while not reach_goal:
        
        currentNode = closed_list[0]
        
        if util.checkIfGoalState(currentNode, goal1, goal2):
            reach_goal = True
        else:
            # find successors
            successors = util.find_successors(puzzle)
            successors = __remove_if_in_closed(successors, closed_list)
            
            # find best successor if have any
            for s in successors:
                s.h1(goal1, goal2)
                # our priority queue will sort by h(n) and remove duplicates
                open_list.push_sort_gbfs(s)
               
            # see if successor has lower h(n) than current node
            if open_list._data:
                bestSuccessor = open_list.pop()
                        
                if bestSuccessor.h_cost < currentNode.h_cost:
                    closed_list.insert(0, bestSuccessor)
                else:
                    reach_goal = True  # nothing can beat current node
            else:
                # no solution if open list is empty and goal is not reached
                break
    
    if not reach_goal:
        print("No solution found with GBFS")
    else:
        # find solution path
        for i in range(len(closed_list)):
            print(closed_list[i].showState())
        

# end func


def run_gbfs(puzzle):
    
    run_with_h0(puzzle)
    


run_with_h0(puzzle)