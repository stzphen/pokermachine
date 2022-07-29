from equityCalc import *
from rangeCharts import *
from rfi_charts import *


# def printInfoEquities(equities):
#     print(f"median: {}")

def equityAgainstRange(hand, rc, board = Board()):
    round = "preflop"
    if len(board.board) == 3:
        round = "flop"
    elif len(board.board) == 4:
        round = "turn"
        
    equities = []
    for i in range(len(rc.chart)):
        for j in range(len(rc.chart)):
            if rc.exists((i, j)):
                combos = rc.combos((i, j))
                for c in combos:
                    oppCards = suitedStringToCards(c)
                    if oppCards[0] not in hand and oppCards[1] not in hand and oppCards[0] not in board.board and oppCards[1] not in board.board:
                        # print(f"hand 7s8s vs opponent {c}", end = " ")
                        if round == "preflop":
                            equities.append((c, runPreFlopSim(2, [hand, oppCards])))
                            print(f"7s8s wins against {c}: {equities[-1][1][0][0] * 100.0}%")
                            print(f"7s8s ties against {c}: {equities[-1][1][0][1] * 100.0}%")
                            print(f"7s8s loses against {c}: {equities[-1][1][1][0] * 100.0}%")
                            print()
                            break
                        elif round == "flop":
                            equities.append((c, runFlopSim(2, [hand, oppCards], board.board)))
                            print(f"7s8s wins against {c}: {equities[-1][1][0][0] * 100.0}%")
                            print(f"7s8s ties against {c}: {equities[-1][1][0][1] * 100.0}%")
                            print(f"7s8s loses against {c}: {equities[-1][1][1][0] * 100.0}%")
                            print()
                        elif round == "turn":
                            equities.append((c, runTurnSim(2, [hand, oppCards], board.board)))
                            print(f"7s8s wins against {c}: {equities[-1][1][0][0] * 100.0}%")
                            print(f"7s8s ties against {c}: {equities[-1][1][0][1] * 100.0}%")
                            print(f"7s8s loses against {c}: {equities[-1][1][1][0] * 100.0}%")
                            print()
    
    return equities

h = [Card("7s"), Card("8s")]
utgChart = RangeChart()
utgChart.editChart(utg)

b = Board()
# b.addCards([Card("6s"), Card("Ks"), Card("Qc"), Card("Ah")])
# 3 board cards, 2 hole cards for hero ->
    # remove 5 cards from rc
    # card x:
        # 13 + 12 = 25 sets * 7 
        # { Kh6s, Kc6c, .. .. , }
        # [Kh][6s] = 0 

equityAgainstRange(h, utgChart,utgChart,utgChart,utgChart,utgChart,utgChart,utgChart, b)
# equityAgainstRange(h, utgChart, b)
# equityAgainstRange(h, utgChart, b)
# equityAgainstRange(h, utgChart, b)
# equityAgainstRange(h, utgChart, b)
# equityAgainstRange(h, utgChart, b)
# equityAgainstRange(h, utgChart, b)

