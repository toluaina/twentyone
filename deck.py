import random
from card import Card
from suit import Suit
from face import Face
from error import EmptyDeckError

class Deck(object):

    def __init__(self):
        self.cards = [Card(face, suit) for suit in [Suit.Hearts, Suit.Clubs,
                                                    Suit.Spades, Suit.Diamonds]
                      for face in list(xrange(2, 11))]
        for face in [Face.Ace, Face.Jack, Face.Queen, Face.King]:
            for suit in [Suit.Hearts, Suit.Clubs, Suit.Spades, Suit.Diamonds]:
                self.cards.append(Card(face, suit))

    def shuffle(self):
        ''' shuffle deck
        '''
        random.shuffle(self.cards)

    def draw(self):
        ''' draw card from top of deck
        '''
        if len(self.cards) < 1:
            raise EmptyDeckError('Cannot draw from an empty deck')
        return self.cards.pop(-1)

    def restore(self, card):
        ''' return card to deck
        '''
        if not card in self.cards:
            self.cards.append(card)

    def show(self):
        ''' show deck
        '''
        for i, card in enumerate(self.cards):
            print ('%d) %s' % (i + 1, card))
