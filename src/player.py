# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    default_start = "outside"

    def __init__(self, name, room=default_start, items=[]):
        self.name = name
        self.room = room
        self.items = items

    def __str__(self):
        return f"{self.name} is in {self.room}"

    def travel(self, player_input):
        try:
            if player_input == 'n':
                print('You attempt to travel' +
                      '\033[1;32;40m north \033[0;37;40m')
                self.room = self.room.n_to

            if player_input == 'e':
                print('You attempt to travel' +
                      '\033[1;32;40m east \033[0;37;40m')

                self.room = self.room.e_to

            if player_input == 's':
                print('You attempt to travel' +
                      '\033[1;32;40m south \033[0;37;40m')

                self.room = self.room.s_to

            if player_input == 'w':
                print('You attempt to travel' +
                      '\033[1;32;40m west \033[0;37;40m')

                self.room = self.room.w_to

        except:
            print("The way is blocked")
