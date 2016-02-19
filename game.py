from deck import Deck
from hand import Hand
from turn import Turn

# initialization of the game
# Instantiate a deck of cards and shuffle it
# Draw you first hand and then start the first turn
d = Deck()
d.shuffle()
h = Hand(d)
t = Turn(h, d, True)

