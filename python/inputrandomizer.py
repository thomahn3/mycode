import random
print("Put in your favorite games below ! :)")

game1 = input("1.")
game2 =input("2.")
game3 = input("3.")

print("Randomizing...")

mylist = [game1, game2, game3]

print(random.choice(mylist))