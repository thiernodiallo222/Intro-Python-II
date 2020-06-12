from room import Room
from player import Player
from item import SpecItem

# Declare all the rooms

# def Game():

#Creating instances of item
gun = SpecItem('gun', 'this is a gun for my safety')
knife = SpecItem('Knife', 'This is a knife to enforce my safety')
shoes = SpecItem('Shoes', '''these are adventurer shoes to make sure I am well dressed up and ready''')
bag=SpecItem('Bag', '''this is my bag that contains all the food I need during my adventure''')

    
outside = Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",[gun, knife,shoes, bag])

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [knife,shoes, bag])

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [gun, knife, bag])

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [gun,shoes, bag])

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [gun,knife,shoes])



# Link rooms togethers

outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player("Thierno", outside, [gun, knife,shoes, bag])
# choice = -1
    # REPL <- Read Evaluate Print Loop
print(player)
print("type q to quit")
while True:
        # Read 
    choice = input("please input a direction name (N, S, E or W): ").split()
    if len(choice)==1:
         # Evaluate 
        if (choice == 'q'):
            break
        # choice = int(choice)
        if choice == 'N' or choice == 'n':
            if player.current_room is not None:
                player.current_room = player.current_room.n_to
            else:
                print('Direction not available for this room')
        elif choice == 'S' or choice == 's':
            if player.current_room is not None:
                player.current_room = player.current_room.s_to
            else:
                print('Direction not available for this room')

        elif choice == 'E' or choice == 'e':
            if player.current_room is not None:
                player.current_room = player.current_room.e_to
            else:
                print('Direction not available for this room')

        elif choice == 'S' or choice == 's':
            if player.current_room is not None:
                player.current_room = player.current_room.n_to
            else:
                print('Direction not available for this room')

        elif choice == 'W' or choice == 'w':
            if player.current_room is not None:
                player.current_room = player.current_room.w_to
            else:
                print('Direction not available for this room')
        print(player)
    elif len(choice)==2:
        if (choice[0] == 'get' or choice[0] == 'take'):
            if choice[1] in player.current_room.item_list:
                player.add_Item(player.current_room.remove(choice[1]))
                player.current_room.choice[1].on_take()
            else:
                print(f'error: {choice[1]} does not exist in that room')

        elif choice[0] == 'drop':
            if choice[1] in player.item_list:
                player.current_room.add_item(player.remove_Item(choice[1]))
                player.item_list.choice[1].on_drop(choice[1])

    


                
            

        
       
                
   

