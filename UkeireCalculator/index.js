import { tilesToHand, RuleSet } from 'mahjong-tile-efficiency'

const args = process.argv.slice(2);

function parseTiles(input) {
    let res = []
    for (let i = 0; i < input.length; i += 2) {
        res.push(input[i] + input[i + 1])
    }
    return res
}

const tiles = parseTiles(args[0])
const hand = tilesToHand(tiles)

const riichiRule = new RuleSet('Riichi')
const shantenResult = riichiRule.calShanten(hand)
// const ukeireResult = riichiRule.calUkeire(hand)

console.log(shantenResult)
// console.log(ukeireResult)