import ast
import heapq
import Hand
from MahjongProblem import MahjongProblem

import subprocess
shanten_path = r'C:\Users\trana\Desktop\cse537-project\ShantenCalculator\ShantenCalculator\bin\Debug\net6.0\ShantenCalculator.exe'

with open('initial_state.txt', 'r') as f:
    lines = f.readlines()
    hand = lines[0].strip()
    deck = ast.literal_eval(lines[1])

start = MahjongProblem(hand, deck)
# print(start.state)
# print(start.actions)
# print(start.deck[0])

# for action in start.actions:
#     print("Discarding:", Hand.index_to_tile(action))
#     print(start.transition_function(action).state)

def h(state):
    command = [shanten_path, str(state)]
    return int(subprocess.run(command, capture_output=True, text=True, check=True).stdout)

def A_star_search(start, h):
    explored = set() # Set of serialized states
    frontier = [] # Priority queue of nodes of the form (f(n), Hand, list of actions)
    heapq.heappush(frontier, (h(start.state), start, []))

    while frontier:
        current = heapq.heappop(frontier)
        if current[1].goal_test():
            # print(len(explored))
            return current[2], str(current[1].state)
        if str(current[1].state) not in explored:
            explored.add(str(current[1].state))
            for action in current[1].actions:
                new = current[1].transition_function(action)
                new.g += 1
                heapq.heappush(frontier, (new.g + h(new.state), new, current[2] + [Hand.index_to_tile(action)]))

path, ready_hand = A_star_search(start, h)
print(path)
print(ready_hand)
