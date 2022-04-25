from blackjackDeck import BlackjackDeck
from hand import Hand
from toolbox import get_boolean


class Dealer(object):

    def __init__(self, name, money, table):
        self._name = name
        self._hand = Hand(0)
        self._deck = BlackjackDeck()
        self._money = money
        self._table = table

    def __str__(self):
        string = f'Dealer {self._name}:\n{self._hand}'
        return string

    def ask_in(self):
        """Asks a player if they want to buy in."""
        for player in self._table.players:
            buyIn = get_boolean(f'Do you want to buy in {player.name}?')
            if buyIn:
                player.buy_in()

    def deal(self):
        """Passes out the first two cards to the dealer and each of the players."""
        for _ in range(2):
            dealerCard = self._deck.pop()
            dealerCard.flip()
            self._hand.cards.append(dealerCard)
            print(self._hand)
            for player in self._table.players:
                card = self._deck.pop()
                for hand in player.hands:
                    card.flip()
                    hand.hit(card)
                    print(hand)

    def shuffle(self):
        """Shuffles his deck."""
        self._deck.shuffle()

    def process_hands(self):
        """For each completed hand, performs the respective command (pay out, draw, or rake in)."""
        for player in self._table.players:
            for hand in player.hands:
                if hand.is_busted():
                    self._money += hand.bet
                elif hand.is_blackjack() and not self._hand.is_blackjack():
                    player.money += 1.5 * hand.bet
                elif hand.soft_value() == self._hand.soft_value():
                    player.money += hand.bet
                elif hand.soft_value() < self._hand.soft_value():
                    self._money += hand.bet
                elif hand.soft_value() > self._hand.soft_value():
                    player.money += 1.5 * hand.bet

    def get_money(self):
        return self._money

    def get_hand(self):
        return self._hand

    hand = property(get_hand)
    money = property(get_money)
