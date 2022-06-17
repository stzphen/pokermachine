from poker import *

deck = Deck()

def testGenerateCombos():
    generateCombos([Card(1), Card(2), Card(3), Card(4), Card(5), Card(8), Card(9)])

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

def testAll():
    testGenerateHandID()

testAll()