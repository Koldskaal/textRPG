from termcolor import colored
import time
from random import randint
from random import choice
from . import shopkeeper, stat_window, combat, character, room
from .game_log import log
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
        self.canvas = log.canvas

        self.current_room = room.Room((10,9), p, room_nr='0')
        self.RN = 0
        self.prev_room = None
        self.spawn_player_controller()
        self.current_room.spawn_player()
        self.list_of_rooms = []
        self.list_of_rooms.append(self.current_room)

        self.stat_window = stat_window.StatWindow(p, self.canvas)

        log.add_to_log('Welcome to infinite rooms!', 'Announcer', 'surprise')
        log.add_to_log('A game with infinite rooms and infinite fights.', 'Announcer', 'surprise')
        log.add_to_log('Sounds fun, eh? AHAHAHAHAHAHAHAHAHAHAHA! ', 'Announcer', 'surprise')
        log.add_to_log('Sorry about that... are you ready? Then', 'Announcer', 'surprise')
        log.add_to_log('LET THE GAMES BEGIN!', 'Announcer', 'surprise')

    def change_room(self):
        if len(self.list_of_rooms)-1 > self.RN:
            self.prev_room = self.current_room
            self.current_room= self.list_of_rooms[self.RN+1]
            self.RN = self.RN + 1

        else:
            self.prev_room = self.current_room
            self.current_room = room.Room((randint(5,15),randint(5,15)), p, choice(["right"]), str(self.RN+1))
            self.list_of_rooms.append(self.current_room)
            self.RN = self.RN + 1

    def change_room_backwards(self):
        self.current_room = self.prev_room
        self.prev_room = self.list_of_rooms[self.RN-2]
        self.RN = self.RN - 1

    def change_to_shop(self):
        self.current_room = shopkeeper.Shop(self.canvas)

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
            self.current_room.print_room(clear)

    def use_key(self, key):
        if isinstance(self.current_room, room.Room):
            movement = {'a': (0,-1), 's': (1,0), 'd': (0,1), 'w': (-1,0), '\r': (0,0)}
            if key in movement:
                self.move_player(movement[key])
            if key == "i":
                pass


        elif isinstance(self.current_room, shopkeeper.Shop):
            response = self.current_room.shop_menu(key)
            if response == "Leave":
                self.current_room = self.list_of_rooms[self.RN]
                self.print_room(True)
            if response == "Buy":
                self.current_room = shopkeeper.Buy(self.canvas, p)
                self.print_room(True)
            if response == "Sell":
                self.current_room = shopkeeper.Sell(self.canvas, p)
                self.print_room(True)
        elif isinstance(self.current_room, shopkeeper.Buy):
            response = self.current_room.buy_item(key)
            if response == "leave_buy":
                self.current_room = shopkeeper.Shop(self.canvas)
                self.print_room(True)
        elif isinstance(self.current_room, shopkeeper.Sell):
            response = self.current_room.sell_item(key)
            if response == "leave_sell":
                self.current_room = shopkeeper.Shop(self.canvas)
                self.current_room.menu_position = 1
                self.print_room(True)

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
            log.scroll(-1)
        # page down
        if key == 81:
            log.scroll(1)
