from poker import *

def generateStraightFlush(pokerDict, counter):
    for hicard in range(12, 2, -1):
        cardID = 0
        for i in range(5):
            cardID |= RANKS[hicard - i] << (4 * (4 - i))
        handID = suitedID | cardID
        # print(readableHandID(handID))
        pokerDict[handID] = counter
        counter += 1
    return counter

def generateQuads(pokerDict, counter):
    for quadcard in range(12, -1, -1):
        quadID = 0
        for i in range(4):
            quadID |= RANKS[quadcard] << (4 * (4 - i))
        for kicker in range(12, -1, -1):
            if kicker != quadcard:
                handID = quadID | RANKS[kicker]
                # print(readableHandID(handID))
                pokerDict[handID] = counter
                counter += 1
    return counter

def generateFullHouse(pokerDict, counter):
    for tripcard in range(12, -1, -1):
        tripID = 0
        for i in range(3):
            tripID |= RANKS[tripcard] << (4 * (4 - i))
        for paircard in range(12, -1, -1):
            if paircard != tripcard:
                pairID = 0
                for i in range(2):
                    pairID |= RANKS[paircard] << (4 * (1 - i))
                handID = tripID | pairID
                # print(readableHandID(handID))
                pokerDict[handID] = counter
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
                        cardID = 0
                        cardID |= RANKS[firstcard] << 16
                        cardID |= RANKS[secondcard] << 12
                        cardID |= RANKS[thirdcard] << 8
                        cardID |= RANKS[fourthcard] << 4
                        cardID |= RANKS[fifthcard]
                        handID = suitedID | cardID
                        # print(readableHandID(handID))
                        pokerDict[handID] = counter
                        counter += 1
    return counter
    
def generateStraight(pokerDict, counter):
    for hicard in range(12, 2, -1):
        cardID = 0
        for i in range(5):
            cardID |= RANKS[hicard - i] << (4 * (4 - i))
        handID = cardID
        # print(readableHandID(handID))
        pokerDict[handID] = counter
        counter += 1
    return counter

def generateTrips(pokerDict, counter):
    for tripcard in range(12, -1, -1):
        tripID = 0
        for i in range(3):
            tripID |= RANKS[tripcard] << (4 * (4 - i))
        for kicker1 in range(12, -1, -1):
            if kicker1 != tripcard:
                kicker1ID = 0
                kicker1ID |= RANKS[kicker1] << 4
                for kicker2 in range(kicker1 - 1, -1, -1):
                    if kicker2 != tripcard and kicker2 != kicker1:
                        kicker2ID = RANKS[kicker2]
                        handID = tripID | kicker1ID | kicker2ID
                        # print(readableHandID(handID))
                        pokerDict[handID] = counter
                        counter += 1
    return counter

def generateTwoPair(pokerDict, counter):
    for pair1card in range(12, -1, -1):
        pair1ID = 0
        for i in range(2):
            pair1ID |= RANKS[pair1card] << (4 * (4 - i))
        for pair2card in range(pair1card - 1, -1, -1):
            if pair2card != pair1card:
                pair2ID = 0
                for i in range(2):
                    pair2ID |= RANKS[pair2card] << (4 * (2 - i))
                for kicker in range(12, -1, -1):
                    if kicker != pair1card and kicker != pair2card:
                        kickerID = RANKS[kicker]
                        handID = pair1ID | pair2ID | kickerID
                        # print(readableHandID(handID))
                        pokerDict[handID] = counter
                        counter += 1
    return counter

def generatePair(pokerDict, counter):
    for paircard in range(12, -1, -1):
        pairID = 0
        for i in range(2):
            pairID |= RANKS[paircard] << (4 * (4 - i))
        for kicker1 in range(12, -1, -1):
            if kicker1 != paircard:
                kicker1ID = 0
                kicker1ID |= RANKS[kicker1] << 8
                for kicker2 in range(kicker1 - 1, -1, -1):
                    if kicker2 != paircard and kicker2 != kicker1:
                        kicker2ID = RANKS[kicker2] << 4
                        for kicker3 in range(kicker2 - 1, -1, -1):
                            if kicker3 != paircard and kicker3 != kicker2 and kicker3 != kicker1:
                                kicker3ID = RANKS[kicker3]
                                handID = pairID | kicker1ID | kicker2ID | kicker3ID
                                # print(readableHandID(handID))
                                pokerDict[handID] = counter
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
                        cardID = 0
                        cardID |= RANKS[firstcard] << 16
                        cardID |= RANKS[secondcard] << 12
                        cardID |= RANKS[thirdcard] << 8
                        cardID |= RANKS[fourthcard] << 4
                        cardID |= RANKS[fifthcard]
                        handID = cardID
                        # print(readableHandID(handID))
                        pokerDict[handID] = counter
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

