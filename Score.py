import Straightplush
import Fourcard
import Fullhouse
import Plush
import Straight
import Triple
import Twopair
import Onepair

def Score(my_card):
    card = sorted(my_card[:])
    if Straightplush.check(card):
        score = 8
    elif Fourcard.check(card):
        score = 7
    elif Fullhouse.check(card):
        score = 6
    elif Plush.check(card):
        score = 5
    elif Straight.check(card):
        score = 4
    elif Triple.check(card):
        score = 3
    elif Twopair.check(card):
        score = 2
    elif Onepair.check(card):
        score = 1
    else:
        score = 0
    return score