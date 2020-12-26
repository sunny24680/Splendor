import numpy as np

class Deck:

    def __init__(self, cards):
        self.cards = np.array(cards)

    def nextCard(self):
        return cards.pop()