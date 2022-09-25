'''
Four in a row

Author: Tony Lindgren
'''
from copy import deepcopy

class FourInARow:
    def __init__(self, player, chip):
        new_board = []
        for _ in range(7):
            new_board.append([])
        self.board = new_board
        self.action = list(range(7))
        if chip != 'r' and chip != 'w':
            print('The provided value is not a valid chip (must be, r or w): ', chip)
        if player == 'human' and chip == 'w':
            self.ai_player = 'r'
        else:
            self.ai_player = 'w'
        self.curr_move = chip
    
    def to_move(self):
        return self.curr_move
        
    #actions
    def actions(self):
        actions = []
        for i in range(len(self.board)):
            if len(self.board[i]) < 6:
                actions.append(i)
        return actions


    def result(self, action):                    
        dc = deepcopy(self)
        if len(dc.board[action])<6:
            if self.to_move() == 'w':
                dc.curr_move = 'r'
                dc.board[action].append(self.to_move())  
            else:
                dc.curr_move = 'w'
                dc.board[action].append(self.to_move())  
        else:
            raise Exception("Invalid input") 
        return dc
        
    #eval
    #TODO
        
    def is_terminal(self):
        #check vertical
        for c in range(0, len(self.board)):
            count = 0
            curr_chip = None
            for r in range(0, len(self.board[c])):
                if curr_chip == self.board[c][r]:
                    count = count + 1
                else:
                    curr_chip = self.board[c][r]     
                    count = 1
                if count == 4:
                    if self.ai_player == curr_chip:        
                        #print('Found vertical win')
                        return True, 100          #MAX ai wins positive utility
                    else:
                        #print('Found vertical loss')
                        return True, -100         #MIN player wins negative utility
                    
        #check horizontal 
        #TODO   
        for r in range (0, 6):
            count = 0
            curr_chip = None

            for c in range(0, len(self.board)):
                if len(self.board[c]) >r :
                    if curr_chip == self.board[c][r]:
                        count = count + 1
                    else:
                        curr_chip = self.board[c][r]     
                        count = 1
                    if count == 4:
                        if self.ai_player == curr_chip:        
                            #print('Found horizontal win')
                            return True, 100          #MAX ai wins positive utility
                        else:
                            #print('Found horizontal loss')
                            return True, -100         #MIN player wins negative utility
            
                    
        #check positive diagonal
        for c in range(7-3): 
            for r in range(6-3):    
                if len(self.board[c]) > r and len(self.board[c+1]) > r+1 and len(self.board[c+2]) > r+2 and len(self.board[c+3]) > r+3:
                    if self.ai_player == self.board[c][r] and self.ai_player == self.board[c+1][r+1] and self.ai_player == self.board[c+2][r+2] and self.ai_player == self.board[c+3][r+3]:  
                        #print('Found positive diagonal win')
                        return True, 100
                    elif self.ai_player != self.board[c][r] and self.ai_player != self.board[c+1][r+1] and self.ai_player != self.board[c+2][r+2] and self.ai_player != self.board[c+3][r+3]:  
                        #print('Found positive diagonal loss')
                        return True, -100
        
        #check negative diagonal 
        #TODO   
        for c in range(7-3): 
            for r in range(6-3, 6):    
                if len(self.board[c]) > r and len(self.board[c+1]) > r - 1 and len(self.board[c+2]) > r - 2 and len(self.board[c+3]) > r - 3:
                    if self.ai_player == self.board[c][r] and self.ai_player == self.board[c+1][r - 1] and self.ai_player == self.board[c+2][r - 2] and self.ai_player == self.board[c+3][r - 3]:  
                        #print('Found negative diagonal win')
                        return True, 100
                    elif self.ai_player != self.board[c][r] and self.ai_player != self.board[c+1][r - 1] and self.ai_player != self.board[c+2][r - 2] and self.ai_player != self.board[c+3][r - 3]:  
                        #print('Found negative diagonal loss')
                        return True, -100
             
        #check draw
        #TODO
        count_d = 0
        for r in range(5,-1,-1):
            for c in range(6):
                try:
                    if self.board[c][r]:
                        count_d = count_d + 1
                except:
                    pass
        
        if count_d==42:
            return True, 0

                
        return False, 0                                            
                
    #pretty_print
    def pretty_print(self):
        for r in range(5,-1,-1):
            for c in range(7):
                try:
                    print(self.board[c][r], end=" ") 
                except:
                    print('_', end=" ")
            print()
