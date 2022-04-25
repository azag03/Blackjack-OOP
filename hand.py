from errors import CallError


class Hand(object):

    def __init__(self, bet):
        self._cards = []
        self._bet = bet
        self.isDoubled = False
        self.isSplit = False
        self.isDone = False

    def __str__(self):
        if self.isDone:
            string = 'Hand is no longer playable'
        else:
            string = f'Bet: {self._bet}\n'
            string += 'Hand:\n'
            for card in self._cards:
                string += f'{card}\n'
        return string

    def soft_value(self):
        """Returns the value of a hand using the soft value of each card."""
        value = 0
        for card in self._cards:
            value += card.softValue
        return value

    def hard_value(self):
        """Returns the value of a hand using the hard value of each card."""
        value = 0
        for card in self._cards:
            value += card.hardValue
        return value

    def can_hit(self):
        """Checks to see if a hand is able to hit."""
        canHit = True
        if self.is_blackjack() or self.is_doubled() or self.is_busted():
            canHit = False
        return canHit

    def hit(self, card):
        """Adds a card to a hand."""
        if self.can_hit():
            self._cards.append(card)
        else:
            raise CallError('Cannot hit a closed hand')

    def can_split(self):
        """Checks to see if a hand is able to split."""
        canSplit = False
        if len(self._cards) == 2 and self._cards[0].hardValue == self._cards[1].hardValue:
            canSplit = True
        return canSplit

    def split(self):
        """Splits a hand into two separate ones."""
        if self.can_split():
            card = self._cards.pop()
            self.isSplit = True
        else:
            raise CallError('Can only split 2 cards of the same value.')
        return card

    def stand(self):
        """Disables a hand from being played."""
        self.isDone = True

    def can_double(self):
        """Checks to see if a hand is able to double down."""
        canDouble = False
        if len(self._cards) == 2:
            canDouble = True
        return canDouble

    def double_down(self, card, bet):
        """Doubles down on a hand and hits one last time."""
        if self.can_double():
            self._bet += bet
            self.hit(card)
            self.isDoubled = True
        else:
            raise CallError('Can only double down after being dealt two cards from the dealer.')

    def is_blackjack(self):
        """Checks to see if a hand is blackjack."""
        isBlackjack = False
        if len(self._cards) == 2:
            if self._cards[0].shortName and self._cards[1].shortName in ['A', 'K', 'Q', 'J', '10']:
                if self.soft_value() == 21:
                    isBlackjack = True
                    self.isDone = True
        return isBlackjack

    def is_busted(self):
        """Checks to see if a hand is busted"""
        isBusted = False
        if self.hard_value() > 21:
            isBusted = True
            self.isDone = True
        return isBusted

    def is_doubled(self):
        """Checks to see if a hand is doubled."""
        if self.isDoubled:
            self.isDone = True
        return self.isDoubled

    def is_split(self):
        """Checks to see if a hand is split."""
        return self.isSplit

    def get_bet(self):
        return self._bet

    def get_cards(self):
        return self._cards

    cards = property(get_cards)
    bet = property(get_bet)
