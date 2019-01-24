from random import randint, choice
from .textures import *
from . import combat, monsters
from .game_log import log
import time
from termcolor import colored
from . import astar
import ansiwrap
import copy

class Room:
    def __init__(self, size, player, prev_room_door='', room_nr=''):
        """
        Arguments
        ---------
            size : tuple
                (x, y) The size of the room

            prev_room_door : string
                Previous position of the door that was walked thorugh
                ("left", "right", "up" or "down")
        """
        self.player = player
        self.size = size
        self.__room = []
        self.room = self.generate_border()
        self.generate_room_nr(room_nr)

        self.monsters = {}
        self.shop_position = None
        self.door = {}
        self.print_door(prev_room_door)
        self.go_to_next = None
        self.go_to_prev = None
        self.go_to_shop = None
        self.leave_shop = None

        self.start_time = time.time()
        self.time_between_moves = 0.5
        self.st_time_between_moves = self.time_between_moves
        self.flee_time = 1.5

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

    def unpack_room(self, original):
        copy_list = copy.deepcopy(original)
        for i, n in enumerate(copy_list):
            for j, m in enumerate(n):
                # print(m)
                ansiwrap.strip_color(str(m))
                if ansiwrap.strip_color(str(m)) != ' ':
                    copy_list[i][j] = 1
                else:
                    copy_list[i][j] = 0

        copy_list[self.player_position[0]][self.player_position[1]] = 0
        return copy_list

    def generate_room_nr(self, room_nr):
        if int(room_nr) == 1:
            log.add_to_log('Oooh, a new room. How exciting!', 'Announcer', 'surprise')
        if int(room_nr) == 2:
            log.add_to_log('AAAAND another room! Does this ever end?', 'Announcer', 'surprise')
        koord_y = 0
        for number in room_nr:
            self.room[0][koord_y] = number
            koord_y += 1

    def spawn_player(self):

        self.room[self.player_position[0]][self.player_position[1]] = PLAYER_CHAR
        if self.shop_position:
            self.room[self.shop_position[0]][self.shop_position[1]] = SHOP_STAND
        if not self.monsters:
            self.spawn_monsters()

    def spawn_monsters(self, amount=None):
        if not amount:
            amount = randint(6,10)
        monster_coord = set()
        while len(monster_coord) != amount:
            rand_coord = (randint(1, self.size[0]-2),randint(1, self.size[1]-2))
            if list(rand_coord) != self.player_position and list(rand_coord) != self.shop_position:
                monster_coord.add(rand_coord)

        for i, coord in enumerate(monster_coord):
            e = monsters.Monster()
            self.monsters[e.name+f'{i}'] = {'monster':e, 'coord':list(coord)}
            self.room[coord[0]][coord[1]] = MONSTER_CHAR


    def print_room(self, clear=False):
        string = ""
        for row in self.room:
            if " " in row or PLAYER_CHAR in row:
                string += ' '.join(row) + '\n'
            else:
                string +=  WALL_CHAR_UP_DOWN.join(row) + '\n'
        string.replace
        settings = {
            'column_priority'  : 2,     # Order of who goes first from left to right
            'delay'             : 4,     # if it needs to be x lines below
            'width'             : 41,    # how wide will it print
            'alignment'        : '^',
            'max_lines'         : 0,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'MAP'
        }
        # print(string)
        log.canvas.add_to_print('room', string, settings)
        log.canvas.print_canvas(clear)



    def move_player(self, coordinates):
        player_coord = (self.player_position[0] + coordinates[0],
                        self.player_position[1] + coordinates[1])

        if self.door.get("prev"):
            if (player_coord[0] == self.door['prev'][0] and
                    player_coord[1] == self.door['prev'][1]):
                self.change_room_backwards()
                return

        if self.room[player_coord[0]][player_coord[1]] == WALL_CHAR_UP_DOWN:
            pass

        elif (player_coord[0] == self.door['next'][0] and
                player_coord[1] == self.door['next'][1]):
            self.change_room()

        elif (self.room[player_coord[0]][player_coord[1]] != WALL_CHAR_UP_DOWN and
                self.room[player_coord[0]][player_coord[1]] != " "):
            if self.room[player_coord[0]][player_coord[1]] == MONSTER_CHAR:
                winning = ''
                for key, value in self.monsters.items():
                    if value['coord'] == list(player_coord):
                        e = value['monster']
                        c = combat.Combat(self.player, e, self)
                        winning = c.encounter()
                        if winning == "enemy_killed":
                            winning = key
                if winning:
                    self.room[player_coord[0]][player_coord[1]] = " "
                    self.monsters.pop(winning)
                else:
                    self.start_time = time.time()
                    self.time_between_moves += self.flee_time


            elif self.room[player_coord[0]][player_coord[1]] == SHOP_STAND:
                self.change_to_shop()

        else:
            self.room[self.player_position[0]][self.player_position[1]] = ' '
            self.player_position[0] = player_coord[0]
            self.player_position[1] = player_coord[1]
            self.room[self.player_position[0]][self.player_position[1]] = PLAYER_CHAR

    def move_monsters(self):
        if time.time() - self.start_time > self.time_between_moves:
            fight = None
            for k,monster in self.monsters.items():
                room = self.unpack_room(self.room)
                path = astar.astar(room, tuple(monster['coord']), tuple(self.player_position))
                # print(path)
                if path:
                    monster_coord = list(path[1])
                else:
                    monster_coord = monster['coord']
                # print(monster_coord)
                # print(self.player_position)
                if self.room[monster_coord[0]][monster_coord[1]] == WALL_CHAR_UP_DOWN:
                    pass
                elif self.room[monster_coord[0]][monster_coord[1]] == MONSTER_CHAR:
                    pass
                elif self.room[monster_coord[0]][monster_coord[1]] == SHOP_STAND:
                    pass
                elif (
                    monster_coord == self.door['next'] or
                    monster_coord == self.door.get('prev')):
                    pass
                elif monster_coord == self.player_position:
                    fight = k
                else:
                    self.room[monster['coord'][0]][monster['coord'][1]] = ' '
                    monster['coord'][0] = monster_coord[0]
                    monster['coord'][1] = monster_coord[1]
                    self.room[monster['coord'][0]][monster['coord'][1]] = MONSTER_CHAR
                self.start_time = time.time()
                self.print_room()
                if self.time_between_moves != self.st_time_between_moves:
                    self.time_between_moves = self.st_time_between_moves
            if fight:
                e = self.monsters[fight]['monster']
                c = combat.Combat(self.player, e, self)
                winning = c.encounter()
                if winning == "enemy_killed":
                    winning = fight
                if winning:
                    self.room[self.monsters[fight]['coord'][0]][self.monsters[fight]['coord'][1]] = " "
                    self.monsters.pop(winning)
                    self.print_room()
                else:
                    self.start_time = time.time()
                    self.time_between_moves += self.flee_time

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
        self.room[self.door['next'][0]][self.door['next'][1]] = DOOR_CHAR

        # Hvis vi kom fra en "left" dør, så vil vi lave en "prev" dør på højre side
        if prev_room_door == 'left':
            # max vandret, helt til højre
            horizontal_coord = len(self.room[1])-1
            # random int mellem 1 og en mindre end max lodret
            vertical_coord = randint(1, len(self.room)-2)
            # her gemmer  vi det i en "prev" key, så vi kan slå op senere hvilken dør vi går igennem
            self.door['prev'] = [vertical_coord, horizontal_coord]
            # og sætter den ind i rummet
            self.room[self.door['prev'][0]][self.door['prev'][1]] = DOOR_CHAR

        elif prev_room_door == 'right':
            # resten er samme princip som den første.
            # døren her kommer fra en dør der lå til højre, så den må ligge til venstre.
            horizontal_coord = 0
            vertical_coord = randint(1, len(self.room)-2)
            self.door['prev'] = [vertical_coord, horizontal_coord]
            self.room[self.door['prev'][0]][self.door['prev'][1]] = DOOR_CHAR

        elif prev_room_door == 'up':
            # kommer fra op så den må ligge nederst.
            horizontal_coord = randint(1, len(self.room[1])-2)
            vertical_coord = len(self.room[0])-1
            self.door['prev'] = [vertical_coord, horizontal_coord]
            self.room[self.door['prev'][0]][self.door['prev'][1]] = DOOR_CHAR

        elif prev_room_door == 'down':
            # kommer fra nede så den må ligge øverst
            horizontal_coord = randint(1, len(self.room[1])-2)
            vertical_coord = 0
            self.door['prev'] = [vertical_coord, horizontal_coord]
            self.room[self.door['prev'][0]][self.door['prev'][1]] = DOOR_CHAR

    def change_room(self):
        self.room[self.door['next'][0]][self.door['next'][1]] = DOOR_CHAR_OPEN_NEXT
        self.print_room(True)
        time.sleep(0.3)
        self.room[self.door['next'][0]][self.door['next'][1]] = DOOR_CHAR
        self.go_to_next = True

    def change_room_backwards(self):
        self.room[self.door['prev'][0]][self.door['prev'][1]] = DOOR_CHAR_OPEN_PREV
        self.print_room(True)
        time.sleep(0.3)
        self.room[self.door['prev'][0]][self.door['prev'][1]] = DOOR_CHAR
        self.go_to_prev = True

    def change_to_shop(self):
        self.go_to_shop = True

    def leave_shop(self):
        self.leave_shop = True

if __name__ == '__main__':
    r = Room((9,9), 'up') #tester med et rum der er 25 gange 25
    r.print_room()
