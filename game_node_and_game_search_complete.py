'''
Definitions for GameNode, GameSearch and MCTS

Author: Tony Lindgren
'''
from time import process_time
import random
import math


class GameNode:
    '''
    This class defines game nodes in game search trees. It keep track of: 
    state
    '''
    def __init__(self, state, node=None):
        self.state = state   
           
class GameSearch:
    '''
    Class containing different game search algorithms, call it with a defined game/node
    '''                 
    def __init__(self, game, depth=3):
        self.state = game       
        self.depth = depth

    def mcts(self):                     
        start_time = process_time() 
        tree = GameNode(self.state)
        tree.actions_left = tree.state.actions()   
        elapsed_time = 0
        while elapsed_time < self.time:   
            leaf = self.select(tree)
            child = self.expand(leaf)               
            result = self.simulate(child) 
            self.back_propagate(result, child)         
            stop_time = process_time()
            elapsed_time = stop_time - start_time
        move = self.actions(tree)
        return move
    
    def minimax_search(self): 
        start_time = process_time()   
        _, move = self.max_value(self.state, self.depth)  
        return move
    
    def max_value(self, state, depth):
        move = None
        terminal, value = state.is_terminal()
        if terminal or depth == 0:
            return value, None
        v = -100000
        actions = state.actions()
        for action in actions: 
            new_state = state.result(action)
            v2, _ = self.min_value(new_state, depth - 1)
            if v2 > v:
                v = v2
                move = action
        return v, move
    
    def min_value(self, state, depth):
        move = None
        terminal, value = state.is_terminal()
        if terminal or depth == 0:
            return value, None  
        v = 100000
        actions = state.actions()
        for action in actions: 
            new_state = state.result(action)
            v2, _ = self.max_value(new_state, depth - 1)
            if v2 < v:
                v = v2
                move = action
        return v, move
