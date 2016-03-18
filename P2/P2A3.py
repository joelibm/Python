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
    play = "y"
    while play.lower()[0] == "y":
        money += play_hand(player)
        print (player," has $",money,sep ='')
        if money > 0:
            play = input ("Play again? (y/n) ")
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
#Deals one card
def deal(person):
    card = random.randint(1,13)
    print (person," was dealt a ",string_of_card(card),".",sep='')
    return (value_of_card(card))
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
def play_hand(player):
    dealer = "Dealer"
    moneyChange = -25
    dealerTotal = deal(dealer)
    playerTotal = deal(player)
    playerTotal += deal(player)
    report(player,dealerTotal,playerTotal)
    move = input("Move? (hit/stay)")
    while True:
        if move.lower()[0] == ("h") or move.lower()[0] == ("s"):
            while move.lower()[0] == "h":
                playerTotal += deal(player)
                report(player,dealerTotal,playerTotal)
                if playerTotal > 21:
                    print ("Bust!")
                    break
                else:
                    move = input("Move? (hit/stay)")
            while move.lower()[0] == "s":
                while dealerTotal < 17:
                    dealerTotal += deal(dealer)
                    report(player,dealerTotal,playerTotal)
                while dealerTotal > 21:
                    print ("Dealer busts! You win!")
                    moneyChange = 25
                    break
                else:
                    if dealerTotal > playerTotal:
                        print ("Dealer stays. You lose.")
                    elif dealerTotal < playerTotal:
                        print ("Dealer stays. You win!")
                        moneyChange = 25
                    elif dealerTotal == playerTotal:
                        print ("Push! Bet refunded.")
                        moneyChange = 0
                break
            return moneyChange
            break
        else:
           move = input("Move? (hit/stay)")
main()
