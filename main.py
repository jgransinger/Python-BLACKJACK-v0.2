import random
from art import logo

def deal_cards():
    for card in range(2):
        player_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))

    print(f"Your cards: {player_cards}, total: {sum(player_cards)}")
    print(f"Dealer's first card: {dealer_cards[0]}")
    if sum(player_cards) == 21:
        calculate_winner()
    hit_or_stay()

def hit_or_stay():
    choice = input("Would like to draw another card?: y/n : \n")
    if choice == "y":
        player_cards.append(random.choice(cards))
        print(f"Your cards: {player_cards}, total: {sum(player_cards)}")
        if sum(player_cards) < 21:
            hit_or_stay()
        else:
            calculate_winner()
    elif choice == "n":
        dealer_turn()
    else:
        print("Please enter a valid selection.")

def calculate_winner():
    print("*********** RESULT **************") #Bug here : this prints when Aces are turned to one. it shouldn't
    if sum(player_cards) == 21:
        print(f"BLACKJACK : Player total: {sum(player_cards)} || Dealer total: {sum(dealer_cards)}")
    elif sum(dealer_cards) == 21:
        print(f"Dealer BLACKJACK : Player total: {sum(player_cards)} || Dealer total: {sum(dealer_cards)} ")
    elif sum(player_cards) > 21 and 11 in player_cards:
        ace_swap()
        hit_or_stay()
    elif sum(dealer_cards) > 21 and 11 in dealer_cards:
        ace_swap()
        dealer_turn()
    elif sum(player_cards) > 21 and 11 not in player_cards:
        print(f"BUST : Player total: {sum(player_cards)} || Dealer total: {sum(dealer_cards)}")
    elif sum(dealer_cards) > 21 and 11 not in dealer_cards:
        print(f"DEALER BUST. You WIN. : Player total: {sum(player_cards)} || Dealer total: {sum(dealer_cards)}")
    elif sum(player_cards) > sum(dealer_cards):
        print(f"WINNER : Player total: {sum(player_cards)} || Dealer total: {sum(dealer_cards)}")
    elif sum(player_cards) < sum(dealer_cards):
        print(f"You lose! : Player total: {sum(player_cards)} || Dealer total: {sum(dealer_cards)}")
    elif sum(player_cards) == sum(dealer_cards):
        print(f"It's a DRAW! : Player total: {sum(player_cards)} || Dealer total: {sum(dealer_cards)}")
    print("*********************************** \n")
    play_again()

def ace_swap():
    for each_card in player_cards:
        if each_card == 11 and sum(player_cards) > 21:
            player_cards.remove(each_card)
            player_cards.append(1)
            print(f"Ace card is now a 1, new total: {sum(player_cards)}")
    for each_card in dealer_cards:
        if each_card == 11 and sum(dealer_cards) > 21:
            dealer_cards.remove(each_card)
            dealer_cards.append(1)
            print(f"Ace card is now a 1, new total: {sum(dealer_cards)}")

def dealer_turn():
    if sum(dealer_cards) < 17:
        dealer_cards.append(random.choice(cards))
        dealer_turn()
    elif sum(dealer_cards) >= 17 or sum(dealer_cards) == 21:
        print(f"Dealers cards: {dealer_cards}")
        calculate_winner()

def play_again():
    again = input("Do you want to play again? y/n : ")
    if again == "y":
        print(logo)
        player_cards.clear()
        dealer_cards.clear()
        deal_cards()
    elif again == "n":
        print("Game has ended.")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []

print(logo + "\n")
start_game = input("Do you want to play blackjack?: y/n : \n")
if start_game == "y":
    deal_cards()
else:
    print("Goodbye.")

