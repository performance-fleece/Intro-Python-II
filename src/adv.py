from room import Room
from player import Player

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
    # print(
    #     f"Current Room: {player.room.name} \n === Description === \n {player.room.description}")
    print(player.room)

    player_input = input(
        'Which Direction do you wish to go?\n N, E, S, W or q to quit? ')

    if player_input == 'q':
        print('Thanks for playing')
        break

    if player_input == 'n':
        print('You attempt to travel' + '\033[1;32;40m north \033[0;37;40m')
        try:
            player.room = player.room.n_to

        except:
            print('Error moving north')

    if player_input == 'e':
        print('You attempt to travel' + '\033[1;32;40m east \033[0;37;40m')

        try:
            player.room = player.room.e_to

        except:
            print('Error moving east')

    if player_input == 's':
        print('You attempt to travel' + '\033[1;32;40m south \033[0;37;40m')

        try:
            player.room = player.room.s_to

        except:
            print('Error moving south')

    if player_input == 'w':
        print('You attempt to travel' + '\033[1;32;40m west \033[0;37;40m')

        try:
            player.room = player.room.w_to

        except:
            print('Error moving West')
