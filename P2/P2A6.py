import random
def main():
    try:
        player, money = restore()
        print("Resume saved game '", player,"'? (y/n)",sep='')
        load = input()
        if load.lower()[0] != "y":
            player = input("What is your name? ")
            money = 1000
    except ValueError:
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
#Get point value of cards
def value_of_card(card):
    if card >= 11:
        return 10
    elif card == 1:
        return 11
    else:
        return card
#Get suit of card
def suit_of_card(suit):
    if suit == 1:
        return '\u2660'
    elif suit == 2:
        return '\u2662'
    elif suit == 3:
        return '\u2663'
    elif suit == 4:
        return '\u2661'
#Get name of card
def string_of_card(card):
    if card == 11:
        return "J"
    elif card == 12:
        return "Q"
    elif card == 13:
        return "K"
    elif card == 1:
        return "A"
    else:
        return card
#New Deck
def new_deck():
    deck = []
    for suit in range (1, 5):
        for rank in range (1,14):
            a = [rank,suit]
            deck.append(tuple(a))
    random.shuffle(deck)
    return deck
#Deals one card
def deal(person,deck):
    card = deck.pop(0)
    print (person," was dealt ",string_of_card(card[0]),suit_of_card(card[1]),".",sep='')
    return (value_of_card(card[0]))
#reports the current score
def report(player,dealerTotal,playerTotal):
    print ("Dealer total:",dealerTotal)
    print (player,"total:",playerTotal)
#save function
def save(name, money):
    file = open('blackjack.save','w')
    file.write(name + '\n' + money)
    file.close()
#load function
def restore():
    file = open('blackjack.save','r')
    name = file.readline().rstrip('\n')
    money = file.readline()
    return name, int(money)
    file.close()
#A full hand of play
def play_hand(player,bet):
    deck = new_deck()
    dealer = "Dealer"
    moneyChange = -bet
    dealerTotal = deal(dealer,deck)
    playerTotal = deal(player,deck)
    playerTotal += deal(player,deck)
    report(player,dealerTotal,playerTotal)
    move = input("Move? (hit/stay)")
    while True:
        if move.lower()[0] == ("h") or move.lower()[0] == ("s"):
            while move.lower()[0] == "h":
                playerTotal += deal(player,deck)
                report(player,dealerTotal,playerTotal)
                if playerTotal > 21:
                    print ("Bust!")
                    break
                else:
                    move = input("Move? (hit/stay)")
            while move.lower()[0] == "s":
                while dealerTotal < 17:
                    dealerTotal += deal(dealer,deck)
                    report(player,dealerTotal,playerTotal)
                while dealerTotal > 21:
                    print ("Dealer busts! You win!")
                    moneyChange = bet
                    break
                else:
                    if dealerTotal > playerTotal:
                        print ("Dealer stays. You lose.")
                    elif dealerTotal < playerTotal:
                        print ("Dealer stays. You win!")
                        moneyChange = bet
                    elif dealerTotal == playerTotal:
                        print ("Push! Bet refunded.")
                        moneyChange = 0
                break
            return moneyChange
            break
        else:
           move = input("Move? (hit/stay)")
#Place your bets!
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
main()
