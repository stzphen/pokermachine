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

runtimes = 3000

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

# preflop

def runPreFlopSim(numPlayers: int, playerList: list):
    # change playerList to list of players, currently list of hole cards
    wins = {}
    deckgoat = Deck()
    # remove hole cards
    for holeCards in playerList:
        for card in holeCards:
            assert(card in deckgoat.deck)
            deckgoat.removeCard(card)
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
    # generate random hands for each player
    player1Hands = []
    player2Hands = []

def runRiverSim(numPlayers: int, playerList: list, board: list):



