import  random

from card import Card
from hand import Hand
from suit import Suit
from face import Face
from deck import Deck
from dealer import Dealer
from player import Player

'''
standard deck playing card games.
A "standard" deck of playing cards consists of 52 Cards in each of the 4 suits
of Spades, Hearts, Diamonds, and Clubs.
Each suit contains 13 cards: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King
'''

GAMES = 11  # should be an odd number

class Game(object):

    def __init__(self, players):
        self._deck = Deck()
        self._players = players

    def play(self):
        self._deck.shuffle()
        # self._deck.show()
        # each player draws a card interleaved
        for _ in xrange(2):
            for player in self._players:
                player.hand.draw(self._deck)
        self.select()
        for player in self._players:
            print player

    def select(self):
        for player in self._players:
            if (player.hand.value < random.randint(12, 19) and
                random.randint(0, 1) == 1):
                player.hand.draw(self._deck)

    def winner(self):
        ''' declare the winner
        '''
        values = [player.hand.value for player in self._players if
                  player.hand.value <= 21]
        value = max(values) if values else 0
        winners = []
        for player in self._players:
            if player.hand.value == value:
                player.won()
                winners.append(player)
        if winners:
            if len(winners) == 1:
                print ('%s wins! %d' % (winners[0].name, value))
            else:
                print ('tie! %s = %d' % (', '.join([winner.name for winner in
                                                    winners]), value))
        else:
            print ('no winner')
        # return all cards back to the deck
        for player in self._players:
            player.hand.restore(self._deck)
            player.hand = Hand()
        # self._deck.show()


def main():
    players = ['Alice', 'Cooper', 'Bob']
    game = Game(set([Player(player) for player in players]))
    for i in xrange(GAMES):
        print ('Game #%d:' % (i + 1))
        game.play()
        game.winner()
        print ('-' * 80)

    for player in game._players:
        print ('%s %d wins' % (player.name, player._wins))

    print ('Winner!!! ')

if __name__ == '__main__':
    main()
