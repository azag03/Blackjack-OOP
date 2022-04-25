from toolbox import get_integer_between
from hand import Hand


class Player(object):

    def __init__(self, name, money):
        self._name = name
        self._hands = []
        self._money = money

    def __str__(self):
        return f'Name: {self._name}\nAmount: {self._money}\nHands: {self._hands}'

    def buy_in(self):
        """Allows the player to place an initial bet; creates a hand from that bet."""
        bet = get_integer_between(0, self._money, f'How much would you like to bet {self._name}?')
        self._money -= bet
        hand = Hand(bet)
        self._hands.append(hand)
        return hand

    # def join_table(self):

    # def leave_table(self):

    def get_hands(self):
        return self._hands

    def get_name(self):
        return self._name

    def get_money(self):
        return self._money

    def set_money(self, money):
        self._money = money

    money = property(get_money, set_money)
    name = property(get_name)
    hands = property(get_hands)
