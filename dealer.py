from blackjackDeck import BlackjackDeck
from hand import Hand
from toolbox import get_integer_between


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

    def take_bets(self):
        """Allows the player to place an initial bet; creates a hand from that bet."""
        hand = None
        for player in self._table.players:
            bet = get_integer_between(0, player.money, f'How much would you like to bet on this hand, {player.name}?')
            if bet == 0:
                print(f'{player.name} is sitting out this hand.')
            else:
                hand = Hand(bet)
                player.money -= bet
                player.hands.append(hand)
        return hand

    def deal(self):
        """Passes out the initial two cards to the dealer and each of the players."""
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
                    print(player)

    def play_hands(self):
        """Loops through each players' hand and performs their desired action."""
        for player in self._table.players:
            for hand in player.hands:
                command = player.play(hand)
                if command == 'H':
                    self.player_hit(hand)
                elif command == 'S':
                    self.player_stand(hand)
                elif command == 'D':
                    self.player_double(hand)
                elif command == 'P':
                    self.player_split(player, hand)

    def player_hit(self, hand):
        """Hits a player's hand."""
        card = self._deck.pop()
        card.flip()
        hand.hit(card)

    def player_stand(self, hand):
        """Disables a player's hand."""
        hand.stand()

    def player_double(self, hand):
        """Doubles a player's hand."""
        card = self._deck.pop()
        card.flip()
        hand.double_down(card, hand.bet)

    def player_split(self, player, hand):
        """Splits and player's hand."""
        card = hand.split()
        newBet = get_integer_between(0, player.money, f'How much would you like to bet on this hand, {player.name}?')
        newHand = Hand(newBet)
        newHand.cards.append(card)
        self.player_hit(newHand)
        player.money -= newBet
        player.hands.append(newHand)

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
