from dealer import Dealer


class Table(object):

    def __init__(self):
        self._players = []
        self._dealer = Dealer('Dealer', 10000, self)

    def __str__(self):
        pass

    def manage(self):
        pass

    def add_player(self, player):
        self._players.append(player)

    def get_dealer(self):
        return self._dealer

    def get_players(self):
        return self._players

    players = property(get_players)
    dealer = property(get_dealer)
