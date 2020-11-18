# -*- coding: utf-8 -*-
"""
Puzzle class that represents a state of a Puzzle node.

TODO: Separate Wrapping moves and Diagonal moves (since they might result different heuristics)

Created on Thu Nov 12 16:53:49 2020
Updated on Thu Nov 16 - Separated moves + added g_cost
@author: NgoWi, Shifat Khan
"""
class Puzzle:
    def __init__(self, height, width, init_list, g_cost, parent):
        self.matrix = []
        for i in init_list:
            self.matrix.append(i)
        self.height = height
        self.width = width
        self.g_cost = g_cost
        self.h_cost = 0
        self.upLeftCorner = 0
        self.upRightCorner = self.width - 1
        self.downLeftCorner = len(self.matrix) - (self.width)
        self.downRightCorner = len(self.matrix) - 1
        self.moveTile = 0
        self.moveCost = 0
        self.parent = parent
    
    def __swapNumbers(self, zero_index, move_index):
        temp = self.matrix[move_index]
        self.matrix[move_index] = 0
        self.matrix[zero_index] = temp
        
    #======================== DEFAULT MOVEMENTS ===========================#
    
    def moveUp(self):
        zero_index = self.matrix.index(0)
        move_index = zero_index - self.width
        
        #swap the tiles
        if move_index >= 0:
            child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 1, self)
            child.moveTile = self.matrix[move_index]
            child.moveCost = 1
            child.__swapNumbers(zero_index, move_index)
            return child
        else:
            #print("Cannot move up if zero is located on top row")
            return None
        
    def moveDown(self):
        zero_index = self.matrix.index(0)
        move_index = zero_index + self.width
        
        #swap the tiles
        if move_index < len(self.matrix):
            child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 1, self)
            child.moveTile = self.matrix[move_index]
            child.moveCost = 1
            child.__swapNumbers(zero_index, move_index)
            return child
        else:
            #print("Cannot move down if zero is located on bottom row")
            return None
        
    def moveRight(self):
        zero_index = self.matrix.index(0)
        move_index = zero_index + 1
            
        # Check if we went out of range
        if move_index % self.width == 0:
            #print("Cannot move right if zero is located on far right")
            return None

        #swap the tiles
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 1, self)
        child.moveTile = self.matrix[move_index]
        child.moveCost = 1
        child.__swapNumbers(zero_index, move_index)
        return child
        
    def moveLeft(self):
        zero_index = self.matrix.index(0)
        move_index = zero_index - 1
            
        # Check if we went out of range
        if move_index % self.width == self.width -1 or move_index < 0:
            #print("Cannot move left if zero is located on far left")
            return None
        
        #swap the tiles
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 1, self)
        child.moveTile = self.matrix[move_index]
        child.moveCost = 1
        child.__swapNumbers(zero_index, move_index)
        return child
    
    #======================== WRAPPING MOVEMENTS ===========================#
    
    def moveRightWrap(self):
        zero_index = self.matrix.index(0)
        move_index = -1
        w = self.width
        
        #if the zero is located on a right corner
        if zero_index == self.upRightCorner or zero_index == self.downRightCorner:
            #wrap around and swap with left corner same row
            move_index = zero_index - (w - 1)
        else:
            #print("Cannot wrap right if zero is not in the corner")
            return None
        
        #swap the tiles
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 2, self)
        child.moveTile = self.matrix[move_index]
        child.moveCost = 2
        child.__swapNumbers(zero_index, move_index)
        return child
    
    def moveLeftWrap(self):
        zero_index = self.matrix.index(0)
        move_index = -1
        w = self.width
        
        #if the zero is located on a left corner
        if zero_index == self.upLeftCorner or zero_index == self.downLeftCorner:
            #wrap around and swap with right corner same row
            move_index = zero_index + (w - 1)
        else:
            #print("Cannot wrap left if zero is not in the corner")
            return None
        
        #swap the tiles
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 2, self)
        child.moveTile = self.matrix[move_index]
        child.moveCost = 2
        child.__swapNumbers(zero_index, move_index)
        return child
    
    def moveUpWrap(self):
        # only for scale up
        if self.height <= 2:
            return None
        
        zero_index = self.matrix.index(0)
        move_index = -1
        w = self.width
        h = self.height
        
        #if the zero is located on top left or right corner
        if zero_index == self.upLeftCorner or zero_index == self.upRightCorner:
            #wrap around and swap with right corner same row
            move_index = zero_index + (w * (h - 1))
        else:
            #print("Cannot wrap left if zero is not in the up corner")
            return None
        
        #swap the tiles
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 2, self)
        child.moveTile = self.matrix[move_index]
        child.moveCost = 2
        child.__swapNumbers(zero_index, move_index)
        return child
    
    def moveDownWrap(self):
        # only for scale up
        if self.height <= 2:
            return None
        
        zero_index = self.matrix.index(0)
        move_index = -1
        w = self.width
        h = self.height
        
        #if the zero is located on bottom left or right corner
        if zero_index == self.downLeftCorner or zero_index == self.downRightCorner:
            #wrap around and swap with right corner same row
            move_index = zero_index - (w * (h - 1))
        else:
            #print("Cannot wrap left if zero is not in the down corner")
            return None
        
        #swap the tiles
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 2, self)
        child.moveTile = self.matrix[move_index]
        child.moveCost = 2
        child.__swapNumbers(zero_index, move_index)
        return child
    
    
    #======================== DIAGONAL MOVEMENTS ===========================#
    
    def moveUpRight(self):
        zero_index = self.matrix.index(0)
        move_index = -1
        w = self.width        
        
        #if zero is located on down left corner, move diagonal
        if zero_index == self.downLeftCorner:
            move_index = zero_index - w + 1
        else:
            #print("Can only perform an upward diagonal if zero is located on a bottom corner.")
            return None
            
        #swap the tiles
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 3, self)
        child.moveTile = self.matrix[move_index]
        child.moveCost = 3
        child.__swapNumbers(zero_index, move_index)
        return child
        
    def moveUpLeft(self):
        zero_index = self.matrix.index(0)
        w = self.width
        move_index = -1
        
        #if zero located on down right corner, move diagonal left
        if zero_index == self.downRightCorner:
            move_index = zero_index - w - 1
        else:
            #print("Can only perform a upward diagonal if zero is located on bottom corner")
            return None
        
        #swap the tiles
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 3, self)
        child.moveTile = self.matrix[move_index]
        child.moveCost = 3
        child.__swapNumbers(zero_index, move_index)
        return child
        
    def moveDownRight(self):
        zero_index = self.matrix.index(0)
        move_index = -1
        w = self.width        
        
        #if zero is located on down left corner, move diagonal
        if zero_index == self.upLeftCorner:
            move_index = zero_index + (w + 1)
        else:
            #print("Can only perform an downward diagonal if zero is located on a top corner.")
            return None
            
        #swap the tiles
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 3, self)
        child.moveTile = self.matrix[move_index]
        child.moveCost = 3
        child.__swapNumbers(zero_index, move_index)
        return child
        
    def moveDownLeft(self):
        zero_index = self.matrix.index(0)
        w = self.width
        move_index = -1
        
        #if zero located on up right corner, move diagonal left
        if zero_index == self.upRightCorner:
            move_index = zero_index + w - 1
        else:
            #print("Can only perform a downward diagonal if zero is located on top corner")
            return None
        
        #swap the tiles
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 3, self)
        child.moveTile = self.matrix[move_index]
        child.moveCost = 3
        child.__swapNumbers(zero_index, move_index)
        return child
        
    #=================== WRAPPING DIAGONAL MOVEMENTS =+=====================#
    
    def moveUpRightWrap(self):
        zero_index = self.matrix.index(0)
        move_index = -1   
        
        #if zero is located on down left corner, perform diagonal wrap
        if zero_index == self.downLeftCorner:
            move_index = self.width - 1
        else:
            #print("Can only perform an upward diagonal if zero is located on a bottom corner.")
            return None
            
        #swap the tiles
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 3, self)
        child.moveTile = self.matrix[move_index]
        child.moveCost = 3
        child.__swapNumbers(zero_index, move_index)
        return child
        
    def moveUpLeftWrap(self):
        zero_index = self.matrix.index(0)
        move_index = -1
        
        #if zero is on down right corner, perform diagonal wrap
        if zero_index == self.downRightCorner:
            move_index = 0
        else:
            #print("Can only perform a upward diagonal if zero is located on bottom corner")
            return None
        
        #swap the tiles
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 3, self)
        child.moveTile = self.matrix[move_index]
        child.moveCost = 3
        child.__swapNumbers(zero_index, move_index)
        return child
        
    def moveDownRightWrap(self):
        zero_index = self.matrix.index(0)
        move_index = -1 
        
        #if zero is located on up left corner, perform diagonal wrap
        if zero_index == self.upLeftCorner:
            move_index = len(self.matrix) - 1
        else:
            #print("Can only perform an downward diagonal if zero is located on a top corner.")
            return None
            
        #swap the tiles
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 3, self)
        child.moveTile = self.matrix[move_index]
        child.moveCost = 3
        child.__swapNumbers(zero_index, move_index)
        return child
        
    def moveDownLeftWrap(self):
        zero_index = self.matrix.index(0)
        move_index = -1
        
        #if zero is on up right corner, perform diagonal wrap
        if zero_index == self.upRightCorner:
            move_index = len(self.matrix) - self.width
        else:
            #print("Can only perform a downward diagonal if zero is located on top corner")
            return None
        
        #swap the tiles
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 3, self)
        child.moveTile = self.matrix[move_index]
        child.moveCost = 3
        child.__swapNumbers(zero_index, move_index)
        return child
    
    def __eq__(self, other):
        return self.matrix == other.matrix
    
    """
    Calculates and Assigns the heuristic h0 
    Returns the puzzle's h0 heuristic
    """
    def h0(self):
        if self.matrix[len(self.matrix) - 1] == 0:
            self.h_cost = 0
            return 0
        else:
            self.h_cost = 1
            return 1
    
    """
    Heuristic h1: by finding the distance from 
    correct index like Manhattan distance except we can 
    move diagonally
    """
    def h1(self, goal1, goal2):
        
        w = self.width
        goal1_h1_n = 0
        goal2_h1_n = 0
        g1_distance = 0
        g2_distance = 0
        
        # calc for both goal1 and goal2
        for i in range(len(self.matrix)):
            g1_correct_index = goal1.index(self.matrix[i])
            g2_correct_index = goal2.index(self.matrix[i])
            
            # find rows & cols of i and its correct index
            i_row = int(i / w) + 1
            i_col = (i % w) + 1
            g1_corr_row = int(g1_correct_index / w) + 1
            g1_corr_col = (g1_correct_index % w) + 1
            g2_corr_row = int(g2_correct_index / w) + 1
            g2_corr_col = (g2_correct_index % w) + 1
            
            # calc distance between i and correct by rows/cols
            g1_row_dist = abs(g1_corr_row - i_row)
            g1_col_dist = abs(g1_corr_col - i_col)
            g2_row_dist = abs(g2_corr_row - i_row)
            g2_col_dist = abs(g2_corr_col - i_col)
            
            # do math calc to find number of moves to reach correct index
            diagonal_moves = min(g1_row_dist, g1_col_dist)
            adjacent_moves = max(g1_row_dist, g1_col_dist) - diagonal_moves
            g1_distance = diagonal_moves + adjacent_moves
            diagonal_moves = min(g2_row_dist, g2_col_dist)
            adjacent_moves = max(g2_row_dist, g2_col_dist) - diagonal_moves
            g2_distance = diagonal_moves + adjacent_moves
            
            goal1_h1_n += g1_distance
            goal2_h1_n += g2_distance
            
        h1_n = min(goal1_h1_n, goal2_h1_n)
        
        self.h_cost = h1_n
        return h1_n
        
    """
    Heuristic h2: by finding the distance from 
    correct index like sum of permutation inversion 
    except it can wrap from index 0 to last index of list
    """
    def h2(self, goal1, goal2):
        
        goal1_h2_n = 0
        goal2_h2_n = 0
        puzz_len = len(self.matrix)
        midpoint = len(self.matrix) / 2
        
        # calc for both goal1 and goal2
        for i in range(puzz_len):
            g1_correct_index = goal1.index(self.matrix[i])
            g2_correct_index = goal2.index(self.matrix[i])
            
            g1_distance = g1_correct_index - i
            g2_distance = g2_correct_index - i
            
            # calc distance for goal1
            if abs(g1_distance) >= midpoint:
                # if it's too far, wrap other way
                if g1_distance > 0:
                    g1_distance = i + (puzz_len - g1_correct_index)
                else:
                    g1_distance = g1_correct_index + (puzz_len - i)
            else:
                g1_distance = abs(g1_distance)
                
            # calc distance for goal2
            if abs(g2_distance) >= midpoint:
                # if it's too far, wrap other way
                if g2_distance > 0:
                    g2_distance = i + (puzz_len - g2_correct_index)
                else:
                    g2_distance = g2_correct_index + (puzz_len - i)
            else:
                g2_distance = abs(g2_distance)
                
            goal1_h2_n += g1_distance
            goal2_h2_n += g2_distance
        
        h2_n = min(goal1_h2_n, goal2_h2_n)
        
        self.h_cost = h2_n
        return h2_n
                
    def showState(self):
        print(self.matrix)