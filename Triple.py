def check(my_card):
    card = sorted(my_card[:])
    Tcount = 0
    for i in range(7): # item for else
        for j in range(7):
            if card[i][1] == card[j][1]:
                Tcount += 1
            if Tcount == 3:
                break
        if Tcount == 3:
            return True
        Tcount = 0
    else:
        return False