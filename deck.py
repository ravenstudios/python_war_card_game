import random


suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]



def make_deck():
    deck = []
    for s in suits:
        for v in values:
            deck.append({"suit": s, "value": v})

    return deck

def shuffle_deck(deck):
    d = deck
    random.shuffle(d)
    return d
