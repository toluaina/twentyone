from face import Face

class Hand(object):

    def __init__(self):
        self.cards = []

    def __str__(self):
        return '%s value: %d' % ([card for card in self.cards], self.value)

    def __repr__(self):
        return self.__str__()

    def draw(self, deck, num=1):
        ''' draw a number of cards from the deck into hand
        '''
        for _ in xrange(num):
            self.cards.append(deck.draw())

    def restore(self, deck):
        ''' return all cards back to the deck
        '''
        for card in self.cards:
            deck.restore(card)
        for card in self.cards:
            self.cards.remove(card)

    @property
    def value(self):
        _value = sum([card.value for card in self.cards])
        if Face.Ace in [card.face for card in self.cards] and _value <= 11:
            _value += 10
        return _value
