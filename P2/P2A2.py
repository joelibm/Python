import random
def main():
    player = input("What is your name? ")
    dealer = "Dealer"
    money = 1000
    print (player," has $",money,sep ='')
    play = "y"
    while play.lower()[0] == "y":
        money += play_hand(player)
        print (player," has $",money,sep ='')
        if money > 0:
            play = input ("Play again? (y/n) ")
        else:
            play = "n"
            print ("You're out of money! Game over.")
def value_of_card(card):
    if card >= 11:
        return 10
    elif card == 1:
        return 11
    else:
        return card
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
def deal(person):
    card = random.randint(1,13)
    print (person," was dealt a ",string_of_card(card),".",sep='')
    return (value_of_card(card))
def report(player,dealerTotal,playerTotal):
    print ("Dealer total:",dealerTotal)
    print (player,"total:",playerTotal)
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
                    elif dealerTotal == playerTotal:
                        print ("Push! Bet refunded.")
                        moneyChange = 0
                break
            return moneyChange
            break
        else:
           move = input("Move? (hit/stay)")
main()
