import random
import time
import os 
## Casino Game
## games available: blackjack, roulette, slots, dice

#initilize variables
dtext = '\033[0m'
blueboldtext = '\033[1;36m'
greentext = '\033[32m'
whitetext = '\033[37m'
redtext = '\033[31m'
win = 0
lose = 0
money = 10000

while True:
    stop = " "
    
    print(blueboldtext+"Welcome to the Grand Casino!"+dtext)
    time.sleep(0.5)
    print("Welcome to my casino, where you can play games and earn money! Try your luck and see if you can beat the house!")
    time.sleep(0.5)
    gameselection = input("What "+whitetext+"GAME "+dtext+ "would you like to play? (Blackjack, Roulette, Slots, Dice, Wheel of Fortune): ").lower()
    #dice start
    if gameselection == "blackjack":
        while True: 
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

            # initialize scores
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

            def play_again():
                again = input("Do you want to play again? (Y/N): ").lower()
                if again == "y":
                    dealer_hand = []
                    player_hand = []
                    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
                    game()
                else:
                    print("Bye!")
                    break

            def total(hand):
                total = 0
                for card in hand:
                    if card == "J" or card == "Q" or card == "K":
                        total+= 10
                    elif card == "A":
                        if total >= 11: total+= 1
                        else: total+= 11
                    else: total += card
                return total

            def hit(hand):
                card = deck.pop()
                if card == 11:card = "J"
                if card == 12:card = "Q"
                if card == 13:card = "K"
                if card == 14:card = "A"
                hand.append(card)
                return hand

            def print_results(dealer_hand, player_hand):
               
                print("\n    WELCOME TO BLACKJACK!\n")
                print("-"*30+"\n")
                print("    \033[1;32;40mwin:  \033[1;37;40m%s   \033[1;31;40mlose:  \033[1;37;40m%s\n" % (win, lose))
                print("-"*30+"\n")
                print ("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
                print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

            def blackjack(dealer_hand, player_hand):
                global win
                global lose
                global money
                if total(player_hand) == 21:
                    print_results(dealer_hand, player_hand)
                    print ("Congratulations! You got a Blackjack!\n")
                    win += 1
                    play_again()
                elif total(dealer_hand) == 21:
                    print_results(dealer_hand, player_hand)
                    print ("Sorry, you lose. The dealer got a blackjack.\n")
                    lose += 1
                    play_again()

            def score(dealer_hand, player_hand):
                    # score function now updates to global win/loss variables
                    global win
                    global lose
                    global money
                    if total(player_hand) == 21:
                        print_results(dealer_hand, player_hand)
                        print ("Congratulations! You got a Blackjack!\n")
                        win += 1
                    elif total(dealer_hand) == 21:
                        print_results(dealer_hand, player_hand)
                        print ("Sorry, you lose. The dealer got a blackjack.\n")
                        lose += 1
                    elif total(player_hand) > 21:
                        print_results(dealer_hand, player_hand)
                        print ("Sorry. You busted. You lose.\n")
                        lose += 1
                    elif total(dealer_hand) > 21:
                        print_results(dealer_hand, player_hand)
                        print ("Dealer busts. You win!\n")
                        win += 1
                    elif total(player_hand) < total(dealer_hand):
                        print_results(dealer_hand, player_hand)
                        print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
                        lose += 1
                    elif total(player_hand) > total(dealer_hand):
                        print_results(dealer_hand, player_hand)
                        money += bet
                        print ("Congratulations. Your score is higher than the dealer. You win You now have "+str(money)+".\n")
                        win += 1

            def game():
                global win
                global lose
                global money
                choice = 0
                print("\n    WELCOME TO BLACKJACK!\n")
                print("-"*30+"\n")
                print("\033[1;42m WIN:" + str(win) + " \033[0;0m \033[1;41m LOSE:" + str(lose) + " \033[0;0m") ## Printing win and lose variables    
                print("-"*30+"\n")
                dealer_hand = deal(deck)
                player_hand = deal(deck)
                print ("The dealer is showing a " + str(dealer_hand[0]))
                print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
                blackjack(dealer_hand, player_hand)
                quit=False
                while not quit:
                    choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
                    if choice == 'h':
                        hit(player_hand)
                        print(player_hand)
                        print("Hand total: " + str(total(player_hand)))
                        if total(player_hand)>21:
                            print('You busted')
                            lose += 1
                            money -= bet
                            play_again()
                    elif choice=='s':
                        while total(dealer_hand)<17:
                            hit(dealer_hand)
                            print(dealer_hand)
                            if total(dealer_hand)>21:
                                money += bet
                                print('Dealer busts, you win! You now have '+str(money)+'.')
                                
                                win += 1
                                play_again()
                        score(dealer_hand,player_hand)
                        play_again()
                    elif choice == "q":
                        print("Bye!")
                        quit=True
                        break


            if __name__ == "__main__":
                while True:
                    try: ## Trying to execute the following code
                        bet = int(input("\n You have \033[0;32m$"+ str(money) +"\033[0;0m. How much would you like to bet?")) ## Asking user to input bet

                    except: ## If user inputs anything other than a number
                        print("Please enter a number") ## Printing error message
                        continue ## Continuing to the beginning of the loop
                    
                    if bet > money: ## If bet is greater than money
                        print("You don't have that much money.") ## Printing error message
                        continue ## Continuing to the beginning of the loop
                    
                    elif bet <= 0: ## If bet is less than or equal to 0
                            print("Please enter a number greater than 0") ## Printing error message
                            continue ## Continuing to the beginning of the loop
                        
                    else: ## If bet is greater than 0 and less than or equal to money
                        print ("You bet \033[0;32m$" + str(bet)+ "\033[0;0m. You now have \033[0;32m$" + str(money - bet) + "\033[0;0m.") ## Printing message to user confirming their bet
                        break
                game()
                break

    if gameselection == "roulette":
        print("roulette")

    if gameselection == "slots":
        print("slots")


    if gameselection == "dice":
        while True: ## Main loop to keep the game running over and over again
            if stop == "n":
                break ## Initializing stop variable
            stop = " "
            dice1 = [1, 2, 3, 4, 5, 6] ## Initializing dice numbers
            dice2 = [1, 2, 3, 4, 5, 6] 
            even = [2, 4, 6, 8, 10, 12] ## Initializing even numbers
            odd = [1, 3, 5, 7, 9, 11] ## Initializing odd numbers
            bet = 0

            def roll_dice(): ## Defining roll_dice function
                global dice1 ## Globalizing dice1 variable
                global dice2 ## Globalizing dice2 variable
                dice1 = random.choice(dice1) ## Assigning random choice from dice1 list to dice1 variable
                dice2 = random.choice(dice2) ## Assigning random choice from dice2 list to dice2 variable
                return dice1, dice2 ## Returning dice1 and dice2
    
            def roll_dice_sum(dice1, dice2): ## Defining roll_dice_sum function
                dice_sum = dice1 + dice2 ## Assigning sum of dice1 and dice2 to dice_sum variable
                return dice_sum ## Returning dice_sum
    
            def roll_dice_sum_even(dice_sum): ## Defining roll_dice_sum_even function
                if dice_sum in even: ## Checking if dice_sum is in even list
                    return True ## Returning True
                else: ## If dice_sum is not in even list
                    return False ## Returning False
    
            def roll_dice_sum_odd(dice_sum): ## Defining roll_dice_sum_odd function
                if dice_sum in odd: ## Checking if dice_sum is in odd list
                    return True ## Returning True
                else: ## If dice_sum is not in odd list
                    return False ## Returning False
    
            print("\033[1;42m WIN:" + str(win) + " \033[0;0m \033[1;41m LOSE:" + str(lose) + " \033[0;0m") ## Printing win and lose variables    
            try: ## Trying to execute the following code
                bet = int(input("\n You have "+greentext+str(money)+dtext+". How much would you like to bet?")) ## Asking user to input bet
    
            except: ## If user inputs anything other than a number
                print("Please enter a number") ## Printing error message
                continue ## Continuing to the beginning of the loop
            
            if bet > money: ## If bet is greater than money
                print("You don't have that much money.") ## Printing error message
                continue ## Continuing to the beginning of the loop
            
            elif bet <= 0: ## If bet is less than or equal to 0
                    print("Please enter a number greater than 0") ## Printing error message
                    continue ## Continuing to the beginning of the loop
                
            else: ## If bet is greater than 0 and less than or equal to money
                print("You bet \033[0;32m$" + str(bet)+ "\033[0;0m. You now have \033[0;32m$" + str(money - bet) + "\033[0;0m.") ## Printing message to user confirming their bet
                time.sleep(1) ## Sleeping for 1 second
                print("Rolling the dice...") ## Printing message to user
                time.sleep(3) ## Sleeping for 3 seconds
                while True: ## loop so when someone wants to play again they can 
                    if stop == "y":
                        break 
                    elif stop == "n":
                        break
                    choice = str(input("Is the sum Even or Odd?").lower()) ## Asking user to input their choice
    
                    if choice == "even" or choice == "cho": ## If user inputs even or cho
                        dice1, dice2 = roll_dice() ## Calling roll_dice function
                        dice_sum = roll_dice_sum(dice1, dice2) ## Calling roll_dice_sum function
                        if roll_dice_sum_even(dice_sum): ## Calling roll_dice_sum_even function
                            print("\033[1;37;42m WIN \033[0;0m") ## Printing message to user
                            print("You rolled a "+str(dice1)+" and a "+str(dice2)+" which is "+str(dice_sum)+". Thats even so you win!") ## Printing message to user
                            win += 1 ## Adding 1 to win variable
                            money = money + (bet*0.9) ## Adding bet to money
                            print("You now have \033[0;32m$" + str(money) + "\033[0;0m. House gets \033[0;31m$" +str(bet*0.1)+"\033[0;0m.") ## Printing message to user
                            while True: ## loops until user inputs y or n
                                try: ## Trying to execute the following code
                                    stop = str(input("Do you want to play again "+greentext+"y " +dtext+ "or "+redtext+"n"+dtext+"?").lower()) ## Asking user to input y or n
                                except:
                                    print("Please enter a valid response")
                                    continue
                                if stop == "y":
                                    break
                                elif stop == "n":
                                    print("Thanks for playing!")
                                    break
                                else:
                                    print("Please enter a valid response")
                                    continue
                        else:
                            print("\033[1;37;41m LOSE \033[0;0m") ## Printing message to user
                            print("You rolled a "+str(dice1)+" and a "+str(dice2)+" which is "+str(dice_sum)+". Thats odd so you lose!")
                            lose += 1 ## Adding 1 to lose variable
                            money -= bet
                            print("You now have \033[0;32m$" + str(money) + "\033[0;0m.")
                            if money <= 0:
                                print("You have no money left. You lose.")
                                print("\033[1;42m WIN:" + str(win) + " \033[0;0m \033[1;41m LOSE:" + str(lose) + " \033[0;0m") ## Printing win and lose variables 
                                exit()
                            while True:
                                try:
                                     stop = str(input("Do you want to play again "+greentext+"y " +dtext+ "or "+redtext+"n"+dtext+"?").lower())
                                except:
                                    print("Please enter a valid response")
                                    continue
                                if stop == "y":
                                    break
                                elif stop == "n":
                                    print("Thanks for playing!")
                                    break
                                else:
                                    print("Please enter a valid response")
                                    continue
                                
                    elif choice == "odd" or choice == "han":
                        dice1, dice2 = roll_dice()
                        dice_sum = roll_dice_sum(dice1, dice2)
                        if roll_dice_sum_odd(dice_sum):
                            print("\033[1;37;42m WIN \033[0;0m") ## Printing message to user
                            print("You rolled a "+str(dice1)+" and a "+str(dice2)+" which is "+str(dice_sum)+". Thats odd so you win!") ## Printing message to user 
                            win += 1 ## Adding 1 to win variable
                            money = money + (bet*0.9) ## Adding bet to money
                            print("You now have \033[0;32m$" + str(money) + "\033[0;0m. House gets \033[0;31m$" +str(bet*0.1)+"\033[0;0m.") ## Printing message to user
                            while True: ## loops until user inputs y or n
                                try: ## Trying to execute the following code
                                     stop = str(input("Do you want to play again "+greentext+"y " +dtext+ "or "+redtext+"n"+dtext+"?").lower()) ## Asking user to input y or n
                                except: ## If user inputs anything other than a string
                                    print("Please enter a valid response") ## Printing error message
                                    continue ## Continuing to the beginning of the loop
                                if stop == "y":
                                    break
                                elif stop == "n":
                                    print("Thanks for playing!")
                                    break
                                else:
                                    print("Please enter a valid response")
                                    continue 
                        else: 
                            print("\033[1;37;41m LOSE \033[0;0m") ## ODD LOSE
                            print("You rolled a "+str(dice1)+" and a "+str(dice2)+" which is "+str(dice_sum)+". Thats evens so you lose!") 
                            lose += 1 ## Adding 1 to lose variable
                            money -= bet ## Subtracting bet from money
                            print("You now have \033[0;32m$" + str(money) + "\033[0;0m.") ## Printing message to user
                            if money <= 0: ## If money is less than or equal to 0
                                print("You have no money left. You lose.") ## Printing message to user
                                print("\033[1;42m WIN:" + str(win) + " \033[0;0m \033[1;41m LOSE:" + str(lose) + " \033[0;0m") ## Printing win and lose variables 
                                exit() 
                            while True: ## loops until user inputs y or n
                                try: ## Trying to execute the following code
                                     stop = str(input("Do you want to play again "+greentext+"y " +dtext+ "or "+redtext+"n"+dtext+"?").lower()) ## Asking user to input y or n
                                except: ## If user inputs anything other than a number
                                    print("Please enter a valid response") ## Printing error message
                                    continue ## Breaking out of to reanswer the above question
                                if stop == "y":
                                    break ## Breaking out of loop so they can exit the program
                                elif stop == "n": ## If user inputs n
                                    print("Thanks for playing!") ## Printing message to user
                                    break ## Exiting the program
                                else: ## If user inputs anything other than y or n
                                    print("Please enter a valid response") ## Printing error message
                                    continue ## Continuing to the beginning of the loop
                    else: ## If user inputs anything other than even or odd
                        print("Please enter a valid response") ## Printing error message
                        continue ## Continuing to the beginning of the loop            
    
    if gameselection == "wheel of fortune":
        while True:
            if stop == "n":
                break
            print("\nYou have a 50% of winning which then a random multiplier between 2 and 10 will be selected. ")
            time.sleep(3)
            print("\033[1;42m WIN:" + str(win) + " \033[0;0m \033[1;41m LOSE:" + str(lose) + " \033[0;0m") ## Printing win and lose variables    
            try: ## Trying to execute the following code
                bet = int(input("\n You have "+greentext+ "$"+str(money) +dtext+". How much would you like to bet?")) ## Asking user to input bet
                
            except: ## If user inputs anything other than a number
                print("Please enter a number") ## Printing error message
                continue ## Continuing to the beginning of the loop
            
            if bet > money: ## If bet is greater than money
                print("You don't have that much money.") ## Printing error message
                continue ## Continuing to the beginning of the loop
            
            elif bet <= 0: ## If bet is less than or equal to 0
                    print("Please enter a number greater than 0") ## Printing error message
                    continue ## Continuing to the beginning of the loop

            else:
                print ("You bet "+greentext+"$"+ str(bet)+ dtext+". You now have "+greentext+"$"+ str(money - bet) +dtext) ## Printing message to user confirming their bet
                time.sleep(1)
                print("\n Wheel is spinning...")
                time.sleep(1.5)
                winlossdecider = random.randint(1,2)
                multiplier = random.randint(2,10)
                if winlossdecider < 2:
                    lose += 1
                    money -= bet
                    print("\n You lost! You now have "+greentext+"$"+ str(money) +dtext+".")
                    if money <= 0:
                                print("You have no money left. You lose.")
                                print("\033[1;42m WIN:" + str(win) + " \033[0;0m \033[1;41m LOSE:" + str(lose) + " \033[0;0m") ## Printing win and lose variables 
                                exit()
                    while True: ## loops until user inputs y or n
                        try: ## Trying to execute the following code
                            stop = str(input("Do you want to play again "+greentext+"y " +dtext+ "or "+redtext+"n"+dtext+"?").lower()) ## Asking user to input y or n
                        except:
                            print("Please enter a valid response")
                            continue
                        if stop == "y":
                            break
                        elif stop == "n":
                            print("Thanks for playing!")
                            break
                        else:
                            print("Please enter a valid response")
                            continue

                elif winlossdecider == 2:
                    win += 1
                    money = money+bet*multiplier
                    print("\n You have won "+greentext+ "$"+str(bet*multiplier)+dtext+"! You got a multiplier of x"+str(multiplier)+" You now have "+greentext+"$"+str(money)+dtext+".") ## Printing message to user confirming their bet
                    while True: ## loops until user inputs y or n
                        try: ## Trying to execute the following code
                            stop = str(input("Do you want to play again "+greentext+"y " +dtext+ "or "+redtext+"n"+dtext+"?").lower()) ## Asking user to input y or n
                        except:
                            print("Please enter a valid response")
                            continue
                        if stop == "y":
                            break
                        elif stop == "n":
                            print("Thanks for playing!")
                            break
                        else:
                            print("Please enter a valid response")
                            continue

                
               