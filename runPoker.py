from poker import *
from rangeCharts import *
from runPreflop import *
from runFlop import *
from runTurn import *
from runRiver import *

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
                players.append(Player(names[j], stacks[j], POSITIONS[j], None, True, holeCards))
            else:
                players.append(Player(names[j], stacks[j], POSITIONS[j], RangeChart(), False))
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
        currAction = None

        foldExp = regex.compile(" folds")
        betExp = regex.compile(" bets ")
        raiseExp = regex.compile(" raises to ")
        callExp = regex.compile(" calls ")
        checkExp = regex.compile(" checks")
        allInExp = regex.compile(" goes all in") #lmao copilot suggested this

        actionExps = [foldExp, betExp, raiseExp, callExp, checkExp, allInExp]

        cardExp = regex.compile("\d+.")
        flopExp = regex.compile("Flop: .+")
        turnExp = regex.compile("Turn: .+")
        riverExp = regex.compile("River: .+")

        betToMatch = bb
        action = 2 % len(players) # add in mod in case heads up, but don't need
        option = players.copy()

        line, line2, line3 = None, None, None

        # update: players, option, table

        line = runPreflopAction(log, 4, action, players, table, betThisRound, betToMatch, None, option, actionExps, flopExp)

        if line != None:
            line2 = runFlopAction(log, line, 0, players, table, [0] * len(players), 0, None, players.copy(), actionExps, flopExp, turnExp, cardExp)

        if line2 != None:
            line3 = runTurnAction(log, line2, 0, players, table, [0] * len(players), 0, None, players.copy(), actionExps, turnExp, riverExp, cardExp)

        if line3 != None:
            runRiverAction(log, line3, 0, players, table, [0] * len(players), 0, None, players.copy(), actionExps, riverExp, cardExp)

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