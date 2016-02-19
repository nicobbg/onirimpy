


class Hand:
    """
    This is a Hand.
    A hand is composed of 5 cards.
    """
    cards_in_hand = 0
    cards_in_hand_list = []
    limbo = []

    def __init__(self, deck):
        """
        The 5 cards are drown from the top of the Deck
        The first hand is only composed of Labyrinth cards
        Every Door and Nightmare cards that are drown during the 1st hand phase are put into the Limbo stack and then
        the Limbo is put back into the deck. Finally the deck is shuffled.
        """
        while self.cards_in_hand < 5:
            c = deck.pop_card()
            if c.type is not 'Labyrinth':
                self.limbo.append(c)
            else:
                self.cards_in_hand_list.append(c)
                self.cards_in_hand += 1
        for l_card in self.limbo:
            deck.put_card(l_card)
        deck.shuffle()

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

    def play_card(self):
        """
        play_card makes you choose 1 card from your hand
        this card will be appended to the play mat
        :return: the select card to play
        """
        print "this is your hand"
        self.show()
        choice = input("select and play one card from your hand (1...10)\n")
        choice -= 1
        card_to_play = self.cards_in_hand_list.pop(choice)
        self.cards_in_hand -= 1
        return card_to_play

    def draw_card(self, deck):
        """
        draw_card will take the top card from the deck and append it to your hand
        :return: nothing
        """
        self.cards_in_hand_list.append(deck.pop_card())
        self.cards_in_hand += 1
        print "this is your hand"
        self.show()
