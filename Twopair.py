def check(my_card):
    card = sorted(my_card[:])
    count = 0
    Dcount = 0
    
    for i in range(7):
        for j in range(7):
            if card[i][1] == card[j][1]:
                count +=1
        if count >= 2:
            Dcount += 1
        count = 0
    if Dcount / 2 > 1:
        return True
    else:
        return False