import deck as d

deck = d.make_deck()
player1 = []
player2 = []

def deal_hands():
    for c in range(26):
        player1.append(deck[0])
        deck.pop(0)
        player2.append(deck[0])
        deck.pop(0)



def main():

    d.shuffle_deck(deck)
    deal_hands()
    print(len(deck), len(player1), len(player2))
if __name__ == "__main__":
    main()
