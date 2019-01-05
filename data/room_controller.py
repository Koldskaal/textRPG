from . import room
from random import randint
from random import choice

class RoomController:
    def __init__(self, starter_room):
        """
        Arguments
        ---------
            starter_room : class Room
                An instance of a Room()
        """
        self.current_room = starter_room
        self.next_room = room.Room((randint(5,15),randint(5,15)),choice(["right"]))
        self.prev_room = None
        self.spawn_player_controller()
        self.current_room.spawn_player()
        self.list_of_rooms = []
        self.list_of_rooms.append(self.current_room)
        self.RN = 0

    def assign_next_room(self, room):
        self.next_room = room

    def change_room(self):

        if len(self.list_of_rooms)-1 > self.RN:
            self.prev_room = self.current_room
            self.current_room = self.next_room
            self.next_room = self.list_of_rooms[self.RN+1]
            self.RN = self.RN + 1
            print(f'RN: {self.RN}')
            print(f'len of roomlist{len(self.list_of_rooms)}')

        else:
            self.prev_room = self.current_room
            self.current_room = self.next_room
            self.list_of_rooms.append(self.current_room)
            self.next_room = room.Room((randint(5,15),randint(5,15)),choice(["right"]))
            self.RN = self.RN + 1
            print(f'RN: {self.RN}')
            print(f'len of roomlist{len(self.list_of_rooms)}')

    def change_room_backwards(self):
        self.next_room = self.current_room
        self.current_room = self.prev_room
        self.prev_room = self.list_of_rooms[self.RN-2]
        self.RN = self.RN - 1
        print(f'RN: {self.RN}')
        print(f'len of roomlist{len(self.list_of_rooms)}')

    def spawn_player_controller(self):
        if self.prev_room == None:
            self.current_room.player_position = [2,2]
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
    def print_room(self):
        self.current_room.print_room()

    def move_player(self, coordinates):
        self.current_room.move_player(coordinates)
        if self.current_room.go_to_next == True:
            self.current_room.go_to_next = False
            self.change_room()
            self.spawn_player_controller()
            self.current_room.spawn_player()


        elif self.current_room.go_to_prev == True:
            self.current_room.go_to_prev = False
            self.change_room_backwards()
            #self.spawn_player_controller()
            #self.current_room.spawn_player()
