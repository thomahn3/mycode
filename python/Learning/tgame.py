while True:
    answer = input("Would you like to play? (yes/no): ").lower().strip()

    if answer == "yes":
        answer = input("You reach a T section do you want to go left or right?: ").lower().strip()
        
        if answer == "left":
            answer = input("You encounter a dragon do you want to fight or run?: ").lower().strip()
            
            if answer == "fight":
                print("You really thought you were gonna beat a dragon stupid?")
                print("YOU LOSE")

            else:
                print("Good choice you got away safely")

        elif answer == "right":
            answer = input("You walk forever not seeing the end of the road until a dwarf offers you some pills do you choose the left or right pill?: ").lower().strip()
            
            if answer == "right":
                print("You just took cyanide")
                print("YOU LOSE") 

            else:
                print("You take the left pill but it was a narcotic you wake up in a stomach of some animal")
                print("YOU LOSE")


        else: 
            print("Invalid choice, you lose")

    else:
        print("Thats too bad :(")
        break