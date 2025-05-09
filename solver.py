import ast
import heapq
import Hand
from MahjongProblem import MahjongProblem

import subprocess
shanten_path = r'UkeireCalculator\index.js'

import time
import tracemalloc

with open('hard_tests/3.txt', 'r') as f:
# with open('initial_state.txt', 'r') as f:
    lines = f.readlines()
    hand = lines[0].strip()
    deck = ast.literal_eval(lines[1])

start = MahjongProblem(hand, deck)

# Shanten heuristic function
def h(state):
    command = ["node", shanten_path, str(state), "0"]
    return int(subprocess.run(command, capture_output=True, text=True, check=True).stdout.strip())

def A_star_search(start, h):
    explored = set() # Set of serialized states
    frontier = [] # Priority queue of nodes of the form (f(n), tile acceptance, Hand, list of actions)
    heapq.heappush(frontier, (h(start.state), 0, start, []))

    while frontier:
        current = heapq.heappop(frontier)
        if current[2].goal_test():
            print(f'States explored: {len(explored)}')
            return current[3], Hand.compact_serialize(current[2].state.hand)
        if str(current[2].state) not in explored:
            explored.add(str(current[2].state))
            for action, ukeire in current[2].actions.items():
                index = Hand.tile_to_index[action]
                new = current[2].transition_function(index)
                new.g += 1
                heapq.heappush(frontier, (new.g + h(new.state), 0, new, current[3] + [action])) # Use this for pruned discards only
                # heapq.heappush(frontier, (new.g + h(new.state), -ukeire, new, current[3] + [action])) # Use this for ukeire (slower)

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