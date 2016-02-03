"""
Python Onirim Game Developement.
"""

class Card:
    """
    This is a card.
    A card is defined by its type, colour and symbol.
    There are 3 card's type in the classic game : Labyrinth, Nightmare and Door.
    There are 4 colours of cards : Red, Blue, Green and White. Nightmare cards are colourless.
    There are 3 symbols : Key, Moon, Sun. Nightmare cards are symbolless.
    """

    def __init__(self, type, colour=None, symbol=None):
        self.type = type
        self.colour = colour
        self.symbol = symbol

    def get(self):
        """
        :rtype: dict
        :return: all attributes of the card object
        """
        return vars(self)