##import random
##
##
##class Card(object):
##    """Represents a standard playing card.
##    
##    Attributes:
##      suit: integer 0-3
##      rank: integer 1-13
##    """
##
##    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
##    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", 
##              "8", "9", "10", "Jack", "Queen", "King"]
##
##    def __init__(self, suit=0, rank=2):
##        self.suit = suit
##        self.rank = rank
##
##    def __str__(self):
##        """Returns a human-readable string representation."""
##        return '%s of %s' % (Card.rank_names[self.rank],
##                             Card.suit_names[self.suit])
##
##    def __cmp__(self, other):
##        """Compares this card to other, first by suit, then rank.
##
##        Returns a positive number if this > other; negative if other > this;
##        and 0 if they are equivalent.
##        """
##        t1 = self.suit, self.rank
##        t2 = other.suit, other.rank
##        return cmp(t1, t2)
##
##
##class Deck(object):
##    """Represents a deck of cards.
##
##    Attributes:
##      cards: list of Card objects.
##    """
##    
##    def __init__(self):
##        self.cards = []
##        for suit in range(4):
##            for rank in range(1, 14):
##                card = Card(suit, rank)
##                self.cards.append(card)
##
##    def __str__(self):
##        res = []
##        for card in self.cards:
##            res.append(str(card))
##        return '\n'.join(res)
##
##    def add_card(self, card):
##        """Adds a card to the deck."""
##        self.cards.append(card)
##
##    def remove_card(self, card):
##        """Removes a card from the deck."""
##        self.cards.remove(card)
##
##    def pop_card(self, i=-1):
##        """Removes and returns a card from the deck.
##
##        i: index of the card to pop; by default, pops the last card.
##        """
##        return self.cards.pop(i)
##
##    def shuffle(self):
##        """Shuffles the cards in this deck."""
##        random.shuffle(self.cards)
##
####    def sort(self):
####        """Sorts the cards in ascending order."""
####        self.cards.sort()
##
##    def move_cards(self, hand, num):
##        """Moves the given number of cards from the deck into the Hand.
##
##        hand: destination Hand object
##        num: integer number of cards to move
##        """
##        for i in range(num):
##            hand.add_card(self.pop_card())
##
##
##class Hand(Deck):
##    """Represents a hand of playing cards."""
##    
##    def __init__(self, label=''):
##        self.cards = []
##        self.label = label
##
##
##def find_defining_class(obj, method_name):
##    """Finds and returns the class object that will provide 
##    the definition of method_name (as a string) if it is
##    invoked on obj.
##
##    obj: any python object
##    method_name: string method name
##    """
##    for ty in type(obj).mro():
##        if method_name in ty.__dict__:
##            return ty
##    return None
##
##
##if __name__ == '__main__':
##    deck = Deck()
##    deck.shuffle()
##
##    hand = Hand()
##    print(hand, 'shuffle')
##
##    deck.move_cards(hand, 5)
####    hand.sort()
##    print (hand)
import random
#creating the deck of cards
cards = ['AS', 'KS', 'QS', 'JS', '10S', '9S', '8S', '7S', '6S', '5S', '4S', '3S', '2S',\
         'AD', 'KD', 'QD', 'JD', '10D', '9D', '8D', '7D', '6D', '5D', '4D', '3D', '2D',\
         'AC', 'KC', 'QC', 'JC', '10C', '9C', '8C', '7C', '6C', '5C', '4C', '3C', '2C',\
         'AH', 'KH', 'QH', 'JH', '10H', '9H', '8H', '7H', '6H', '5H', '4H', '3H', '2H']
#for this example I have 2 hands
hand1 = []
hand2 = []
#shuffle the cards
random.shuffle(cards)
num = int(input('How many cards to deal to each player? '))
while num > 0:
        hand1.append(cards.pop(0))
        hand2.append(cards.pop(0))
        num = num - 1
print ('hand one is: ')
print (hand1)
print ('hand two is: ')
print (hand2)
print ('the cards remaining in the deck are: ')
print (cards)
