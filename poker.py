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
    def __init__(self, name, stack, position, hero, holeCards = None):
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
    
    def call(self, amount, betSoFar, round):
        self.stack -= (amount - betSoFar)
        self.actions[round].append(("call", amount))
    
    def raises(self, amount, betSoFar, round):
        self.stack -= (amount - betSoFar)
        self.actions[round].append(("raise", amount))
    
    def fold(self, round):
        self.actions[round].append(("fold", 0))


class Table(object):
    def __init__(self):
        self.board = []
        self.pot = 0
        self.deck = Deck()

    def dealFlop(self, deck):
        for i in range(3):
            self.board.add(deck.deal())

    def dealTurn(self, deck):
        self.board.add(deck.deal())

    def dealRiver(self, deck):
        self.board.add(deck.deal())


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


class Game(object):
    def __init__(self, filename, hero):
        self.parseText(filename, hero)

    def parseText(self, filename, hero):
        #read in game log
        with open(filename) as f:
            log = f.readlines()
            log.reverse()
        #get rid of unnecessary lines
        i = 0
        while i < len(log):
            if len(log[i]) <= 6:
                log.remove(log[i]) 
            else:
                log[i] = log[i].strip()
                i += 1
        #print(log)
        # find dealer
        dealExp = regex.compile("dealer: \S+")
        tmpDeal = dealExp.findall(log[0])[0]
        dealer = tmpDeal[8:-1]
        #print(dealer)

        # find names and stacks, rotate so sb -> dealer
        playerExp = regex.compile("#\d+ \S+")
        stackExp = regex.compile("\((\d+(\.\d+)?)\)")

        tmpPlay = playerExp.findall(log[1])
        #print(tmpPlay)
        tmpStack = stackExp.findall(log[1])
        #print(tmpStack)

        names = []
        stacks = []

        for i in range(len(tmpPlay)):
            names.append(tmpPlay[i].split(" ")[1])
            stacks.append(float(tmpStack[i][0]))

        assert(len(stacks) == len(tmpPlay) and len(names) == len(tmpPlay))

        d = names.index(dealer)
        names = names[(d + 1) % len(names):] + names[:(d + 1) % len(names)]
        stacks = stacks[(d + 1) % len(stacks):] + stacks[:(d + 1) % len(stacks)]
        #print(names)
        #print(stacks)

        # read hole cards
        holeCards = []
        if log[2][:13] == "Your hand is ":
            tmpCards = log[2][13:].split(",")
            #print(tmpCards)
            for card in tmpCards:
                card = card.strip()
                rank = card[0]
                suit = SUITSYMBOLS[card[1]]
                holeCards.append(Card(rank+suit))
            log.remove(log[2])
        
        print(log)

        #actually make players
        players = []
        betThisRound = []
        for j in range(len(names)):
            if hero == names[j]:
                players.append(Player(names[j], stacks[j], POSITIONS[j], True, holeCards))
            else:
                players.append(Player(names[j], stacks[j], POSITIONS[j], False))
            betThisRound.append(0)

        table = Table()
        for card in holeCards:
            table.deck.removeCard(card)
        
        assert(table.pot == 0 and table.board == [])

        #get blinds
        sbExp = regex.compile(".+posts a small blind of ")
        bbExp = regex.compile(".+posts a big blind of ")
        
        sb = float(log[2][sbExp.search(log[2]).end():])
        players[0].smallBlind(sb)
        betThisRound[0] += sb
        bb = float(log[3][bbExp.search(log[3]).end():])
        players[1].bigBlind(bb)
        betThisRound[1] += bb
        table.pot += (sb + bb)

        foldExp = regex.compile(" folds")
        betExp = regex.compile(" bets ")
        raiseExp = regex.compile(" raises to ")
        callExp = regex.compile(" calls ")
        checkExp = regex.compile(" checks")
        cardExp = regex.compile("\d+.")
        flopExp = regex.compile("Flop: .+")
        turnExp = regex.compile("Turn: .+")
        riverExp = regex.compile("River: .+")

        betToMatch = bb
        action = 2 % len(players) # add in mod in case heads up, but don't need
        option = players.copy()
        round = "preflop"
        
        #NEED TO ADD BETS TO POT
        for line in log[4:]:
            print("pot", table.pot)
            print("player", players[action].name)
            if foldExp.search(line) != None: #find player name, removes player from player list
                print("fold")
                name = line[:foldExp.search(line).start()]
                tmp = next((x for x in players if x.name == name), None)
                tmp.fold(round)

                betThisRound.remove(betThisRound[action])
                players.remove(tmp)
                option.remove(tmp)
                action = action % len(players)

            elif betExp.search(line) != None:
                print("bet")
                name = line[:betExp.search(line).start()]
                betAmt = float(line[betExp.search(line).end():])
                print(betAmt)
                tmp = next((x for x in players if x.name == name), None)
                tmp.bet(betAmt, round)
                table.pot += betAmt
                
                betThisRound[action] = betAmt
                betToMatch = betAmt
                #everyone else gets option
                option = players.copy()
                option.remove(tmp)
                action = (action + 1) % len(players)

            elif raiseExp.search(line) != None:
                print("raise")
                name = line[:raiseExp.search(line).start()]
                raiseAmt = float(line[raiseExp.search(line).end():])
                print(raiseAmt)
                tmp = next((x for x in players if x.name == name), None)
                tmp.raises(raiseAmt, betThisRound[action], round)
                table.pot += (raiseAmt - betThisRound[action])

                betThisRound[action] = raiseAmt
                betToMatch = raiseAmt
                #everyone else gets option
                option = players.copy()
                option.remove(tmp)
                action = (action + 1) % len(players)

            elif callExp.search(line) != None:
                print("call")
                name = line[:callExp.search(line).start()]
                callAmt = float(line[callExp.search(line).end():])
                tmp = next((x for x in players if x.name == name), None)
                tmp.call(callAmt, betThisRound[action], round)
                table.pot += (callAmt - betThisRound[action])

                betThisRound[action] = callAmt
                option.remove(tmp)
                action = (action + 1) % len(players)

            elif checkExp.search(line) != None:
                print("check")
                name = line[:checkExp.search(line).start()]
                tmp = next((x for x in players if x.name == name), None)
                tmp.check(round)

                #move action
                option.remove(tmp)
                action = (action + 1) % len(players)

            elif flopExp.search(line) != None:
                print("flop")
                round = "flop"
                for tmp in (cardExp.findall(line)):
                    flopCard = Card(tmp)
                    table.board.append(flopCard)
                    table.deck.removeCard(flopCard)

                option = players.copy()
                action = 0
                betThisRound = [0] * len(players)
                betToMatch = 0
                #read the cards, remove from deck, add to board
            elif turnExp.search(line) != None:
                print("turn")
                round = "turn"
                turnCard = Card(cardExp.findall(line)[3])
                table.board.append(turnCard)
                table.deck.removeCard(turnCard)

                option = players.copy()
                action = 0
                betThisRound = [0] * len(players)
                betToMatch = 0
                #read the cards, remove from deck, add to board
            elif riverExp.search(line) != None:
                print("river")
                round = "river"
                riverCard = Card(cardExp.findall(line)[4])
                table.board.append(riverCard)
                table.deck.removeCard(riverCard)

                option = players.copy()
                action = 0
                betThisRound = [0] * len(players)
                betToMatch = 0
                #read the cards, remove from deck, add to board
            else:
                continue

        print("action", players[action].name)
        print("betToMatch", betToMatch)

        for play in players:
            play.debugPrintInfo()


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

Game("log.txt", "sack")

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