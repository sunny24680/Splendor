import pandas as pd
import card
import gems

deck_file = "Deck.xlsx"

def getGem(str):
    for name, gem in gems.Gems.__members__.items():
        if str.upper() == name:
            return gem

def convertDeck(deck):
    newDeck = []
    for index, row in deck.iterrows():
        gem = getGem(row['Card Color'])
        print(row[3:])
        c = 4
        req = []
        for requirement in row[3:]:
            res = (requirement, getGem(deck.columns[c]))
            req.append(res)
        c = card.Card(gem, row['Points'], req)
        newDeck.append(c)
    return newDeck


def loadDeck():
    df = pd.read_excel(deck_file)
    df = df.dropna(axis=0)
    decks = [df[df["Deck"] == 1], df[df["Deck"] == 2], df[df["Deck"] == 3]]
    res = []
    print(decks)
    for deck in decks:
        res.append(convertDeck(deck))
    return res

print(loadDeck())