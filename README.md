# Assignment 2

### Course: Principals and foundations of artificial intelligence

### Students: Laura Galera Alfaro (laga6199), América Castrejón Porres (amca6849)

#### Minimax vs minimax alpha beta

From our point of view, including alpha-beta pruning reduces the space of search and, hence, the AI has a faster time of response. We played a game "AI with minimax against an AI with minimax alpha-beta", depth of search was 8 for both, and we could appreciate that minimax alpha-beta made a decision way faster; specially at the begining of the game, whereas for the normal AI took minutes. 

#### Eval function

We created an evaluation function that checks columns and rows. We left out diagonals to keep it simple.

It iterates each column, from top to bottom, counting empty tiles and the following chains of discs belonging to our AI. It stops when it reaches the end of the column or it finds a disc from the human player. Similar for rows. The difference is that it keeps evaluating the row after finding a disc from the human player, but spliting the chain.

There is a big difference when including this evaluation function. Not only it beats the normal AI, but it also beats [this AI](https://www.helpfulgames.com/subjects/brain-training/connect-four.html) until level 11 (depth = 8). Before, the AI played more or less randomly because the value was 0 when the state was not final. However, the current AI takes into account the state of the board. Regarding time, there is no much difference since the evaluation function is O(n*m) time complexity.

#### Monte Carlo Tree Search

Our thoughts are that this AI is clever enough to block win moves of the human player and try to win by creating chains of chips. Moreover, it tends to place the chips in central columns because these moves lead to higher ucb nodes. 

We tested this AI for times of 10 seconds and 20 seconds. In the first case, the AI was beaten at level 7, whereas for 20 seconds it was beaten at level 9. 

In light of the above, we can conclude that Minimax algorithm gave better results than Monte Carlo.
