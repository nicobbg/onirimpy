import random
from onirimcard import *

class Deck:
    """
    This is a Deck.
    A Deck is a list of 76 cards : 58 Labyrinth cards, 8 Door cards and 10 Nightmare cards.
    There are 2 Door cards or each colour in the deck
    There are 16 Red Labyrinth cards, 15 Blue Lab cards, 14 Green Lab cards and 13 White Lab cards.
    """
    deck = []
    colours = ['Red','Blue','Green','White']

    def __init__(self):
        for i in range(10):
            self.deck.append(Card('Nightmare'))
        for c in self.colours:
            for i in range(2):
                self.deck.append(Door(c))
            for i in range(3):
                self.deck.append(Labyrinth(c,'Key'))
            for i in range(4):
                self.deck.append(Labyrinth(c,'Moon'))
        for i in range(9):
            self.deck.append(Labyrinth('Red','Sun'))
        for i in range(8):
            self.deck.append(Labyrinth('Blue','Sun'))
        for i in range(7):
            self.deck.append(Labyrinth('Green','Sun'))
        for i in range(6):
            self.deck.append(Labyrinth('White','Sun'))

    def get(self):
        """
        This method print the content of the deck card by card
        """
        for card in self.deck:
            print card.get()

    def len(self):
        """
        :return: number of cards in the deck
        """
        return len(self.deck)

    def shuffle(self):
        """
        This method shuffle the deck randomly
        :rtype: list
        """
        random.shuffle(self.deck)
        """
        This method shuffle the whole deck
        """

    def pop_card(self):
        """
        This method pop out the card on top of the pile
        """
