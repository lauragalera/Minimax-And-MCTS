'''
Definitions for GameNode, GameSearch and MCTS

Author: Tony Lindgren
Coauthors: Laura Galera and 
'''
from time import process_time
import random
import math
import numpy as np


class GameNode:
    '''
    This class defines game nodes in game search trees. It keep track of: 
    state
    '''
    def __init__(self, state, node=None, parent=None, move = 0):
        self.state = state
        self.parent = parent 
        self.wins = 0 
        self.succesors = [] 
        self.move = move 
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
        '''
        Monte Carlo tree search algorithm
        '''                     
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
        
    def select(self, node):
        '''
        selects successive child nodes until a leaf node with a
        potential child is reached
        '''
        if len(node.actions_left) or node.state.is_terminal()[0]:
            return node
        
        node = self.compute_ucb(node) 

        if not len(node.succesors): #node never expanded
            node.actions_left = node.state.actions()  

        return self.select(node)

    def expand(self, leaf):
        '''
        randomly picks an unexplored node of a leaf node.
        '''
        if leaf.state.is_terminal()[0]:
            return leaf
        move = random.choice(leaf.actions_left)
        leaf.actions_left.remove(move)
        node = GameNode(leaf.state.result(move), parent = leaf, move = move)
        leaf.succesors.append(node)
        return node
    
    def simulate(self, child):
        '''
        completes a random playout until the game is decided 
        '''
        if child.state.is_terminal()[0]:
            return child
        move = random.choice(child.state.actions())
        node = GameNode(child.state.result(move), parent = child, move = move)
        return self.simulate(node)       

    def back_propagate(self, result, child):
        '''
        uses the result of the playout to update the information in
        the nodes from the path child to the root.
        '''
        _, value = result.state.is_terminal()    
        flag = child.state.ai_player != child.state.curr_move
            
        while child!= None:
            child.visits +=1
            #keep track of the player
            if value > 0 and flag:
                child.wins +=1
            child = child.parent
            flag = not flag

    def actions(self, tree):
        '''
        returns the best move from the simulated playouts
        '''
        node = self.compute_ucb(tree)
        return node.move

    def compute_ucb(self, node):
        '''
        returns the child of node with the highest ucb 
        '''
        max_ucb = -np.Infinity
        max_node = node
        for child in node.succesors:
            if child.visits > 0 and node.visits > 0: 
                ucb = child.wins/child.visits + 1.4 * np.sqrt(np.log(node.visits)/child.visits)
                if ucb > max_ucb :
                    max_ucb = ucb
                    max_node = child
            else: #node never visited
                max_node = child
                break
        return max_node

    def minimax_search(self):
        '''
        Minimax algorithm
        ''' 
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
