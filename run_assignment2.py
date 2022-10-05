'''
Define game and start execution of game search

Author: Tony Lindgren
Coauthor: Laura Galera and America Castrejon
'''
from four_in_a_row_complete import FourInARow
from game_node_and_game_search_complete import GameSearch

    
def ask_ai(state0):
    '''
    returns the state of the game after the AI made a move
    and whether the game ended with the last move or not
    '''
    gs = GameSearch(state0, depth=3, time=10)
    #move = gs.minimax_search()
    move = gs.mcts()
    state1 = state0.result(move)
    print('--------')
    print('AI moves')
    print('--------')
    state1.pretty_print()  
    stop, value = state1.is_terminal() 
    if stop == True:
        if value > 0:
            print('AI won')                      
        else:
            print('Human won')
        return state1, True
    return state1, False 

def ask_player(state0):
    '''
    returns the state of the game after the human made a move
    and whether the game ended with the last move or not
    '''
    print('--------')
    print('Player moves')
    print('--------')

    ans= False
    while not ans:
        try:
            move = int(input('Choose a row (0-6): '))
            if move>6 or move<0 :
                print("Invalid input")
            
            else:
                state1 = state0.result(move)
                ans = True
        except:
            print("Invalid input")

    state1.pretty_print() 
    stop, value = state1.is_terminal() 
    if stop == True:
        if value > 0:
            print('AI won')                       
        else:
            print('Human won')
        return state1, True
    return state1, False  

 
def main():
    print('Welcome to play for-in-a-row!')
    answer = None
    while answer != 'y' and answer != 'n':
        answer = input('Would you like to start [y/n]: ')        
    if(answer == 'y'):  
        state0 = FourInARow('human', 'w') 
        stop = False
        while not stop:            
        #Ask player         
            state1, stop1 = ask_player(state0)
            if stop1:
                break
            else:
        #AI move
                state0, stop2 = ask_ai(state1)  
                if stop2:
                    break                
    else:
        state0 = FourInARow('ai','w') 
        stop = False
        while not stop: 
        #AI move
            state1, stop1 = ask_ai(state0)    
            if stop1:
                break
            else:  
        #Ask player
                state0, stop2 = ask_player(state1)    
                if stop2:
                    break               
       
if __name__ == "__main__":
    main()