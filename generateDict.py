from poker import *
import itertools

def generateStraightFlush(pokerDict, counter):
    for hicard in range(12, 2, -1):
        cards = []
        for i in range(5):
            cards.append(RANKS[hicard - i])
        allCombos = set(itertools.permutations(cards, 5))
        for combo in allCombos:
            cardID = 0
            for x in range(5):
                cardID |= combo[x] << (4 * (4 - x))
            handID = suitedID | cardID
            # print(readableHandID(handID))
            pokerDict[handID] = counter
        counter += 1
    return counter

def generateQuads(pokerDict, counter):
    for quadcard in range(12, -1, -1):
        cards = []
        for i in range(4):
            cards.append(RANKS[quadcard])
        for kicker in range(12, -1, -1):
            if kicker != quadcard:
                cards2 = cards.copy()
                cards2.append(RANKS[kicker])
                allCombos = set(itertools.permutations(cards2, 5))
                for combo in allCombos:
                    cardID = 0
                    for x in range(5):
                        cardID |= combo[x] << (4 * (4 - x))
                    pokerDict[cardID] = counter
                # print(readableHandID(handID))
                counter += 1
    return counter

def generateFullHouse(pokerDict, counter):
    for tripcard in range(12, -1, -1):
        cards = []
        for i in range(3):
            cards.append(RANKS[tripcard])
        for paircard in range(12, -1, -1):
            if paircard != tripcard:
                cards2 = cards.copy()
                for i in range(2):
                    cards2.append(RANKS[paircard])
                allCombos = set(itertools.permutations(cards2, 5))
                for combo in allCombos:
                    cardID = 0
                    for x in range(5):
                        cardID |= combo[x] << (4 * (4 - x))
                    pokerDict[cardID] = counter
                # print(readableHandID(handID))
                counter += 1
    return counter

def generateFlush(pokerDict, counter):
    for firstcard in range(12, -1, -1):
        for secondcard in range(firstcard - 1, -1, -1):
            for thirdcard in range(secondcard - 1, -1, -1):
                for fourthcard in range(thirdcard - 1, -1, -1):
                    for fifthcard in range(fourthcard - 1, -1, -1):
                        if firstcard - 1 == secondcard and secondcard - 1 == thirdcard and thirdcard - 1 == fourthcard and fourthcard - 1 == fifthcard:
                            continue
                        if firstcard == 12 and secondcard == 3 and thirdcard == 2 and fourthcard == 1 and fifthcard == 0:
                            continue
                        cards = [RANKS[firstcard], RANKS[secondcard], RANKS[thirdcard], RANKS[fourthcard], RANKS[fifthcard]]
                        allCombos = set(itertools.permutations(cards, 5))
                        for combo in allCombos:
                            cardID = 0
                            for x in range(5):
                                cardID |= combo[x] << (4 * (4 - x))
                            handID = suitedID | cardID
                            pokerDict[handID] = counter
                        # print(readableHandID(handID))
                        counter += 1
    return counter
    
def generateStraight(pokerDict, counter):
    for hicard in range(12, 2, -1):
        cards = []
        for i in range(5):
            cards.append(RANKS[hicard - i])
        allCombos = set(itertools.permutations(cards, 5))
        for combo in allCombos:
            cardID = 0
            for i in range(5):
                cardID |= combo[i] << (4 * (4 - i))
            handID = cardID
            # print(readableHandID(handID))
            pokerDict[handID] = counter# print(readableHandID(handID))
        counter += 1
    return counter

def generateTrips(pokerDict, counter):
    for tripcard in range(12, -1, -1):
        cards = []
        for i in range(3):
            cards.append(RANKS[tripcard])
        for kicker1 in range(12, -1, -1):
            if kicker1 != tripcard:
                cards2 = cards.copy()
                cards2.append(RANKS[kicker1])
                for kicker2 in range(kicker1 - 1, -1, -1):
                    if kicker2 != tripcard and kicker2 != kicker1:
                        cards3 = cards2.copy()
                        cards3.append(RANKS[kicker2])
                        allCombos = set(itertools.permutations(cards3, 5))
                        for combo in allCombos:
                            cardID = 0
                            for x in range(5):
                                cardID |= combo[x] << (4 * (4 - x))
                            pokerDict[cardID] = counter
                            # print(readableHandID(handID))
                        counter += 1
    return counter

