import { tilesToHand, RuleSet } from 'mahjong-tile-efficiency'

// Get the command line arguments
const args = process.argv.slice(2);

// Split the input string into an array of tiles
function parseTiles(input) {
    let res = []
    for (let i = 0; i < input.length; i += 2) {
        res.push(input[i] + input[i + 1])
    }
    return res
}

const tiles = parseTiles(args[0])
const hand = tilesToHand(tiles)
const mode = args[1]

const riichiRule = new RuleSet('Riichi')

// If mode is '0', calculate the shanten number and exit
if (mode === '0') {
    const shantenResult = riichiRule.calShanten(hand)
    console.log(shantenResult)
    process.exit(0)
}

// If mode is '1', calculate the tile acceptance and exit
const ukeireResult = riichiRule.calUkeire(hand)
const discard = {}

// Calculate the tile acceptance for each tile in the discard
for (const [key, value] of Object.entries(ukeireResult.normalDiscard)) {
    let tile_acceptance = 0
    for (const [key2, value2] of Object.entries(value)) {
        tile_acceptance += value2
    }
    discard[key] = tile_acceptance
}

console.log(discard)