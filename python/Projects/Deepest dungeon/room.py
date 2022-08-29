# room.py

class Room():

    def __init__(self, room_name):
        # initilise room object 
        self.name = room_name.lower()
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def describe(self):
        # Display a description og the room in the UI.
        print(f"\nYou are in the {self.name}.")
        print(self.description)
        if self.character is not None:
            self.character.describe()
        if self.item is not None:
            self.item.describe()
        for direction in self.linked_rooms:
            print(f"To the {direction} is the {self.linked_rooms[direction].name}")

    def link_rooms(self, room_to_link, direction):
        # links the provided room in the provided direction
        self.linked_rooms[direction.lower()] = room_to_link

    def move(self, direction):
        # returns the room linked in the given direction
        if direction in self.linked_rooms.keys():
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self