class Turn:
    """
    A round or turn is composed of 3 steps
    1st step: play or discard a card of your hand
    2nd step: fill your hand
    3rd step: shuffle the limbo pile
    To play a round, you need a deck and a hand of cards
    """

    step = 0
    start = 0

    def __init__(self, hand, deck, game_start=False):
        self.step = 1
        self.start = game_start
        if self.start is True:
            c = hand.play_card()
            c.show()
            self.game_start = False
        else:
            choice = raw_input("Do you want to PLAY a card or DRAW a card ?\n")
            if 'PLAY' in choice:
                c = hand.play_card()
            else:
                if 'DRAW' in choice:
                    c = hand.draw_card(deck)

    def step(self, num=2):
        self.step = num
        if self.step == 2:
            #TODO fill your hand
            pass
        else:
            if self.step == 3:
                #TODO shuffle the limbo pile
                pass
