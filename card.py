from suit import Suit
from face import Face
from error import InvalidCardFaceError
from error import InvalidCardSuitError

class Card(object):

    def __init__(self, face, suit):
        if not face in (Face.Ace, Face.Jack, Face.Queen,
                        Face.King) and face not in list(xrange(2, 11)):
            raise InvalidCardFaceError('Invalid face "%s"' % face)
        if not suit in (Suit.Clubs, Suit.Diamonds, Suit.Hearts, Suit.Spades):
            raise InvalidCardSuitError('Invalid suit "%s"' % suit)
        self._face = face
        self._suit = suit

    def __str__(self):
        return '{0._face} of {0._suit}'.format(self)

    def __repr__(self):
        return self.__str__()

    @property
    def value(self):
        if self.face == Face.Ace:
            return 1
        elif self.face in (Face.Jack, Face.Queen, Face.King):
            return 10
        else:
            return self.face

    @property
    def face(self):
        return self._face

    @property
    def suit(self):
        return self._suit
