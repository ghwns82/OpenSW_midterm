def check(my_card):
    card = sorted(my_card[:]) # item
    Fcount = 0
    for i in range(7): # item for else
        for j in range(7):
            if card[i][1] == card[j][1]:
                Fcount += 1
            if Fcount == 4:
                break
        if Fcount == 4:
            return True
        
        Fcount = 0
    
    else:
        return False