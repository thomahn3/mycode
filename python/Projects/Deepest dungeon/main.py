#main.py

from room import Room
from character import Character

# create rooms
cavern = Room("Cavern")
cavern.description = "A room so big that the light of your torch doesn't reach the walls."

armoury = Room("Armoury")
armoury.description = "The walls are lined with racks that once held weapons and armour!"

lab = Room("lab")
lab.description = "A strange odour hangs in a room filled with unknowable contraptions."

throne_room = Room("Throne Room")
throne_room.description = "The room is empty except for a throne and a mysterious character!"


cavern.link_rooms(armoury, "south")
armoury.link_rooms(cavern, "north")
armoury.link_rooms(lab, "east")
armoury.link_rooms(throne_room, 'south')
lab.link_rooms(armoury, "west")
throne_room.link_rooms(armoury, "north")

# Create chracters
ugine = Character('Ugine')
ugine.description = 'a huge troll with rotting teeth'

nigel = Character('Nigel')
nigel.description = "a burly dwarf with golden beads woven through his beard"
nigel.conversation = "Well youngan, what are you doing here?"

skeleton_king = Character('Skelton King')
skeleton_king.description = 'he looms over you with red glowing eyes!'
skeleton_king.conversation = 'Run before I change my mind about you!'

# add character to rooms
armoury.character = ugine
lab.character = nigel
throne_room.character = skeleton_king

#Init variables
current_room = cavern
running  = True
# ----- MAIN LOOP ----- #
while running:
    current_room.describe()

    command = input("You: > ").lower()

    if command in ["north",'south','east','west']:
        current_room = current_room.move(command)

    elif command == "talk":
        if current_room.character is not None:
            current_room.character.talk()
        else:
            print("There is none here to talk to.")

    elif command == "hug":
        if current_room.character is not None:
            current_room.character.hug()
        else:
            print("There is no one here to hug.")
    
    elif command == "fight":
        if current_room.character is not None:
            current_room.character.fight()
        else:
            print("There is no one to fight.")
    elif command == 'quit':
        running = False
    else:
        print("I don't understand!")
        