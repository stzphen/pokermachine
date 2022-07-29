from poker import *
from equityCalc import *


player2 = [Card("5s"), Card("6s")]
player1 = [Card("Kh"), Card("Qh")]

deckgoatbigtongkaT = Deck().deck

for p1c1 in deckgoatbigtongkaT:
    for p1c2 in deckgoatbigtongkaT:
        if p1c1 != p1c2:
            for p2c1 in deckgoatbigtongkaT:
                if p2c1 != p1c1 and p2c1 != p1c2:
                    for p2c2 in deckgoatbigtongkaT:
                        if p2c2 != p1c1 and p2c2 != p1c2 and p2c2 != p2c1:
                            playerList = [[p1c1, p1c2], [p2c1, p2c2]]
                            printHVHDict(runPreFlopSim(2, playerList), playerList)
        
