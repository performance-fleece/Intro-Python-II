from room import Room
from player import Player
import time

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Jeremy", room['outside'])


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
print("\033[0;37;40m Welcome to my first MUD")
while True:
    time.sleep(.5)
    # print(
    #     f"Current Room: {player.room.name} \n === Description === \n {player.room.description}")
    print(player.room)

    player_input = input(
        'Which Direction do you wish to go?\n N, E, S, W or q to quit? ')

    print(player_input.split())
    print(len(player_input.split()))

    if player_input == 'q':
        print('Thanks for playing')
        break

    # if player_input == ('n' or 's' or 'e' or 'w'):
    #     player.travel(player_input)
    if len(player_input.split()) == 2:
        if player_input == "take":
            print("take method here")

    if player_input == 'n' or player_input == 'e' or player_input == 's' or player_input == 'w':
        player.travel(player_input)

    else:
        print("You are \033[1;31;40mconfused\033[0;37;40m and sit down")
