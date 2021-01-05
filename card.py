class Card:

    def __init__(self, gem, points, requirements, decknum=None):
        self.gem = gem
        self.points = points
        self.requirements = requirements
        self.decknum = decknum

    def __str__(self):
        return "Points = " + self.points + " \t| Gem = " + self.gem
