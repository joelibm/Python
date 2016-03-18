import random
#1 Main Function
#Calls #10 Restore, #12 Bet, #11 Play, #9 Save
#Used by nothing
def main():
    try:
        player, money = restore()
        print("Resume saved game '", player,"'? (y/n)",sep='')
        load = input()
        if load.lower()[0] != "y":
            player = input("What is your name? ")
            money = 1000
    except FileNotFoundError:
        player = input("What is your name? ")
        money = 1000
    dealer = "Dealer"
    print (player," has $",money,sep ='')
    bet = 25
    bet = input_bet(bet, money)
    while bet > 0:
        money += play_hand(player,bet)
        print (player," has $",money,sep ='')
        if money > 0:
            bet = input_bet(bet, money)
        else:
            print ("You're out of money! Game over.")
            break
    saveGame = input ("Would you like to save this game? (y/n) ")
    if saveGame.lower()[0] == "y":
        save(player, str(money))

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
def deal(deck,hand,personAce,personTotal):
    card = deck.pop(0)
    hand = string_of_hand(hand,string_of_card(card))
    if value_of_card(card[0]) == 11:
        personAce += 1
    personTotal += value_of_card(card[0])
    return (hand,personAce,personTotal)

#8 Report
#Calls nothing
#Used by #11 Play Hand
def report(player,dealerTotal,playerTotal,dealerHand,playerHand):
    print ("Dealer's Hand:",dealerHand,sep='')
    print ("Value:",dealerTotal)
    print (player,"'s Hand:",playerHand,sep='')
    print ("Value:",playerTotal)

#9 Save
#Calls nothing
#Used by #1 Main
def save(name, money):
    file = open('blackjack.save','w')
    file.write(name + '\n' + money)
    file.close()

#10 load function
#Calls nothing
#Used by #1 Main
def restore():
    file = open('blackjack.save','r')
    name = file.readline().rstrip('\n')
    money = file.readline()
    return name, int(money)
    file.close()

#11 A full hand of play
#Calls #5 New Deck, #7 Deal, #8 Report, #13 Ace
#Used in #1 Main
def play_hand(player,bet):
    dealer = "Dealer"
    dealerHand, playerHand = "",""
    playerAce, dealerAce, playerTotal, dealerTotal = 0,0,0,0
    deck = new_deck()
    moneyChange = -bet
    
    dealerHand,dealerAce,dealerTotal = deal(deck,dealerHand,dealerAce,dealerTotal)
    
    playerHand,playerAce,playerTotal = deal(deck,playerHand,playerAce,playerTotal)  
    playerHand,playerAce,playerTotal = deal(deck,playerHand,playerAce,playerTotal) 
    
    report(player,dealerTotal,playerTotal,dealerHand,playerHand)
    
    move = input("Move? (hit/stay)")
    while True:
        if move.lower()[0] == ("h") or move.lower()[0] == ("s"):
            while move.lower()[0] == "h":
                playerHand,playerAce,playerTotal = deal(deck,playerHand,playerAce,playerTotal)
                if (playerTotal > 21) and (playerAce > 0):
                    playerAce -= 1
                    playerTotal -= 10
                report(player,dealerTotal,playerTotal,dealerHand,playerHand)
                if playerTotal > 21:
                    print ("Bust!")
                    break
                move = input("Move? (hit/stay)")
            while move.lower()[0] == "s":
                while dealerTotal < 17:
                    dealerHand,dealerAce,dealerTotal = deal(deck,dealerHand,dealerAce,dealerTotal)
                    if (dealerTotal > 21) and (dealerAce > 0):
                        dealerAce -=1
                        dealerTotal -=10
                    report(player,dealerTotal,playerTotal,dealerHand,playerHand)
                while dealerTotal > 21:
                    print ("Dealer busts! You win!")
                    moneyChange = bet
                    break
                while 17 <= dealerTotal <=21:
                    if dealerTotal > playerTotal:
                        print ("Dealer stays. You lose.")
                        break
                    elif dealerTotal < playerTotal:
                        print ("Dealer stays. You win!")
                        moneyChange = bet
                        break
                        moneyChange = bet
                    elif dealerTotal == playerTotal:
                        print ("Push! Bet refunded.")
                        moneyChange = 0
                        break
                break
            return moneyChange
            break
        else:
           move = input("Move? (hit/stay)")

#12 Place your bets!
#Calls nothing
#Used by #1 Main
def input_bet(bet, money):
    while True:
        print("Bet? (0 to quit, Enter to stay at $",bet,")",sep='')
        new_bet = input()
        if not new_bet:
            if bet <= money:
                return bet
                break
            else:
                print("Cannot bet more than $",money,".",sep='')
                continue
        try:
            new_bet = int(new_bet)
            if new_bet == 0:
                return 0
            elif abs(new_bet) > money:
                print("Cannot bet more than $",money,".",sep='')
                continue
            break
        except ValueError:
            continue
    return abs(new_bet)

#13 Ace Check
#Calls nothing
#Used by #11 Play
def ace_check(personAce,personTotal):
    if personAce > 0:
        personAce -= 1
        personTotal -= 10
    return personAce, personTotal
main()
