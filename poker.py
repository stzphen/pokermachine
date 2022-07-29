import random
import itertools
import regex
from pokerDict import pokerDict

CARDS = {2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"T", 11:"J", 12:"Q", 13:"K", 14:"A"}
RANKIDS = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
SUITIDS = {"c":0, "d":1, "h":2, "s":3}
SUITS = ("c", "d", "h", "s")
SUITSYMBOLS = {"♣": "c", "♦": "d", "♥": "h", "♠": "s"}
POSITIONS = ("SB", "BB", "UTG", "UTG1", "LJ", "HJ", "CO", "D")
suitedID = 1 << 20

# takes handID and converts it to readable format
def readableHandID(handID: int):
    result = ""
    if handID & suitedID:
        result += "suited "
    else:
        result += "not suited "
    mask = 0xF
    for i in range(5):
        currMask = mask << (4 * (4 - i))
        currCard = handID & currMask
        currCard >>= 4 * (4 - i)
        result += CARDS[currCard] + " "
    return result

class Card(object):
    def __init__(self, input):
        #error handling: cards that don't exist
        if type(input) == str:
            if len(input) > 2: #10 case
                input = "T" + input[-1]
            self.rank = RANKIDS[input[0]]
            if input[-1].isalpha():
                self.suit = input[-1]
                self.printID = input
            else:
                self.suit = SUITSYMBOLS[input[-1]]
                self.printID = input[:-1] + self.suit
            self.id = self.rank + (13 * SUITIDS[self.suit])
        else:
            self.id = input
            self.suit = SUITS[input // 13]
            self.rank = RANKS[input % 13]
            self.printID = CARDS[self.rank] + self.suit

    def __eq__(self, other): 
        if not isinstance(other, Card):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.rank == other.rank and self.suit == other.suit
    
    def __repr__(self):
        return f"{self.printID}"

    def rank(self):
        return self.rank

    def suit(self):
        return self.suit

    def compareRank(self, other) -> int:
        if self.rank() < other.rank():
            return -1
        if self.rank() > other.rank():
            return 1
        return 0

class Deck(object):
    def __init__(self):
        self.reset()
        # self.shuffle()
        
    def reset(self):
        self.deck = []
        for i in range(52):
            self.deck.append(Card(i))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if len(self.deck) == 0:
            print("deck empty")
            pass
        else:
            return self.deck.pop(random.randrange(len(self.deck)))
    
    def removeCard(self, card):
        self.deck.remove(card)
    

class Player(object):

    def __init__(self, name, stack, position, rc, hero, holeCards = None):
        self.name = name
        self.position = position
        self.stack = stack
        self.hero = hero
        if hero:
            self.holeCards = holeCards
        self.actions = {}
        self.actions["preflop"] = []
        self.actions["flop"] = []
        self.actions["turn"] = []
        self.actions["river"] = []
        self.rc = rc    
    #write methods that edit range chart

    def debugPrintInfo(self):
        print(f"player: {self.name}\n")
        print(f"stack: {self.stack}\n")
        print(f"position: {self.position}\n")
        if self.hero:
            print(f"holeCards: {self.holeCards}\n")
        print(f"actions: {self.actions}\n")
    
    def smallBlind(self, amount):
        self.stack -= amount
        self.actions["preflop"].append(("small blind", amount))
    
    def bigBlind(self, amount):
        self.stack -= amount
        self.actions["preflop"].append(("big blind", amount))
    
    def check(self, round):
        self.actions[round].append(("check", 0))
    
    def bet(self, amount, round):
        self.stack -= amount
        self.actions[round].append(("bet", amount))
    
    def call(self, type, amount, betSoFar, round):
        self.stack -= (amount - betSoFar)
        self.actions[round].append((type, amount))
    
    def raises(self, type, amount, betSoFar, round):
        self.stack -= (amount - betSoFar)
        self.actions[round].append((type, amount))
    
    def fold(self, round):
        self.actions[round].append(("fold", 0))

class Board(object):
    def __init__(self):
        self.board = []
    
    def addCards(self, cards: list):
        for c in cards:
            self.board.append(c)

class Table(object):
    def __init__(self):
        self.board = Board()
        self.pot = 0
        self.deck = Deck()

class Hand(object): #should change hand so it takes in a list, generates best hand
    def __init__(self, holecards: list, table: Table):
        self.choices = holecards + table.board
        self.bestHand = self.generateBestHand()
        self.handID = self.generateHandID(self.bestHand)

    def generateHandID(self, hand : list) -> int:
        # generate hand ID
        handID = 0
        for i in range(5):
            handID |= (hand[i].rank << (4 * (4 - i)))
        if hand[0].suit == hand[1].suit and hand[1].suit == hand[2].suit and hand[2].suit == hand[3].suit and hand[3].suit == hand[4].suit:
            handID |= suitedID
        # print(readableHandID(handID))
        return handID

    def generateBestHand(self) -> int:
        cards = self.choices
        allCombos = list(itertools.combinations(cards, 5))
        minValue = 1000000000
        for hand in allCombos:
            generatedValue = self.generateHandID(hand)
            if pokerDict[generatedValue] < minValue:
                minValue = pokerDict[generatedValue]
        return minValue

    def compareHands(self, other):
        pass

# will be deleted, for testing purposes

def generateHandID(hand : list) -> int:
        # generate hand ID
        handID = 0
        for i in range(5):
            handID |= (hand[i].rank << (4 * (4 - i)))
        if hand[0].suit == hand[1].suit and hand[1].suit == hand[2].suit and hand[2].suit == hand[3].suit and hand[3].suit == hand[4].suit:
            handID |= suitedID
        # print(readableHandID(handID))
        return handID

def generateBestHand(hand) -> int:
    allCombos = list(itertools.combinations(hand, 5))
    minValue = 1000000000
    for tmp in allCombos:
        generatedValue = generateHandID(tmp)
        if pokerDict[generatedValue] < minValue:
            minValue = pokerDict[generatedValue]
    return minValue