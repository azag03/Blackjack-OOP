# from table import Table
from card import Card
from blackjackDeck import BlackjackDeck
from hand import Hand
from callError import CallError


# def main():
# table = Table()
# table.manage()


def card_test():
    print('-----Card Test-----')
    card = Card(1, 11, 'Ace', 'A', 'Diamonds', 'D')
    print(card.visibility)
    print(card)
    card.flip()
    print(card.visibility)
    print(card)


def deck_test():
    print('-----Deck Test-----')
    deck = BlackjackDeck()
    deck.create_deck()
    deck.flip()
    print(len(deck.cards))
    print(deck)

    print('-----Shuffle Test-----')
    deck2 = BlackjackDeck()
    deck2.create_deck()
    deck2.shuffle()
    print(deck2)

    print('-----Pop Test-----')
    deck3 = BlackjackDeck()
    deck3.create_deck()
    deck3.pop()
    deck3.pop()
    print(len(deck3.cards))

    print('-----Size Test-----')
    deck4 = BlackjackDeck('Blackjack', 2)
    deck4.create_deck()
    print(len(deck4.cards))
    print(deck4)


def hand_test():
    d = BlackjackDeck()
    d.create_deck()
    h = Hand(10)
    h.isVerbose = True
    print(h)
    c = d.pop()
    c.flip()
    print(c)
    if h.can_hit():
        h.hit(c)
        print(h)
    c = d.pop()
    c.flip()
    print(c)
    if h.can_hit():
        h.hit(c)
        print(h)
    print('Can double:', h.can_double())
    print('Can hit:', h.can_hit())
    print('Can split:', h.can_split())
    c = d.pop()
    c.flip()
    h.double_down(c, h.bet)
    print(h)
    print(h.is_doubled())
    # should be busted now if first cards are K, Q, J
    print('Is busted:', h.is_busted())
    try:
        c = d.pop()
        c.flip()
        h.hit(c)
    except CallError:
        print("Tried and failed to hit a busted hand.")


hand_test()
