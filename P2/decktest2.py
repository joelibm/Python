import random
##def new_deck():
##    deck = []
##    for suit in range (1, 5):
##        for rank in range (1,14):
##            deck.append(rank)
##    random.shuffle(deck)
##    return deck
##print (new_deck())

##def suit_of_card(suit):
##    if suit == 1:
##        return '\u2660'
##    elif suit == 2:
##        return '\u2662'
##    elif suit == 3:
##        return '\u2663'
##    elif suit == 4:
##        return '\u2661'
##print (suit_of_card(4))

def new_deck():
    deck = []
    for suit in range (1, 5):
        for rank in range (1,14):
            a = [rank,suit]
            deck.append(tuple(a))
    random.shuffle(deck)
    return deck
def deal(person,deck):
    card = deck.pop(0)
    print (person," was dealt ",string_of_card(card[0]),suit_of_card(card[1]),".",sep='')
    return (value_of_card(card[0]))
print(deal("Steve",new_deck()))
