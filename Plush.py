def check(my_card):
    card = sorted(my_card[:])
    for i in range(3):
        if card[i][0] == card[i+4][0]:
            plush = i
            break
    else:
        return False
    return True