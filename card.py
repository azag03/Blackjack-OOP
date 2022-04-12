class Card(object):

    def __init__(self, hardValue, softValue, name, suit):
        self._hardValue = hardValue
        self._softValue = softValue
        self._name = name
        self._suit = suit
        self._visibility = False

    def __str__(self):
        if self._visibility:
            string = f'{self._name} of {self._suit}: {self._hardValue}'
        else:
            string = 'Cool card design'
        return string

    def flip(self):
        """Changes the visibility state."""
        self._visibility = not self._visibility
