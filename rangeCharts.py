from poker import *
import string

RANKINDS = {"2":0, "3":1, "4":2, "5":3, "6":4, "7":5, "8":6, "9":7, "T":8, "J":9, "Q":10, "K":11, "A":12}
SUITED = {"o":0, "s":1}

def cardsToString(c1 : Card, c2 : Card):
    result = CARDS[c1.rank] + CARDS[c2.rank]
    if c1.suit == c2.suit:
        result += "s"
    else: 
        result += "o"
    return result

#ur gay

class rangeChart(object):

    def __init__(self) -> None:
        self.chart = [[[]]*13 for i in range(13)]
        pass

    def cardsToIndex(self, cards):
        r1 = RANKINDS[cards[0]]
        r2 = RANKINDS[cards[1]]
        if SUITED[cards[2].lower()]:
            return [max(r2, r1), min(r2, r1)]
        return [min(r2, r1), max(r2, r1)]
    

    def exists(self, cards):
        pass

    # AA          AK suited    AQ suited

    # AK unsuited KK

    # AQ unsuited KQ unsuited


    # rangeChart.exists("AKo")
    # rangeChart.getDict("AKs", combos)


    # rangeChart = {
    #     "A": {"A": 1, "K": 1, "Q": 1, "J": 1, "T": 1, "9": 1, "8": 1, "7": 1, "6": 1, "5": 1, "4": 1, "3": 1, "2": 1},
    #     "K": {"A": 1, "K": 1, "Q": 1, "J": 1, "T": 1, "9": 1, "8": 1, "7": 1, "6": 1, "5": 1, "4": 1, "3": 1, "2": 1},
    #     "Q": {"A": 1, "K": 1, "Q": 1, "J": 1, "T": 1, "9": 1, "8": 1, "7": 1, "6": 1, "5": 1, "4": 1, "3": 1, "2": 1},
    #     "J": {"A": 1, "K": 1, "Q": 1, "J": 1, "T": 1, "9": 1, "8": 1, "7": 1, "6": 1, "5": 1, "4": 1, "3": 1, "2": 1},
    #     "T": {"A": 1, "K": 1, "Q": 1, "J": 1, "T": 1, "9": 1, "8": 1, "7": 1, "6": 1, "5": 1, "4": 1, "3": 1, "2": 1},
    #     "9": {"A": 1, "K": 1, "Q": 1, "J": 1, "T": 1, "9": 1, "8": 1, "7": 1, "6": 1, "5": 1, "4": 1, "3": 1, "2": 1},
    #     "8": {"A": 1, "K": 1, "Q": 1, "J": 1, "T": 1, "9": 1, "8": 1, "7": 1, "6": 1, "5": 1, "4": 1, "3": 1, "2": 1},
    #     "7": {"A": 1, "K": 1, "Q": 1, "J": 1, "T": 1, "9": 1, "8": 1, "7": 1, "6": 1, "5": 1, "4": 1, "3": 1, "2": 1},
    #     "6": {"A": 1, "K": 1, "Q": 1, "J": 1, "T": 1, "9": 1, "8": 1, "7": 1, "6": 1, "5": 1, "4": 1, "3": 1, "2": 1},
    #     "5": {"A": 1, "K": 1, "Q": 1, "J": 1, "T": 1, "9": 1, "8": 1, "7": 1, "6": 1, "5": 1, "4": 1, "3": 1, "2": 1},
    #     "4": {"A": 1, "K": 1, "Q": 1, "J": 1, "T": 1, "9": 1, "8": 1, "7": 1, "6": 1, "5": 1, "4": 1, "3": 1, "2": 1},
    #     "3": {"A": 1, "K": 1, "Q": 1, "J": 1, "T": 1, "9": 1, "8": 1, "7": 1, "6": 1, "5": 1, "4": 1, "3": 1, "2": 1},
    #     "2": {"A": 1, "K": 1, "Q": 1, "J": 1, "T": 1, "9": 1, "8": 1, "7": 1, "6": 1, "5": 1, "4": 1, "3": 1, "2": 1}
    # }

    # dictAces = {"combos": 6, suits: ""}

rc = rangeChart()
print(rc.cardsToIndex("JTs"))

print(rc.cardsToIndex("JTo"))
print(rc.cardsToIndex("88o"))