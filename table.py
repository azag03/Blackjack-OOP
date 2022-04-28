from dealer import Dealer
from player import Player
from toolbox import get_integer_between


class Table(object):

    def __init__(self):
        self._players = []
        self._dealer = Dealer('Roy', 10000, self)

    def __str__(self):
        pass

    def manage(self):
        """Runs the blackjack program."""
        numberOfPlayers = get_integer_between(1, 7, 'How many players will there be?')
        #
        # Range from 1 to numberOfPlayers+1, so I don't ask for player 0's name
        #
        for number in range(1, numberOfPlayers+1):
            name = input(f"What is player {number}'s name? ")
            player = Player(name, 100)
            self._players.append(player)
        self._dealer.take_bets()
        while self._players is not None:
            self._dealer.deal()
            self._dealer.play_hands()
            self._dealer.play_own()
            self._dealer.process_hands()
        print('Table is empty. Dealer can go home.')

    def add_player(self, player):
        self._players.append(player)

    def get_dealer(self):
        return self._dealer

    def get_players(self):
        return self._players

    players = property(get_players)
    dealer = property(get_dealer)
