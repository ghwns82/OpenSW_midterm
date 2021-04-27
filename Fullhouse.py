def check(my_card):
    card = sorted(my_card[:])
    count = 0
    Tcount = 0
    Dcount = 0
    
    for i in range(7):
        for j in range(7):
            if card[i][1] == card[j][1]:
                count +=1
        if count == 3:
            Tcount += 1
        if count ==2:
            Dcount += 1
        count = 0
    if Tcount /3 == 2:
        return True
    elif Tcount / 3 and Dcount / 2 > 0:
        return True
    else:
        return False