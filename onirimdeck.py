class Deck:
    """
    This is a Deck.
    A Deck is composed of xx cards : nn Labyrinth cards, 8 Door cards and mm Nightmare cards.
    """

    def __init__(self):
        deck = []
        colour = ['blue', 'red', 'white', 'green']
        for count in range(0, 1): 
            for i in colour:
                a_door = Door(i)
                deck.append(a_door)


