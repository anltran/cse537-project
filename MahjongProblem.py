from collections import deque
from copy import deepcopy
import Hand

import subprocess
import ast
# shanten_path = r'UkeireCalculator\index.js' # Use this for 1 player
shanten_path = r'..\UkeireCalculator\index.js' # Use this for 4 players

class MahjongProblem:

    def __init__(self, state, deck):
        self.state = Hand.Hand(state) # Hand object containing the list of tiles in the hand

        command = ["node", shanten_path, str(self.state), "1"]
        discard = subprocess.run(command, capture_output=True, text=True, check=True).stdout.strip()
        self.actions = ast.literal_eval(discard) # dictionary of tiles to potentially discard in the form {tile: resulting tile acceptance}

        self.deck = deque(deck) # queue for the remaining tiles in the wall
        self.g = 0

    def discard(self, i):
        self.state.hand[i] -= 1
        tile = self.deck.popleft()
        self.state.hand[Hand.tile_to_index[tile]] += 1

        command = ["node", shanten_path, str(self.state), "1"]
        discard = subprocess.run(command, capture_output=True, text=True, check=True).stdout.strip()
        self.actions = ast.literal_eval(discard)

        return self

    # Create a deepcopy of the current state and apply the action
    def transition_function(self, action):
        return deepcopy(self).discard(action)

    # Goal is reached if the hand is 0-shanten
    def goal_test(self):
        command = ["node", shanten_path, str(self), "0"]
        result = subprocess.run(command, capture_output=True, text=True, check=True).stdout.strip()
        return result == '0'

    # Serialize the state for set membership and printing
    def __str__(self):
        return str(self.state)
    
    # Tie breaker for heapq for identical f(n)
    def __lt__(self, other):
        return str(self.state) < str(other.state)