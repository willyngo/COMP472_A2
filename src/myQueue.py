# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:47:42 2020

@author: NgoWi
"""
import Puzzle
import heapq

class myQueue:
    def __init__(self):
       self.index = 0
       self._data = []
       
    def __check_if_exists(self, puzzle):
        doesExists = False
               
    """
    myQueue is a data structure that takes in a tuple in the form of 
    (cost, matrix). The cost will allow the heapq to sort the entries in the queue
    """
    def push_sort_uniform(self, puzzle):
        cost = puzzle.g_cost
        heapq.heappush(self._data, (cost, self.index, puzzle))
        self.index += 1
        
    """
    heapq pop function pops item with lowest cost of the (cost, matrix) tuple
    """
    def pop(self):
        popped = heapq.heappop(self._data)[2]
        
        #loop through the list and check for duplicates
        for i in range(1, len(self._data)):
            current = self._data[i][2]
            if (popped == current):
                self._data.pop(i)
                
        return popped
                   
    """
    Prints content of queue. For debugging purposes
    """
    def showQueue(self):
        print("current puzzle configurations in this queue is: ")
        for item in self._data:
            print(item[0], ": ", item[2].matrix)
        
        print("=================================================")