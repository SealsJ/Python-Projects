import random
playerIn = True
dealerIn = True

# deck of cards / player dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A',]
player = []
dealer = []

# deal the cards function
def dealCards(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# take the dealer / player hands and calculate the total of each hand
def total(turn):
    total = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 1
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total

# logic that can figure out if player or dealer won
def dealerHand():
    if len(dealer) == 2:
        return dealer[0]
    elif len(dealer) > 2:
        return dealer[0], dealer[1]

# game loop
for _ in range(2):
    dealCards(dealer)
    dealCards(player)

while playerIn or dealerIn:
    print(f"Dealer had {dealerHand} and X")
    print(f"You have {player} for a total of {total(player)}")
    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if total(dealer) > 16:
        dealerIn = False
    else:
        dealCards(dealer)
    if stayOrHit == '1':
        playerIn = False
    else: 
        dealCards(player)
    if total(player) >= 21:
        break
    elif total(dealer) >= 21:
        break

#Code if dealer gets blackjack
if total(player) == 21:
    print(f"\nYou Have {player} for a total of total{(player)} and the dealer has {dealer} for a total of {total(dealer)}")
    print("Blackjack! Congrats!")
elif total(dealer) == 21:
    print(f"\nYou Have {player} for a total of total{(player)} and the dealer has {dealer} for a total of {total(dealer)}")
    print("Blackjack! Dealer wins!")
elif total(player) > 21:
    print(f"\nYou Have {player} for a total of total{(player)} and the dealer has {dealer} for a total of {total(dealer)}")
    print("You bust! Dealer wins!")
elif total(dealer) > 21:
    print(f"\nYou Have {player} for a total of total{(player)} and the dealer has {dealer} for a total of {total(dealer)}")
    print("Dealer busts! You Win!")
elif 21 - total(dealer) < 21 - total(player):
    print(f"\nYou Have {player} for a total of total{(player)} and the dealer has {dealer} for a total of {total(dealer)}")
    print("Dealer wins!")
elif 21 - total(dealer) > 21 - total(player):
    print(f"\nYou Have {player} for a total of total{(player)} and the dealer has {dealer} for a total of {total(dealer)}")
    print("You win!")





