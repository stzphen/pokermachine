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


print("runtimes: ", runtimes)

actual1 = {0 : (.7345, .0128), 1 : (.2527, .0128)}
compareRunouts(runPreFlopSim(2, [[Card(12), Card(11)], [Card(13), Card(24)]]), actual1)

actual2 = {0 : (.6120, 0.0179), 1: (0.3701, 0.0179)}
compareRunouts(runPreFlopSim(2, [[Card("8s"), Card("Ts")], [Card("6h"), Card("5h")]]), actual2)
 
actual3 = {0: (.4959, .0041), 1 : (.4999, .0041)}
compareRunouts(runPreFlopSim(2, [[Card(8), Card(9)], [Card(19), Card(32)]]), actual3)

actual4 = {0 : (.6747, .0060), 1 : (.1703, .0060), 2 : (.1490, .0060)}
compareRunouts(runPreFlopSim(3, [[Card("As"), Card("Ac")], [Card("Ks"), Card("Kc")], [Card("Qs"), Card("Qc")]]), actual4)

actual5 = {0 : (.6721, .0050), 1 : (.1760, .0050), 2 : (.1469, .0050)}
compareRunouts(runPreFlopSim(3, [[Card("As"), Card("Ac")], [Card("Kh"), Card("Kc")], [Card("Qs"), Card("Qh")]]), actual5)

actual6 = {0 : (.6432, .0078), 1 : (.1224, .0078), 2 : (.2266, .0035)}
compareRunouts(runPreFlopSim(3, [[Card("As"), Card("Ac")], [Card("Ah"), Card("Kh")], [Card("5s"), Card("6s")]]), actual6)

actual7 = {0 : (.5520, .0077), 1 : (.1352, .0077), 2 : (.1389, .0026), 3 : (.1661, .0026)}
compareRunouts(runPreFlopSim(4, [[Card("As"), Card("Ac")], [Card("Ah"), Card("Kh")], [Card("5s"), Card("6s")], [Card("7s"), Card("8s")]]), actual7)

actual8 = {0 : (.4536, .0071), 1 : (.1418, .0071), 2 : (.1375, .0022), 3 : (.1097, .0022), 4 : (.1502, .0022)}
compareRunouts(runPreFlopSim(5, [[Card("As"), Card("Ac")], [Card("Ah"), Card("Kh")], [Card("5s"), Card("6s")], [Card("7s"), Card("8s")], [Card("9s"), Card("Ts")]]), actual8)

actual9 = {0 : (.3774, .0053), 1 : (.1444, .0053), 2 : (.1471, .0021), 3 : (.1064, .0021), 4 : (.1125, .0021), 5 : (.1068, .0021)}
compareRunouts(runPreFlopSim(6, [[Card("As"), Card("Ac")], [Card("Ah"), Card("Kh")], [Card("5s"), Card("6s")], [Card("7s"), Card("8s")], [Card("9s"), Card("Ts")], [Card("Js"), Card("Qs")]]), actual9)

actual10 = {0 : (.3556, .0045), 1 : (.1344, .0077), 2 : (.1605, .0027), 3 : (.1072, .0027), 4 : (.1148, .0027), 5 : (.0702, .0080), 6 : (.0441, .0112)}
compareRunouts(runPreFlopSim(7, [[Card("As"), Card("Ac")], [Card("Ah"), Card("Kh")], [Card("5s"), Card("6s")], [Card("7s"), Card("8s")], [Card("9s"), Card("Ts")], [Card("Js"), Card("Qs")], [Card("Ks"), Card("Qc")]]), actual10)

actual11 = {0 : (.3635, .0043), 1 : (.1102, .00491), 2 : (.1799, .0035), 3 : (.1214, .0035), 4 : (.1223, .0035), 5 : (.0654, .0056), 6 : (.0001, .0363), 7 : (.0001, .0363)}
compareRunouts(runPreFlopSim(8, [[Card("As"), Card("Ac")], [Card("Ah"), Card("Kh")], [Card("5s"), Card("6s")], [Card("7s"), Card("8s")], [Card("9s"), Card("Ts")], [Card("Js"), Card("Qs")], [Card("Ks"), Card("Qc")], [Card("Kc"), Card("Qh")]]), actual11)


# postflop 

def runTurnSim(numPlayers: int, playerList: list, board: list):
    # generate random hands for each player
    player1Hands = []
    player2Hands = []

def runRiverSim(numPlayers: int, playerList: list, board: list):



