import random   ## Importing random module
import time ## Importing time module

money = 5000    ## Initializing money variable
win = 0
lose = 0
dtext = '\033[0m'
greentext = '\033[32m'
whitetext = '\033[37m'
redtext = '\033[31m'

while True: ## Main loop to keep the game running over and over again
    stop = " " ## Initializing stop variable
    dice1 = [1, 2, 3, 4, 5, 6] ## Initializing dice numbers
    dice2 = [1, 2, 3, 4, 5, 6] 
    even = [2, 4, 6, 8, 10, 12] ## Initializing even numbers
    odd = [1, 3, 5, 7, 9, 11] ## Initializing odd numbers
    
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
        time.sleep(1) ## Sleeping for 1 second
        print("Rolling the dice...") ## Printing message to user
        time.sleep(3) ## Sleeping for 3 seconds
        while True: ## loop so when someone wants to play again they can 
            if stop == "y":
                break ## Breaking out of loop so they can exit the program
            choice = str(input("Is the sum Cho (Even) or Han (odd)?").lower()) ## Asking user to input their choice
                
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
                            exit()
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
                            exit()
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
                            exit()
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
                            exit() ## Exiting the program
                        else: ## If user inputs anything other than y or n
                            print("Please enter a valid response") ## Printing error message
                            continue ## Continuing to the beginning of the loop
            else: ## If user inputs anything other than even or odd
                print("Please enter a valid response") ## Printing error message
                continue ## Continuing to the beginning of the loop