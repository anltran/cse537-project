class Hand:

    # The hand is represented by an int array, where hand[i] is the number of tiles i in the hand
    # 3 suits, 9 tiles each, plus 7 honor tiles
    # [0, 8] : man, [9, 17] : pin, [18, 26] : sou, [27, 33] : honors
    def __init__(self, input):
        self.hand = parse(input)
    
    # Serializes the hand in a compact and sorted format
    def __str__(self):
        man = ""
        pin = ""
        sou = ""
        honor = ""

        for i in range(0, 9):
            for _ in range(self.hand[i]):
                man += str(i % 9 + 1)
        if man:
            man += 'm'
        for i in range(9, 18):
            for _ in range(self.hand[i]):
                pin += str(i % 9 + 1)
        if pin:
            pin += 'p'
        for i in range(18, 27):
            for _ in range(self.hand[i]):
                sou += str(i % 9 + 1)
        if sou:
            sou += 's'
        for i in range(27, 34):
            for _ in range(self.hand[i]):
                honor += str(i % 9 + 1)
        if honor:
            honor += 'z'

        return man + pin + sou + honor

# Parses a string representing the hand into the int array, can handle verbose or compact format
def parse(hand):
    res = [0] * ((3 * 9) + 7)
    ranks = []
    for c in hand:
        if c.isnumeric():
            ranks.append(int(c)-1)
        else:
            if c == 'm':
                offset = 0
            elif c == 'p':
                offset = 9
            elif c == 's':
                offset = 18
            elif c == 'z':
                offset = 27
            else:
                raise ValueError("Invalid tile suit")
            for rank in ranks:
                res[rank+offset] += 1
            ranks = []
    return res

# Takes in a string of length 2 representing a tile and outputs its index in the hand
def tile_to_index(tile):
    rank, suit = int(tile[0])-1, tile[1]
    if suit == 'm':
        offset = 0
    elif suit == 'p':
        offset = 9
    elif suit == 's':
        offset = 18
    elif suit == 'z':
        offset = 27
    else:
        raise ValueError("Invalid tile suit")
    return rank + offset

# Takes in a tile index and outputs the string representation of the tile
def index_to_tile(index):
    rank = index % 9 + 1
    suit = index // 9

    if suit == 0:
        suit = 'm'
    elif suit == 1:
        suit = 'p'
    elif suit == 2:
        suit = 's'
    elif suit == 3:
        suit = 'z'
    else:
        raise ValueError("Tile index out of range")
    return str(rank) + suit