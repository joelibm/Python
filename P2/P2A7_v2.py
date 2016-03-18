import random

def main():
    try:
        player, money = restore()
        print("Resume saved game '", player,"'? (y/n)",sep='')
        load = input()
        if load != "" and load.lower()[0] != "y":
            player = input("What is your name? ")
            money = 1000
            log_new_game(player)
    except FileNotFoundError:
        player = input("What is your name? ")
        money = 1000
        log_new_game(player)
    dealer = "Dealer"
    print (player," has $",money,sep ='')
    bet = 25
    bet = input_bet(bet, money)
    while bet > 0:
        money += play_hand(player,bet)
        log_book(money)
        print (player," has $",money,sep ='')
        if money <= 0:
            print ("You're out of money! Game over.")
            break
        bet = input_bet(bet, money)
    if money != 0:
        saveGame = input ("Would you like to save this game? (y/n) ")
        if saveGame.lower()[0] == "y":
            save(player, str(money))

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

def new_deck():
    deck = []
    for suit in range (1, 5):
        for rank in range (1,14):
            a = [rank,suit]
            deck.append(tuple(a))
    random.shuffle(deck)
    return deck

def string_of_hand(hand,cardString):
    hand = hand + " " + cardString
    return hand

def deal(deck,hand,personAce,personTotal):
    card = deck.pop(0)
    hand = string_of_hand(hand,string_of_card(card))
    if value_of_card(card[0]) == 11:
        personAce += 1
    personTotal += value_of_card(card[0])
    return (hand,personAce,personTotal)

def report_player(player, playerTotal, playerHand):
    print (player,"'s Hand:",playerHand,sep='')
    print ("Value:",playerTotal)
    
def report_dealer(dealerTotal,dealerHand):
    print ("Dealer's Hand:",dealerHand,sep='')
    print ("Value:",dealerTotal)

def save(name, money):
    file = open('blackjack.save','w')
    file.write(name + '\n' + money)
    file.close()

def restore():
    file = open('blackjack.save','r')
    name = file.readline().rstrip('\n')
    money = file.readline()
    return name, int(money)
    file.close()

def play_hand(player,bet):
    dealer = "Dealer"
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
    playerHand,playerAce,playerTotal = deal(deck,playerHand,playerAce,playerTotal) 


    playerTotal = snake_eyes(playerTotal)#fixes issue when double aces are drawn
    dealerTotal = snake_eyes(dealerTotal)

    if dealerTotal == 21:#handles dealer blackjacks
        report_dealer(dealerTotal,dealerHand)
        report_player(player, playerTotal, playerHand)
        if playerTotal == 21:
            print ("DOUBLE BLACKJACK! Bet refunded.")
            moneyChange=0
        elif playerTotal != 21:
            print("Dealer has blackjack! You lose.")
        return moneyChange
    elif playerTotal == 21:#handles player blackjacks
        report_dealer(dealerTotal,dealerHand)
        report_player(player, playerTotal, playerHand)
        print("BLACKJACK! You win 1.5x!")
        moneyChange = int(1.5*bet)
        return moneyChange
    else:
        report_dealer(hiddenDealerTotal,hiddenDealerHand)
        report_player(player, playerTotal, playerHand)

        while True:
            if 9 <= playerTotal <= 11 and move != "s": #allows player to double down
                doubleDown = input("Double Down? Your bet doubles and you hit exactly once. (y/n)")
                if doubleDown=="" or doubleDown.lower()[0]=="y":
                    print("You double down.")
                    moneyChange *= 2
                    deck,playerHand,playerAce,playerTotal,busted = player_hit(deck,player,playerHand,playerAce,playerTotal,hiddenDealerTotal,hiddenDealerHand)
                    move = "s"
                else:
                    print("You do not double down.")
            else:
                move = input("Move? (hit/stand)")
            if move != "" and (move.lower()[0] == ("h") or move.lower()[0] == ("s")):
                while move.lower()[0] == "h":
                    deck,playerHand,playerAce,playerTotal,busted = player_hit(deck,player,playerHand,playerAce,playerTotal,hiddenDealerTotal,hiddenDealerHand)
                    if busted == True:
                        break
                    move = input("Move? (hit/stand)")
                if move.lower()[0] == "s":
                    moneyChange = dealer_play(deck,dealerHand,dealerAce,dealerTotal,player,playerHand,playerTotal,moneyChange)
                return moneyChange
                break

def player_hit(deck,player,playerHand,playerAce,playerTotal,hiddenDealerTotal,hiddenDealerHand):
    playerHand,playerAce,playerTotal = deal(deck,playerHand,playerAce,playerTotal)
    busted = False
    if (playerTotal > 21) and (playerAce > 0):
        playerAce -= 1
        playerTotal -= 10
    report_player(player, playerTotal, playerHand)
    if playerTotal > 21:
        print ("Bust!")
        busted = True
    return (deck,playerHand,playerAce,playerTotal,busted)

def dealer_play(deck,dealerHand,dealerAce,dealerTotal,player,playerHand,playerTotal,moneyChange):
    dealer_drew = False
    if dealerTotal < 17:
        report_dealer(dealerTotal,dealerHand)
    while dealerTotal < 17:
        dealer_drew = True 
        dealerHand,dealerAce,dealerTotal = deal(deck,dealerHand,dealerAce,dealerTotal)
        if (dealerTotal > 21) and (dealerAce > 0):
            dealerAce -=1
            dealerTotal -=10
        report_dealer(dealerTotal,dealerHand)
    if dealerTotal > 21:
        print ("Dealer busts! You win!")
        moneyChange = abs(moneyChange)
    if 17 <= dealerTotal <=21:
        if dealer_drew == False:
            report_dealer(dealerTotal,dealerHand)
            report_player(player, playerTotal, playerHand)
            dealer_drew = True
        if dealerTotal > playerTotal:
            print ("Dealer stands. You lose.")
        elif dealerTotal < playerTotal:
            print ("Dealer stands. You win!")
            moneyChange = abs(moneyChange)
        elif dealerTotal == playerTotal:
            print ("Push! Bet refunded.")
            moneyChange = 0
    return moneyChange

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

def ace_check(personAce,personTotal):
    if personAce > 0:
        personAce -= 1
        personTotal -= 10
    return personAce, personTotal

def log_book(money):
    try:
        f = open('blackjack.csv','a')
        f.write('\n' + get_last_log() + ',' + str(money))
        f.close()
    except FileNotFoundError:
        f = open('blackjack.csv','w')
        f.write("1," + str(money))
        f.close()
    except IndexError:
        f = open('blackjack.csv','w')
        f.write("1," + str(money))
        f.close()
        
def get_last_log():
    f = open('blackjack.csv','r')
    contents = f.readlines()
    backwards = list(reversed(contents))
    last = backwards[0]
    number = int(last.split(',')[0]) + 1
    f.close()
    return str(number)

def snake_eyes(personTotal):
    if personTotal == 22:
        return 12
    else:
        return personTotal

def log_new_game(name):
    try:
        f = open('blackjack.csv','a')
        f.write('\n' + get_last_log() + ",1000,New Game: " + name)
        f.close()
    except FileNotFoundError:
        f = open('blackjack.csv','w')
        f.write("1,1000,New Game: " + name)
        f.close()
    except IndexError:
        f = open('blackjack.csv','w')
        f.write("1,1000,New Game: " + name)
        f.close()    

main()
