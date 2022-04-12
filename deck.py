import random


class Deck(object):

    def __init__(self, deckType, size):
        self._cards = []
        self._deckType = deckType
        self._size = size

    def __str__(self):
        string = f'Deck Type: {self._deckType}\n'
        string += f'Size: {self._size}\n'
        for card in self._cards:
            string += f'{card}\n'
        return string

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self._cards)

    def pop(self):
        """Removes a card from the list of cards to be dealt."""
        card = random.choice(self._cards)
        self._cards.remove(card)
        print(card)
