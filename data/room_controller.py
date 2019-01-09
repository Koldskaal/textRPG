from . import room
from random import randint
from random import choice
<<<<<<< HEAD
from . import shopkeeper
=======
from .canvas import Canvas
>>>>>>> temporary

class RoomController:
    def __init__(self):
        """
        Arguments
        ---------
            starter_room : class Room
                An instance of a Room()
        """
        self.canvas = Canvas()

        self.current_room = room.Room((10,9), room_nr='0', canvas=self.canvas)
        self.RN = 0
        self.next_room = room.Room((randint(5,15),randint(5,15)),choice(["right"]), str(self.RN+1), canvas=self.canvas)
        self.prev_room = None
        self.spawn_player_controller()
        self.current_room.spawn_player()
        self.list_of_rooms = []
        self.list_of_rooms.append(self.current_room)




    def assign_next_room(self, room):
        self.next_room = room

    def change_room(self):

        if len(self.list_of_rooms)-1 > self.RN:
            self.prev_room = self.current_room
            self.current_room= self.list_of_rooms[self.RN+1]
            self.RN = self.RN + 1

        else:
            self.prev_room = self.current_room
            self.current_room = room.Room((randint(5,15),randint(5,15)),choice(["right"]), str(self.RN+1), canvas=self.canvas)
            self.list_of_rooms.append(self.current_room)
            self.RN = self.RN + 1

    def change_room_backwards(self):
        self.current_room = self.prev_room
        self.prev_room = self.list_of_rooms[self.RN-2]
        self.RN = self.RN - 1

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
            movement = {'a': (0,-1), 's': (1,0), 'd': (0,1), 'w': (-1,0)}
            self.move_player(movement[key])

        elif isinstance(self.current_room, shopkeeper.Shop):
            def move(key):
                if key.name == 'q':
                    global running
                    running = False
                if direction.name == 'w' or 's' or 'ENTER':
                    print('\n'*20)
                    shop_keeper.shop_menu(key)

    def move_player(self, coordinates):
        self.current_room.move_player(coordinates)
        if self.current_room.go_to_next == True:
            self.current_room.go_to_next = False
            self.change_room()
            self.spawn_player_controller()
            self.current_room.spawn_player()
            self.print_room(True)


        elif self.current_room.go_to_prev == True:
            self.current_room.go_to_prev = False
            self.change_room_backwards()
<<<<<<< HEAD
            #self.spawn_player_controller()
            #self.current_room.spawn_player()

        elif self.current_room.go_to_shop == True:
            self.current_room.go_to_shop = False
            self.change_to_shop()
=======
            self.print_room(True)


        self.print_room()
>>>>>>> temporary
