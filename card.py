class Card:

    def __init__(self, gem, points, requirements):
        self.gem = gem
        self.points = points
        self.requirements = requirements

    def __str__(self):
        return "Points = " + self.points + " \t| Gem = " + self.gem

    