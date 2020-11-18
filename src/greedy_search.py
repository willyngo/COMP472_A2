# -*- coding: utf-8 -*-
import util
import time
from Puzzle import Puzzle
from myQueue import myQueue

puzzle_arr = util.read_puzzle()
puzzle_50 = util.read_50_puzzles()


def __remove_if_in_closed(success_list, closed_list):
    return [item for item in success_list if item not in closed_list]

def run_gbfs(root, goal1, goal2, heuristic):
    
    # init vars
    open_list = myQueue()
    closed_list = []
    reach_goal = False
    time_start = time.time()
    time_limit = time_start + 60
    
    # get h(n) of root and add it to open list
    if heuristic == 0:
        root.h0()
    elif heuristic == 1:
        root.h1(goal1, goal2)
    elif heuristic == 2:
        root.h2(goal1, goal2)
    open_list.push_sort_gbfs(root)
    
    while not reach_goal:
        if time.time() > time_limit:
            break
        
        currentNode = open_list.pop()
        closed_list.append(currentNode)
        
        if util.checkIfGoalState(currentNode, goal1, goal2):
            reach_goal = True
            break
        
        # find successors
        successors = util.find_successors(currentNode)
        successors = __remove_if_in_closed(successors, closed_list)
        
        # find best successor if have any
        for s in successors:
            if heuristic == 0:
                s.h0()
            elif heuristic == 1:
                s.h1(goal1, goal2)
            elif heuristic == 2:
                s.h2(goal1, goal2)
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
        return closed_list, reach_goal, (time.time() - time_start)
        

def run_50(heuristic):
    total_solution_path = 0
    total_search_path = 0
    total_number_no_solution = 0
    total_cost = 0
    total_time = 0
    
    for i in range(50):
        currPuzzle = Puzzle(2, 4, puzzle_50[i], 0, None)
        
        # Get goal states
        goal1, goal2 = util.createGoalStates(currPuzzle)
        
        # Run GBFS
        search_list, goalReached, time_taken = run_gbfs(currPuzzle, goal1, goal2, heuristic)

        # Get Solution path
        solution_list = util.create_solution_list(search_list[-1])
        
        # Calculate total values
        total_solution_path += len(solution_list)
        total_search_path += len(search_list)
        total_number_no_solution += 1 if not goalReached else 0
        total_cost += search_list[-1].g_cost
        total_time += time_taken
    
    util.output_analysis_50(total_solution_path, total_search_path, total_number_no_solution, total_cost, total_time, "gbfs", "h"+str(heuristic))

def run(heuristic):
    for i in range(3):
        currPuzzle = Puzzle(2, 4, puzzle_arr[i], 0, None)
        
        # Get goal states
        goal1, goal2 = util.createGoalStates(currPuzzle)
        
        # Run GBFS
        search_list, goalReached, time_taken = run_gbfs(currPuzzle, goal1, goal2, heuristic)

        # Get Solution path
        solution_list = util.create_solution_list(search_list[-1])
        
        if goalReached:
            util.output_solution_list(solution_list, i, time_taken, search_list[-1].g_cost, "gbfs", "h"+str(heuristic))
            util.output_search_list(search_list, i, "gbfs", "h"+str(heuristic))
        else:
            util.output_no_solution(i, "gbfs", "h"+str(heuristic))

run(1)
run_50(1)