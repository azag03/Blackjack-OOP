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
        string = f'Dealer: {self._name}\n\n{self._hand}'
        return string

    def take_bets(self):
        """Allows the player to place an initial bet; creates a hand from that bet."""
        hand = None
        for player in self._table.players:
            bet = get_integer_between(0, player.money, f'How much would you like to bet this round, {player.name}?')
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
            for player in self._table.players:
                for hand in player.hands:
                    card = self._deck.pop()
                    card.flip()
                    hand.hit(card)
        print(self)
        for player in self._table.players:
            print(player)

    def play_hands(self):
        """Loops through each players' hand and performs their desired action."""
        for player in self._table.players:
            for hand in player.hands:
                while not hand.is_done():
                    command = player.play(hand)
                    if command == 'H':
                        self.player_hit(hand)
                    elif command == 'T':
                        self.player_stand(hand)
                    elif command == 'D':
                        self.player_double(hand)
                    elif command == 'S':
                        self.player_split(player, hand)
        for player in self._table.players:
            print(player)

    def play_own(self):
        """Plays the dealer's hand."""
        #
        # Dealer must hit on soft-values below 17 and stand on 17 and above.
        #
        while self._hand.soft_value() < 17:
            card = self._deck.pop()
            card.flip()
            self._hand.hit(card)
        if self._hand.soft_value() > 17:
            self._hand.stand()
        print(self)

    def player_hit(self, hand):
        """Hits a player's hand."""
        card = self._deck.pop()
        card.flip()
        hand.hit(card)

    def player_stand(self, hand):
        """Disables a player's hand."""
        hand.stand()

    def player_double(self, hand):
        """Doubles down on a player's hand."""
        card = self._deck.pop()
        card.flip()
        hand.double_down(card, hand.bet)
        print(hand, hand.bet)

    def player_split(self, player, hand):
        """Splits and player's hand."""
        card = hand.split()
        newBet = get_integer_between(0, player.money, f"What's the bet on this new hand, {player.name}?")
        newHand = Hand(newBet)
        newHand.cards.append(card)
        player.money -= newBet
        player.hands.append(newHand)
        for hand in player.hands:
            print(hand)

    def shuffle(self):
        """Shuffles his deck."""
        self._deck.shuffle()

    def cleanup(self):
        """Removes cards from everyone's hands."""
        print('\nRound is over next round begins now.\n')
        self._hand.cards = []
        #
        # Gets rid of the print statement from the last round.
        #
        self._hand.isStood = False
        self._hand.isDoubled = False
        self._hand.isSplit = False
        for player in self._table.players:
            for hand in player.hands:
                player.hands.remove(hand)

    #
    # Why doesn't this work??
    #
    def process_hands(self):
        """For each completed hand, performs the respective command (pay out, draw, or rake in)."""
        for player in self._table.players:
            for hand in player.hands:
                if hand.is_busted():
                    self._money += hand.bet
                elif self._hand.is_busted() and not hand.is_busted:
                    player.money += 1.5 * hand.bet
                elif hand.is_blackjack() and not self._hand.is_blackjack():
                    player.money += 1.5 * hand.bet
                elif hand.value() == self._hand.value():
                    player.money += hand.bet
                elif hand.value() < self._hand.value():
                    self._money += hand.bet
                elif hand.value() > self._hand.value():
                    player.money += 1.5 * hand.bet
        print(self._money)
        for player in self._table.players:
            print(player.money)

    def get_money(self):
        return self._money

    def get_hand(self):
        return self._hand

    hand = property(get_hand)
    money = property(get_money)
