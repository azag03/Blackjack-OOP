# from table import Table
from card import Card
from blackjack import Blackjack


def main():
    table = Table()
    table.manage()


def card_test():
    print('-----Card Test-----')
    card = Card(1, 11, 'Ace', 'Diamonds')
    print(card.visibility)
    print(card)
    card.flip()
    print(card.visibility)
    print(card)


def deck_test():
    """
    print('-----Deck Test-----')
    deck = Blackjack()
    deck.create_deck()
    print(len(deck.cards))
    print(deck)

    print('-----Shuffle Test-----')
    deck2 = Blackjack()
    deck2.create_deck()
    deck2.shuffle()
    print(deck2)

    print('-----Pop Test-----')
    deck3 = Blackjack()
    deck3.create_deck()
    deck3.pop()
    deck3.pop()
    print(len(deck3.cards))

    print('-----Size Test-----')
    deck4 = Blackjack('Blackjack', 2)
    deck4.create_deck()
    print(len(deck4.cards))
    print(deck4)
    """
    print('-----Stack Test-----')
    deck5 = Blackjack('Blackjack', 1)
    deck5.stack()
    print(deck5)

deck_test()