import random
from Hand import Hand, compact_serialize

tiles = [
    '1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m',  # Manzu (Characters)
    '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p',  # Pinzu (Dots)
    '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s',  # Souzu (Bamboo)
    '1z', '2z', '3z', '4z', '5z', '6z', '7z'  # Honors
]

# 1z : ton (East), 2z : nan (South), 3z : sha (West), 4z : pei (North)
# 5z : haku (White Dragon), 6z : hatsu (Green Dragon), 7z : chun (Red Dragon)

deck = tiles * 4
random.shuffle(deck)

num_tiles = 14

hand = deck[:num_tiles]
deck = deck[num_tiles:]

hand = Hand("".join(hand))
deck = str(deck)

with open('initial_state.txt', 'w') as f:
    f.write(compact_serialize(hand.hand) + '\n')
    f.write(deck + '\n')

import subprocess

path = r'UkeireCalculator\index.js'
command = ["node", path, str(hand), "0"]
result = subprocess.run(command, capture_output=True, text=True, check=True).stdout.strip()
print(f'Initial shanten: {result}')