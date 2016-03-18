import random

def deal(deck,hand,personAce,personTotal):
    card = deck.pop(0)
    hand = string_of_hand(hand,string_of_card(card))
    if value_of_card(card[0]) == 11:
        personAce += 1
    personTotal += value_of_card(card[0])
    return (hand,personAce,personTotal)

def string_of_hand(hand,cardString):
    hand = hand + " " + cardString
    return hand

def new_deck():
    deck = []
    for suit in range (1, 5):
        for rank in range (1,14):
            a = [rank,suit]
            deck.append(tuple(a))
    random.shuffle(deck)
    return deck

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

def value_of_card(card):
    if card >= 11:
        return 10
    elif card == 1:
        return 11
    else:
        return card

def suit_of_card(suit):
    if suit == 1:
        return '\u2660'
    elif suit == 2:
        return '\u2662'
    elif suit == 3:
        return '\u2663'
    elif suit == 4:
        return '\u2661'

def report_player(player, playerTotal, playerHand):
    print (player,"'s Hand:",playerHand,sep='')
    print ("Value:",playerTotal)
    
def report_dealer(dealerTotal,dealerHand):
    print ("Dealer's Hand:",dealerHand,sep='')
    print ("Value:",dealerTotal)

def snake_eyes(personTotal):
    if personTotal == 22:
        return 12
    else:
        return personTotal
    
def split_test(player,bet):
    player = "Joel"
    player1 = "First " + player
    player2 = "Second " + player
    player3 = "Third " + player
    player4 = "Fourth " + player

    dealerHand, playerHand = "",""
    playerAce, dealerAce, playerTotal, dealerTotal = 0,0,0,0
    deck = new_deck()
    moneyChange = -bet
    dealer_drew = False
    move = "unknown"
    
    dealerHand,dealerAce,dealerTotal = deal(deck,dealerHand,dealerAce,dealerTotal)
    hiddenDealerHand, hiddenDealerTotal = dealerHand+" []", dealerTotal#deals second dealer card face down
    dealerHand,dealerAce,dealerTotal = deal(deck,dealerHand,dealerAce,dealerTotal)
    
    playerHand,playerAce,playerTotal = deal(deck,playerHand,playerAce,playerTotal)
    firstCard = playerTotal#primes option for splitting
    playerHand,playerAce,playerTotal = playerHand*2,playerAce*2,playerTotal *2

    playerTotal = snake_eyes(playerTotal)#fixes issue when double aces are drawn
    dealerTotal = snake_eyes(dealerTotal)

    report_player(player, playerTotal, playerHand)
    report_dealer(dealerTotal,dealerHand)

split_test("Joel",50)
