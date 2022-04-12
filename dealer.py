class Dealer(object):

    def __init__(self, name, deck, hand, money):
        self._name = name
        self._deck = deck
        self._hand = hand
        self._money = money

    def __str__(self):
        pass

    def deal(self):
        """Passes out a card to each of the players."""
        self._deck.pop()

    def shuffle(self):
        """Shuffles his deck."""
        self._deck.shuffle()

    def pay_out(self):
        """Gives reward to those who win."""
        pass

    def rake_in(self):
        """Collects a loser's bet."""
        pass

    def play(self):
        pass
