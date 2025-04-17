from collections import deque
from copy import deepcopy
import numpy as np
import Hand

class MahjongProblem:

    def __init__(self, state, deck):
        self.state = Hand.Hand(state) # Hand object containing the list of tiles in the hand
        self.actions = np.nonzero(self.state.hand)[0] # list of tiles to potentially discard
        self.deck = deque(deck) # queue for the remaining tiles in the wall

    def discard(self, i):
        self.state.hand[i] -= 1
        tile = self.deck.popleft()
        self.state.hand[self.state.index(tile)] += 1
        self.unique_tiles = np.nonzero(self.state.hand)[0]

    # # Create a deepcopy of the current state and apply the action
    # def transition_function(self, action):
    #     return action(deepcopy(self))

    # # Goal is reached if the blank tile is at the bottom right corner and the tiles are in ascending order
    # def goal_test(self):
    #     if self.blank_index != (self.n - 1, self.n - 1):
    #         return False
        
    #     count = 1
    #     end = (self.n ** 2) - 1
    #     for i in range(self.n):
    #         for j in range(self.n):
    #             if self.state[i][j] != count:
    #                 return False
    #             if count == end:
    #                 break
    #             count += 1
    #     return True

    # # Serialize the state for set membership and printing
    # def __str__(self):
    #     return str(self.state)
    
    # # Tie breaker for heapq for identical f(n)
    # def __lt__(self, other):
    #     return self.blank_index < other.blank_index