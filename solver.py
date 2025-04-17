from Hand import Hand
import ast
import heapq
from MahjongProblem import MahjongProblem
from copy import deepcopy

with open('initial_state.txt', 'r') as f:
    lines = f.readlines()
    hand = lines[0].strip()
    deck = ast.literal_eval(lines[1])

# print(hand)
# print(deck)

start = MahjongProblem(hand, deck)
print(start.state)
print(start.actions)
print(start.deck[0])

for action in start.actions:
    # print(action)
    temp = deepcopy(start)
    print("Discarding:", temp.state.index_to_tile(action))
    temp.discard(action)
    print(temp.state)

# def A_star_search(start, h):
#     explored = set() # Set of serialized states
#     frontier = [] # Priority queue of nodes of the form (f(n), Hand, list of actions)
#     # h_log = {} # Heuristic Effectiveness: Log h(n) for each state 
#     heapq.heappush(frontier, (h(start.state), start, []))

#     while frontier:
#         current = heapq.heappop(frontier)
#         if current[1].goal_test():
#             print(f'Number of states explored: {len(explored)}') # Heuristic Effectiveness
#             print(f'Memory used: {sys.getsizeof(explored)} bytes') # Space complexity analysis
#             return current[2], h_log
#         if str(current[1].state) not in explored:
#             h_log[str(current[1].state)] = h(current[1].state)
#             explored.add(str(current[1].state))
#             for action in current[1].actions:
#                 new = current[1].transition_function(action)
#                 new.g += 1
#                 heapq.heappush(frontier, (new.g + h(new.state), new, current[2] + [action.__name__]))