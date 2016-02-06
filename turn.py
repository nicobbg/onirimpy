class Turn:
    """
    A round or turn is composed of 3 steps
    1st step: play or discard a card of your hand
    2nd step: fill your hand
    3rd step: shuffle the limbo pile
    """

    step = 0

    def __init__(self, game_start=False):
        self.step = 1
        if game_start is True:
            pass
            # TODO play a card in hand on the table
        else:
            pass
            # TODO propose draw or play