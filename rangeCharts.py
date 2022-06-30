from poker import *
from rc_init import rc as rc
import string

RANKINDS = {"2":12, "3":11, "4":10, "5":9, "6":8, "7":7, "8":6, "9":5, "T":4, "J":3, "Q":2, "K":1, "A":0}
SUITED = {"o":0, "s":1}

"""

RangeChart documentation:
rc = rangeChart()
rc.chart[x][y] = [exists, combos]
rc.exists() fetches exists
    can check whether a given hand is in the range
    1) generic hand (i.e., AAo, KQs, 56o)
    2) specific hand (i.e., KhQh, 5s6d)


"""

def cardsToString(c1 : Card, c2 : Card) -> string:
    result = CARDS[c1.rank] + CARDS[c2.rank]
    if c1.suit == c2.suit:
        result += "s"
    else: 
        result += "o"
    return result

def stringToIndex(cards: string) -> list: #make pairs not need o or s
    r1 = RANKINDS[cards[0]]
    r2 = RANKINDS[cards[1]]
    if SUITED[cards[2].lower()]:
        return [min(r2, r1), max(r2, r1)]
    return [max(r2, r1), min(r2, r1)]

class rangeChart(object):

    def __init__(self) -> None:
        self.chart = rc
        pass

    # Use cases:
        # 1) rc.exists( "KQs" ) checks if KQs is in the range
        # 2) rc.exists( [Card("Kh"), Card("Qh")], True ) checks if KQ of hearts is in the range
    def exists(self, cards, cardParam = False) -> int:
        print(cardParam)
        if cardParam:
            # assert(type of cards == list of 2 cards)
            cards = cardsToString(cards[0], cards[1])
        # else assert(type of cards == string)
        index = stringToIndex(cards)
        print(index[0], index[1])
        return self.chart[index[0]][index[1]][0]

    def combos(self, cards, cardParam = False):
        if cardParam:
            # assert(type of cards == list of 2 cards)
            cards = cardsToString(cards[0], cards[1])
        # else assert(type of cards == string)
        index = stringToIndex(cards)
        return self.chart[index[0]][index[1]][1]

rc = rangeChart()
print(rc.chart)