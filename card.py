class Card(object):

    def __init__(self, hardValue, softValue, name, shortName, suit, shortSuit):
        self._hardValue = hardValue
        self._softValue = softValue
        self._name = name
        self._shortName = shortName
        self._suit = suit
        self._shortSuit = shortSuit
        self._visibility = False

    def __str__(self):
        if self._visibility:
            if self._name == 'Ace':
                string = f'{self._shortName} of {self._suit} {self._shortSuit}: {self._hardValue} or {self._softValue}'
            else:
                string = f'{self._shortName} of {self._suit} {self._shortSuit}: {self._hardValue}'
        else:
            string = 'Cool card design'
        return string

    def flip(self):
        """Changes the visibility state."""
        self._visibility = not self._visibility

    def get_visibility(self):
        return self._visibility

    def get_soft_value(self):
        return self._softValue

    def get_hard_value(self):
        return self._hardValue

    def get_name(self):
        return self._name

    def get_short_name(self):
        return self._shortName

    def get_suit(self):
        return self._shortSuit

    def get_short_suit(self):
        return self._shortSuit

    visibility = property(get_visibility)
    softValue = property(get_soft_value)
    hardValue = property(get_hard_value)
    name = property(get_name)
    shortName = property(get_short_name)
    suit = property(get_suit)
    shortSuit = property(get_short_suit)
