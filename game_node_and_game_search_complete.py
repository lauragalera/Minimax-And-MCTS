'''
Definitions for GameNode, GameSearch and MCTS

Author: Tony Lindgren
'''
from lib2to3.pytree import Leaf
from platform import node
from time import process_time
import random
import math
from turtle import left
import numpy as np


class GameNode:
    '''
    This class defines game nodes in game search trees. It keep track of: 
    state
    '''
    def __init__(self, state, node=None, parent=None):
        self.state = state
        self.parent = parent 
        self.wins = 0 
        self.succesors = [] 
        self.move = 0 
        self.actions_left = []  
        self.visits = 0 
           
class GameSearch:
    '''
    Class containing different game search algorithms, call it with a defined game/node
    '''                 
    def __init__(self, game, depth=3, time=10):  
        self.state = game
        self.depth = depth
        self.time = time

    def mcts(self):                     
        start_time = process_time() 
        tree = GameNode(self.state)
        tree.actions_left = tree.state.actions()   
        elapsed_time = 0
        iteracion = 0
        while elapsed_time < self.time:
            iteracion+=1  
            leaf = self.select(tree)
            child = self.expand(leaf)          
            result = self.simulate(child) 
            self.back_propagate(result, child)         
            stop_time = process_time()
            elapsed_time = stop_time - start_time
        move = self.actions(tree)
        return move
        
    def select(self, node):
        '''
        selects a node to expand and the expand function 
        that creates new children nodes
        '''
        max_ucb = -np.Infinity
        if len(node.actions_left):
            return node
        
        node = self.compute_ucb(node, max_ucb) 
   
        if node.state.is_terminal()[0]:
            return node

        if len(node.succesors)<1:
            node.actions_left = node.state.actions()  

        return self.select(node)

    def expand(self, leaf):
        '''
        we randomly pick an unexplored node of a leaf node.
        '''
        if leaf.state.is_terminal()[0] or not len(leaf.actions_left):
            return leaf
        move = random.choice(leaf.actions_left)
        leaf.actions_left.remove(move)
        node = GameNode(leaf.state.result(move), parent = leaf)
        leaf.succesors.append(node)
        return node
    
    def simulate(self, child):
        '''
        we roll out multiple simulations 
        '''
        if child.state.is_terminal()[0] or not len(child.actions_left):
            return child
        move = random.choice(child.state.actions())
        node = GameNode(child.state.result(move), parent = child)
        return self.simulate(node)       

    def back_propagate(self, result, child):
        '''
        keep track of which player turn it is to
        move
        '''
        terminal, value = result.state.is_terminal()
        # if flag>1 is human
        flag = 1
        
        while child.parent!=None:
            child.visits +=1
            if value>0:
                child.wins +=1

            child = child.parent
            flag*=-1

    def actions(self, tree):
        node = None # terminal node must not be
        max_ucb = -np.Infinity
        node = self.compute_ucb(tree, max_ucb)

        for a in tree.state.actions():
            if node.state.board == tree.state.result(a).board:
                return a

    def compute_ucb(self, node, max_ucb):
        for child in node.succesors:
            if child.visits!=0 and node.wins !=0 :
                ucb = child.wins/child.visits + 1.4 * np.sqrt((np.log(node.wins)/child.visits))
                if ucb > max_ucb :
                    max_ucb = ucb
                    node = child
            else:
                node = child
                break
        return node

    def minimax_search(self): 
        start_time = process_time()   
        _, move = self.max_value(self.state, self.depth, -1*math.inf, math.inf, start_time)  
        return move
    
    def max_value(self, state, depth, alfa, beta, start_time):
        move = None
        terminal, value = state.is_terminal()
        stop_time = process_time()
        elapsed_time = stop_time - start_time
        if terminal:
            return value, None
        elif (depth == 0 or elapsed_time >= self.time):
            return state.eval(), None
        actions = state.actions()
        for action in actions: 
            new_state = state.result(action)
            v2, _ = self.min_value(new_state, depth - 1, alfa, beta, start_time)
            if v2 > alfa:
                alfa = v2
                move = action
            if(alfa >= beta):
                break
        if(len(actions) == 0):
            print(move)
        return alfa, move
    
    def min_value(self, state, depth, alfa, beta, start_time):
        move = None
        terminal, value = state.is_terminal()
        stop_time = process_time()
        elapsed_time = stop_time - start_time
        if terminal:
            return value, None
        elif (depth == 0 or elapsed_time >= self.time):
            return state.eval(), None
        actions = state.actions()
        for action in actions: 
            new_state = state.result(action)
            v2, _ = self.max_value(new_state, depth - 1, alfa, beta, start_time)
            if v2 < beta:
                beta = v2
                move = action
            if alfa >= beta:
                break
        if(len(actions) == 0):
            print(move)
        return beta, move
