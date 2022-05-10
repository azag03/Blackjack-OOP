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
        leavingPlayers = []
        for player in self._table.players:
            bet = get_integer_between(-1, player.money, f'How much would you like to bet this round, {player.name}?')
            if bet == 0:
                print(f'{player.name} is sitting out this hand.\n')
            elif bet == -1:
                print(f'{player.name} has left the table.\n')
                leavingPlayers.append(player)
            else:
                hand = Hand(bet)
                player.money -= bet
                player.hands.append(hand)
        #
        # Must happen outside the for loop to ensure that when someone leaves the program doesn't skip over the
        # succeeding player.
        #
        for player in leavingPlayers:
            self.player_leave(player)

    def deal(self):
        """Passes out the initial two cards to the dealer and each of the players."""
        if self._deck.should_shuffle():
            self.shuffle()
            print('Deck has been shuffled.')
        for _ in range(2):
            dealerCard = self._deck.pop()
            dealerCard.flip()
            self._hand.cards.append(dealerCard)
            for player in self._table.players:
                for hand in player.hands:
                    card = self._deck.pop()
                    card.flip()
                    hand.hit(card)
        print(f"Dealer is showing:\n{self._hand.cards[0]}\n{self._hand.cards[1]}\n")

    def play_hands(self):
        """Loops through each players' hand and performs their desired action."""
        for player in self._table.players:
            for hand in player.hands:
                while not hand.is_done():
                    command = player.play(hand)
                    if command == 'H':
                        self.player_hit(hand)
                    elif command == 'S':
                        self.player_stand(hand)
                    elif command == 'D':
                        self.player_double(hand)
                    elif command == 'P':
                        self.player_split(player, hand)
        # for player in self._table.players:
        # print(player)

    def play_own(self):
        """Plays the dealer's hand."""
        #
        # Dealer must hit on soft-values below 17 and stand on 17 and above.
        #
        while self._hand.value() < 17:
            card = self._deck.pop()
            card.flip()
            self._hand.hit(card)
        if self._hand.value() > 17:
            self._hand.stand()
        # print(f'{self}\n')

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

    def player_leave(self, player):
        """Removes a player from the table."""
        self._table.players.remove(player)

    def shuffle(self):
        """Shuffles his deck."""
        self._deck = BlackjackDeck()
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
            player.hands = []

    def process_hands(self):
        """For each completed hand, performs the respective command (pay out, draw, or rake in)."""
        for player in self._table.players:
            for hand in player.hands:
                if hand.is_busted():
                    self._money += hand.bet
                    print(f"{player.name}'s hand is busted.")
                elif hand.value() == self._hand.value():
                    player.money += hand.bet
                    print(f"{player.name}'s hand has the same value as the dealer.")
                elif hand.is_blackjack():
                    self._money -= 2.5 * hand.bet
                    player.money += 2.5 * hand.bet
                    print(f"{player.name} has blackjack!!")
                elif self._hand.is_busted():
                    self._money -= 2 * hand.bet
                    player.money += 2 * hand.bet
                    print(f'Dealer has busted. {player.name} wins the hand.')
                elif hand.value() < self._hand.value():
                    self._money += hand.bet
                    print(f"Dealer's hand is higher than {player.name}'s.")
                elif hand.value() > self._hand.value():
                    self._money -= 2 * hand.bet
                    player.money += 2 * hand.bet
                    print(f"{player.name}'s hand is higher than the dealer's.")
        print(f"\nDealer's Money: {self._money}")
        for player in self._table.players:
            print(f"{player.name}'s money: {player.money}")

    def get_money(self):
        return self._money

    def get_hand(self):
        return self._hand

    def get_deck(self):
        return self._deck

    hand = property(get_hand)
    money = property(get_money)
    deck = property(get_deck)
