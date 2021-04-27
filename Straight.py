def check(my_card):
    card = sorted(my_card[:])
    count = 0
    for i in range(6):
        if card[i][1] + 1 == card[i+1][1]:
            count += 1
    if count >= 4:
        return True
    else:
        return False