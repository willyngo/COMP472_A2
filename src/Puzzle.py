# -*- coding: utf-8 -*-
"""
Puzzle class that represents a state of a Puzzle node.

TODO: Separate Wrapping moves and Diagonal moves (since they might result different heuristics)

Created on Thu Nov 12 16:53:49 2020
Updated on Thu Nov 16 - Separated moves + added g_cost
@author: NgoWi, Shifat Khan
"""
class Puzzle:
    def __init__(self, height, width, init_list, g_cost):
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
            child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 1)
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
            child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 1)
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
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 1)
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
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 1)
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
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 2)
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
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 2)
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
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 2)
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
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 2)
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
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 3)
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
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 3)
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
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 3)
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
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 3)
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
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 3)
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
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 3)
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
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 3)
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
        child = Puzzle(self.height, self.width, self.matrix, self.g_cost + 3)
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
    
    def showState(self):
        print(self.matrix)