# -*- coding: utf-8 -*-
import util
from Puzzle import Puzzle

#try: import operator
#except ImportError: keyfun = lambda x: x.cost
#else: keyfun = operator.attrgetter("cost")

puzzle_arr = util.read_puzzle() #puzzle_arr contains all the initial puzzle in a list




def find_successors(puzzle):
    
    successors = []
    
    p1 = puzzle.moveUp()
    if (p1 is not None): successors.append(p1)
    p2 = puzzle.moveDown()
    if (p2 is not None): successors.append(p2)
    p3 = puzzle.moveRight()
    if (p3 is not None): successors.append(p3)
    p4 = puzzle.moveLeft()
    if (p4 is not None): successors.append(p4)
    p5 = puzzle.moveRightWrap()
    if (p5 is not None): successors.append(p5)
    p6 = puzzle.moveLeftWrap()
    if (p6 is not None): successors.append(p6)
    p7 = puzzle.moveUpRight()
    if (p7 is not None): successors.append(p7)
    p8 = puzzle.moveUpLeft()
    if (p8 is not None): successors.append(p8)
    p9 = puzzle.moveDownRight()
    if (p9 is not None): successors.append(p9)
    p10 = puzzle.moveDownLeft()
    if (p10 is not None): successors.append(p10)
    p11 = puzzle.moveUpRightWrap()
    if (p11 is not None): successors.append(p11)
    p12 = puzzle.moveUpLeftWrap()
    if (p12 is not None): successors.append(p12)
    p13 = puzzle.moveDownRightWrap()
    if (p13 is not None): successors.append(p13)
    p14 = puzzle.moveDownLeftWrap()
    if (p14 is not None): successors.append(p14)
    
    return successors
# end func


def run_with_h0(puzzle):
    
    open_list = []
    closed_list = []
    #closed_list.insert(0, puzzle)
    puzzle.showState()

    #successors = find_successors(puzzle)
    #for s in successors:
        #s.showState()
    puzzle.showState()
# end func


def run_gbfs(puzzle):
    
    run_with_h0(puzzle)
    

puzzle = Puzzle(2, 4, puzzle_arr[0], 0)
run_with_h0(puzzle)