# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:53:49 2020

@author: NgoWi
"""

class Puzzle:
    def __init__(self, height, width, init_list, cost):
        self.matrix = init_list
        self.height = height
        self.width = width
        self.cost = cost
    
    def regularMoveUp(self):
        return self.matrix.index(0)




        