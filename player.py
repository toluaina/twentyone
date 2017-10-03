from hand import Hand

class Player(object):

    def __init__(self, name):
        self.name = name
        self._wins = 0
        self.hand = Hand() # initializes an empty hand

    def __str__(self):
        return '%s: %s' % (self.name, self.hand)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return (not self.__eq__(other))

    def won(self):
        self._wins += 1
