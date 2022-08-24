class Character():

    def __init__(self,name):
        # initialises the character object
        self.name = name
        self.description = None
        self.conversation = None

    def describe(self):
        # sends a description of the character to the terminal
        print(f'{self.name} is here, {self.description}')

    def hug(self):
        # the character response to a hug
        print(f"{self.name} doesnt want to hug you.")
    
    def fight(self):
        # the character responds to a threat
        print(f"{self.name} doesn't want to fight you.")

    def talk(self):
        # the character responds to a conversation
        if self.conversation is not None:
            print(f"{self.name}: > {self.conversation}")
        else:
            print("The character doesn't want to talk to you.")