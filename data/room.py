from random import randint
from .textures import *
from . import combat,character

p = character.Player()

class Room:
    def __init__(self, size, prev_room_door='', room_nr='', canvas=None):
        """
        Arguments
        ---------
            size : tuple
                (x, y) The size of the room

            prev_room_door : string
                Previous position of the door that was walked thorugh
                ("left", "right", "up" or "down")
        """
        self.canvas = canvas

        self.size = size
        self.room = self.generate_border()
        self.generate_room_nr(room_nr)


        self.door = {}
        self.print_door(prev_room_door)
        self.go_to_next = None
        self.go_to_prev = None



    def generate_border(self):
        map = []
        x, y = self.size
        for i_x in range(x):
            row = []
            for i_y in range(y):
                if i_x == 0  or i_x == x - 1:
                    row.append(WALL_CHAR_UP_DOWN)
                elif i_y == 0 or i_y == y - 1:
                    row.append(WALL_CHAR_LEFT_RIGHT)
                else:
                    row.append(' ')
            map.append(row)

        return map

    def generate_room_nr(self, room_nr):
        koord_y = 0
        for number in room_nr:
            self.room[0][koord_y] = number
            koord_y += 1

    def spawn_player(self):
            self.room[self.player_position[0]][self.player_position[1]] = PLAYER_CHAR
            self.spawn_monsters()

    def spawn_monsters(self, amount=None):
        if not amount:
            amount = randint(1, 5)
        monster_coord = set()
        while len(monster_coord) <= amount:
            rand_coord = (randint(1, self.size[0]-2),randint(1, self.size[1]-2))
            if rand_coord[0] != self.player_position[0] and rand_coord[1] != self.player_position[1]:
                monster_coord.add(rand_coord)

        for coord in monster_coord:
            self.room[coord[0]][coord[1]] = MONSTER_CHAR


    def print_room(self, clear=False):
        string = ""
        for row in self.room:
            if " " in row or PLAYER_CHAR in row:
                string += '\n' + ' '.join(row)
            else:
                string += '\n' + WALL_CHAR_UP_DOWN.join(row)
        string.replace
        settings = {
            'horizontal_order'  : 1,     # Order of who goes first from left to right
            'delay'             : 0,     # if it needs to be x lines below
            'width'             : 40,    # how wide will it print
            'allignment'        : '^',
            'max_lines'         : 0,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : ''
        }
        # print(string)
        self.canvas.add_to_print('room', string, settings)
        self.canvas.print_canvas(clear)


    def move_player(self, coordinates):
        if (
        self.room
        [self.player_position[0] + coordinates[0]]
        [self.player_position[1] + coordinates[1]]
        == WALL_CHAR_UP_DOWN
        ):
            pass
        elif (
        self.player_position[0] + coordinates[0]
        == self.door['next'][0]
        and
        self.player_position[1] + coordinates[1]
        == self.door['next'][1]
        ):
            self.change_room()

        elif (
        self.room
        [self.player_position[0] + coordinates[0]]
        [self.player_position[1] + coordinates[1]]
        != WALL_CHAR_UP_DOWN
        and
        self.room
        [self.player_position[0] + coordinates[0]]
        [self.player_position[1] + coordinates[1]]
        != " "
        ):
            e = character.Monster()
            winning = combat.encounter(p,e, self.canvas)
            if winning == "enemy_killed":
                self.room[self.player_position[0] + coordinates[0]][self.player_position[1] + coordinates[1]] = " "

        else:
            if self.door.get("prev"):
                if (
                self.player_position[0] + coordinates[0]
                == self.door['prev'][0]
                and
                self.player_position[1] + coordinates[1]
                == self.door['prev'][1]
                ):
                    self.change_room_backwards()
                    return
            self.room[self.player_position[0]][self.player_position[1]] = ' '
            self.player_position[0] = self.player_position[0] + coordinates[0]
            self.player_position[1] = self.player_position[1] + coordinates[1]
            self.room[self.player_position[0]][self.player_position[1]] = PLAYER_CHAR

    def print_door(self, prev_room_door):
        # to koordinater sat ind dictionariet door med key next.
        # det første er: randint(1, len(self.room[0])-2), betyder random int mellem 1 og max tal på det lodrette koordinat - 1
        # det andet er: len(self.room[1])-1 , er max tal på det vandrette koordinat så helt til højre.
        # Vi kan overveje at gøre så den vælger en random væg at placere døren i. Lige nu er det altid til højre
        # vi har nu gemt koordinaterne på døren "next"
        self.door['next'] = [0, 0]
        self.door['next'][1] = len(self.room[1])-1
        self.door['next'][0] = randint(1, len(self.room)-2)

        # Her bruger vi de koordinater vi lige har genereret til at skrive døren ind i rummet.
        # Jeg har valgt at lave døren tom i stedet for en | men det kan vi altid ændre igen.
        self.room[self.door['next'][0]][self.door['next'][1]] = " "

        # Hvis vi kom fra en "left" dør, så vil vi lave en "prev" dør på højre side
        if prev_room_door == 'left':
            # max vandret, helt til højre
            horizontal_coord = len(self.room[1])-1
            # random int mellem 1 og en mindre end max lodret
            vertical_coord = randint(1, len(self.room)-2)
            # her gemmer  vi det i en "prev" key, så vi kan slå op senere hvilken dør vi går igennem
            self.door['prev'] = [vertical_coord, horizontal_coord]
            # og sætter den ind i rummet
            self.room[self.door['prev'][0]][self.door['prev'][1]] = " "

        elif prev_room_door == 'right':
            # resten er samme princip som den første.
            # døren her kommer fra en dør der lå til højre, så den må ligge til venstre.
            horizontal_coord = 0
            vertical_coord = randint(1, len(self.room)-2)
            self.door['prev'] = [vertical_coord, horizontal_coord]
            self.room[self.door['prev'][0]][self.door['prev'][1]] = " "

        elif prev_room_door == 'up':
            # kommer fra op så den må ligge nederst.
            horizontal_coord = randint(1, len(self.room[1])-2)
            vertical_coord = len(self.room[0])-1
            self.door['prev'] = [vertical_coord, horizontal_coord]
            self.room[self.door['prev'][0]][self.door['prev'][1]] = " "

        elif prev_room_door == 'down':
            # kommer fra nede så den må ligge øverst
            horizontal_coord = randint(1, len(self.room[1])-2)
            vertical_coord = 0
            self.door['prev'] = [vertical_coord, horizontal_coord]
            self.room[self.door['prev'][0]][self.door['prev'][1]] = " "

    def change_room(self):
        self.go_to_next = True

    def change_room_backwards(self):
        self.go_to_prev = True

if __name__ == '__main__':
    r = Room((9,9), 'up') #tester med et rum der er 25 gange 25
    r.print_room()
