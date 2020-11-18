# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:04:35 2020

@author: NgoWi
"""

from Puzzle import Puzzle
import util
from myQueue import myQueue
import heapq
import os.path
import time

def __remove_if_in_closed(success_list, closed_list):
    new_success_list = []
    
    for success_list_item in success_list:
        for closed_item in closed_list:
            if not (success_list_item.matrix == closed_item.matrix):
                new_success_list.append(success_list_item)
                
    return new_success_list

# puzzle_arr = util.read_puzzle()
# puzzle_1 = puzzle_arr[0]
# puzzle_2 = [0,1,2,3,4,5,6,7,8] #3x3
# puzzle_3 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] #3x6

# p1 = Puzzle(2, 4, puzzle_1, 3)
# p2 = Puzzle(2, 4, puzzle_arr[1], 2)
# p3 = Puzzle(2, 4, puzzle_arr[2], 2)

# p4 = Puzzle(2, 4, [1,2,3,4,5,6,7,8], 4)
# p5 = Puzzle(2, 4, [2,4,5,6,7,8,9,8], 2)

# p6 = Puzzle(2, 4, [3,3,3,4,5,6,7,8], 0)
# p7 = Puzzle(2, 4, [3,3,3,4,5,6,7,8], 4)


for i in range(3):
    print(i)
    
# open_list= myQueue()

# open_list.push_sort_uniform(p7)
# open_list.push_sort_uniform(p4)
# open_list.push_sort_uniform(p5)
# open_list.push_sort_uniform(p6)

# popped = open_list.pop()
# print("popped: ", popped.matrix)
# open_list.showQueue()

# closed_list = [p1,p2,p3,p4]
# successor = [p5,p6,p1]

# print(closed_list[0] == successor[2])

# n = [item for item in successor if item not in closed_list]
# search_list = ["hello ", "how are you ", "yes "]

#     #output block into a new file
# with open("../outputs/ucs_search.txt", "w") as output_file:
#     #new_block_file.write(json.dumps(spimi_index))
#     for result in search_list:
#         result = result + str(2) + "\n"
#         output_file.write(result)
    



# q = myQueue()

# q.push(p)
# q.push(p2)
# q.push(p3)

# q.showQueue()

# first = q.pop()
# second = q.pop()
# third = q.pop()

# print("first: ", first.matrix)
# print("sec: ", second.matrix)
# print("thr: ", third.matrix)

# q = []
# heapq.heappush(q, p)
# heapq.heappush(q, p2)
# heapq.heappush(q, p3)

# for item in list(q):
#     print(item.matrix)