import deck as d
#Jordan love big DECKSSSSSS!!!!!!
deck = d.make_deck()
player1 = []
player2 = []
p1l = []
p1l = []

def deal_hands():
    for c in range(26):
        player1.append(deck[0])
        deck.pop(0)
        player2.append(deck[0])
        deck.pop(0)

def get_card_value(card):

    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    num_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    return num_values[values.index(card["value"])]


def war(card1, card2):
    """
    the problem with this function is that the p1l and p2l gets reset
    every time function is called. So we need a way to
    add those lists togather
    """
    p1l = [card1, player1[0], player1[1]]#player1 list
    p2l = [card2, player2[0], player2[1]]

    p1wc = player1[1]#player1 war card
    p1wcv = get_card_value(player1[1])#player1 war card value

    p2wc = player2[1]#player2 war card
    p2wcv = get_card_value(player2[1])#player2 war card value

    player1.pop(0)
    player1.pop(1)

    player2.pop(0)
    player2.pop(1)

    if p1wcv > p2wcv:
        for card in p1l:
            player1.append(card)
        for card in p2l:
            player1.append(card)

    if p1wcv > p2wcv:
        for card in p1l:
            player2.append(card)
        for card in p2l:
            player2.append(card)

    if p1wcv > p2wcv:
        war(p1wc, p2wc)

def play_game():
    #draw a card from each hand
    card1 = player1[0]
    card1_value = get_card_value(player1[0])
    player1.pop(0)
    card2 = player2[0]
    card2_value = get_card_value(player2[0])
    player2.pop(0)

    if card1_value == card2_value:
        #war(card1, card2)
        pass





    if card1_value > card2_value:
        player1.append(card1)
        player1.append(card2)



    if card1_value < card2_value:
        player2.append(card1)
        player2.append(card2)


    #what ever card is bigger, than that card, than that card goes to the bottom
    #if both cards match than we go to war
    #war is each player draws 2 cards, the last cards are compared amd winner gets all, repeat as necessary
    #game is over when one player has all 52 cards
def main():

    d.shuffle_deck(deck)
    deal_hands()
    play_game()

if __name__ == "__main__":
    main()
