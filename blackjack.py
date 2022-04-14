from deck import Deck
from card import Card


class Blackjack(Deck):

    suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']

    names = ['Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two']

    shortNames = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

    hardValues = {"A": 1, "K": 10, "Q": 10, "J": 10, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3,
                  "2": 2}

    softValues = {"A": 11, "K": 10, "Q": 10, "J": 10, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3,
                  "2": 2}

    def __init__(self, deckType='Blackjack', size=1):
        super().__init__(deckType, size)

    def create_deck(self):
        """Creates a deck based on the given card information."""
        #
        # For a deck with a given size, go through each list and dictionary to create cards based on the information,
        # then append to self.cards.
        #
        for deck in range(self.size):
            for suit in Blackjack.suits:
                for name in Blackjack.shortNames:
                    hardValue = Blackjack.hardValues[name]
                    softValue = Blackjack.softValues[name]
                    card = Card(hardValue, softValue, name, suit)
                    # card.flip()
                    self.cards.append(card)

    def stack(self):
        """
        Create a deck with cards in a certain order for testing or scamming purposes.
        """
        shortSuits = ["C", "S", "H", "D"]
        suitDictionary = dict(zip(shortSuits, Blackjack.suits))
        nameDictionary = dict(zip(Blackjack.shortNames, Blackjack.names))

        self._cards = []
        with open("stacked_deck1.txt", "r") as deckFile:
            #
            # stack1.txt is of the form: QC\nAD\n2S\n10H\n...
            #
            for line in deckFile:
                line = line[:-1] # Remove the new line character.
                shortSuit = line[-1]
                shortName = line[:-1]
                try:
                    name = nameDictionary[shortName]
                    suit = suitDictionary[shortSuit]
                    hardValue = Blackjack.hardValues[shortName]
                    softValue = Blackjack.softValues[shortName]
                    card = Card(hardValue, softValue, name, suit)
                    self._cards.append(card)
                except:
                    raise ValueError(f"'{shortName}{shortSuit}' does not correspond to a known card.")


