import random
from cards.card import Card


class Deck:
    """
    This is a Deck.
    A Deck is a list of 76 cards : 58 Labyrinth cards, 8 Door cards and 10 Nightmare cards.
    There are 2 Door cards of each colour in the deck
    There are 16 Red Labyrinth cards, 15 Blue Lab cards, 14 Green Lab cards and 13 White Lab cards.
    """
    deck = []
    colours = ['Red','Blue','Green','White']

    def __init__(self):
        for i in range(10):
            self.deck.append(Card('Nightmare'))
        for c in self.colours:
            for i in range(2):
                self.deck.append(Card('Door', c))
            for i in range(3):
                self.deck.append(Card('Labyrinth', c, 'Key'))
            for i in range(4):
                self.deck.append(Card('Labyrinth', c,'Moon'))
        for i in range(9):
            self.deck.append(Card('Labyrinth', 'Red', 'Sun'))
        for i in range(8):
            self.deck.append(Card('Labyrinth', 'Blue', 'Sun'))
        for i in range(7):
            self.deck.append(Card('Labyrinth', 'Green', 'Sun'))
        for i in range(6):
            self.deck.append(Card('Labyrinth', 'White', 'Sun'))

    def show(self):
        """
        This method print the content of the deck card by card
        """
        for card in self.deck:
            print card.show()

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
        return self.deck.pop()

    def put_card(self, card):
        """
        This method adds a card on top of the deck
        """
        self.deck.append(card)


