from deck import Deck
from card import Card


class BlackjackDeck(Deck):

    suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']

    shortSuits = ['\u2663', '\u2660', '\u2665', '\u2666']

    names = ['King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'Ace']

    shortNames = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']

    hardValues = {"K": 10, "Q": 10, "J": 10, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2,
                  "A": 1}

    softValues = {"K": 10, "Q": 10, "J": 10, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2,
                  "A": 11}

    def __init__(self, deckType='Blackjack', size=1):
        super().__init__(deckType, size)

    def create_deck(self):
        """Creates a deck based on the given card information."""
        #
        # For a deck with a given size, go through each list and dictionary to create cards based on the information,
        # then append to self.cards.
        #
        for deck in range(self._size):
            #
            # Zip(): Allows you to loops through two lists at the same time (puts the two lists together in a tuple
            # (x,y) allowing for easy access)
            #
            for suit, shortSuit in zip(BlackjackDeck.suits, BlackjackDeck.shortSuits):
                for name, shortName in zip(BlackjackDeck.names, BlackjackDeck.shortNames):
                    hardValue = BlackjackDeck.hardValues[shortName]
                    softValue = BlackjackDeck.softValues[shortName]
                    card = Card(hardValue, softValue, shortName, name, suit, shortSuit)
                    self._cards.append(card)

    def stack(self):
        """
        Create a deck with cards in a certain order for testing or scamming purposes.
        """
        shortSuits = ["C", "S", "H", "D"]
        suitDictionary = dict(zip(shortSuits, BlackjackDeck.suits))
        unicodeDictionary = dict(zip(shortSuits, BlackjackDeck.shortSuits))
        nameDictionary = dict(zip(BlackjackDeck.shortNames, BlackjackDeck.names))

        self._cards = []
        with open("stacked_deck1.txt", "r") as deckFile:
            #
            # stack1.txt is of the form: QC\nAD\n2S\n10H\n...
            #
            for line in deckFile:
                line = line[:-1] # Remove the new line character.
                shortSuitLetter = line[-1]
                shortName = line[:-1]
                try:
                    name = nameDictionary[shortName]
                    suit = suitDictionary[shortSuitLetter]
                    shortSuit = unicodeDictionary[shortSuitLetter]
                    hardValue = BlackjackDeck.hardValues[shortName]
                    softValue = BlackjackDeck.softValues[shortName]
                    card = Card(hardValue, softValue, name, shortName, suit, shortSuit)
                    self._cards.append(card)
                except:
                    raise ValueError(f"'{shortName}{shortSuit}' does not correspond to a known card.")
