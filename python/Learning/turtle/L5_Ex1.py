# Alfred's security guard program

#####################################################
## Write a program that asks for a person's name   ##
## and then grants entry of that person is Alfred ##
## everyone else is told, politely, to go away     ##
#####################################################

name = input("What is your name? ").lower()

if name == "alfred":
    print("Welcome, Alfred.")
else:
    print("You are not Alfred. Please leave.")