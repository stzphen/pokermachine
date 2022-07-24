from poker import *
from rc_init import rc as rc
from rfi_charts import *
import string

RANKINDS = {"2":12, "3":11, "4":10, "5":9, "6":8, "7":7, "8":6, "9":5, "T":4, "J":3, "Q":2, "K":1, "A":0}
SUITED = {"o":0, "s":1}

"""

RangeChart documentation:
rc = rangeChart()
rc.chart[x][y] = [exists, combos]
    exists = 1 or 0
    combos = [number of combos, {set of combos}]
rc.exists() fetches exists
    can check whether a given hand is in the range
    1) generic hand (i.e., AAo, KQs, 56o)
    2) specific hand (i.e., KhQh, 5s6d)


"""

# cardsToString(Card("Kh"), Card("Qh")) = "KQs"
def cardsToString(c1 : Card, c2 : Card) -> string:
    result = CARDS[c1.rank] + CARDS[c2.rank]
    if c1.suit == c2.suit:
        result += "s"
    else: 
        result += "o"
    return result

# cardToSuitedString(Card("Kh"), Card("Qh")) = "KhQh"
def cardsToSuitedString(c1 : Card, c2 : Card) -> string:
    result = CARDS[c1.rank] + c1.suit + CARDS[c2.rank] + c2.suit
    return result

# stringToIndex("KQs") = [1, 2]
def stringToIndex(cards: string) -> list: #make pairs not need o or s
    r1 = RANKINDS[cards[0]]
    r2 = RANKINDS[cards[1]]
    if SUITED[cards[2].lower()]:
        return [min(r2, r1), max(r2, r1)]
    return [max(r2, r1), min(r2, r1)]

class RangeChart(object):

    def __init__(self) -> None:
        self.chart = rc
        pass
    
    # printCell("KQs")
    def printCell(self, cards):
        index = stringToIndex(cards)
        print(self.chart[index[0]][index[1]])

    def dbg_removeCombo(self):
        self.printCell("KQs")
        self.removeCombo([Card("Kh"), Card("Qh")], True)
        self.printCell("KQs")
        self.removeCombo([Card("Kc"), Card("Qc")], True)
        self.printCell("KQs")
        self.removeCombo([Card("Ks"), Card("Qs")], True)
        self.printCell("KQs")
        self.removeCombo([Card("Ks"), Card("Qs")], True)
        self.printCell("KQs")
        self.removeCombo([Card("Kd"), Card("Qd")], True)
        self.printCell("KQs")
        self.removeCombo("KQs")
        self.printCell("KQs")

        self.printCell("56o")
        self.removeCombo("56o")
        self.printCell("56o")
    
    # merge into self? other? new?
    def mergeCharts(self, other):
        pass

    # Index: 0
    # Use cases:
        # 1) rc.exists( "KQs" ) checks if KQs is in the range
        # 2) rc.exists( [Card("Kh"), Card("Qh")] , True ) checks if KQ of hearts is in the range
    def exists(self, cards, cardParam = False) -> int:
        if cardParam:
            # assert(type of cards == list of 2 cards)
            cardstring = cardsToString(cards[0], cards[1])
            index = stringToIndex(cardstring)
            if not self.chart[index[0]][index[1]][0]:
                return 0
            suitedCards = cardsToSuitedString(cards[0], cards[1])
            return int(suitedCards in self.chart[index[0]][index[1]][1])
        # else assert(type of cards == string)
        index = stringToIndex(cards)
        return self.chart[index[0]][index[1]][0]

    # updates combos (1). Also updates exists (0) if necesabgeary
    # Use cases:
        # 1) rc.removeCombo( "KQs" ) removes all KQs from range
        # 2) rc.removeCombo( [Card("Kh"), Card("Qh")], True ) removes KhQh from range
    def removeCombo(self, cards, cardParam = False):
        if cardParam:
            # assert(type of cards == list of 2 cards)
            cardstring = cardsToString(cards[0], cards[1])
            index = stringToIndex(cardstring)
            if not self.chart[index[0]][index[1]][0]:
                return
            suitedCards = cardsToSuitedString(cards[0], cards[1])
            if suitedCards in self.chart[index[0]][index[1]][1][1]:
                self.chart[index[0]][index[1]][1][1].remove(suitedCards)
                # decrement combos size by 1
                self.chart[index[0]][index[1]][1][0] -= 1
                if self.chart[index[0]][index[1]][1][0] == 0:
                    # no combos left, set exists to 0
                    self.chart[index[0]][index[1]][0] = 0
        else:
            # assert(type of cards == string)
            index = stringToIndex(cards)
            self.chart[index[0]][index[1]][0] = 0
            # no combos remaining
            self.chart[index[0]][index[1]][1] = [0, set()]
        return
    
    # Index: 1
    # returns a set
    def combos(self, cards, cardParam = False):
        if cardParam:
            # assert(type of cards == list of 2 cards)
            cards = cardsToString(cards[0], cards[1])
        # else assert(type of cards == string)
        index = stringToIndex(cards)
        return self.chart[index[0]][index[1]][1][1]

range_chart = RangeChart()
# range_chart.dbg_removeCombo()