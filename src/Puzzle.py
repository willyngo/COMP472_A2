# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:53:49 2020

@author: NgoWi
"""

"""
This class 
"""
class Puzzle:
    def __init__(self, height, width, init_list, cost):
        self.matrix = init_list
        self.height = height
        self.width = width
        self.cost = cost
        self.upLeftCorner = 0
        self.upRightCorner = self.width - 1
        self.downLeftCorner = len(self.matrix) - (self.width)
        self.downRightCorner = len(self.matrix) - 1
    
    def __swapNumbers(self, zero_index, move_index):
        temp = self.matrix[move_index]
        self.matrix[move_index] = 0
        self.matrix[zero_index] = temp
        
    def moveUp(self):
        zero_index = self.matrix.index(0)
        move_index = zero_index - self.width
        
        #swap the tiles
        if move_index > 0:
            self.__swapNumbers(zero_index, move_index)
        else:
            print("Cannot move up if zero is located on top row")
        
    def moveDown(self):
        zero_index = self.matrix.index(0)
        move_index = zero_index + self.width
        
        #swap the tiles
        if move_index < len(self.matrix):
            self.__swapNumbers(zero_index, move_index)
        else:
            print("Cannot move down if zero is located on bottom row")
        
    def moveRight(self):
        zero_index = self.matrix.index(0)
        move_index = -1
        w = self.width
        
        #if the zero is located on a right corner
        if zero_index == self.upRightCorner or zero_index == self.downRightCorner:
            #wrap around and swap with left corner same row
            move_index = zero_index - (w - 1)
        else:
            #else, move to the left like normal
            move_index = zero_index + 1
        
        
        #swap the tiles
        self.__swapNumbers(zero_index, move_index)
        
    def moveLeft(self):
        zero_index = self.matrix.index(0)
        move_index = -1
        w = self.width
        
        #if the zero is located on a left corner
        if zero_index == self.upLeftCorner or zero_index == self.downLeftCorner:
            #wrap around and swap with right corner same row
            move_index = zero_index + (w - 1)
        else:
            #else, move to the left like normal
            move_index = zero_index - 1
        
        #swap the tiles
        self.__swapNumbers(zero_index, move_index)
        
    #============ DIAGONAL MOVEMENTS ===============
    def moveUpRight(self):
        zero_index = self.matrix.index(0)
        move_index = -1
        w = self.width        
        
        #if zero is located on down left corner, move diagonal
        if zero_index == self.downLeftCorner:
            move_index = zero_index - w + 1
        #else if zero is located on down right corner, perform diagonal wrap
        elif zero_index == self.downRightCorner:
            move_index = zero_index - w - (w - 1)
        else:
            print("Can only perform an upward diagonal if zero is located on a bottom corner.")
            
        #swap the tiles
        self.__swapNumbers(zero_index, move_index)
        
    def moveUpLeft(self):
        zero_index = self.matrix.index(0)
        w = self.width
        move_index = -1
        
        #if zero located on down right corner, move diagonal left
        if zero_index == self.downRightCorner:
            move_index = zero_index - w - 1
        #else if zero is on down left corner, perform diagonal wrap
        elif zero_index == self.downLeftCorner:
            move_index = zero_index - w + (w - 1)
        else:
            print("Can only perform a upward diagonal if zero is located on bottom corner")
        
        #swap the tiles
        self.__swapNumbers(zero_index, move_index)
        
    def moveDownRight(self):
        zero_index = self.matrix.index(0)
        move_index = -1
        w = self.width        
        
        #if zero is located on down left corner, move diagonal
        if zero_index == self.upLeftCorner:
            move_index = zero_index + (w + 1)
        #else if zero is located on down right corner, perform diagonal wrap
        elif zero_index == self.upRightCorner:
            move_index = zero_index + w - (w - 1)
        else:
            print("Can only perform an downward diagonal if zero is located on a top corner.")
            
        #swap the tiles
        self.__swapNumbers(zero_index, move_index) 
        
    def moveDownLeft(self):
        zero_index = self.matrix.index(0)
        w = self.width
        move_index = -1
        
        #if zero located on down right corner, move diagonal left
        if zero_index == self.upRightCorner:
            move_index = zero_index + w - 1
        #else if zero is on down left corner, perform diagonal wrap
        elif zero_index == self.upLeftCorner:
            move_index = zero_index + w + (w - 1)
        else:
            print("Can only perform a downward diagonal if zero is located on top corner")
        
        #swap the tiles
        self.__swapNumbers(zero_index, move_index)  
        
        
    def showState(self):
        print(self.matrix)