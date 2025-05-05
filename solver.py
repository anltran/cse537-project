import ast
import heapq
import Hand
from MahjongProblem import MahjongProblem

import subprocess
shanten_path = r'UkeireCalculator\index.js'

import time
import tracemalloc

with open('easy_tests/4.txt', 'r') as f:
# with open('initial_state.txt', 'r') as f:
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
    command = ["node", shanten_path, str(state)]
    return int(subprocess.run(command, capture_output=True, text=True, check=True).stdout.strip())

def A_star_search(start, h):
    explored = set() # Set of serialized states
    frontier = [] # Priority queue of nodes of the form (f(n), Hand, list of actions)
    heapq.heappush(frontier, (h(start.state), start, []))

    while frontier:
        current = heapq.heappop(frontier)
        if current[1].goal_test():
            print(f'States explored: {len(explored)}')
            return current[2], Hand.compact_serialize(current[1].state.hand)
        if str(current[1].state) not in explored:
            explored.add(str(current[1].state))
            for action in current[1].actions:
                new = current[1].transition_function(action)
                new.g += 1
                heapq.heappush(frontier, (new.g + h(new.state), new, current[2] + [Hand.index_to_tile[action]]))

tracemalloc.start()
start_time = time.time()
path, ready_hand = A_star_search(start, h)
end_time = time.time()

elapsed_time = end_time - start_time
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Elapsed time: {elapsed_time:.2f} seconds")
print(f"Peak memory usage: {peak / 10**6:.2f}MB")
print(f"Solution path length: {len(path)}")
print(f"Discarded tiles: {path}")
print(f"Ready hand: {ready_hand}")