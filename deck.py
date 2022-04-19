import random


class Deck(object):

    def __init__(self, deckType, size):
        self._cards = []
        self._deckType = deckType
        self._size = size

    def __str__(self):
        string = f'Deck Type: {self._deckType}\n'
        string += f'Size: {len(self._cards)}\n'
        for card in self._cards:
            card.flip()
            string += f'{card}\n'
            card.flip()
        return string

    def shuffle(self):
        """Shuffles a deck."""
        random.shuffle(self._cards)

    def pop(self):
        """Removes a card from the top of a deck."""
        #
        # Takes the top card from a deck and removes it
        #
        card = self._cards[0]
        self._cards.remove(card)
        return card

    def flip(self):
        """Flips all the cards in the deck, so we can see their suit in order for testing."""
        for card in self._cards:
            card.flip()

    def get_cards(self):
        return self._cards

    cards = property(get_cards)
