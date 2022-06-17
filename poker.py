import random
import itertools
from pokerDict import pokerDict

CARDS = {2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"T", 11:"J", 12:"Q", 13:"K", 14:"A"}
RANKIDS = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
SUITIDS = {"c":0, "d":1, "h":2, "s":3}
SUITS = ("c", "d", "h", "s")
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
        if type(input) == str:
            self.rank = RANKIDS[input[0]]
            self.suit = input[1]
            self.id = self.rank + (13 * SUITIDS[self.suit])
            self.printID = input
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
        self.shuffle()
        
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
    def __init__(self, name, stack):
        self.name = name
        self.stack = stack
        self.holeCards = []
        pass


class Table(object):
    def __init__(self):
        self.board = []

    def dealFlop(self, deck):
        for i in range(3):
            self.board.add(deck.deal())

    def dealTurn(self, deck):
        self.board.add(deck.deal())

    def dealRiver(self, deck):
        self.board.add(deck.deal())


class Hand(object): #should change hand so it takes in a list, generates best hand
    def __init__(self, player: Player, table: Table):
        self.choices = player.holeCards + table.board

    #only generate with 5 cards

    def compareHands(self, other):
        pass


class Game(object):
    def __init__(self, sb, bb):
        self.players = []
        self.smallBlind = sb
        self.bigBlind = bb
        pass

    def startHand(self):
        self.deck = Deck().shuffle()

    def rotateButton(self):
        newDealer = self.players.pop(0)
        self.players.append(newDealer)

    def dealHands(self, deck):
        for i in range(2):
            for player in self.players:
                pass
                # player.holeCards.append(deck.)

    def restartHand(self):
        pass

def generateHandID(hand: list) -> int:
    # sort hand by rank greatest to least
    hand.sort(key=lambda x: x.rank, reverse=True)

    # wheel straight
    if hand[0].rank == 14 and hand[1].rank == 5 and hand[2].rank == 4 and hand[3].rank == 3 and hand[4].rank == 2:
        hand = [hand[1], hand[2], hand[3], hand[4], hand[0]]

    # quads
    # A A A A 2
    if (hand[0].rank == hand[1].rank and hand[1].rank == hand[2].rank and hand[2].rank == hand[3].rank):
        pass
    # K 9 9 9 9
    elif (hand[1].rank == hand[2].rank and hand[2].rank == hand[3].rank and hand[3].rank == hand[4].rank):
        hand = [hand[1], hand[2], hand[3], hand[4], hand[0]]

    # full house
    # 8 8 8 2 2
    elif (hand[0].rank == hand[1].rank and hand[1].rank == hand[2].rank and hand[3].rank == hand[4].rank):
        pass
    # 2 2 2 8 8
    elif (hand[0].rank == hand[1].rank and hand[2].rank == hand[3].rank and hand[3].rank == hand[4].rank):
        hand = [hand[2], hand[3], hand[4], hand[0], hand[1]]

    # trips
    # 9 9 9 3 2
    elif (hand[0].rank == hand[1].rank and hand[1].rank == hand[2].rank):
        pass
    # 10 9 9 9 3
    elif (hand[1].rank == hand[2].rank and hand[2].rank == hand[3].rank):
        hand = [hand[1], hand[2], hand[3], hand[0], hand[4]]
    # J 10 9 9 9
    elif (hand[2].rank == hand[3].rank and hand[3].rank == hand[4].rank):
        hand = [hand[2], hand[3], hand[4], hand[0], hand[1]]

    # two pair
    # A A K K 10
    elif (hand[0].rank == hand[1].rank and hand[2].rank == hand[3].rank):
        pass
    # A A 10 9 9
    elif (hand[0].rank == hand[1].rank and hand[3].rank == hand[4].rank):
        hand = [hand[0], hand[1], hand[3], hand[4], hand[2]]
    # A K K 9 9
    elif (hand[1].rank == hand[2].rank and hand[3].rank == hand[4].rank):
        hand = [hand[1], hand[2], hand[3], hand[4], hand[0]]

    # one pair
    # 10 10 8 6 5
    elif (hand[0].rank == hand[1].rank):
        pass
    # J 10 10 8 6
    elif (hand[1].rank == hand[2].rank):
        hand = [hand[1], hand[2], hand[0], hand[3], hand[4]]
    # Q J 10 10 8
    elif (hand[2].rank == hand[3].rank):
        hand = [hand[2], hand[3], hand[0], hand[1], hand[4]]
    # K Q J 10 10
    elif (hand[3].rank == hand[4].rank):
        hand = [hand[3], hand[4], hand[0], hand[1], hand[2]]

    # generate hand ID
    handID = 0
    for i in range(5):
        handID |= (hand[i].rank << (4 * (4 - i)))
    if hand[0].suit == hand[1].suit and hand[1].suit == hand[2].suit and hand[2].suit == hand[3].suit and hand[3].suit == hand[4].suit:
        handID |= suitedID

    # print(readableHandID(handID))
    return handID

def generateBestHand(cards: list) -> int:
    allCombos = list(itertools.combinations(cards, 5))
    minValue = 1000000000
    for hand in allCombos:
        generatedValue = generateHandID(list(hand))
        if pokerDict[generatedValue] < minValue:
            minValue = pokerDict[generatedValue]
    return minValue



