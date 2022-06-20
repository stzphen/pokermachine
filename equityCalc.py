from poker import *

# steps
# 1. take in each player's hands, board
# 2. for each player, determine preflop/flop/turn
# 3a. preflop: 150k simulations
    # 3a.1. generate 5 random cards from deck, determine best hand, add win/tie to one of players
    # 3a.2. find equity
# 3b. flop/turn
    # 3b.1. go through every combination of turn/river, determine best hand, add win/tie to one of players
    # 3b.2. find equity

runtimes = 9090

# for testing
def compareRunouts(wins, actual):
    winsAvg = 0.0
    tiesAvg = 0.0
    winsHi = 0.0
    tiesHi = 0.0
    for i in range(len(wins)):
        winsAvg += abs(wins[i][0] - actual[i][0])
        tiesAvg += abs(wins[i][1] - actual[i][1])
        winsHi = max(abs(wins[i][0] - actual[i][0]), winsHi)
        tiesHi = max(abs(wins[i][1] - actual[i][1]), tiesHi)
    winsAvg = winsAvg / len(wins)
    tiesAvg = tiesAvg / len(wins)
    result = f"numHands: {len(wins)}, winsAvg: {round((winsAvg * 100), 2)}%, tiesAvg: {round((tiesAvg * 100), 2)}%, winsHi: {round((winsHi * 100), 2)}%, tiesHi: {round((tiesHi * 100), 2)}%\n"
    print(result)

def beautifyOutput(wins, playerList):
    result = ""
    for key in wins:
        result += f"Player {key} ({playerList[key][0].printID}, {playerList[key][1].printID}): {round((wins[key][0] * 100), 2)}% wins, {round((wins[key][1] * 100), 2)}% ties\n"
    return result[0:-1]

def removeAllCards(deck, playerList, board = []):
    # remove hole cards / board cards
    for holeCards in playerList:
        for card in holeCards:
            assert(card in deck.deck)
            deck.removeCard(card)
    for card in board:
        assert(card in deck.deck)
        deck.removeCard(card)
# preflop

def runPreFlopSim(numPlayers: int, playerList: list):
    wins = {}
    deckgoat = Deck()
    removeAllCards(deckgoat, playerList)
    # change playerList to list of players, currently list of hole cards
    for i in range(numPlayers):
        wins[i] = [0, 0]
    for i in range(runtimes):
        board = []
        prevDeckgoatDeck = deckgoat.deck.copy()
        for bc in range(5):
            board.append(deckgoat.deal())
        minScore = 8000
        minPlayer = []
        for j in range(numPlayers):
            allCards = playerList[j] + board
            # print(allCards)
            score = generateBestHand(allCards)
            if score < minScore:
                minScore = score
                minPlayer = [j]
            elif score == minScore:
                minPlayer.append(j)
        if len(minPlayer) == 1:
            wins[minPlayer[0]] = (wins[minPlayer[0]][0] + 1, wins[minPlayer[0]][1])
        else:
            for i, player in enumerate(minPlayer):
                wins[player] = (wins[player][0], wins[player][1] + 1)
        deckgoat.deck = prevDeckgoatDeck
    for key in wins:
         wins[key] = (wins[key][0] / runtimes, wins[key][1] / runtimes)
    return wins

# postflop 

def runTurnSim(numPlayers: int, playerList: list, board: list):
    wins = {}
    deck = Deck()
    removeAllCards(deck, playerList, board)
    deckList = deck.deck
    for i in range(numPlayers):
        wins[i] = [0, 0]
    for i in range(len(deckList)):
        for j in range(len(deckList)):
            if i != j:
                prevBoard = board.copy()
                board.append(deckList[i])
                board.append(deckList[j])
                minScore = 8000
                minPlayer = []
                for k in range(numPlayers):
                    allCards = playerList[k] + board
                    # print(allCards)
                    score = generateBestHand(allCards)
                    if score < minScore:
                        minScore = score
                        minPlayer = [k]
                    elif score == minScore:
                        minPlayer.append(k)
                if len(minPlayer) == 1:
                    wins[minPlayer[0]] = (wins[minPlayer[0]][0] + 1, wins[minPlayer[0]][1])
                else:
                    for i, player in enumerate(minPlayer):
                        wins[player] = (wins[player][0], wins[player][1] + 1)
                board = prevBoard
    for key in wins:
         wins[key] = (wins[key][0] / len(deckList), wins[key][1] / len(deckList))
    print(beautifyOutput(wins, playerList))
    return wins


def runRiverSim(numPlayers: int, playerList: list, board: list):
    wins = {}
    deck = Deck()
    removeAllCards(deck, playerList, board)
    deckList = deck.deck
    for i in range(numPlayers):
        wins[i] = [0, 0]
    for i in range(len(deckList)):
        prevBoard = board.copy()
        board.append(deckList[i])
        minScore = 8000
        minPlayer = []
        for j in range(numPlayers):
            allCards = playerList[j] + board
            # print(allCards)
            score = generateBestHand(allCards)
            if score < minScore:
                minScore = score
                minPlayer = [j]
            elif score == minScore:
                minPlayer.append(j)
        if len(minPlayer) == 1:
            wins[minPlayer[0]] = (wins[minPlayer[0]][0] + 1, wins[minPlayer[0]][1])
        else:
            for i, player in enumerate(minPlayer):
                wins[player] = (wins[player][0], wins[player][1] + 1)
        board = prevBoard
    for key in wins:
         wins[key] = (wins[key][0] / len(deckList), wins[key][1] / len(deckList))
    print(beautifyOutput(wins, playerList))
    return wins




