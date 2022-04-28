class Player(object):

    def __init__(self, name, money):
        self._name = name
        self._hands = []
        self._money = money

    def __str__(self):
        string = f'Name: {self._name}\nMoney: {self._money}\n'
        for hand in self._hands:
            string += f'{hand}'
        return string

    def add_hand(self, hand):
        """Adds a hand to self._hands."""
        self._hands.append(hand)

    def play(self, hand):
        """Returns a players move (either hit, stand, double, or split)."""
        commandString = '[H]it      [S]tand     [D]ouble        s[P]lit\n'
        validCommands = 'HSDP'
        command = None
        if hand.isDone:
            print('Hand cannot be played.')
        else:
            print(commandString)
            print(hand)
            prompt = f"Your move {self._name}: "
            command = input(prompt).upper()
            while command not in validCommands:
                prompt += '(type the corresponding letter) '
                command = input(prompt).upper()
        return command

    def get_hands(self):
        return self._hands

    def get_name(self):
        return self._name

    def get_money(self):
        return self._money

    def set_money(self, money):
        self._money = money

    money = property(get_money, set_money)
    name = property(get_name)
    hands = property(get_hands)
