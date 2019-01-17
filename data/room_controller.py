from termcolor import colored
import time
from random import randint
from random import choice
from . import shopkeeper, stat_window, combat, room, char_menu, spell_menu, player
from .game_log import log
from .canvas import Canvas

p = player.Player()
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
        self.current_room = shopkeeper.Shop(self.canvas, p, self.current_room)

    def change_to_combat(self):
        self.current_room = ''

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
                self.current_room = char_menu.Char_menu(self.canvas)
                self.print_room(True)
            if key == "o":
                self.current_room = spell_menu.BuySpellMenu(p, self.current_room)
                self.print_room(True)

        elif isinstance(self.current_room, char_menu.Char_menu):
            response = self.current_room.char_menu(key)
            if response == "Show Equipped":
                self.current_room = char_menu.Show_Equip(self.canvas, p)
                self.print_room(True)
            if response == "Items":
                self.current_room = char_menu.Items(self.canvas, p)
                self.print_room(True)
            if response == "Save":
                self.current_room = char_menu.Save(self.canvas)
                self.print_room(True)
            if response == "Quit Game":
                self.current_room = char_menu.Quit_Game(self.canvas)
                self.print_room(True)
            if response == "leave char_menu":
                self.current_room = self.list_of_rooms[self.RN]
                self.print_room(True)

        elif isinstance(self.current_room, char_menu.Items):
            response = self.current_room.item_menu(key)
            if response == "leave items":
                self.current_room = char_menu.Char_menu(self.canvas)
                self.print_room(True)
        elif isinstance(self.current_room, char_menu.Save):
            response = self.current_room.save_menu(key)
            if response == "leave save":
                self.current_room = char_menu.Char_menu(self.canvas)
                self.print_room(True)
        elif isinstance(self.current_room, char_menu.Quit_Game):
            response = self.current_room.quit_menu(key)
            if response == "leave quit game":
                self.current_room = char_menu.Char_menu(self.canvas)
                self.print_room(True)

        elif isinstance(self.current_room, char_menu.Show_Equip):
            response = self.current_room.equip_menu(key)
            if response == "equip helmet":
                self.current_room = char_menu.Equip_Helmets(self.canvas, p)
                self.print_room(True)
            if response == "equip armor":
                self.current_room = char_menu.Equip_Armors(self.canvas, p)
                self.print_room(True)
            if response == "equip ring":
                self.current_room = char_menu.Equip_Rings(self.canvas, p)
                self.print_room(True)
            if response == "equip weapon":
                self.current_room = char_menu.Equip_Weapons(self.canvas, p)
                self.print_room(True)
            if response == "equip amulet":
                self.current_room = char_menu.Equip_Amulets(self.canvas, p)
                self.print_room(True)
            if response == "leave show equip":
                self.current_room = char_menu.Char_menu(self.canvas)
                self.print_room(True)


        elif isinstance(self.current_room, char_menu.Equip_Helmets):
            response = self.current_room.helmets_menu(key)
            if response == "leave helmets":
                self.current_room = char_menu.Show_Equip(self.canvas, p)
                self.print_room(True)
        elif isinstance(self.current_room, char_menu.Equip_Armors):
            response = self.current_room.armors_menu(key)
            if response == "leave armors":
                self.current_room = char_menu.Show_Equip(self.canvas, p)
                self.print_room(True)
        elif isinstance(self.current_room, char_menu.Equip_Rings):
            response = self.current_room.rings_menu(key)
            if response == "leave rings":
                self.current_room = char_menu.Show_Equip(self.canvas, p)
                self.print_room(True)
        elif isinstance(self.current_room, char_menu.Equip_Amulets):
            response = self.current_room.amulets_menu(key)
            if response == "leave amulets":
                self.current_room = char_menu.Show_Equip(self.canvas, p)
                self.print_room(True)
        elif isinstance(self.current_room, char_menu.Equip_Weapons):
            response = self.current_room.weapons_menu(key)
            if response == "leave weapons":
                self.current_room = char_menu.Show_Equip(self.canvas, p)
                self.print_room(True)

        else:
            response = self.current_room.use_key(key)
            if response:
                self.current_room = response
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
