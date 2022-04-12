class Hand(object):

    def __init__(self, bet):
        self._cards = []
        self._bet = bet
        self._done = False
        self._doubled = False
        self._split = False

    def __str__(self):
        pass

    def soft_value(self):
        pass

    def hard_value(self):
        pass

    def bust(self):
        pass

    def hit(self):
        pass

    def stand(self):
        pass

