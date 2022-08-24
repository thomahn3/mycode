import os
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

# initialize scores
wins = 0
losses = 0

# play the game
def game():
    global deck
    global wins
    global losses
    clear()
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print("\nDealer: {} and [Hidden]".format(dealer_hand[0]))
    print("\nPlayer: {} and {}".format(player_hand[0], player_hand[1]))
    while True:
        player_total = total(player_hand)
        if player_total == 21:
            print("\nPlayer has 21! You win!")
            wins += 1
            break
        elif player_total > 21:
            print("\nPlayer has busted at {}! You lose!".format(player_total))
            losses += 1
            break
        else:
            hit_or_stand(player_hand, player_total)

# hit or stand
def hit_or_stand(player_hand, player_total):
    global deck
    global wins
    global losses
    while True:
        x = input("\nWould you like to Hit or Stand? (H/S) : ").lower()
        if x == "h":
            player_hand = hit(player_hand)
            player_total = total(player_hand)
            print("\nPlayer: {} and {}".format(player_hand[0], player_hand[1]))
            if player_total == 21:
                print("\nPlayer has 21! You win!")
                wins += 1
                break
            elif player_total > 21:
                print("\nPlayer has busted at {}! You lose!".format(player_total))
                losses += 1
                break
        elif x == "s":
            print("\nPlayer stands at {}".format(player_total))
            break
        else:
            print("\nPlease enter H or S")
            continue
    dealer_total = total(dealer_hand)
    print("\nDealer: {} and {}".format(dealer_hand[0], dealer_hand[1]))
    while dealer_total < 17:
        dealer_hand = hit(dealer_hand)
        dealer_total = total(dealer_hand)
        print("\nDealer: {} and {}".format(dealer_hand[0], dealer_hand[1]))
    if dealer_total > 21:
        print("\nDealer has busted at {}! You win!".format(dealer_total))
        wins += 1
    elif dealer_total > player_total:
        print("\nDealer has {}! You lose!".format(dealer_total))
        losses += 1
    elif dealer_total < player_total:
        print("\nDealer has {}! You win!".format(dealer_total))
        wins += 1
    else:
        print("\nDealer has {}! It's a tie!".format(dealer_total))
    play_again()

# hit
def hit(hand):
    global deck
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand

# total
def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += card
    return total

# play again
def play_again():
    global wins
    global losses
    while True:
        x = input("\nWould you like to play again? (Y/N) : ").lower()
        if x == "y":
            game()
        elif x == "n":
            print("\nThanks for playing!")
            print("\nWins: {}".format(wins))
            print("\nLosses: {}".format(losses))
            break
        else:
            print("\nPlease enter Y or N")
            continue

# clear
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# main
def main():
    game()
