from poker import *
from equityCalc import *
from equityAgainstRange import *
from rfi_charts import *

import time

deck = Deck()

def testGenerateHandID():
    generateHandID([six, ten, jack, ten, ace])
    generateHandID([ace2, seven, ace, king, queen])
    generateHandID([queen, king, king, two, three])
    generateHandID([jack, six, nine, five, five])
    generateHandID([ace, king, queen, jack, ten])
    generateHandID([eight, two, eight, eight, two]) 
    generateHandID([nine, nine, eight, eight, eight])
    generateHandID([king, Card(24), Card(37), queen, Card(23)])
    generateHandID([ace, ace, king, king, king])
    generateHandID([five, three, six, three, nine])
    generateHandID([two, six, eight, king, queen])
    generateHandID([ace, three, two, four, five])
    generateHandID([ace2, ace, ace, ace, king])
    generateHandID([queen, jack, jack, jack, jack])
    generateHandID([ten, ten, nine, eight, eight])
    generateHandID([ten, nine, nine, eight, eight])
    generateHandID([ten, ten, nine, nine, eight])

def testGenerateBestHand():
    pass

def testPreflopCalculator():
    print("runtimes: ", runtimes)
    start = time.time()
    actual1 = {0 : (.7345, .0128), 1 : (.2527, .0128)}
    compareRunouts(runPreFlopSim(2, [[Card(12), Card(11)], [Card(13), Card(24)]]), actual1)
    print("preflop runtimes: ", time.time() - start)
    start = time.time()
    
    actual2 = {0 : (.6120, 0.0179), 1: (0.3701, 0.0179)}
    compareRunouts(runPreFlopSim(2, [[Card("8s"), Card("Ts")], [Card("6h"), Card("5h")]]), actual2)
    print("preflop runtimes: ", time.time() - start)
    start = time.time()
    
    actual3 = {0: (.4959, .0041), 1 : (.4999, .0041)}
    compareRunouts(runPreFlopSim(2, [[Card(8), Card(9)], [Card(19), Card(32)]]), actual3)
    print("preflop runtimes: ", time.time() - start)
    start = time.time()
    
    actual4 = {0 : (.6747, .0060), 1 : (.1703, .0060), 2 : (.1490, .0060)}
    compareRunouts(runPreFlopSim(3, [[Card("As"), Card("Ac")], [Card("Ks"), Card("Kc")], [Card("Qs"), Card("Qc")]]), actual4)
    print("preflop runtimes: ", time.time() - start)
    start = time.time()

    actual5 = {0 : (.6721, .0050), 1 : (.1760, .0050), 2 : (.1469, .0050)}
    compareRunouts(runPreFlopSim(3, [[Card("As"), Card("Ac")], [Card("Kh"), Card("Kc")], [Card("Qs"), Card("Qh")]]), actual5)
    print("preflop runtimes: ", time.time() - start)
    start = time.time()

    actual6 = {0 : (.6432, .0078), 1 : (.1224, .0078), 2 : (.2266, .0035)}
    compareRunouts(runPreFlopSim(3, [[Card("As"), Card("Ac")], [Card("Ah"), Card("Kh")], [Card("5s"), Card("6s")]]), actual6)
    print("preflop runtimes: ", time.time() - start)
    start = time.time()

    actual7 = {0 : (.5520, .0077), 1 : (.1352, .0077), 2 : (.1389, .0026), 3 : (.1661, .0026)}
    compareRunouts(runPreFlopSim(4, [[Card("As"), Card("Ac")], [Card("Ah"), Card("Kh")], [Card("5s"), Card("6s")], [Card("7s"), Card("8s")]]), actual7)
    print("preflop runtimes: ", time.time() - start)
    start = time.time()

    actual8 = {0 : (.4536, .0071), 1 : (.1418, .0071), 2 : (.1375, .0022), 3 : (.1097, .0022), 4 : (.1502, .0022)}
    compareRunouts(runPreFlopSim(5, [[Card("As"), Card("Ac")], [Card("Ah"), Card("Kh")], [Card("5s"), Card("6s")], [Card("7s"), Card("8s")], [Card("9s"), Card("Ts")]]), actual8)
    print("preflop runtimes: ", time.time() - start)
    start = time.time()

    actual9 = {0 : (.3774, .0053), 1 : (.1444, .0053), 2 : (.1471, .0021), 3 : (.1064, .0021), 4 : (.1125, .0021), 5 : (.1068, .0021)}
    compareRunouts(runPreFlopSim(6, [[Card("As"), Card("Ac")], [Card("Ah"), Card("Kh")], [Card("5s"), Card("6s")], [Card("7s"), Card("8s")], [Card("9s"), Card("Ts")], [Card("Js"), Card("Qs")]]), actual9)
    print("preflop runtimes: ", time.time() - start)
    start = time.time()

    actual10 = {0 : (.3556, .0045), 1 : (.1344, .0077), 2 : (.1605, .0027), 3 : (.1072, .0027), 4 : (.1148, .0027), 5 : (.0702, .0080), 6 : (.0441, .0112)}
    compareRunouts(runPreFlopSim(7, [[Card("As"), Card("Ac")], [Card("Ah"), Card("Kh")], [Card("5s"), Card("6s")], [Card("7s"), Card("8s")], [Card("9s"), Card("Ts")], [Card("Js"), Card("Qs")], [Card("Ks"), Card("Qc")]]), actual10)
    print("preflop runtimes: ", time.time() - start)
    start = time.time()

    actual11 = {0 : (.3635, .0043), 1 : (.1102, .00491), 2 : (.1799, .0035), 3 : (.1214, .0035), 4 : (.1223, .0035), 5 : (.0654, .0056), 6 : (.0001, .0363), 7 : (.0001, .0363)}
    compareRunouts(runPreFlopSim(8, [[Card("As"), Card("Ac")], [Card("Ah"), Card("Kh")], [Card("5s"), Card("6s")], [Card("7s"), Card("8s")], [Card("9s"), Card("Ts")], [Card("Js"), Card("Qs")], [Card("Ks"), Card("Qc")], [Card("Kc"), Card("Qh")]]), actual11)
    print("preflop runtimes: ", time.time() - start)
    start = time.time()

def testFlopCalculator():
    b = Board()
    b.addCards([Card("4s"), Card("4c"), Card("5s")])
    runFlopSim(2, [[Card("As"), Card("Ks")], [Card("3h"), Card("3d")]], b.board)

def testTurnCalculator():
    b = Board()
    b.addCards([Card("As"), Card("Ah"), Card("2s"), Card("2h")])
    runTurnSim(2, [[Card("Ks"), Card("Kh")], [Card("Qs"), Card("Qh")]], b.board)

def testEquityAgainstRange():
    b = Board()
    b.addCards([Card("Ks"), Card("7h"), Card("9h")])

    


def testAll():
    #testGenerateHandID()
    testGenerateBestHand()
    testPreflopCalculator()
    #testFlopCalculator()

#testAll()

# testAll()