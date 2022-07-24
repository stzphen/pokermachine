from poker import *

def runTurnAction(log, start, action, players, table, betThisRound, betToMatch, currAction, option, actionExps, turnExp, riverExp, cardExp):
    for i in range(start, len(log)):
        line = log[i]

        if turnExp.search(line) != None:
            print("turn")
            round = "turn"
            currAction = None
            turnCard = Card(cardExp.findall(line)[3])
            table.board.append(turnCard)
            table.deck.removeCard(turnCard)

            option = players.copy()
            action = 0
            betThisRound = [0] * len(players)
            betToMatch = 0
            #read the cards, remove from deck, add to board

        elif actionExps[0].search(line) != None: #fold
            print("fold")
            name = line[:actionExps[0].search(line).start()]
            p = next((x for x in players if x.name == name), None)
            p.fold(round)

            betThisRound.remove(betThisRound[action])
            players.remove(p)
            option.remove(p)
            action = action % len(players)

        elif actionExps[1].search(line) != None: #bet
            print("bet")
            name = line[:actionExps[1].search(line).start()]
            betAmt = float(line[actionExps[1].search(line).end():])
            print(betAmt)
            p = next((x for x in players if x.name == name), None)
            p.bet(betAmt, round)
            table.pot += betAmt
            
            betThisRound[action] = betAmt
            betToMatch = betAmt
            #everyone else gets option
            option = players.copy()
            option.remove(p)
            action = (action + 1) % len(players)

        elif actionExps[2].search(line) != None: # raise

            if currAction == None:
                currAction = "raise"
            elif currAction == "raise":
                currAction = "3bet"
            elif currAction == "3bet":
                currAction = "4bet+"
            
            print(currAction)

            name = line[:actionExps[2].search(line).start()]
            raiseAmt = float(line[actionExps[2].search(line).end():])
            print(raiseAmt)
            p = next((x for x in players if x.name == name), None)
            p.raises(currAction, raiseAmt, betThisRound[action], round)
            table.pot += (raiseAmt - betThisRound[action])

            betThisRound[action] = raiseAmt
            betToMatch = raiseAmt
            #everyone else gets option
            option = players.copy()
            option.remove(p)
            action = (action + 1) % len(players)

        elif actionExps[3].search(line) != None: #call

            tmpAction = None
            if currAction == None:
                tmpAction = "call"
            elif currAction == "raise":
                tmpAction = "call raise"
            elif currAction == "3bet":
                tmpAction = " call 3bet"
            elif currAction == "4bet+":
                tmpAction = "call 4bet+"
            
            print(tmpAction)

            name = line[:actionExps[3].search(line).start()]
            callAmt = float(line[actionExps[3].search(line).end():])
            p = next((x for x in players if x.name == name), None)
            p.call(tmpAction, callAmt, betThisRound[action], round)
            table.pot += (callAmt - betThisRound[action])

            betThisRound[action] = callAmt
            option.remove(p)
            action = (action + 1) % len(players)

        elif actionExps[4].search(line) != None: #check
            print("check")
            name = line[:actionExps[4].search(line).start()]
            p = next((x for x in players if x.name == name), None)
            p.check(round)

            #move action
            option.remove(p)
            action = (action + 1) % len(players)

        elif riverExp.search(line) != None:
            return i

def updateRange(action, player):
    # if action == xx
        # setPreflop(position, player,)
    # elif
    pass