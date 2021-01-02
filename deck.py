import numpy as np


class Deck:
    def __init__(self, cards):
        self.cards = cards
        print(cards)

    def nextCard(self):
        return self.__pop()

    def __pop(self):
        c = self.cards[-1]
        print(c)
        print("card taken out = " + c)
        self.cards.pop(-1)
        return c