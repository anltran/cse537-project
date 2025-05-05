import { tilesToHand, RuleSet } from 'mahjong-tile-efficiency'

const args = process.argv.slice(2);

function parseTiles(input) {
    let res = []
    let ranks = []
    for (let i = 0; i < input.length; i++) {
        const char = input[i]
        if (char >= '1' && char <= '9') {
            ranks.push(char)
        } else if (char === 'm' || char === 'p' || char === 's' || char === 'z') {
            ranks.forEach(tile => {
                res.push(tile + char)
            })
            ranks = []
        }
    }
    return res
}

const tiles = parseTiles(args[0])
const hand = tilesToHand(tiles)

const riichiRule = new RuleSet('Riichi')
const ukeireResult = riichiRule.calUkeire(hand)

console.log(ukeireResult)