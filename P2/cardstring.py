import random
player = "Joel"

#2 Value of Card
#Calls nothing
#Used by #7 Deal
def value_of_card(card):
    if card >= 11:
        return 10
    elif card == 1:
        return 11
    else:
        return card

#3 Suit of Card
#Calls nothing
#Used by #4 Card String 
def suit_of_card(suit):
    if suit == 1:
        return '\u2660'
    elif suit == 2:
        return '\u2662'

    elif suit == 3:
        return '\u2663'

    elif suit == 4:
        return '\u2661'


#4 String of Card
#Calls #3 Suit
#Used by #7 Deal
def string_of_card(card):
    if card[0] == 11:
        rank = "J"
    elif card[0] == 12:
        rank = "Q"
    elif card[0] == 13:
        rank = "K"
    elif card[0] == 1:
        rank = "A"
    else:
        rank = str(card[0])
    suit = suit_of_card(card[1])
    return rank + suit
    
#5 New Deck
#Calls nothing
#Used by #11 Play Hand
def new_deck():
    deck = []
    for suit in range (1, 5):
        for rank in range (1,14):
            a = [rank,suit]
            deck.append(tuple(a))
    random.shuffle(deck)
    return deck

#6 String of Hand
#Calls nothing
#Used by #7 Deal
def string_of_hand(hand,cardString):
    hand = hand + " " + cardString
    return hand
    
#7 Deals one card
#Calls #4 String of Card, #2 Value of Card, #6 String of Hand
#Used by #11 Play Hand
def deal(person,deck,hand):
    card = deck.pop(0)
    hand = string_of_hand(hand,string_of_card(card)) 
    return (value_of_card(card[0]),hand)

#8 Report
#Calls nothing
#Used by #11 Play Hand
def report(player,dealerTotal,playerTotal,dealerHand,playerHand):
    print ("Dealer's Hand:",dealerHand)
    print ("Value:",dealerTotal)
    print (player,"'s Hand: ",playerHand,sep='')
    print ("Value:",playerTotal)



deck = new_deck()

dealer = "Dealer"
dealerHand = ""

playerHand = ""
dealTemp = deal(dealer,deck,dealerHand)
dealerTotal = dealTemp[0]
dealerHand = dealTemp[1]
dealTemp = deal(player,deck,playerHand)
playerTotal = dealTemp[0]
playerHand = dealTemp[1]
dealTemp = deal(player,deck,playerHand)
playerTotal += dealTemp[0]
playerHand = dealTemp[1]
report(player,dealerTotal,playerTotal,dealerHand,playerHand)

