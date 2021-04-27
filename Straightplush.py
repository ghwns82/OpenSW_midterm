def check(my_card):
    card = sorted(my_card[:]) # item
    plush = -1
    # item for else
    for i in range(3):
        if card[i][0] == card[i+4][0]:
            plush = i
            break
    else:
        return False
    count = 0
    for i in range(6):
        if card[i][0] == card[plush][0] and card[i][1] + 1 == card[i+1][1]:
            count += 1
    if count >= 4:
        return True
    else:
        return False