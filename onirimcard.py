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

    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

class Door(Card):
    """
    This is a Door card.
    It inherits from a Card.
    A Door card has a colour but no symbol.
    """

    def __init__(self, colour):
        Card.__init__(self, "Door")
        self.colour = colour

    def get_colour(self):
        return self.colour

class Labyrinth(Card):
    """
    This is a Labyrinth card.
    It inherits from a Card.
    A Labyrinth card has a colour and a symbol.
    """

    def __init__(self, colour, symbol):
        Card.__init__(self, "Labyrinth")
	self.colour = colour
        self.symbol = symbol

