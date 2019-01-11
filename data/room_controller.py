from termcolor import colored
import time
from random import randint
from random import choice
from . import shopkeeper, stat_window, combat, character, game_log, room
from .canvas import Canvas

p = character.Player()
class RoomController:
    def __init__(self):
        """
        Arguments
        ---------
            starter_room : class Room
                An instance of a Room()
        """
        self.canvas = Canvas()
        self.log = game_log.log
        self.log.canvas = self.canvas

        self.current_room = room.Room((10,9), p, room_nr='0', canvas=self.canvas)
        self.RN = 0
        self.prev_room = None
        self.spawn_player_controller()
        self.current_room.spawn_player()
        self.list_of_rooms = []
        self.list_of_rooms.append(self.current_room)

        self.stat_window = stat_window.StatWindow(p, self.canvas)

        self.log.add_to_log('Welcome to infinite rooms!', 'Announcer', 'surprise')
        self.log.add_to_log('A game with infinite rooms and infinite fights.', 'Announcer', 'surprise')
        self.log.add_to_log('Sounds fun, eh? AHAHAHAHAHAHAHAHAHAHAHA! ', 'Announcer', 'surprise')
        self.log.add_to_log('Sorry about that... are you ready? Then', 'Announcer', 'surprise')
        self.log.add_to_log('LET THE GAMES BEGIN!', 'Announcer', 'surprise')

    def change_room(self):
        if len(self.list_of_rooms)-1 > self.RN:
            self.prev_room = self.current_room
            self.current_room= self.list_of_rooms[self.RN+1]
            self.RN = self.RN + 1

        else:
            self.prev_room = self.current_room
            self.current_room = room.Room((randint(5,15),randint(5,15)), p, choice(["right"]), str(self.RN+1), canvas=self.canvas)
            self.list_of_rooms.append(self.current_room)
            self.RN = self.RN + 1

    def change_room_backwards(self):
        self.current_room = self.prev_room
        self.prev_room = self.list_of_rooms[self.RN-2]
        self.RN = self.RN - 1

    def change_to_shop(self):
        self.current_room = shopkeeper.Shop(self.canvas)

    def leave_shop(self):
        self.current_room = self.list_of_rooms[self.RN]

    def spawn_player_controller(self):
        if self.prev_room == None:
            self.current_room.player_position = [2,2]
            self.current_room.shop_position = [4,4]
        else:
            #hvis P kommer fra venstre
            if self.prev_room.player_position[1] < self.prev_room.door["next"][1]:
                self.current_room.player_position = [0,0]
                self.current_room.player_position[0] = self.current_room.door["prev"][0]
                self.current_room.player_position[1] = self.current_room.door["prev"][1]+1
            #hvis P kommer fra højre
            elif self.prev_room.player_position[1] > self.prev_room.door["next"][1]:
                self.current_room.player_position = [0,0]
                self.current_room.player_position[0] = self.current_room.door["prev"][0]
                self.current_room.player_position[1] = self.current_room.door["prev"][1]-1
            #hvis P kommer nede fra
            elif self.prev_room.player_position[0] > self.prev_room.door["next"][0]:
                self.current_room.player_position = [0,0]
                self.current_room.player_position[0] = self.current_room.door["prev"][0]-1
                self.current_room.player_position[1] = self.current_room.door["prev"][1]
            #hvis P kommer oppe fra
            elif self.prev_room.player_position[0] < self.prev_room.door["next"][0]:
                self.current_room.player_position = [0,0]
                self.current_room.player_position[0] = self.current_room.door["prev"][0]+1
                self.current_room.player_position[1] = self.current_room.door["prev"][1]

    def print_room(self, clear=False):
        if isinstance(self.current_room, room.Room):
            self.current_room.print_room(clear)
        elif isinstance(self.current_room, shopkeeper.Shop):
            self.current_room.print_room()

    def use_key(self, key):
        if isinstance(self.current_room, room.Room):
            movement = {'a': (0,-1), 's': (1,0), 'd': (0,1), 'w': (-1,0), '\r': (0,0)}
            self.move_player(movement[key])

        elif isinstance(self.current_room, shopkeeper.Shop):
            self.current_room.shop_menu(key)

    def move_player(self, coordinates):
        self.current_room.move_player(coordinates)
        if self.current_room.go_to_next == True:
            self.current_room.go_to_next = False
            self.change_room()
            self.spawn_player_controller()
            self.current_room.spawn_player()
            #self.print_room(True)


        elif self.current_room.go_to_prev == True:
            self.current_room.go_to_prev = False
            self.change_room_backwards()
            #self.print_room(True)

        elif self.current_room.go_to_shop == True:
            self.current_room.go_to_shop = False
            self.change_to_shop()
            #self.print_room(True)

        self.stat_window.draw()
        self.print_room()

    def scroll_log(self, key):
        # page up
        if key == 73:
            self.log.scroll(-1)
        # page down
        if key == 81:
            self.log.scroll(1)
