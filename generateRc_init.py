# ace to 2
ranks = [14,13,12,11,10,9,8,7,6,5,4,3,2]
output = {2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"T", 11:"J", 12:"Q", 13:"K", 14:"A"}
# suits
suits = ["c", "d", "h", "s"]

# print("rc = [  ", end = "")
for i, rank1 in enumerate(ranks):
    print("        [   ", end = "")
    for j in range(13):
        if j != 0:
            print("            ", end = "")
        combos = [0, set()]
        rank2 = ranks[j]
        if rank1 > rank2:
            # suited
            for suit1 in suits:
                suit2 = suit1
                card = output[rank1] + suit1 + output[rank2] + suit2
                combos[0] += 1
                combos[1].add(card)
            assert(combos[0] == 4)
            # print(output[rank1] + output[rank2] + "s", combos)
        elif rank1 < rank2:
            # offsuit
            for suit1 in suits:
                for suit2 in suits:
                    if suit2 == suit1:
                        continue
                    card = output[rank2] + suit1 + output[rank1] + suit2
                    combos[0] += 1
                    combos[1].add(card)
            assert(combos[0] == 12)
            # print(output[rank2] + output[rank1] + "o", combos)
        else:
            #pocket pair
            for x, suit1 in enumerate(suits):
                for y in range(x + 1, 4):
                    suit2 = suits[y]
                    card = output[rank2] + suit1 + output[rank1] + suit2
                    combos[0] += 1
                    combos[1].add(card)
            assert(combos[0] == 6)
            # print(output[rank1] + output[rank2], combos)
        print("[1, ", end = "")
        print(combos, end = "")
        print("]", end = "")
        if j == 12:
            print("]", end = "")
        print(", ")