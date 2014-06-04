from onirimcard import Card

class Deck:
    """
    This is a Deck.
    A Deck is a list of 76 cards : 58 Labyrinth cards, 8 Door cards and 10 Nightmare cards.
    """
    deck = []

    def __init__(self):
        for i in range(0, 9):
            self.deck.append(Card('nightmare'))

    def get_deck(self):
    """
    This method print the content of the deck card by card
    """
        print self.deck

    def shuffle_deck(self):
    """
    This method shuffle the whole deck
    """

