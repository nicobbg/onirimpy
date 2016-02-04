class Hand:
    """
    This is a Hand.
    A hand is composed of 5 cards.
    The 5 cards are drown from the top of the Deck
    """
    cards_in_hand = 0
    cards_in_hand_list = []

    def __init__(self, deck):
        while self.cards_in_hand < 5:
            c = deck.pop_card()
            print c.type
            if c.type is not 'Labyrinth':
                print 'this is not a Labyrinth card\n'
            else:
                self.cards_in_hand_list.append(c)
                self.cards_in_hand += 1
        print str(self.cards_in_hand) + ' cards in your hand\n'


    def show(self):
        """
        :return: the cards in my hand
        """
        for c in self.cards_in_hand_list:
            print c.show()

    def len(self):
        """
        :return: the number of cards in my hand
        """
        return self.cards_in_hand


