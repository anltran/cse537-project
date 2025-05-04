from collections import deque
from copy import deepcopy
import Hand

import subprocess
shanten_path = r'C:\Users\trana\Desktop\cse537-project\ShantenCalculator\ShantenCalculator\bin\Debug\net6.0\ShantenCalculator.exe'

class MahjongProblem:

    def __init__(self, state, deck):
        self.state = Hand.Hand(state) # Hand object containing the list of tiles in the hand
        self.actions = set([i for i, x in enumerate(self.state.hand) if x != 0]) # list of tiles to potentially discard
        self.deck = deque(deck) # queue for the remaining tiles in the wall
        self.g = 0

    def discard(self, i):
        self.state.hand[i] -= 1
        if self.state.hand[i] == 0:
            self.actions.remove(i)
        tile = self.deck.popleft()
        self.state.hand[Hand.tile_to_index[tile]] += 1
        self.actions.add(Hand.tile_to_index[tile])
        return self

    # Create a deepcopy of the current state and apply the action
    def transition_function(self, action):
        return deepcopy(self).discard(action)

    # Goal is reached if the hand is 0-shanten
    def goal_test(self):
        command = [shanten_path, str(self)]
        result = subprocess.run(command, capture_output=True, text=True, check=True).stdout
        return result == '0'

    # Serialize the state for set membership and printing
    def __str__(self):
        return str(self.state)
    
    # Tie breaker for heapq for identical f(n)
    def __lt__(self, other):
        return str(self.state) < str(other.state)