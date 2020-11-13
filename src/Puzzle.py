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
    
    def __swapNumbers(self, zero_index, move_index):
        temp = self.matrix[move_index]
        self.matrix[move_index] = 0
        self.matrix[zero_index] = temp
        
    def moveUp(self):
        zero_index = self.matrix.index(0)
        move_index = zero_index - self.width
        
        #swap the tiles
        self.__swapNumbers(zero_index, move_index)
        
    def moveDown(self):
        zero_index = self.matrix.index(0)
        move_index = zero_index + self.width
        
        #swap the tiles
        self.__swapNumbers(zero_index, move_index)
        
    def moveRight_regular(self):
        zero_index = self.matrix.index(0)
        move_index = zero_index + 1
        
        #swap the tiles
        self.__swapNumbers(zero_index, move_index)
        
    def moveLeft_regular(self):
        zero_index = self.matrix.index(0)
        move_index = zero_index - 1
        
        #swap the tiles
        self.__swapNumbers(zero_index, move_index)
    
    def moveRight_wrap(self):
        zero_index = self.matrix.index(0)
        move_index = zero_index - (self.width - 1)
        
        #swap the tiles
        self.__swapNumbers(zero_index, move_index)
        
    def moveLeft_wrap(self):
        zero_index = self.matrix.index(0)
        move_index = zero_index + (self.width - 1)
        
        #swap the tiles
        self.__swapNumbers(zero_index, move_index)
        
    def moveUpRight(self):
        zero_index = self.matrix.index(0)
        move_index = (zero_index - self.width) + 1
        
        #swap the tiles
        self.__swapNumbers(zero_index, move_index)
        
    def moveUpLeft(self):
        zero_index = self.matrix.index(0)
        move_index = (zero_index - self.width) - 1
        
        #swap the tiles
        self.__swapNumbers(zero_index, move_index)
        
    def moveDownRight(self):
        zero_index = self.matrix.index(0)
        move_index = (zero_index + self.width) + 1
        
        #swap the tiles
        self.__swapNumbers(zero_index, move_index)  
        
    def moveDownLeft(self):
        zero_index = self.matrix.index(0)
        move_index = (zero_index + self.width) - 1
        
        #swap the tiles
        self.__swapNumbers(zero_index, move_index)  
        
        
    def showState(self):
        print(self.matrix)