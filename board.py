
class Board:

    def __init__(self, players, cards, nobles):
        self.players = players
        if len(nobles) != players + 1:
            return Exception("Incorrect number of nobles for the game: " + len(nobles) + " \t The proper amount should be " + str(players + 1))

        if len(cards) > 12:
            return Exception("Incorrect number of cards for the game: " + len(cards))

        self.grid = []
        for c in cards:
            row = c.decknum
            if len(self.grid[row]) > 4:
                return Exception("There were too many cards from the same deck " + str(row))
            self.grid[row].append(c)