def generateTwoPair(pokerDict, counter):
    for pair1card in range(12, -1, -1):
        cards = []
        for i in range(2):
            cards.append(RANKS[pair1card])
        for pair2card in range(pair1card - 1, -1, -1):
            if pair2card != pair1card:
                cards2 = cards.copy()
                for i in range(2):
                    cards2.append(RANKS[pair2card])
                for kicker in range(12, -1, -1):
                    if kicker != pair1card and kicker != pair2card:
                        cards3 = cards2.copy()
                        cards3.append(RANKS[kicker])
                        allCombos = set(itertools.permutations(cards3, 5))
                        for combo in allCombos:
                            cardID = 0
                            for x in range(5):
                                cardID |= combo[x] << (4 * (4 - x))
                            pokerDict[cardID] = counter
                        counter += 1
    return counter

def generatePair(pokerDict, counter):
    for paircard in range(12, -1, -1):
        cards = []
        for i in range(2):
            cards.append(RANKS[paircard])
        for kicker1 in range(12, -1, -1):
            if kicker1 != paircard:
                cards2 = cards.copy()
                cards2.append(RANKS[kicker1])
                for kicker2 in range(kicker1 - 1, -1, -1):
                    if kicker2 != paircard and kicker2 != kicker1:
                        cards3 = cards2.copy()
                        cards3.append(RANKS[kicker2])
                        for kicker3 in range(kicker2 - 1, -1, -1):
                            if kicker3 != paircard and kicker3 != kicker2 and kicker3 != kicker1:
                                cards4 = cards3.copy()
                                cards4.append(RANKS[kicker3])
                                allCombos = set(itertools.permutations(cards4, 5))
                                for combo in allCombos:
                                    cardID = 0
                                    for x in range(5):
                                        cardID |= combo[x] << (4 * (4 - x))
                                    pokerDict[cardID] = counter
                                    # print(readableHandID(handID))
                                counter += 1
    return counter

def generateHighCard(pokerDict, counter):
    for firstcard in range(12, -1, -1):
        for secondcard in range(firstcard - 1, -1, -1):
            for thirdcard in range(secondcard - 1, -1, -1):
                for fourthcard in range(thirdcard - 1, -1, -1):
                    for fifthcard in range(fourthcard - 1, -1, -1):
                        if firstcard - 1 == secondcard and secondcard - 1 == thirdcard and thirdcard - 1 == fourthcard and fourthcard - 1 == fifthcard:
                            continue
                        if firstcard == 12 and secondcard == 3 and thirdcard == 2 and fourthcard == 1 and fifthcard == 0:
                            continue
                        cards = [RANKS[firstcard], RANKS[secondcard], RANKS[thirdcard], RANKS[fourthcard], RANKS[fifthcard]]
                        allCombos = set(itertools.permutations(cards, 5))
                        for combo in allCombos:
                            cardID = 0
                            for x in range(5):
                                cardID |= combo[x] << (4 * (4 - x))
                            pokerDict[cardID] = counter
                        # print(readableHandID(handID))
                        counter += 1
    return counter

def generateDictionary(pokerDict):
    counter = 0
    counter = generateStraightFlush(pokerDict, counter)
    counter = generateQuads(pokerDict, counter) 
    counter = generateFullHouse(pokerDict, counter) 
    counter = generateFlush(pokerDict, counter)
    counter = generateStraight(pokerDict, counter)
    counter = generateTrips(pokerDict, counter)
    counter = generateTwoPair(pokerDict, counter)
    counter = generatePair(pokerDict, counter)
    counter = generateHighCard(pokerDict, counter)

pokerDict = {} 
generateDictionary(pokerDict)
print(pokerDict)


